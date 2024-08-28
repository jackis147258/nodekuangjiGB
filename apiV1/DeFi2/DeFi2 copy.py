# -*- coding: utf-8 -*-
 

import time
# import winsound
from os import system
import sys 
sys.path.append("..") 
from bs4 import BeautifulSoup as bsp
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Options
from web3 import Web3
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

# from BuyTokens import buyTokens
# sys.path.append("..") 
# from Auto1.BuyTokens2 import buyTokens2
# # from CommandPromptVisuals import changeCmdPosition
# sys.path.append("..") 
# from Auto1.SellTokens import sellTokens
# from ThreadingWithReturn import ThreadWithResult


# import abi
from abi import tokenAbi
# import .. abi
# from sendWhatsappMessage import sendMessage
# import config as config
from decimalData import getTokenDecimal

import requests
import json
import  random 
import Defi2Token
import datetime
# 用户配置区域  --Start
# YOUR_WALLET_ADDRESS = '0x2B50433f2050281122684E19916CB5A4FfEef01E'  # Add Your Wallet Address here by removing whole line
# YOUR_PRIVATE_KEY = '2d6875cf2b8879962cb5cb324b30b6832e59a2823b34d98bec2088cf512e6959'  # Add Your Private Key here by removing whole line

TRADE_TOKEN_ADDRESS = '0x768a62a22b187EB350637e720ebC552D905c0331'  #None  # Add token address here example : "0xc66c8b40e9712708d0b4f27c9775dc934b65f0d9"


USDT_TOKEN_ADDRESS = '0x55d398326f99059fF775485246999027B3197955'  

# WBNB_ADDRESS = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
WBNB_ADDRESS = "0x55d398326f99059fF775485246999027B3197955"

PANCAKE_ROUTER_ADDRESS = "0x10ED43C718714eb63d5aA57B78B54704E256024E"
SHOW_TX_ON_BROWSER = True

SELL_TOKENS = None
BUY_TOKENS = None


#auto 自动化设置
# priceNow=1.5
buyNumberTotal=5
# buyNumberNow=0
priceDown=2  # 设置项目价格   逻辑 :低于项目价格价格 10% 开始 第一个 购买，购买后 项目价格=当前价格  ，高于 项目价格 10% 出售
buyPrice={'price':1.80,'up':1,'down':0.2,'upStart':1,'upEnd':10}
sellPrice={'price':1.95,'up':1,'down':0.2,'upStart':1,'upEnd':10}
AmountBuy={'defalut':60,'start': 10,'end':30} #每次购买量
# AmountBuy1=60
AmountSell={'defalut':60,'start':10,'end':30} #每次出售量
PercentBuy=0.1 #下调 10% 购买 
PercenttSell=0.1 #上调 10% 出售 
# 用户配置区域 --End

