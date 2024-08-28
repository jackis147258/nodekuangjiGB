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
import Defi2Token
import datetime
from multiprocessing import Process
# 用户配置区域  --Start
# YOUR_WALLET_ADDRESS = '0x2B50433f2050281122684E19916CB5A4FfEef01E'  # Add Your Wallet Address here by removing whole line
# YOUR_PRIVATE_KEY = '2d6875cf2b8879962cb5cb324b30b6832e59a2823b34d98bec2088cf512e6959'  # Add Your Private Key here by removing whole line

TRADE_TOKEN_ADDRESS = '0x768a62a22b187EB350637e720ebC552D905c0331'  #None  # Add token address here example : "0xc66c8b40e9712708d0b4f27c9775dc934b65f0d9"


USDT_TOKEN_ADDRESS = '0x55d398326f99059fF775485246999027B3197955'  

WBNB_ADDRESS = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
# WBNB_ADDRESS = "0x55d398326f99059fF775485246999027B3197955"

PANCAKE_ROUTER_ADDRESS = "0x10ED43C718714eb63d5aA57B78B54704E256024E"
SHOW_TX_ON_BROWSER = True

SELL_TOKENS = None
BUY_TOKENS = None

# 总帐号 负责分发 bnb 
Bnb_TokenGas='98b3fb701cc579f6aae77554ae7118aa3e3957a9f1b028509ef4cbd7149068df'

#auto 自动化设置
# priceNow=1.5
buyNumberTotal=5
# buyNumberNow=0
priceDown=2  # 设置项目价格   逻辑 :低于项目价格价格 10% 开始 第一个 购买，购买后 项目价格=当前价格  ，高于 项目价格 10% 出售
buyPrice={'price':1.85,'up':1,'down':0.2,'upStart':1,'upEnd':10}
sellPrice={'price':1.88,'up':1,'down':0.2,'upStart':1,'upEnd':10}
coinsRecharge=0.03 # 子币 每次充值
AmountBuy={'defalut':60,'start': 0.001,'end':0.002} #每次购买量
# AmountBuy1=60
AmountSell={'defalut':60,'start':1,'end':5} #每次出售量
PercentBuy=0.1 #下调 10% 购买 
PercenttSell=0.1 #上调 10% 出售 
# 用户配置区域 --End

