 
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
import config
import logging
logger = logging.getLogger(__name__)


TRADE_TOKEN_ADDRESS =config.TRADE_TOKEN_ADDRESS 
# '0x768a62a22b187EB350637e720ebC552D905c0331'  #None  # Add token address here example : "0xc66c8b40e9712708d0b4f27c9775dc934b65f0d9"


USDT_TOKEN_ADDRESS =config.USDT_TOKEN_ADDRESS 
# '0x55d398326f99059fF775485246999027B3197955'  

WBNB_ADDRESS =config.WBNB_ADDRESS
# "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
# WBNB_ADDRESS = "0x55d398326f99059fF775485246999027B3197955"

PANCAKE_ROUTER_ADDRESS =config.PANCAKE_ROUTER_ADDRESS
# "0x10ED43C718714eb63d5aA57B78B54704E256024E"
LP_ymiiUsdt_ADDRESS =config.LP_ymiiUsdt_ADDRESS 
# '0x6b6b2D8166D13b58155b8d454F239AE3691257A6'  
Tools_lpPrice_ADDRESS =config.Tools_lpPrice_ADDRESS 
# '0x02Fa571EdAd13043EE3f3676E65092c5000E3Ad0'  

EbcState_ADDRESS=config.EbcState_ADDRESS
# '0x5A6c4479e2581aDD0d91fa32563B5faCcb2D61f7'

redis_client = redis.StrictRedis(host='localhost', port=6379, db=3)



class DefiAuto(object):
    
    def __init__(self):
        # self.proxies=self.changeIpweb3()
        
               # 初始化 Web3 连接
        bsc =config.BSC # "https://rpc.ankr.com/bsc/174ba138f2cbc5773ef292c0e0a941ec3f23246439e9f0b8d7bec242a67f8c20"  #免费
    
        self.web3 = Web3(Web3.HTTPProvider(bsc))
        
        logger.info(' 记录bsc:'+str(bsc)  +'个' )

        self.signed_txn=None #
        self.signed_txnSell=None
        self.TokenTransactionTime=60 # 每次交易 间隔 60秒
 
       
        self.address = TRADE_TOKEN_ADDRESS

        # Important Addresses
        self.TokenToSellAddress = self.web3.to_checksum_address(self.address)
        self.WBNB_Address = self.web3.to_checksum_address( WBNB_ADDRESS)
        self.USDT_Address = self.web3.to_checksum_address(USDT_TOKEN_ADDRESS)
        self.pancakeRouterAddress = self.web3.to_checksum_address(PANCAKE_ROUTER_ADDRESS)
        
        # 获得lp价格
  
        self.LP_ymiiUsdt_ADDRESS = self.web3.to_checksum_address(LP_ymiiUsdt_ADDRESS)
        self.Tools_lpPrice_ADDRESS = self.web3.to_checksum_address(Tools_lpPrice_ADDRESS)
        
        self.EbcState_ADDRESS = self.web3.to_checksum_address(EbcState_ADDRESS)

        
      
        self.TradingTokenDecimal = None
       
        # Numbers to send Whatsapp web message
        self.numbersToNotify = ['+92*********']
        try:
           
            sellTokenAbi = tokenAbi(self.TokenToSellAddress )
            pancakeAbi = tokenAbi(self.pancakeRouterAddress )        
            usdtTokenAbi = tokenAbi(self.USDT_Address )
            
            EbcState_ADDRESSAbi = tokenAbi(self.EbcState_ADDRESS )

            
            # 获得lp price
            Tools_lpPrice_ADDRESSAbi = tokenAbi(self.Tools_lpPrice_ADDRESS )
            # Create a contract for both PancakeRoute and Token to Sell
            self.contractPancake = self.web3.eth.contract(address=self.pancakeRouterAddress, abi=pancakeAbi)
            self.contractSellToken = self.web3.eth.contract(self.TokenToSellAddress, abi=sellTokenAbi)
            # 获得lp price 合约
            self.contractTools_lpPrice_ADDRESS = self.web3.eth.contract(self.Tools_lpPrice_ADDRESS, abi=Tools_lpPrice_ADDRESSAbi)
           
            # 获得ebcState 合约
            self.contractEbcState_ADDRESS = self.web3.eth.contract(self.EbcState_ADDRESS, abi=EbcState_ADDRESSAbi)
           
                            
            self.contractUsdtToken = self.web3.eth.contract(self.USDT_Address, abi=usdtTokenAbi)
            # if self.TradingTokenDecimal is None:
            #     self.TradingTokenDecimal = self.contractSellToken.functions.decimals().call()
            #     self.TradingTokenDecimal = getTokenDecimal(self.TradingTokenDecimal)
          
         
            # self.symbol = self.contractSellToken.functions.symbol().call()
          
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
            # self.getLpPrice() 
            
    def getTokenNewUser(self,pyUserNubmerAll):
        # 查看 ymii 余额
        try:
            value=None
            # 得到 新增用户总数
            tokenUserNumberAll= self.contractEbcState_ADDRESS.functions.getInviteCount().call() 
            logger.info(' 记录contractEbcState_ADDRESS:'+str(self.contractEbcState_ADDRESS)  +'个' )

            if pyUserNubmerAll<tokenUserNumberAll:
                # t_startAddUser=tokenUserNumberAll-pyUserNubmerAll            
                # 根据 从现有人数开始添加 进入人数
                value= self.contractEbcState_ADDRESS.functions.getInvitationsFromIndex(pyUserNubmerAll).call() 
            
            return tokenUserNumberAll,value
        except Exception as e:  
            if "HTTPSConnectionPool(host='bsc-dataseed2.binance.org', port=443)"  in str(e):
                self.changeIpweb3()            
            # self.buyTokensBuildTransaction() # 下一次购买准备
            result = ["Failed-getTokenNewUser", f"ERROR: {e}"]
            # self.getLpPrice() 

def work ():
    # redis_client = redis.StrictRedis(host='localhost', port=6379, db=3)

    try:
        # redis_client.set('pyUserNumberAll', 0) 
        # 检查 Redis 中是否存在键 'pyUserNumberAll'
        if not redis_client.exists('pyUserNumberAll'):
            # 如果不存在，则将 t_pyUserNumberAll 设置为 0
            t_pyUserNumberAll = 0
        else:
            # 如果存在，则从 Redis 中获取值
            t_pyUserNumberAll = redis_client.get('pyUserNumberAll')   
        
        # redis_client.set('pyUserNumberAll', 0) 
  
        defi= DefiAuto()   
        # 获得 链上用户总数，和 返回的用户集合 
        tokenUserNumberAll,value=defi.getTokenNewUser(int(t_pyUserNumberAll))     
        # token2sql(value)    
        redis_client.set('pyUserNumberAll', tokenUserNumberAll) 
        # 把集合用户加入数据库
        

        # redis_client.set('pyUserNumberAll', t_userNumber) 
        return value
    except Exception as e:  
        result = ["Failed -defi.runCode", f"ERROR: {e}" ]
        print(result) 
        return 'err'

# def token2sql(value):
#     for sublist in value:
#         for item in sublist:
#             # 在这里处理每个元素
#             print(item)
  