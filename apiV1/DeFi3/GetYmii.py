# -*- coding: utf-8 -*-
import time
# import winsound
from os import system
import sys 
# sys.path.append("..") 
from bs4 import BeautifulSoup as bsp
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Options
from web3 import Web3
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from abi import tokenAbi
from decimalData import getTokenDecimal
import requests
import json
import  random 
import GetTokens,Defi2Token
import datetime
from multiprocessing import Process
 
TRADE_TOKEN_ADDRESS = '0x768a62a22b187EB350637e720ebC552D905c0331'  #None  # Add token address here example : "0xc66c8b40e9712708d0b4f27c9775dc934b65f0d9"

USDT_TOKEN_ADDRESS = '0x55d398326f99059fF775485246999027B3197955' 

WBNB_ADDRESS = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c" 

PANCAKE_ROUTER_ADDRESS = "0x10ED43C718714eb63d5aA57B78B54704E256024E"
# SHOW_TX_ON_BROWSER = True

# SELL_TOKENS = None
# BUY_TOKENS = None

# # 总帐号 负责分发 bnb 
# Bnb_TokenGas='98b3fb701cc579f6aae77554ae7118aa3e3957a9f1b028509ef4cbd7149068df'

# #auto 自动化设置
# # priceNow=1.5
# buyNumberTotal=5
# # buyNumberNow=0
# priceDown=2  # 设置项目价格   逻辑 :低于项目价格价格 10% 开始 第一个 购买，购买后 项目价格=当前价格  ，高于 项目价格 10% 出售
# buyPrice={'price':1.88,'up':1,'down':0.2,'upStart':1,'upEnd':10}
# sellPrice={'price':1.86,'up':1,'down':0.2,'upStart':1,'upEnd':10}
# coinsRecharge=0.03 # 子币 每次充值
# AmountBuy={'defalut':60,'start': 0.001,'end':0.002} #每次购买量
# # AmountBuy1=60
# AmountSell={'defalut':60,'start':1,'end':5} #每次出售量
# PercentBuy=0.1 #下调 10% 购买 
# PercenttSell=0.1 #上调 10% 出售 
# # 用户配置区域 --End
# Token_Transaction_Time=15


# GetBnb Setup
GuiJiWallter='0x710b2D51882bc32e63619310918183c666650Bd1'

