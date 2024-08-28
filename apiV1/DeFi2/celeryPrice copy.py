 
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

# # 用户配置区域  --Start
# # YOUR_WALLET_ADDRESS = '0x2B50433f2050281122684E19916CB5A4FfEef01E'  # Add Your Wallet Address here by removing whole line
# # YOUR_PRIVATE_KEY = '2d6875cf2b8879962cb5cb324b30b6832e59a2823b34d98bec2088cf512e6959'  # Add Your Private Key here by removing whole line

# TRADE_TOKEN_ADDRESS = '0x768a62a22b187EB350637e720ebC552D905c0331'  #None  # Add token address here example : "0xc66c8b40e9712708d0b4f27c9775dc934b65f0d9"


# USDT_TOKEN_ADDRESS = '0x55d398326f99059fF775485246999027B3197955'  

# WBNB_ADDRESS = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
# # WBNB_ADDRESS = "0x55d398326f99059fF775485246999027B3197955"

# PANCAKE_ROUTER_ADDRESS = "0x10ED43C718714eb63d5aA57B78B54704E256024E"
# LP_ymiiUsdt_ADDRESS = '0x6b6b2D8166D13b58155b8d454F239AE3691257A6'  
# Tools_lpPrice_ADDRESS = '0x02Fa571EdAd13043EE3f3676E65092c5000E3Ad0'  


# SHOW_TX_ON_BROWSER = True
# SELL_TOKENS = None
# BUY_TOKENS = None

# # 80bf0820f328d80b571b0576db6d39d89d98e68b3cb83630dfe14b4a704012ee
# # 总帐号 负责分发 bnb 0xC3Ad2B6ee371fDA1646090e86D96d8dBE372E329     98b3fb701cc579f6aae77554ae7118aa3e3957a9f1b028509ef4cbd7149068df
# # Bnb_TokenGas='98b3fb701cc579f6aae77554ae7118aa3e3957a9f1b028509ef4cbd7149068df'