class DefiAuto(object):
    
    def __init__(self):
        
        self.proxies=self.changeIpweb3()
        self.signed_txn=None #
        self.signed_txnSell=None
        self.TokenNumber = 0
        self.TokenNumberTotal=1 #1 从0开始算数 一共多少 参与买卖账号
        self.TokenTransactionTime=2 # 每次交易 间隔 60秒

        self.AmountBuy=random.randint(AmountBuy['start'],AmountBuy['end']) #60-100
        self.AmountSell=random.randint(AmountBuy['start'],AmountBuy['end']) #60-100
        self.priceUp = float(0)
        self.priceDown = priceDown
        self.approveBuy=0
        self.approveSell=0
        # buyNumberNow=0
        self.tradeList=[]
        self.trade = {"price" : 0, "buyNumber"  : 0 }

        # self.bsc = 'https://bsc-dataseed.binance.org/'
        # self.web3 = Web3(Web3.HTTPProvider(bsc))
        while not self.web3.is_connected(): 
            print("Not Connected to BSC wait...")
            
            self.proxies=self.changeIpweb3()

        print("Connected to BSC")
        self.address = TRADE_TOKEN_ADDRESS


        # Important Addresses
        self.TokenToSellAddress = self.web3.to_checksum_address(self.address)
        self.WBNB_Address = self.web3.to_checksum_address(WBNB_ADDRESS)
        self.USDT_Address = self.web3.to_checksum_address(USDT_TOKEN_ADDRESS)
        self.pancakeRouterAddress = self.web3.to_checksum_address(PANCAKE_ROUTER_ADDRESS)
        
        # 私钥 获取 账号
        self.myToken=Defi2Token.tokenList[self.TokenNumber]
        self.privateKey=self.myToken['token']        
        self.account=self.web3.eth.account.from_key(self.privateKey)                
        self.walletAddress=self.account.address 
        

        
        self.TradingTokenDecimal = None
       

        # proxiesFirfox=self.changeIpFirfox()
        # self.driver = webdriver.Firefox(executable_path='/root/bot/difibot/geckodriver', options=self.options,proxy=proxiesFirfox)
        # self.proxiesFirfox=
        self.changeIpFirfox()
        self.Firfox()

        # Numbers to send Whatsapp web message
        self.numbersToNotify = ['+92*********']
       
        
        
        try:
            sellTokenAbi = tokenAbi(self.TokenToSellAddress, self.driver)
            pancakeAbi = tokenAbi(self.pancakeRouterAddress, self.driver)        
            usdtTokenAbi = tokenAbi(self.USDT_Address, self.driver)

            # Enter you wallet Public Address
            BNB_balance = self.web3.eth.get_balance(self.walletAddress)
            BNB_balance = self.web3.fromWei(BNB_balance, 'ether')
            # print(f"Current BNB Balance: {web3.fromWei(BNB_balance, 'ether')}")

            # Create a contract for both PancakeRoute and Token to Sell
            self.contractPancake = self.web3.eth.contract(address=self.pancakeRouterAddress, abi=pancakeAbi)
            self.contractSellToken = self.web3.eth.contract(self.TokenToSellAddress, abi=sellTokenAbi)
                 
            self.contractUsdtToken = self.web3.eth.contract(self.USDT_Address, abi=usdtTokenAbi)
            if self.TradingTokenDecimal is None:
                self.TradingTokenDecimal = self.contractSellToken.functions.decimals().call()
                self.TradingTokenDecimal = getTokenDecimal(self.TradingTokenDecimal)
            
                  
            self.buySellNumber() # 定义 买卖数量
            # Get current avaliable amount of tokens from the wallet
            NoOfTokens = self.contractSellToken.functions.balanceOf(self.walletAddress).call()
            self.NoOfTokens = self.web3.fromWei(NoOfTokens, self.TradingTokenDecimal)
            self.symbol = self.contractSellToken.functions.symbol().call()
        
        except Exception as e:    
        
            result = ["Failed -InitializeTrade", f"ERROR: {e}"]
            print(result)
            # self.changeIpweb3()
            # self.__init__()
            
            
        
        # return BNB_balance, symbol, NoOfTokens, params
    def buySellNumber(self):
        # 具体买多少 
        self.tokenToBuy = self.web3.toWei(self.AmountBuy, self.TradingTokenDecimal)  
        # tokenToSell = self.web3.toWei(self.AmountBuy, self.TradingTokenDecimal)
        self.tokenToSell = self.web3.toWei(self.AmountSell, self.TradingTokenDecimal)
            
    def nextAccount(self):
        self.TokenNumber=self.TokenNumber+1
        if self.TokenNumber>self.TokenNumberTotal:
            self.TokenNumber=0            
        
        self.myToken=Defi2Token.tokenList[self.TokenNumber]        
        self.privateKey=self.myToken['token']
        self.account=self.web3.eth.account.from_key(self.privateKey)                
        self.walletAddress=self.account.address 

    def changeIpweb3(self):
        proxies=self.changeIp()        
        bsc = "https://bsc-dataseed2.binance.org/"              
        # self.web3 = Web3(Web3.HTTPProvider(bsc))        
        self.web3 = Web3(Web3.HTTPProvider(bsc,request_kwargs=proxies)) 
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

        
    def  Firfox(self):
        
        
        # ips='http://api.haiwaiip.com/api/pull?token=809fca7ecb467aafc033528723789277&num=1&format=json&protocol=http&country=sg&state=&city=&ip_type=datacenter&sep=2&area='
        # resp = requests.get(ips) 

        # data = resp.text

        # data_dict = json.loads(data)   
        
        # proxy = data_dict['data'][0]
    
        # proxies= {'https' : proxy, 'http' : proxy }


        self.options = Options()
        self.options.headless = True
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument('--headless')
        
        # profile = webdriver.FirefoxProfile()

        # profile.set_preference("permissions.default.image", 2)  #禁止下载图片，根据情况使用

        # # 禁用浏览器缓存

        # profile.set_preference("network.http.use-cache", False)

        # profile.set_preference("browser.cache.memory.enable", False)

        # profile.set_preference("browser.cache.disk.enable", False)

        # profile.set_preference("browser.sessionhistory.max_total_viewers", 3)

        # profile.set_preference("network.dns.disableIPv6", True)

        # profile.set_preference("Content.notify.interval", 750000)

        # profile.set_preference("content.notify.backoffcount", 3)

        # # 有的网站支持 有的不支持 2 35 profile.set_preference("network.http.pipelining", True)

        # profile.set_preference("network.http.proxy.pipelining", True)

        # profile.set_preference("network.http.pipelining.maxrequests", 32)



        
        # self.driver = webdriver.Firefox(executable_path='/root/bot/difibot/geckodriver', firefox_options=self.options,firefox_profile=profile,proxy=proxies)


        self.driver = webdriver.Firefox(executable_path='/root/bot/difibot/geckodriver', firefox_options=self.options,proxy= self.proxiesFirfox)
        
        # url = f'https://swap.arken.finance/tokens/bsc/{self.address}'
        # self.driver.get(url)   


        

        # return proxies
    
    def buyTokensApproved(self):  
        try:  
            tokenToSell=self.tokenToBuy # 购买数量
            # if self.approveBuy==0:
            
            if self.myToken['ApprovedBuy']==0:
                # usdtTokenInAccount = self.contractUsdtToken.functions.balanceOf(self.walletAddress).call()
                TokenInAccount=999999999999999999999999999
                # usdtSymbol = self.contractUsdtToken.functions.symbol().call()
                approve = self.contractUsdtToken.functions.approve(self.pancakeRouterAddress,  TokenInAccount).build_transaction({
                    'from': self.walletAddress,
                    'gasPrice': self.web3.toWei('5', 'gwei'),
                    'nonce': self.web3.eth.get_transaction_count(self.walletAddress)
                })        
                signed_txn = self.web3.eth.account.sign_transaction(
                    approve, private_key=self.privateKey)
                
                tx_token = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
                print(f"Approved: {self.web3.to_hex(tx_token)}")
                # self.approveBuy=1
                # 记录 approveBuy  已经授权 0. 修改Tokendict 状态 1.改变当前 状态
                self.myToken['ApprovedBuy']=1 #改变了当前装 
                # Defi2Token.tokenList[self.myToken]['ApprovedBuy']=1
        except Exception as e:  
            self.changeIpweb3()
            result = ["Failed-buyApproved", f"ERROR: {e}"]
            print(result)
       
    
    def buyTokensBuildTransaction(self):  
        try:         
            tokenToSell=self.tokenToBuy # 购买数量
            pancakeSwap_txn = self.contractPancake.functions.swapExactTokensForTokens(
                tokenToSell, 0,
                # [TokenToSellAddress, WBNB_Address],
                [self.WBNB_Address, self.TokenToSellAddress],
                self.walletAddress,
                (int(time.time() + 1000000))
            ).build_transaction({
                'from': self.walletAddress,
                'gasPrice':self. web3.toWei('5', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(self.walletAddress)
            })
            # print(f"buildTransaction {web3.fromWei(tokenToSell, TradingTokenDecimal)}   ymii ok")
            self.signed_txn = self.web3.eth.account.sign_transaction(
                pancakeSwap_txn, private_key=self.privateKey)
        except Exception as e:  
            self.changeIpweb3()                         
            
            result = ["Failed-buyBuildTransaction", f"ERROR: {e}"]
            print(result)
    
    def buyTokensSend_raw_transaction(self):  
        try:
            tokenToSell=self.tokenToBuy # 购买数量
            tx_token = self.web3.eth.send_raw_transaction(self.signed_txn.rawTransaction)
            result = [self.web3.to_hex(tx_token), f"buyTokens {self.web3.fromWei(tokenToSell, self.TradingTokenDecimal)} {self.symbol}",self.walletAddress]
            print(result) 
            return 'ok'
        except Exception as e:  
            self.changeIpweb3() 
            # self.sellTokensApproved() # 下一次购买准备
            # self.sellTokensBuildTransaction()# 下一次购买准备
            # self.buyTokensApproved() # 下一次购买准备
            self.buyTokensBuildTransaction() # 下一次购买准备
            result = ["Failed-buySend_raw_transaction", f"ERROR: {e}"]
            print(result)
            

    # # 买 token
    # def buyTokens(self):       
    #     try:  
    #         tokenToSell=self.tokenToBuy # 购买数量
    #         if self.approveBuy==0:
    #             usdtTokenInAccount = self.contractUsdtToken.functions.balanceOf(self.walletAddress).call()
    #             usdtSymbol = self.contractUsdtToken.functions.symbol().call()
    #             approve = self.contractUsdtToken.functions.approve(self.pancakeRouterAddress, usdtTokenInAccount).build_transaction({
    #                 'from': self.walletAddress,
    #                 'gasPrice': self.web3.toWei('5', 'gwei'),
    #                 'nonce': self.web3.eth.get_transaction_count(self.walletAddress)
    #             })        
    #             signed_txn = self.web3.eth.account.sign_transaction(
    #                 approve, private_key=self.privateKey)
                
    #             tx_token = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    #             print(f"Approved: {self.web3.to_hex(tx_token)}")
    #             self.approveBuy=1
       
        
    #         # pancakeSwap_txn = contractPancake.functions.swapExactTokensForETH(
    #         pancakeSwap_txn = self.contractPancake.functions.swapExactTokensForTokens(
    #             tokenToSell, 0,
    #             # [TokenToSellAddress, WBNB_Address],
    #             [self.WBNB_Address, self.TokenToSellAddress],
    #             self.walletAddress,
    #             (int(time.time() + 1000000))
    #         ).build_transaction({
    #             'from': self.walletAddress,
    #             'gasPrice':self. web3.toWei('5', 'gwei'),
    #             'nonce': self.web3.eth.get_transaction_count(self.walletAddress)
    #         })
    #         # print(f"buildTransaction {web3.fromWei(tokenToSell, TradingTokenDecimal)}   ymii ok")
    #         signed_txn = self.web3.eth.account.sign_transaction(
    #             pancakeSwap_txn, private_key=self.privateKey)

         
    #         tx_token = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    #         result = [self.web3.to_hex(tx_token), f"buyTokens {self.web3.fromWei(tokenToSell, self.TradingTokenDecimal)} {self.symbol}"]
    #         print(result)
    #         return 'ok'
    #     except Exception as e:  
    #         self.changeIpweb3()                         
            
    #         result = ["Failed-buy", f"ERROR: {e}"]
    #         print(result)
          

    
    
    
    
    
    def sellTokensApproved(self):  
        try:  
            tokenToSell=self.tokenToSell
            # if self.approveBuy==0:
            
            if self.myToken['ApprovedSell']==0:
                # usdtTokenInAccount = self.contractUsdtToken.functions.balanceOf(self.walletAddress).call()
                TokenInAccount=999999999999999999999999999
                symbol = self.contractSellToken.functions.symbol().call() 
               
                if self.approveSell==0:    

                    approve = self.contractSellToken.functions.approve(self.pancakeRouterAddress, TokenInAccount).build_transaction({
                        'from': self.walletAddress,
                        'gasPrice': self.web3.toWei('5', 'gwei'),
                        'nonce': self.web3.eth.get_transaction_count(self.walletAddress)
                    })

                    signed_txn = self.web3.eth.account.sign_transaction(
                        approve, private_key=self.privateKey)

                    tx_token = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
                    print(f"Approved: {self.web3.to_hex(tx_token)}")
                    self.approveSell=1
                      # 记录 approveBuy  已经授权 0. 修改Tokendict 状态 1.改变当前 状态
                    self.myToken['ApprovedSell']=1 #改变了当前装 
                    # Defi2Token.tokenList[self.myToken]['ApprovedSell']=1

                    # time.sleep(2)

                    # print(f"Swapping {self.web3.fromWei(tokenToSell, self.TradingTokenDecimal)} {symbol} for BNB")
            
            
                
        except Exception as e:  
            self.changeIpweb3()
            result = ["Failed-sellApproved", f"ERROR: {e}"]
            print(result)
       
    
    def sellTokensBuildTransaction(self):  
        try:     
            tokenToSell=self.tokenToSell    
            # tokenToSell=self.tokenToBuy # 购买数量
            pancakeSwap_txn = self.contractPancake.functions.swapExactTokensForTokens(
                tokenToSell, 0,
                [self.TokenToSellAddress, self.WBNB_Address],
                # [WBNB_Address,TokenToSellAddress],
                self.walletAddress,
                (int(time.time() + 1000000))
            ).build_transaction({
                'from': self.walletAddress,
                'gasPrice': self.web3.toWei('5', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(self.walletAddress)
            })

            self.signed_txnSell = self.web3.eth.account.sign_transaction(
                pancakeSwap_txn, private_key=self.privateKey)
            
        except Exception as e:  
            self.changeIpweb3()                         
            
            result = ["Failed-sellBuildTransaction", f"ERROR: {e}"]
            print(result)
    
    def sellTokensSend_raw_transaction(self):  
        try:
            
            tokenToSell=self.tokenToSell
            
            tx_token = self.web3.eth.send_raw_transaction(self.signed_txnSell.rawTransaction)
            result = [datetime.datetime.now(),self.web3.to_hex(tx_token), f"Sold {self.web3.fromWei(tokenToSell, self.TradingTokenDecimal)} {self.symbol}",self.walletAddress]
            print(result)
           
            return 'ok'
        except Exception as e:  
            self.changeIpweb3() 
            # self.sellTokensApproved() # 下一次购买准备
            self.sellTokensBuildTransaction()# 下一次购买准备
            # self.buyTokensApproved() # 下一次购买准备
            # self.buyTokensBuildTransaction() # 下一次购买准备
            result = ["Failed-sellSend_raw_transaction", f"ERROR: {e}"]
            print(result)
            
            
    
    
    
    # 出售
    # def sellTokens(self):
       
    #     # tokenToSell = self.web3.toWei(self.AmountSell, self.TradingTokenDecimal)
    #     tokenToSell=self.tokenToSell
    #     try:
        
    #         TokenInAccount = self.contractSellToken.functions.balanceOf(self.walletAddress).call()
    #         symbol = self.contractSellToken.functions.symbol().call() 
            
    #         if self.approveSell==0:    
        
    #             approve = self.contractSellToken.functions.approve(self.pancakeRouterAddress, TokenInAccount).build_transaction({
    #                 'from': self.walletAddress,
    #                 'gasPrice': self.web3.toWei('5', 'gwei'),
    #                 'nonce': self.web3.eth.get_transaction_count(self.walletAddress)
    #             })
                
    #             signed_txn = self.web3.eth.account.sign_transaction(
    #                 approve, private_key=self.privateKey)
                
    #             tx_token = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    #             print(f"Approved: {self.web3.to_hex(tx_token)}")
    #             self.approveSell=1
            
    #         # time.sleep(2)

    #         print(f"Swapping {self.web3.fromWei(tokenToSell, self.TradingTokenDecimal)} {symbol} for BNB")
     
    #         pancakeSwap_txn = self.contractPancake.functions.swapExactTokensForTokens(
    #             tokenToSell, 0,
    #             [self.TokenToSellAddress, self.WBNB_Address],
    #             # [WBNB_Address,TokenToSellAddress],
    #             self.walletAddress,
    #             (int(time.time() + 1000000))
    #         ).build_transaction({
    #             'from': self.walletAddress,
    #             'gasPrice': self.web3.toWei('5', 'gwei'),
    #             'nonce': self.web3.eth.get_transaction_count(self.walletAddress)
    #         })

    #         signed_txn = self.web3.eth.account.sign_transaction(
    #             pancakeSwap_txn, private_key=self.privateKey)

    #         tx_token = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    #         result = [self.web3.to_hex(tx_token), f"Sold {self.web3.fromWei(tokenToSell, self.TradingTokenDecimal)} {symbol}"]
    #         print(result)
    #         return 'ok'
    #     except ValueError as e:
    #         self.changeIpweb3()
    #         result = ["Failed-sell", f"ERROR: {e}"]
    #         print(result) 

    # 购买 buy
    def downTard(self,t_price):
        
        if t_price<buyPrice['price']:
            # if self.buyTokens() =='ok':
            if self.buyTokensSend_raw_transaction() =='ok':
                self.priceDown=t_price
                self.AmountBuy=random.randint(AmountBuy['start'],AmountBuy['end']) #60-100
                self.nextAccount() #更换账号
                
                self.sellTokensApproved() # 下一次购买准备
                self.sellTokensBuildTransaction()# 下一次购买准备
                self.buyTokensApproved() # 下一次购买准备
                self.buyTokensBuildTransaction() # 下一次购买准备
                
             
                time.sleep(self.TokenTransactionTime)
            
        
    # 售出 sell
    def upTard(self,t_price):                           
        if t_price  > sellPrice['price'] :              
            if self.sellTokensSend_raw_transaction() =='ok':
                self.priceDown=t_price   
                self.AmountSell=random.randint(AmountSell['start'], AmountSell['end']) #60-100
                self.nextAccount()
                self.sellTokensApproved() # 下一次购买准备
                self.sellTokensBuildTransaction()# 下一次购买准备
                self.buyTokensApproved() # 下一次购买准备
                self.buyTokensBuildTransaction() # 下一次购买准备
                time.sleep(self.TokenTransactionTime)

def runCode(defi): 
    # global address,driver
    url = f'https://swap.arken.finance/tokens/bsc/{defi.address}'
    defi.driver.get(url)   
    time.sleep(1)
    while True:
        # Getting Price
        try:
            page_soup = bsp(defi.driver.page_source, features="lxml")
            price = float(page_soup.find_all("b", {"class": "number"})[0].text[1:].replace(",", ""))
            print('当前价格:'+str(price))
             
            # defi.driver.refresh()
            defi.driver.quit()
            defi.Firfox()

        except Exception as e:    
        
            result = ["Failed -defi.driver", f"ERROR: {e}"]
            print(result)
            # defi.driver.close()
            defi.driver.quit()
            defi.changeIpFirfox()
            defi.Firfox()
            # driver = webdriver.Firefox(executable_path='/root/bot/difibot/geckodriver', options=options,proxy=ipChi.getPorx() )
            runCode(defi)
      
    
        defi.downTard(price) #购买
        defi.upTard(price) # 出售
    
        # print('当前价格:'+str(price))
        time.sleep(2)
        runCode(defi)

def ApprovedAll(defi):

    for myToken in Defi2Token.tokenList:
        defi.myToken=myToken    
        defi.privateKey=myToken['token']
        defi.account=defi.web3.eth.account.from_key(defi.privateKey)                
        defi.walletAddress=defi.account.address     
        defi.sellTokensApproved() # 下一次购买准备    
        defi.buyTokensApproved() # 下一次购买准备
    


if __name__ == "__main__":
    defi= DefiAuto()
  
    print("开始...")  
    # inputNumber = input("\nPlease specify 1 runCode, down or updown 2: ApprovedAll : ")     
    inputNumber='1'
    if inputNumber == '1':
        defi.buyTokensApproved()
        defi.buyTokensBuildTransaction()
        defi.sellTokensApproved()
        defi.sellTokensBuildTransaction()
        runCode(defi)
    if inputNumber == '2':
        ApprovedAll(defi)

    