class DefiAuto(object):    
    def __init__(self):        
        self.proxies=self.changeIpweb3()     
        # self.TokenTransactionTime=Token_Transaction_Time # 每次交易 间隔 60秒
         # Important Addresses
        self.TokenToSellAddress = self.web3.to_checksum_address(TRADE_TOKEN_ADDRESS)
        self.WBNB_Address = self.web3.to_checksum_address(WBNB_ADDRESS)
        self.USDT_Address = self.web3.to_checksum_address(USDT_TOKEN_ADDRESS)
        self.pancakeRouterAddress = self.web3.to_checksum_address(PANCAKE_ROUTER_ADDRESS)
        
        try:
            self.changeIpFirfox()
            self.Firfox()
            sellTokenAbi = tokenAbi(self.TokenToSellAddress, self.driver)
            pancakeAbi = tokenAbi(self.pancakeRouterAddress, self.driver)        
            usdtTokenAbi = tokenAbi(self.USDT_Address, self.driver)

            # Enter you wallet Public Address
            # BNB_balance = self.web3.eth.get_balance(self.walletAddress)
            # BNB_balance = self.web3.fromWei(BNB_balance, 'ether')
            # print(f"Current BNB Balance: {web3.fromWei(BNB_balance, 'ether')}")

            # Create a contract for both PancakeRoute and Token to Sell
            self.contractPancake = self.web3.eth.contract(address=self.pancakeRouterAddress, abi=pancakeAbi)
            self.contractSellToken = self.web3.eth.contract(self.TokenToSellAddress, abi=sellTokenAbi)                    
            self.contractUsdtToken = self.web3.eth.contract(self.USDT_Address, abi=usdtTokenAbi)
            self.TradingTokenDecimal = None
            if self.TradingTokenDecimal is None:
                self.TradingTokenDecimal = self.contractSellToken.functions.decimals().call()
                self.TradingTokenDecimal = getTokenDecimal(self.TradingTokenDecimal)
            
            # Get current avaliable amount of tokens from the wallet
            # NoOfTokens = self.contractSellToken.functions.balanceOf(self.walletAddress).call()
            # self.NoOfTokens = self.web3.fromWei(NoOfTokens, self.TradingTokenDecimal)
            # self.symbol = self.contractSellToken.functions.symbol().call()
            
            # self.buySellNumber() # 定义 买卖数量
                    # 账号 自增
            # self.TokenNumber = 0
            # self.nextAccount()
        
        except Exception as e:    
        
            result = ["Failed -InitializeTrade", f"ERROR: {e}"]
            print(result)
            # self.changeIpweb3()
            # self.__init__()
        
        # self.nextAccount()
            
        

    # def nextAccount(self):
    
    #     if self.TokenNumber>=len(Defi2Token.tokenList) :
    #         self.TokenNumber=0            
        
        # 私钥 获取 账号
        # self.myToken=Defi2Token.tokenList[self.TokenNumber]        
        # self.privateKey=self.myToken['token']
        # self.account=self.web3.eth.account.from_key(self.privateKey)                
        # self.walletAddress=self.account.address 
      
    def changeIpweb3(self):
        proxies=self.changeIp()        
        bsc = "https://bsc-dataseed2.binance.org/"              
        # self.web3 = Web3(Web3.HTTPProvider(bsc))        
        self.web3 = Web3(Web3.HTTPProvider(bsc,request_kwargs=proxies)) 
        
        while not self.web3.is_connected(): 
            print("Not Connected to BSC wait...")            
            self.proxies=self.changeIpweb3()        
        print("Connected to BSC")
        
        return proxies
    
    def changeIp(self):
        
        # ips='http://api.haiwaiip.com/api/pull?token=c10a444f7800613d326178a5e18e224c&num='+str(1)+'&format=json&protocol=http&country=sg&state=&city=&ip_type=datacenter&sep=3&area='
        ips='http://api.haiwaiip.com/api/pull?token=809fca7ecb467aafc033528723789277&num=1&format=json&protocol=http&country=sg&state=&city=&ip_type=datacenter&sep=2&area='
        resp = requests.get(ips) 

        data = resp.text

        data_dict = json.loads(data)   
        
        proxy = data_dict['data'][0]
    
        proxies={"proxies":{'https' : proxy, 'http' : proxy }}
        
        return proxies
    def changeIpFirfox(self):
          # ips='http://api.haiwaiip.com/api/pull?token=c10a444f7800613d326178a5e18e224c&num='+str(1)+'&format=json&protocol=http&country=sg&state=&city=&ip_type=datacenter&sep=3&area='
        ips='http://api.haiwaiip.com/api/pull?token=809fca7ecb467aafc033528723789277&num=1&format=json&protocol=http&country=sg&state=&city=&ip_type=datacenter&sep=2&area='
        resp = requests.get(ips) 

        data = resp.text

        data_dict = json.loads(data)   
        
        proxy = data_dict['data'][0]
    
        self.proxiesFirfox= {'https' : proxy, 'http' : proxy }

        
    def Firfox(self):
        self.options = Options()
        self.options.headless = True    
        self.driver = webdriver.Firefox(executable_path='/root/djangotokens/apiV1/DeFi2/geckodriver', options=self.options,proxy= self.proxiesFirfox)
    
     # 给账号 转bnb
    def GetAllYmii(self): # 转gas 费给地址       
       
            # 归集地址
            t_GuiJiWallter=Web3.to_checksum_address(GuiJiWallter)
            tokenList=[]
            for myToken in GetTokens.tokenList: 
                gasbnbToken=myToken['token']                
                gasAccount=self.web3.eth.account.from_key(gasbnbToken)        
                gasAccountWallet = gasAccount.address   
                # to = Web3.to_checksum_address(to)
                # 归集 bnb 
                gasFee=70000000000000 
                
                # 查看 ymii 余额
                value= self.contractSellToken.functions.balanceOf(gasAccountWallet).call() 
                
                nonce = self.web3.eth.get_transaction_count(gasAccountWallet)
                # amount=self.web3.to_wei(value, 'ether')
                t_gas=self.web3.eth.gas_price
                amount=value
                # t_gas=self.web3.eth.gas_price
                # Build a transaction that invokes this contract's function, called transfer
                token_txn = self.contractSellToken.functions.transfer(self.web3.to_checksum_address(t_GuiJiWallter), amount,).build_transaction({
                'chainId': 56,
                'gas': 60000,
                'gasPrice': t_gas,
                'nonce': nonce,
                })            
                signed_txn = self.web3.eth.account.sign_transaction(token_txn, private_key=gasbnbToken)
                
                try:
                    tx_hash=self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)             
                
                    time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    result=[time1,'归集成功到:',t_GuiJiWallter,amount,'token:',gasAccountWallet,self.web3.to_hex(tx_hash)]
                    tokenList.append(result)
                    print(result)
                except Exception as e:
                    self.proxies=self.changeIpweb3()
                    result = ["Failed-transfer_bnbGas", f"ERROR: {e}"]
                    print(result)
                    continue                
                    
            result=['全部归集成功',len(tokenList),'个' ]
            print(result)
            return 'ok'
   
               
    # 给账号 转bnb
    def GetAllBnb(self): # 转gas 费给地址       
        try:
            # 归集地址
            t_GuiJiWallter=Web3.to_checksum_address(GuiJiWallter)
            tokenList=[]
            for myToken in GetTokens.tokenList: 
                gasbnbToken=myToken['token']                
                gasAccount=self.web3.eth.account.from_key(gasbnbToken)        
                gasAccountWallet = gasAccount.address   
                # to = Web3.to_checksum_address(to)
                # 归集 bnb 
                gasFee=70000000000000 
                token_balance = self.web3.eth.get_balance(gasAccountWallet) #self.web3.from_wei(self.web3.eth.get_balance(self.wallet), 'ether')
                time.sleep(1)
                # 如果代币不足返回异常
                # if Decimal(token_balance) < Decimal(value):
                if token_balance < gasFee:
                    str=["小于gas{vule}"]
                    print(str)
                    break 
                value=token_balance-gasFee
                t_gas=self.web3.eth.gasPrice  
                nonce = self.web3.eth.get_transaction_count(gasAccountWallet)
                tx = {
                    'nonce': nonce,
                    'to': t_GuiJiWallter,
                    'gas': 21000,
                    # 'gasPrice': self.web3.to_wei('50', 'gwei'),
                    'gasPrice': t_gas,
                    # 'value': self.web3.to_wei(value, 'ether'),
                    'value': value,
                    'chainId': 56
                }
                # 签名交易
                # signed_tx = self.web3.eth.account.sign_transaction(tx, self.wallet_key)
                signed_tx = self.web3.eth.account.sign_transaction(tx, gasbnbToken)
                tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction) 
               
                time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                result=[time1,'归集成功',t_GuiJiWallter,value,self.web3.to_hex(tx_hash)]
                tokenList.append(result)
                print(result)
            result=[time1,'全部归集成功',len(tokenList),'个' ]
            print(result)
            return 'ok'
        except Exception as e:
            self.proxies=self.changeIpweb3()
            result = ["Failed-transfer_bnbGas", f"ERROR: {e}"]
            print(result)
            return result
            # return None, str(e)
        
   
   

        