# #auto 自动化设置
# # priceNow=1.5
# buyNumberTotal=5
# # buyNumberNow=0
# priceDown=2  # 设置项目价格   逻辑 :低于项目价格价格 10% 开始 第一个 购买，购买后 项目价格=当前价格  ，高于 项目价格 10% 出售
# buyPrice={'price':1.95,'up':1,'down':0.2,'upStart':1,'upEnd':10}
# sellPrice={'price':1.96,'up':1,'down':0.2,'upStart':1,'upEnd':10}
# coinsRecharge=0.03 # 子币 每次充值
# AmountBuy={'defalut':60,'start': 0.01,'end':0.03} #每次购买量
# # AmountBuy1=60
# AmountSell={'defalut':60,'start':3,'end':5} #每次出售量
# PercentBuy=0.1 #下调 10% 购买 
# PercenttSell=0.1 #上调 10% 出售 
# # 用户配置区域 --End
# Token_Transaction_Time=10

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
        
        
        # # 私钥 获取 账号
        # self.myToken=Defi2Token.tokenList[self.TokenNumber]
        # self.privateKey=self.myToken['token']        
        # self.account=self.web3.eth.account.from_key(self.privateKey)                
        # self.walletAddress=self.account.address   
        self.TradingTokenDecimal = None
        # proxiesFirfox=self.changeIpFirfox()
        # self.driver = webdriver.Firefox(executable_path='/root/bot/difibot/geckodriver', options=self.options,proxy=proxiesFirfox)
       
        # Numbers to send Whatsapp web message
        self.numbersToNotify = ['+92*********']
        try:
           
            sellTokenAbi = tokenAbi(self.TokenToSellAddress )
            pancakeAbi = tokenAbi(self.pancakeRouterAddress )        
            usdtTokenAbi = tokenAbi(self.USDT_Address )
            
            # 获得lp price
            Tools_lpPrice_ADDRESSAbi = tokenAbi(self.Tools_lpPrice_ADDRESS )

            # Enter you wallet Public Address
            # BNB_balance = self.web3.eth.get_balance(self.walletAddress)
            # BNB_balance = self.web3.fromWei(BNB_balance, 'ether')
            # print(f"Current BNB Balance: {web3.fromWei(BNB_balance, 'ether')}")

            # Create a contract for both PancakeRoute and Token to Sell
            self.contractPancake = self.web3.eth.contract(address=self.pancakeRouterAddress, abi=pancakeAbi)
            self.contractSellToken = self.web3.eth.contract(self.TokenToSellAddress, abi=sellTokenAbi)
            # 获得lp price 合约
            self.contractTools_lpPrice_ADDRESS = self.web3.eth.contract(self.Tools_lpPrice_ADDRESS, abi=Tools_lpPrice_ADDRESSAbi)
           
                            
            self.contractUsdtToken = self.web3.eth.contract(self.USDT_Address, abi=usdtTokenAbi)
            if self.TradingTokenDecimal is None:
                self.TradingTokenDecimal = self.contractSellToken.functions.decimals().call()
                self.TradingTokenDecimal = getTokenDecimal(self.TradingTokenDecimal)
          
            # Get current avaliable amount of tokens from the wallet
            # NoOfTokens = self.contractSellToken.functions.balanceOf(self.walletAddress).call()
            # self.NoOfTokens = self.web3.fromWei(NoOfTokens, self.TradingTokenDecimal)
            self.symbol = self.contractSellToken.functions.symbol().call()
            # self.symbol
            
            # self.buySellNumber() # 定义 买卖数量
                 # 账号 自增
                 
            # self.tokenList=self.getTokenList()
            # self.TokenNumber = 0
            # self.nextAccount()
            
            
            # self.channel_layer = get_channel_layer()
            
            self.sendMessage('开始执行.')
              # 当读取到新的日志行时
            # async_to_sync(self.channel_layer.group_send)(str(self.objId), {
            #     'type': 'chat_message',
            #     'message': 'start..'
            # }) 
         
        
        except Exception as e:    
        
            result = ["Failed -InitializeTrade", f"ERROR: {e}"]
            print(result)
       
    
    # 获取token 
    # def getTokenList(self): 
    #     T_TokenAddrList=T_TokenAddr.objects.filter(uid=self.userId,status=1)  
    #     return T_TokenAddrList
      
        
    def sendMessage(self,msg):
        self.channel_layer = get_channel_layer()
              # 当读取到新的日志行时
        async_to_sync(self.channel_layer.group_send)(str(self.objId), {
            'type': 'chat_message',
            'message':str(msg)
        })
            
    # def nextAccount(self):
   
    #     if self.TokenNumber>=self.tokenList.count() :
    #         self.TokenNumber=0            
        
    #     # 私钥 获取 账号
    #     # self.myToken=Defi2Token.tokenList[self.TokenNumber]        
    #     self.myToken=self.tokenList[self.TokenNumber]   
    #     # self.privateKey=self.myToken['token']
    #     t_privateKey=self.myToken.TOKEN_private
    #      # 创建Fernet对象    
    #     cipher_suite = Fernet('FRrgJ5KhZNgtdctTbQWV2-Xam9zZP-pdsUsLDDPg0pY=') 
    #     self.privateKey = cipher_suite.decrypt(t_privateKey).decode() 
        
        
    #     self.account=self.web3.eth.account.from_key(self.privateKey)                
    #     self.walletAddress=self.account.address 
        
    #     # 设置单笔 买入 卖出 量 给子号补充bnb 量
    #     self.AmountBuy=random.uniform(self.AmountBuy0,self.AmountBuy1) #60-100
    #     self.tokenToBuy = self.web3.toWei(self.AmountBuy, self.TradingTokenDecimal)  
        
    #     self.AmountSell=random.uniform(self.AmountSell0,self.AmountSell1) #60-100         
    #     self.tokenToSell = self.web3.toWei(self.AmountSell, self.TradingTokenDecimal)        
    #     self.tokenCoinsRecharge=self.web3.toWei(self.coinsRecharge, self.TradingTokenDecimal)
        
    #     # 判断该账号 bnb 是否 太少
    #     self.token_balance = self.web3.eth.get_balance(self.walletAddress)        
    #     time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')               
    #     result=[time1,'Start-地址:',self.walletAddress,'余额bnb:',{ str(self.web3.fromWei(self.token_balance, self.TradingTokenDecimal))},'本次买入bnb:',self.AmountBuy,'本次卖出代币:', self.AmountSell ,'如果充币将补充bnb:',{str(self.web3.fromWei(self.tokenCoinsRecharge, self.TradingTokenDecimal))}]
    #     print(result)        
    #     self.sendMessage(list(result))       
        
    #     if self.token_balance < self.tokenCoinsRecharge :
            
    #         time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #         result=[time1,'当前交易地址:',self.walletAddress,'余额不足去充值..' ]
    #         print(result)      
            
    #         self.sendMessage(list(result))     
            
    #         self.transfer_bnbGas(self.tokenCoinsRecharge)  
       

    def changeIpweb3(self):
        proxies=self.changeIp()        
        bsc = "https://bsc-dataseed2.binance.org/"              
        
        self.web3 = Web3(Web3.HTTPProvider(bsc,request_kwargs=proxies)) 
       
        while not self.web3.is_connected(): 
            print("Not Connected to BSC wait...")    
            self.sendMessage("Not Connected to BSC wait...")        
            self.proxies=self.changeIpweb3()        
        print("Connected to BSC")      
        self.sendMessage("Connected to BSC")
        
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
            result=[time1,defi.symbol,'当前价格 ',str(price),'购买成交价格',str(defi.buyPrice),'出售成交价格',str(defi.sellPrice)] 
            print(result)
            defi.sendMessage(str(result))
            return 'ok'

        except Exception as e:  
            result = ["Failed -defi.runCode", f"ERROR: {e}" ]
            print(result) 
    return 'no'
    