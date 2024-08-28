 
import time
 
from os import system
import sys 
 
from bs4 import BeautifulSoup as bsp
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
 
from web3 import Web3
 
from apiV1.DeFi2.abi import tokenAbi

from apiV1.DeFi2.decimalData import getTokenDecimal
# from decimalData import getTokenDecimal
import requests
import json
import  random 
from apiV1.DeFi2 import Defi2Token
# import Defi2Token
import datetime
from multiprocessing import Process
from app1.models import T_Quantify1,T_TokenAddr, T_task  #保存 task id 以后删除

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from cryptography.fernet import Fernet

import redis


class DefiAuto(object):
    
    def __init__(self,obj):

        self.objId=obj.id
        
        self.userId= obj.uid
        
        self.proxies=self.changeIpweb3()
        self.signed_txn=None #
        self.signed_txnSell=None
      
        
       
        # self.TokenTransactionTime=Token_Transaction_Time # 每次交易 间隔 60秒
        self.TokenTransactionTime=obj.Token_Transaction_Time # 每次交易 间隔 60秒
 
        # self.priceUp = float(0)
        # self.priceDown = priceDown
        # self.approveBuy=0
        # self.approveSell=0
        # buyNumberNow=0
        self.tradeList=[]
        self.trade = {"price" : 0, "buyNumber"  : 0 }
        self.address = obj.TRADE_TOKEN_ADDRESS
        # self.symbol='ymii'        
        # 子币充值
        self.coinsRecharge=obj.coinsRecharge 
        # 设置 买卖 数量 区间

        self.AmountBuy0=float(obj.AmountBuy0)
        self.AmountBuy1=float(obj.AmountBuy1)
        self.AmountSell0=float(obj.AmountSell0)
        self.AmountSell1=float(obj.AmountSell1)
        # 购买价格 出售价格
        self.buyPrice=obj.buyPrice
        self.sellPrice=obj.sellPrice
        
        self.Bnb_TokenGas=obj.Bnb_TokenGas
 

        # Important Addresses
        self.TokenToSellAddress = self.web3.to_checksum_address(self.address)
        self.WBNB_Address = self.web3.to_checksum_address( obj.WBNB_ADDRESS)
        self.USDT_Address = self.web3.to_checksum_address(obj.USDT_TOKEN_ADDRESS)
        self.pancakeRouterAddress = self.web3.to_checksum_address(obj.PANCAKE_ROUTER_ADDRESS)
        
        # 获得lp价格
  
        self.LP_ymiiUsdt_ADDRESS = self.web3.to_checksum_address(obj.LP_ymiiUsdt_ADDRESS)
        self.Tools_lpPrice_ADDRESS = self.web3.to_checksum_address(obj.Tools_lpPrice_ADDRESS)
        
        
      
        self.TradingTokenDecimal = None
       
        # Numbers to send Whatsapp web message
        self.numbersToNotify = ['+92*********']
        try:
           
            sellTokenAbi = tokenAbi(self.TokenToSellAddress )
            pancakeAbi = tokenAbi(self.pancakeRouterAddress )        
            usdtTokenAbi = tokenAbi(self.USDT_Address )
            
            # 获得lp price
            Tools_lpPrice_ADDRESSAbi = tokenAbi(self.Tools_lpPrice_ADDRESS )

          

            # Create a contract for both PancakeRoute and Token to Sell
            self.contractPancake = self.web3.eth.contract(address=self.pancakeRouterAddress, abi=pancakeAbi)
            self.contractSellToken = self.web3.eth.contract(self.TokenToSellAddress, abi=sellTokenAbi)
            # 获得lp price 合约
            self.contractTools_lpPrice_ADDRESS = self.web3.eth.contract(self.Tools_lpPrice_ADDRESS, abi=Tools_lpPrice_ADDRESSAbi)
           
                            
            self.contractUsdtToken = self.web3.eth.contract(self.USDT_Address, abi=usdtTokenAbi)
            if self.TradingTokenDecimal is None:
                self.TradingTokenDecimal = self.contractSellToken.functions.decimals().call()
                self.TradingTokenDecimal = getTokenDecimal(self.TradingTokenDecimal)
          
         
            self.symbol = self.contractSellToken.functions.symbol().call()
          
            ##self.sendMessage('开始执行.')
         
        
        except Exception as e:    
        
            result = ["Failed -InitializeTrade", f"ERROR: {e}"]
            print(result)
       
    
        
    def sendMessage(self,msg):
        self.channel_layer = get_channel_layer()
              # 当读取到新的日志行时
        async_to_sync(self.channel_layer.group_send)(str(self.objId), {
            'type': 'chat_message',
            'message':str(msg)
        })
            
    
       

    def changeIpweb3(self):
        proxies=self.changeIp()        
        bsc = "https://bsc-dataseed2.binance.org/"              
        
        self.web3 = Web3(Web3.HTTPProvider(bsc,request_kwargs=proxies)) 
       
        while not self.web3.is_connected(): 
            print("Not Connected to BSC wait...")    
            ##self.sendMessage("Not Connected to BSC wait...")        
            self.proxies=self.changeIpweb3()        
        print("Connected to BSC")      
        ##self.sendMessage("Connected to BSC")
        
        return proxies
    
    def changeIp(self):
        ips='http://api.haiwaiip.com/api/pull?token=809fca7ecb467aafc033528723789277&num=1&format=json&protocol=http&country=sg&state=&city=&ip_type=datacenter&sep=2&area='
        resp = requests.get(ips) 
        data = resp.text
        data_dict = json.loads(data)  
        proxy = data_dict['data'][0]
        proxies={"proxies":{'https' : proxy, 'http' : proxy }}
        
        return proxies
     
   
    def getLpPrice(self):
        # 查看 ymii 余额
        try:
            value= self.contractTools_lpPrice_ADDRESS.functions.getTokenPrice(self.LP_ymiiUsdt_ADDRESS).call() 
            price=self.web3.fromWei(value, self.TradingTokenDecimal)
            return price
        except Exception as e:  
            if "HTTPSConnectionPool(host='bsc-dataseed2.binance.org', port=443)"  in str(e):
                self.changeIpweb3()            
            # self.buyTokensBuildTransaction() # 下一次购买准备
            result = ["Failed-getLpPrice", f"ERROR: {e}"]
            self.getLpPrice() 

def work (id):
    redis_client = redis.StrictRedis(host='localhost', port=6379, db=3)

    obj=T_Quantify1.objects.filter(id=id).first()
    if not obj==None:    
        defi= DefiAuto(obj)  
        # runCode(defi) self.address
        try:
            # symbol=defi.address+'_'+defi.symbol
            symbol=defi.address
            price=defi.getLpPrice()    
            redis_client.set(symbol, float(price))       
            time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')                    
            # result=[time1,defi.symbol,'当前价格 ',str(price),'购买成交价格',str(defi.buyPrice),'出售成交价格',str(defi.sellPrice)] 
            result=[time1,defi.symbol,'当前价格 ',str(price)] 
            print(result)
            defi.sendMessage(str(result))
            return 'ok'

        except Exception as e:  
            result = ["Failed -defi.runCode", f"ERROR: {e}" ]
            print(result) 
    return 'no'
    