# 前提是 每个子账号  必须有 bnb 才可以完成
def ApprovedAll(defi):
    for myToken in Defi2Token.tokenList:
        defi.myToken=myToken    
        defi.privateKey=myToken['token']
        defi.account=defi.web3.eth.account.from_key(defi.privateKey)                
        defi.walletAddress=defi.account.address     
        defi.sellTokensApproved() # 下一次购买准备    
        # defi.buyTokensApproved() # 下一次购买准备    


#  
def GetBnb():
    defi= DefiAuto()
    defi.GetAllBnb()

# 前提是 每个子账号  必须有 bnb 才可以完成
def GetYmii():
    defi= DefiAuto()
    defi.GetAllYmii()
    
   

def work():
    defi= DefiAuto()
    
if __name__ == "__main__":
    GetYmii()
    # GetBnb()
    # defi= DefiAuto()
  
    # print("开始...")  
    # # inputNumber = input("\nPlease specify 1 runCode, down or updown 2: ApprovedAll : ")     
    # inputNumber='1'
    # if inputNumber == '1':
    #     defi.buyTokensApproved()
    #     defi.buyTokensBuildTransaction()
    #     defi.sellTokensApproved()
    #     defi.sellTokensBuildTransaction()
    #     runCode(defi)
    # if inputNumber == '2':
    #     ApprovedAll(defi)
        
    # defi= DefiAuto()
    # ApprovedAll(defi)
     
    # while(1):
        # t_Process = Process(target=work)     
        # t_Process.start()
        # t_Process.join() 
        # print('next')
    # work()
 
    