class DefiAuto(object):
    
    def __init__(self):
        
        self.proxies=self.changeIpweb3()
        self.signed_txn=None #
        self.signed_txnSell=None
      
        
        # self.TokenNumberTotal=1 #1 从0开始算数 一共多少 参与买卖账号
        self.TokenTransactionTime=2 # 每次交易 间隔 60秒

        # self.AmountBuy=random.uniform(AmountBuy['start'],AmountBuy['end']) #60-100
        # self.AmountSell=random.uniform(AmountSell['start'],AmountSell['end']) #60-100
        self.priceUp = float(0)
        self.priceDown = priceDown
        self.approveBuy=0
        self.approveSell=0
        # buyNumberNow=0
        self.tradeList=[]
        self.trade = {"price" : 0, "buyNumber"  : 0 }
        self.address = TRADE_TOKEN_ADDRESS
        self.symbol='ymii'        
        # 子币充值
        self.coinsRecharge=coinsRecharge 
        # Important Addresses
        self.TokenToSellAddress = self.web3.to_checksum_address(self.address)
        self.WBNB_Address = self.web3.to_checksum_address(WBNB_ADDRESS)
        self.USDT_Address = self.web3.to_checksum_address(USDT_TOKEN_ADDRESS)
        self.pancakeRouterAddress = self.web3.to_checksum_address(PANCAKE_ROUTER_ADDRESS)
        
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
            if self.TradingTokenDecimal is None:
                self.TradingTokenDecimal = self.contractSellToken.functions.decimals().call()
                self.TradingTokenDecimal = getTokenDecimal(self.TradingTokenDecimal)
          
            # Get current avaliable amount of tokens from the wallet
            # NoOfTokens = self.contractSellToken.functions.balanceOf(self.walletAddress).call()
            # self.NoOfTokens = self.web3.fromWei(NoOfTokens, self.TradingTokenDecimal)
            # self.symbol = self.contractSellToken.functions.symbol().call()
            
            # self.buySellNumber() # 定义 买卖数量
                 # 账号 自增
            self.TokenNumber = 0
            self.nextAccount()
            
          
         
        
        except Exception as e:    
        
            result = ["Failed -InitializeTrade", f"ERROR: {e}"]
            print(result)
            # self.changeIpweb3()
            # self.__init__()
            
            
        
        # return BNB_balance, symbol, NoOfTokens, params
    # def buySellNumber(self):
    #     # 具体买多少 
    #     self.tokenToBuy = self.web3.toWei(self.AmountBuy, self.TradingTokenDecimal)  
    #     # tokenToSell = self.web3.toWei(self.AmountBuy, self.TradingTokenDecimal)
    #     self.tokenToSell = self.web3.toWei(self.AmountSell, self.TradingTokenDecimal)
    #     self.tokenCoinsRecharge=self.web3.toWei(self.coinsRecharge, self.TradingTokenDecimal)
        
    #     time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #     result=[time1,'设置单笔买入:',self.AmountBuy,'设置单笔卖出:',self.AmountSell,'设置单笔充值:',self.coinsRecharge]
    #     print(result)
            
    def nextAccount(self):
    # def nowAccount(self):
        # self.TokenNumber=self.TokenNumber+1
        if self.TokenNumber>=len(Defi2Token.tokenList) :
            self.TokenNumber=0            
        
        # 私钥 获取 账号
        self.myToken=Defi2Token.tokenList[self.TokenNumber]        
        self.privateKey=self.myToken['token']
        self.account=self.web3.eth.account.from_key(self.privateKey)                
        self.walletAddress=self.account.address 
        
        # 设置单笔 买入 卖出 量 给子号补充bnb 量
        self.AmountBuy=random.uniform(AmountBuy['start'],AmountBuy['end']) #60-100
        self.tokenToBuy = self.web3.toWei(self.AmountBuy, self.TradingTokenDecimal)  
        
        self.AmountSell=random.uniform(AmountSell['start'],AmountSell['end']) #60-100         
        self.tokenToSell = self.web3.toWei(self.AmountSell, self.TradingTokenDecimal)        
        self.tokenCoinsRecharge=self.web3.toWei(self.coinsRecharge, self.TradingTokenDecimal)
        
        # 判断该账号 bnb 是否 太少
        self.token_balance = self.web3.eth.get_balance(self.walletAddress)        
        time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')               
        result=[time1,'当前交易地址:',self.walletAddress,'余额bnb:',{self.web3.fromWei(self.token_balance, self.TradingTokenDecimal)},'本次买入bnb:',self.AmountBuy,'本次卖出代币:', self.AmountSell ,'子账号补充bnb:',{self.web3.fromWei(self.tokenCoinsRecharge, self.TradingTokenDecimal)}]
        print(result)        
        
        if self.token_balance < self.tokenCoinsRecharge :
            
            time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            result=[time1,'当前交易地址:',self.walletAddress,'余额不足去充值..' ]
            print(result)            
            
            self.transfer_bnbGas(self.tokenCoinsRecharge)        
        # 判断该账号 sell 是否 授权
        #defi.buyTokensApproved()
        # self.sellTokensApproved()        
        # self.sellTokensBuildTransaction()# 下一次购买准备
        # self.buyTokensApproved() # 下一次购买准备
        # self.buyTokensBuildTransaction() # 下一次购买准备

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
        
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # driver = webdriver.Chrome(options=chrome_options)
        
        # options = Options()
        # options.headless = True
        # # options.add_argument("--enable-javascript")
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)



        self.options = Options()
        self.options.headless = True
        # self.options = webdriver.FirefoxOptions()
        # self.options.add_argument('--headless')
        self.driver = webdriver.Firefox(executable_path='/root/djangotokens/apiV1/DeFi2/geckodriver', options=self.options,proxy= self.proxiesFirfox)
      
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
                
            result = ["Failed-buyApproved", f"ERROR: {e}"]
            print(result)
       
    # 给账号 转bnb
    def transfer_bnbGas(self,gasbnb): # 转gas 费给地址       
        try:
            gasbnbToken=Bnb_TokenGas
            # gasbnbToken='9c94be624fc0b0527dfd0db70c0b70d4180e290e30e9c13f688a01fe84e4a5be'
            gasAccount=self.web3.eth.account.from_key(gasbnbToken)        
            gasAccountWallet = gasAccount.address  
            value=gasbnb            
            # to = Web3.to_checksum_address(to)
            to=Web3.to_checksum_address(self.walletAddress)
            
            t_gas=self.web3.eth.gasPrice  
            # nonce = self.web3.eth.get_transaction_count(self.wallet)
            
            nonce = self.web3.eth.get_transaction_count(gasAccountWallet)
            tx = {
                'nonce': nonce,
                'to': to,
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
            result=[time1,'充值成功',to,value,self.web3.to_hex(tx_hash)]
            print(result)
            return self.web3.to_hex(tx_hash), 'pay success'
        except Exception as e:
            self.proxies=self.changeIpweb3()
            result = ["Failed-transfer_bnbGas", f"ERROR: {e}"]
            print(result)
            # return None, str(e)
        
    # def buyTokensBuildTransactionswapExactTokensForTokens(self):  
    #     try:         
    #         # 判断当前 账号 是否 有bnb 如果没有转入 bnb
    #         # self.account
    #            # 查看bnb 数量
    #         token_balance = self.web3.eth.get_balance(self.walletAddress)
    #         if token_balance < self.tokenCoinsRecharge :
    #             self.transfer_bnbGas(self.tokenCoinsRecharge)
                
            
    #         tokenToSell=self.tokenToBuy # 购买数量
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
    #         self.signed_txn = self.web3.eth.account.sign_transaction(
    #             pancakeSwap_txn, private_key=self.privateKey)
    #     except Exception as e:  
    #         self.changeIpweb3()                         
            
    #         result = ["Failed-buyBuildTransaction", f"ERROR: {e}"]
    #         print(result)
            
    # def buyTokensBuildTransaction(self):  
    #         try: 
    #             t_gas=self.web3.eth.gasPrice  
                
    #             tokenToSell=self.tokenToBuy # 购买数量                
    #             pancakeSwap_txn = self.contractPancake.functions.swapExactETHForTokens(0,
    #                 [self.WBNB_Address, self.TokenToSellAddress],
    #                 self.walletAddress,
    #                 (int(time.time() + 1000000))).build_transaction({
    #                 'from': self.walletAddress,
    #                 'value': tokenToSell,  # Amount of BNB
    #                 'gas': 300000,
    #                 'gasPrice': t_gas,
    #                 'nonce': self.web3.eth.get_transaction_count(self.walletAddress)
    #             })
                                                                            
                                                                            
    #             # pancakeSwap_txn = self.contractPancake.functions.swapExactTokensForTokens(
    #             #     tokenToSell, 0,
    #             #     # [TokenToSellAddress, WBNB_Address],
    #             #     [self.WBNB_Address, self.TokenToSellAddress],
    #             #     self.walletAddress,
    #             #     (int(time.time() + 1000000))
    #             # ).build_transaction({
    #             #     'from': self.walletAddress,
    #             #     'gasPrice':self. web3.toWei('5', 'gwei'),
    #             #     'nonce': self.web3.eth.get_transaction_count(self.walletAddress)
    #             # })
    #             # print(f"buildTransaction {web3.fromWei(tokenToSell, TradingTokenDecimal)}   ymii ok")
    #             self.signed_txn = self.web3.eth.account.sign_transaction(
    #                 pancakeSwap_txn, private_key=self.privateKey)
    #             return 'ok'
    #         except Exception as e:  
    #             self.changeIpweb3()
    #             result = ["Failed-buyBuildTransaction", f"ERROR: {e}"]
    #             print(result)
    
    def buyTokensSend_raw_transaction(self):  
        try:
            tokenToSell=self.tokenToBuy # 购买数量            
            t_gas=self.web3.eth.gasPrice                            
            pancakeSwap_txn = self.contractPancake.functions.swapExactETHForTokens(0,
                [self.WBNB_Address,self.USDT_Address, self.TokenToSellAddress],
                self.walletAddress,
                (int(time.time() + 1000000))).build_transaction({
                'from': self.walletAddress,
                'value': tokenToSell,  # Amount of BNB
                'gas': 300000,
                'gasPrice': t_gas,
                'nonce': self.web3.eth.get_transaction_count(self.walletAddress)
            })
                                                                        
                                                                        
            # pancakeSwap_txn = self.contractPancake.functions.swapExactTokensForTokens(
            #     tokenToSell, 0,
            #     # [TokenToSellAddress, WBNB_Address],
            #     [self.WBNB_Address, self.TokenToSellAddress],
            #     self.walletAddress,
            #     (int(time.time() + 1000000))
            # ).build_transaction({
            #     'from': self.walletAddress,
            #     'gasPrice':self. web3.toWei('5', 'gwei'),
            #     'nonce': self.web3.eth.get_transaction_count(self.walletAddress)
            # })
            # print(f"buildTransaction {web3.fromWei(tokenToSell, TradingTokenDecimal)}   ymii ok")
            self.signed_txn = self.web3.eth.account.sign_transaction(
                pancakeSwap_txn, private_key=self.privateKey)
                
                
            tx_token = self.web3.eth.send_raw_transaction(self.signed_txn.rawTransaction)
            
            time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if self.token_balance>self.web3.eth.get_balance(self.walletAddress) :
            # result = [time1, f"购买成功: {self.web3.fromWei(tokenToSell, self.TradingTokenDecimal)} {self.symbol}",self.walletAddress]
            # web3.fromWei(web3.eth.getBalance(eth.coinbase),"ether")
                result = [time1, f"购买成功: {self.web3.fromWei(tokenToSell, self.TradingTokenDecimal)}  ",'购买地址:',self.walletAddress,'hash:',self.web3.to_hex(tx_token),]
                print(result) 
                return 'ok'
            else:
                result = [time1, f"购买不成功 请检查 gas费用: {self.web3.fromWei(tokenToSell, self.TradingTokenDecimal)}  ",'购买地址:',self.walletAddress,'hash:',self.web3.to_hex(tx_token),]
                print(result) 
                return self.web3.to_hex(tx_token)            
        except Exception as e:  
            self.changeIpweb3()            
            # self.buyTokensBuildTransaction() # 下一次购买准备
            result = ["Failed-buySend_raw_transaction", f"ERROR: {e}"]
            print(result)
            

    
    
    def sellTokensApproved(self):  
        try:  
            tokenToSell=self.tokenToSell
            # if self.approveBuy==0:
            
            if self.myToken['ApprovedSell']==0:
                # usdtTokenInAccount = self.contractUsdtToken.functions.balanceOf(self.walletAddress).call()  contractSellToken
                TokenInAccount=999999999999999999999999999
                symbol = self.contractSellToken.functions.symbol().call() 
                if self.approveSell==0:    
                    t_gas=self.web3.eth.gasPrice  
                    approve = self.contractSellToken.functions.approve(self.pancakeRouterAddress, TokenInAccount).build_transaction({
                        'from': self.walletAddress,
                        'gasPrice': t_gas , #self.web3.toWei('5', 'gwei'),
                        'nonce': self.web3.eth.get_transaction_count(self.walletAddress)
                    })

                    signed_txn = self.web3.eth.account.sign_transaction(
                        approve, private_key=self.privateKey)

                    tx_token = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
                    print(f"Approved: {self.web3.to_hex(tx_token)}")
                    
                    
                    self.approveSell=1
                      # 记录 approveBuy  已经授权 0. 修改Tokendict 状态 1.改变当前 状态
                    self.myToken['ApprovedSell']=1 #改变了当前装  
                
        except Exception as e:  
            self.changeIpweb3()
            result = ["Failed-sellApproved", f"ERROR: {e}"]
            print(result)
       
    
    # def sellTokensBuildTransaction(self):  
    #     try:     
    #         tokenToSell=self.tokenToSell   
            
    #         t_gas=self.web3.eth.gasPrice                             
            
    #         pancakeSwap_txn = self.contractPancake.functions.swapExactTokensForETH(
    #             tokenToSell, 0,
    #             [self.TokenToSellAddress, self.WBNB_Address],
    #             self.walletAddress,
    #             (int(time.time() + 1000000))
    #         ).build_transaction({
    #             'from': self.walletAddress,
    #             'gas': 160000,
    #             'gasPrice': t_gas,
    #             # 'gas': 200000,
    #             # 'gasPrice': t_gas ,  #self.web3.toWei('5', 'gwei'),
    #             'nonce': self.web3.eth.get_transaction_count(self.walletAddress)
    #         })
    #         self.signed_txnSell = self.web3.eth.account.sign_transaction(
    #             pancakeSwap_txn, private_key=self.privateKey)            
    #     except Exception as e:  
    #         self.changeIpweb3()
    #         result = ["Failed-sellBuildTransaction", f"ERROR: {e}"]
    #         print(result)
    
    def sellTokensSend_raw_transaction(self):  
        try:  
            tokenToSell=self.tokenToSell   
            t_gas=self.web3.eth.gasPrice  
            pancakeSwap_txn = self.contractPancake.functions.swapExactTokensForETH(
                tokenToSell, 0,
                [self.TokenToSellAddress,self.USDT_Address, self.WBNB_Address],
                self.walletAddress,
                (int(time.time() + 1000000)),
               
            ).build_transaction({
                'from': self.walletAddress,
                'gas': 300000,
                'gasPrice': t_gas,
                'nonce': self.web3.eth.get_transaction_count(self.walletAddress)
            })

            signed_txn = self.web3.eth.account.sign_transaction(
                pancakeSwap_txn, private_key=self.privateKey) 
            try:
                tx_token = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)   
                hash=self.web3.eth.getTransaction(tx_token)  
                time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                if self.token_balance<self.web3.eth.get_balance(self.walletAddress) :
                    result = [time1, f"出售成功: {self.web3.fromWei(tokenToSell, self.TradingTokenDecimal)}  ",'地址:',self.walletAddress,'hash:',self.web3.to_hex(tx_token),]
                    print(result)   
                    return 'ok'                                  
                else:
                    result = [time1, f"出售不成功 请检查账户是否有足够金额和 gas是否足够  : {self.web3.fromWei(tokenToSell, self.TradingTokenDecimal)}  ",'地址:',self.walletAddress,'hash:',self.web3.to_hex(tx_token),]
                    print(result) 
                    # print(hash) 
                    return self.web3.to_hex(tx_token)
            except ValueError as e:
                if e.args[0].get('message') in 'intrinsic gas too low':
                    result = ["Failed", f"ERROR: {e.args[0].get('message')}"]
                else:
                    result = ["Failed", f"ERROR: {e.args[0].get('message')} : {e.args[0].get('code')}"]
                print(result)  
                return result
        
        

            # try:
            # tx_token = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)                
            # time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # result = [time1, f"出售成功: {self.web3.fromWei(tokenToSell, self.TradingTokenDecimal)}  ",'地址:',self.walletAddress,'hash:',self.web3.to_hex(tx_token),]
            # print(result)  
            # return 'ok'
            # except ValueError as e:
            #     print (e)                       
            # print(result)           
            # return 'ok'
        # except ValueError as e:
        except Exception as e:  
            result = ["Failed-sellSend_raw_transaction", f"ERROR: {e}"]
            print(result)
            # MaxRetryError("HTTPSConnectionPool(host='bsc-dataseed2.binance.org', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)')))")
            if "HTTPSConnectionPool(host='bsc-dataseed2.binance.org', port=443)"  in e:
                self.changeIpweb3()
            # self.changeIpweb3() 
            # self.sellTokensApproved() # 下一次购买准备
            # self.sellTokensBuildTransaction()# 下一次购买准备
            # self.buyTokensApproved() # 下一次购买准备
            # self.buyTokensBuildTransaction() # 下一次购买准备
           
    # def buyTokens(self):   
    #     toBuyBNBAmount=self.tokenToBuy
    #     pancakeSwap_txn = self.contractPancake.functions.swapExactETHForTokens(0,
    #                                                                     [self.WBNB_Address, self.TokenToSellAddress],
    #                                                                     self.walletAddress,
    #                                                                     (int(time.time() + 10000))).build_transaction({
    #         'from': self.walletAddress,
    #         'value': toBuyBNBAmount,  # Amount of BNB
    #         'gas': 160000,
    #         'gasPrice': self.web3.toWei('5', 'gwei'),
    #         'nonce': self.web3.eth.get_transaction_count(self.walletAddress)
    #     })

    #     signed_txn = self.web3.eth.account.sign_transaction(pancakeSwap_txn, private_key=self.privateKey)
    #     try:
    #         tx_token = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    #         result = [self.web3.to_hex(tx_token), f"Bought {self.web3.fromWei(toBuyBNBAmount, 'ether')} BNB of {self.symbol}"]
    #         return result
    #     except ValueError as e:
    #         if e.args[0].get('message') in 'intrinsic gas too low':
    #             result = ["Failed", f"ERROR: {e.args[0].get('message')}"]
    #         else:
    #             result = ["Failed", f"ERROR: {e.args[0].get('message')} : {e.args[0].get('code')}"]
    #         return result
    # 购买 buy
    def downTard(self,t_price):
        
        if t_price<buyPrice['price']:
            # if self.buyTokens() =='ok':
            # self.buyTokens()
            if self.buyTokensSend_raw_transaction() =='ok':
                
                time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                result=[time1,'购买成功，更换下一个账号-------------------------------------------------------------------'] 
                print(result)
                
                self.priceDown=t_price
                self.AmountBuy=random.uniform(AmountBuy['start'],AmountBuy['end']) #60-100
                self.TokenNumber=self.TokenNumber+1             
                self.nextAccount() #更换账号
                
                time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                result=[time1,'间歇 ',self.TokenTransactionTime,' 秒'] 
                print(result)
                time.sleep(self.TokenTransactionTime)
            else:
                time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                result=[time1,'购买不成功，更换下一个账号-------------------------------------------------------------------'] 
                print(result)
                self.TokenNumber=self.TokenNumber+1     
                self.nextAccount() #更换账号                
                # self.sellTokensApproved() # 下一次购买准备
                # self.sellTokensBuildTransaction()# 下一次购买准备
                # self.buyTokensApproved() # 下一次购买准备
                # self.buyTokensBuildTransaction() # 下一次购买准备
                
            
        
    # 售出 sell
    def upTard(self,t_price):                           
        if t_price  > sellPrice['price'] :  
            
            self.sellTokensApproved()        
            # self.sellTokensBuildTransaction()# 下一次购买准备
                    
            if self.sellTokensSend_raw_transaction() =='ok':
                
                time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                result=[time1,'出售成功，更换下一个账号----------------------------------------------------------------------']  
                print(result)
                
                self.priceDown=t_price   
                self.AmountSell=random.uniform(AmountSell['start'], AmountSell['end']) #60-100    random.randint
                self.TokenNumber=self.TokenNumber+1      
                self.nextAccount()
                # self.sellTokensApproved() # 下一次购买准备
                # self.sellTokensBuildTransaction()# 下一次购买准备
                # # self.buyTokensApproved() # 下一次购买准备
                # self.buyTokensBuildTransaction() # 下一次购买准备
                
                time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                result=[time1,'间歇 ',self.TokenTransactionTime,' 秒'] 
                print(result)
                
                time.sleep(self.TokenTransactionTime)
            else:
                time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                result=[time1,'出售不成功，更换下一个账号-------------------------------------------------------------------'] 
                print(result)
                self.TokenNumber=self.TokenNumber+1      
                self.nextAccount() #更换账号                
                # self.sellTokensApproved() # 下一次购买准备
                # self.sellTokensBuildTransaction()# 下一次购买准备
                # # self.buyTokensApproved() # 下一次购买准备
                # self.buyTokensBuildTransaction() # 下一次购买准备

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
            time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            result=[time1,'当前价格 ',price,'购买成交价格',buyPrice['price'],'出售成交价格',sellPrice['price'],' 等待交易账号:',defi.walletAddress ] 
            
          
        
            print(result)
            # print('当前价格:'+str(price))
             
            # defi.driver.refresh()
            defi.driver.quit()
            defi.Firfox()

        except Exception as e:    
        
            result = ["Failed -defi.driver", f"ERROR: {e}",'没有获取到价格报错']
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
        
# 前提是 每个子账号  必须有 bnb 才可以完成
def ApprovedAll(defi):
    for myToken in Defi2Token.tokenList:
        defi.myToken=myToken    
        defi.privateKey=myToken['token']
        defi.account=defi.web3.eth.account.from_key(defi.privateKey)                
        defi.walletAddress=defi.account.address     
        defi.sellTokensApproved() # 下一次购买准备    
        # defi.buyTokensApproved() # 下一次购买准备    

def work():
    defi= DefiAuto()
    # defi.buyTokensApproved()
    # defi.buyTokensBuildTransaction()
    # defi.sellTokensApproved()
    # defi.sellTokensBuildTransaction()
    runCode(defi)
    

if __name__ == "__main__":
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
    work()
    
