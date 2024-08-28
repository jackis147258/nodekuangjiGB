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
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.chrome import ChromeDriverManager
# from abi import tokenAbi
from apiV1.DeFi2.abi import tokenAbi

from apiV1.DeFi2.decimalData import getTokenDecimal
# from decimalData import getTokenDecimal
import requests
import json
import  random 
from apiV1.DeFi2 import Defi2Token
# import Defi2Token
from datetime import datetime

from multiprocessing import Process
from app1.models import T_Quantify1,T_TokenAddr, T_task,T_trade  #保存 task id 以后删除

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from cryptography.fernet import Fernet
import redis
from decimal import Decimal 

class DefiAuto(object):
    
    def __init__(self,obj):

        self.objId=obj.id
        
        self.userId= obj.uid

        # 获得 交易 全部  状态
        self.Dlprice_status =obj.Dlprice_status
        #获取 上调 百分比
        self.PercenttSell =obj.PercenttSell

        #获取 下调 百分比
        self.PercentBuy =obj.PercentBuy

        #限制购买数量
        self.DlBuyNumber =obj.DlBuyNumber
        #限制出售数量
        self.DlSellNumber =obj.DlSellNumber

        
       
        # self.TokenTransactionTime=Token_Transaction_Time # 每次交易 间隔 60秒
        self.TokenTransactionTime=obj.Token_Transaction_Time # 每次交易 间隔 60秒
 
        self.priceUp = float(0)
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
        self.TokenToSellAddress =self.address
        self.WBNB_Address = obj.WBNB_ADDRESS
        self.USDT_Address = obj.USDT_TOKEN_ADDRESS
        self.pancakeRouterAddress = obj.PANCAKE_ROUTER_ADDRESS
        
        # 获得lp价格

        self.LP_ymiiUsdt_ADDRESS =obj.LP_ymiiUsdt_ADDRESS
        self.Tools_lpPrice_ADDRESS = obj.Tools_lpPrice_ADDRESS
        self.TradingTokenDecimal = None
        # Numbers to send Whatsapp web message
        self.numbersToNotify = ['+92*********']
        try:
            # 获取下一个 钱包 地址
            obj=self.get_next_data()
            self.nextAccountNew(obj)
            self.QianBaoTokenId=obj.id          
            # self.sendMessage('开始执行.')
        except Exception as e:
            result = ["Failed -InitializeTrade", f"ERROR: {e}"]
            print(result)
         
   
    def changeIpweb3(self):
        proxies=self.changeIp()        
        bsc = "https://bsc-dataseed2.binance.org/"              
        # self.web3 = Web3(Web3.HTTPProvider(bsc))        
        self.web3 = Web3(Web3.HTTPProvider(bsc,request_kwargs=proxies)) 
       
        while not self.web3.is_connected(): 
            print("Not Connected to BSC wait...")    
            self.sendMessage("Not Connected to BSC wait...")        
            self.proxies=self.changeIpweb3()        
        print("Connected to BSC")      
        self.sendMessage("Connected to BSC")
        
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
 
       
    
    def getWeb3(self):        
        self.proxies=self.changeIpweb3()
        self.signed_txn=None #
        self.signed_txnSell=None
        # 获得lp价格
  
        self.LP_ymiiUsdt_ADDRESS = self.web3.to_checksum_address(self.LP_ymiiUsdt_ADDRESS)
        self.Tools_lpPrice_ADDRESS = self.web3.to_checksum_address(self.Tools_lpPrice_ADDRESS)    
        self.TradingTokenDecimal = None

        # Numbers to send Whatsapp web message
        self.numbersToNotify = ['+92*********']
        try:
           
            sellTokenAbi = tokenAbi(self.TokenToSellAddress )
            pancakeAbi = tokenAbi(self.pancakeRouterAddress )        
            usdtTokenAbi = tokenAbi(self.USDT_Address )
            
            # 获得lp price
            Tools_lpPrice_ADDRESSAbi = tokenAbi(self.Tools_lpPrice_ADDRESS ) 
            
            self.contractPancake = self.web3.eth.contract(address=self.pancakeRouterAddress, abi=pancakeAbi)
            self.contractSellToken = self.web3.eth.contract(self.TokenToSellAddress, abi=sellTokenAbi)
            # 获得lp price 合约
            self.contractTools_lpPrice_ADDRESS = self.web3.eth.contract(self.Tools_lpPrice_ADDRESS, abi=Tools_lpPrice_ADDRESSAbi)
           
                            
            self.contractUsdtToken = self.web3.eth.contract(self.USDT_Address, abi=usdtTokenAbi)
            if self.TradingTokenDecimal is None:
                self.TradingTokenDecimal = self.contractSellToken.functions.decimals().call()
                self.TradingTokenDecimal = getTokenDecimal(self.TradingTokenDecimal)
         
            self.symbol = self.contractSellToken.functions.symbol().call()


                 # 设置单笔 买入 卖出 量 给子号补充bnb 量
            # self.AmountBuy=random.uniform(self.AmountBuy0,self.AmountBuy1) #60-100
            self.tokenToBuy = self.web3.toWei(self.AmountBuy, self.TradingTokenDecimal)  
            # self.tokenToBuy = self.web3.toWei(self.AmountBuy, self.TradingTokenDecimal)  
            
            # self.AmountSell=random.uniform(self.AmountSell0,self.AmountSell1) #60-100         
            self.tokenToSell = self.web3.toWei(self.AmountSell, self.TradingTokenDecimal)        
            self.tokenCoinsRecharge=self.web3.toWei(self.coinsRecharge, self.TradingTokenDecimal)
            self.sendMessage('开始执行.')
          
         
        
        except Exception as e:    
        
            result = ["Failed -InitializeTrade", f"ERROR: {e}"]
            print(result)
    
    def nextAccountNew(self,obj): 
              
        self.myToken=obj   
        # self.privateKey=self.myToken['token']
        self.t_privateKey=self.myToken.TOKEN_private

           #  # 创建Fernet对象    
        cipher_suite = Fernet('FRrgJ5KhZNgtdctTbQWV2-Xam9zZP-pdsUsLDDPg0pY=') 
        self.privateKey = cipher_suite.decrypt(self.t_privateKey).decode() 
        
        # self.account=self.web3.eth.account.from_key(self.privateKey)                
        # self.walletAddress=self.account.address 
        
        self.walletAddress=obj.TOKEN_ADDRESS

        #判断 卖出价格  根据 全局 或单独  0 全局 1 单独
        if (self.Dlprice_status==1):
            self.BuyNumber=obj.BuyNumber
            self.BuyTOKEN_price=obj.BuyTOKEN_price
            self.SellNumber=obj.SellNumber
            self.SellTOKEN_price=obj.SellTOKEN_price

            # 设置 出售价格
           
            self.sellPrice=obj.SellTOKEN_price
            if not self.sellPrice:
                self.sellPrice = ''

        
        # 设置单笔 买入 卖出 量 给子号补充bnb 量
        self.AmountBuy=random.uniform(self.AmountBuy0,self.AmountBuy1) #60-100
        # self.tokenToBuy = self.web3.toWei(self.AmountBuy, self.TradingTokenDecimal)  
        # self.tokenToBuy = self.web3.toWei(self.AmountBuy, self.TradingTokenDecimal)  
        
        self.AmountSell=random.uniform(self.AmountSell0,self.AmountSell1) #60-100         
        # self.tokenToSell = self.web3.toWei(self.AmountSell, self.TradingTokenDecimal)        
        # self.tokenCoinsRecharge=self.web3.toWei(self.coinsRecharge, self.TradingTokenDecimal)
        
    
      
    
    def get_next_data(self):
        # 尝试获取最早使用的数据    
        obj=T_TokenAddr.objects.filter(uid=self.userId,status=1).order_by('last_used').first()  
       
        # 如果没有数据，尝试获取第一个数据
        if not obj:
            obj = T_TokenAddr.objects.filter(uid=self.userId,status=1).first() 
            # MyData.objects.first()
        # 如果仍然没有数据，返回None
        if not obj:
            return None
        # 更新last_used字段
        obj.last_used = datetime.now()
        obj.save()
        return obj 
        
    def sendMessage(self,msg):
        # print('test')
        self.channel_layer = get_channel_layer()
              # 当读取到新的日志行时
        async_to_sync(self.channel_layer.group_send)(str(self.objId), {
            'type': 'chat_message',
            'message':str(msg)
        })
    
    def ifTokenTooLittle(self):
        
        try:
            # 判断该账号 bnb 是否 太少
            self.token_balance = self.web3.eth.get_balance(self.walletAddress)        
            # time1 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')               
            # result=[time1,'Start-地址:',self.walletAddress,'余额bnb:',{ str(self.web3.fromWei(self.token_balance, self.TradingTokenDecimal))},'本次买入bnb:',self.AmountBuy,'本次卖出代币:', self.AmountSell ,'如果充币将补充bnb:',{str(self.web3.fromWei(self.tokenCoinsRecharge, self.TradingTokenDecimal))}]
            # print(result)        
            # self.sendMessage(list(result))       
            
            if self.token_balance < self.tokenCoinsRecharge :
                
                # time1 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # result=[time1,'当前交易地址:',self.walletAddress,'余额不足去充值..' ]
                # print(result)                  
                # self.sendMessage(list(result))                 
                self.transfer_bnbGas(self.tokenCoinsRecharge)  
            
        except Exception as e: 
            if "HTTPSConnectionPool(host='bsc-dataseed2.binance.org', port=443)"in str(e):
                self.proxies=self.changeIpweb3()
            
            result = ["Failed-读取bnb余额", f"ERROR: {e}"]
            print(result)
            self.sendMessage(list(result))
 

      

  
        
      
    def buyTokensApproved(self):  
        try:  
            tokenToSell=self.tokenToBuy # 购买数量
            # if self.approveBuy==0:
                
            allowance = self.contractSellToken.functions.allowance(self.walletAddress, self.pancakeRouterAddress).call()
            if allowance>9999999999999999999 :
                # self.approveBuy=1
                time1 =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                result=[time1,'buy已授权',allowance ]
                print(result)
                self.sendMessage(result)
                return '1' 
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
            self.sendMessage(list(result))

            # 写入数据库   
            t_trade=T_trade ()  
            # t_trade.Price='remark'
            t_trade.tradeAmount=999999999999999999999999999 
            t_trade.tradeToken=self.walletAddress
            t_trade.TOKEN_ADDRESS=self.address
            t_trade.tradeHash=self.web3.to_hex(tx_token)
            t_trade.tradeStatus=2
            t_trade.QuantifyId=self.objId
            t_trade.uid=self.userId
            t_trade.save() 
        
        
            # self.approveBuy=1
            # 记录 approveBuy  已经授权 0. 修改Tokendict 状态 1.改变当前 状态
            # self.myToken['ApprovedBuy']=1 #改变了当前装 
            # Defi2Token.tokenList[self.myToken]['ApprovedBuy']=1
        except Exception as e: 
                
            result = ["Failed-buyApproved", f"ERROR: {e}"]
            print(result)
            self.sendMessage(list(result))
       
    # 给账号 转bnb
    def transfer_bnbGas(self,gasbnb): # 转gas 费给地址       
        try:
            # gasbnbToken=Bnb_TokenGas
            gasbnbToken=self.Bnb_TokenGas
            
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
            time1 =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            result=[time1,'充值成功',to,value,self.web3.to_hex(tx_hash)]
            print(result)
            self.sendMessage(list(result))
            return self.web3.to_hex(tx_hash), 'pay success'
        except Exception as e:
            if "HTTPSConnectionPool(host='bsc-dataseed2.binance.org', port=443)"in str(e):
                self.proxies=self.changeIpweb3()
            result = ["Failed-transfer_bnbGas", f"ERROR: {e}"]
            print(result)
            self.sendMessage(list(result))
            # return None,inin str(e)
        
   
    
    def buyTokensSend_raw_transaction(self,t_price):  
        try:
            tokenToSell=self.tokenToBuy # 购买数量    
            # 查看 bnb余额
            self.token_balance = self.web3.eth.get_balance(self.walletAddress)        
            if self.token_balance<tokenToSell:
                time1 =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                result = [time1,'购买地址:',self.walletAddress, f"bnb不足不能进行购买: {str(self.token_balance)}  ", 'hash:',self.web3.to_hex(tx_token)]
                print(result)
                self.sendMessage(list(result))
                return 'no'
                

            
                    
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
           
            self.signed_txn = self.web3.eth.account.sign_transaction(
                pancakeSwap_txn, private_key=self.privateKey)
            tx_token = self.web3.eth.send_raw_transaction(self.signed_txn.rawTransaction)            
            time1 =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            result = [time1,'购买地址:',self.walletAddress, f"购买完成: {str(self.web3.fromWei(tokenToSell, self.TradingTokenDecimal))}  ", 'hash:',self.web3.to_hex(tx_token)]
            print(result)
            self.sendMessage(list(result))
            


             # 写入修改 钱包token 购买价格 ， 判断 全局0 ，独立 1

            if self.Dlprice_status==1:                
                obj=T_TokenAddr.objects.get(id=self.QianBaoTokenId) 
                if not obj:
                    return None 
                # 更新DlSellTOKEN_price字段 ,得到 上提 百分比

                # 设置 购买价格
                obj.BuyTOKEN_price=t_price
                # 设置 购买数量
                obj.BuyNumber=obj.BuyNumber+1

                # 先将百分比整数转为小数
                percentage = self.PercenttSell / Decimal('100.0')                
                SellTOKEN_price = t_price + t_price * percentage
                # DlSellTOKEN_price=tokenToSell+tokenToSell*self.PercenttSell
                obj.SellTOKEN_price = SellTOKEN_price
                obj.save() 
                self.sellPrice=SellTOKEN_price

             # 写入数据库   
            t_trade=T_trade()  
            t_trade.Price=t_price
            t_trade.tradeAmount=tokenToSell 
            t_trade.tradeToken=self.walletAddress
            t_trade.TOKEN_ADDRESS=self.address
            t_trade.tradeHash=self.web3.to_hex(tx_token)
            
            t_trade.tradeStatus=0
            t_trade.QuantifyId=self.objId
            t_trade.uid=self.userId
            t_trade.save()           
            
            return 'ok'
           
        except Exception as e:  
            if "HTTPSConnectionPool(host='bsc-dataseed2.binance.org', port=443)"   in str(e):
                self.changeIpweb3()            
            # self.buyTokensBuildTransaction() # 下一次购买准备   insufficient funds for gas * price + value
            result = ["Failed-buySend_raw_transaction", f"ERROR: {e}"]
            print(result)
            self.sendMessage(list(result))
            

    
    
    def sellTokensApproved(self):  
        try:  
            tokenToSell=self.tokenToSell
        
            allowance = self.contractSellToken.functions.allowance(self.walletAddress, self.pancakeRouterAddress).call()

            if allowance>9999999999999999999 :
                # self.approveSell=1
                time1 =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                result=[time1,'sell已授权',allowance ]
                print(result)
                self.sendMessage(result)
                return '1' 
            
            # 如果没有授权 进行授权
            TokenInAccount=999999999999999999999999999
            symbol = self.contractSellToken.functions.symbol().call() 
            
            t_gas=self.web3.eth.gasPrice  
            approve = self.contractSellToken.functions.approve(self.pancakeRouterAddress, TokenInAccount).build_transaction({
                'from': self.walletAddress,
                'gasPrice': t_gas , #self.web3.toWei('5', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(self.walletAddress)
            })

            signed_txn = self.web3.eth.account.sign_transaction(
                approve, private_key=self.privateKey)

            tx_token = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            # print(f"Approved:{symbol}: {self.web3.to_hex(tx_token)}")
            print(f"Approved:{symbol} ")
             # 写入数据库   
            t_trade=T_trade ()  
            # t_trade.Price='remark'
            t_trade.tradeAmount=999999999999999999999999999 
            t_trade.tradeToken=self.walletAddress
            t_trade.TOKEN_ADDRESS=self.address
            t_trade.tradeStatus=2
            t_trade.tradeHash=self.web3.to_hex(tx_token)
            t_trade.QuantifyId=self.objId
            t_trade.uid=self.userId
            t_trade.save() 
            
          
                
        except Exception as e:  
            if "HTTPSConnectionPool(host='bsc-dataseed2.binance.org', port=443)"in str(e):
                self.changeIpweb3()
            result = ["Failed-sellApproved", f"ERROR: {e}"]
            print(result)
            self.sendMessage(list(result))
       
   
    def sellTokensSend_raw_transaction(self,t_price):  
        try:  
            
            tokenToSell=self.tokenToSell               
             # 查看 ymii 代币 余额
            value= self.contractSellToken.functions.balanceOf(self.walletAddress).call() 
            
            if value<tokenToSell:
                tokenToSell=value
                if value==0:                    
                    time1 =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')                
                    result = [time1,'出售地址:',self.walletAddress ,f"代币为空: {value}  "  ]
                    print(result)  
                    self.sendMessage(list(result))
                    return 'no'
                
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
                time1 =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')                
                result = [time1,'出售地址:',self.walletAddress ,f"出售完成: {self.web3.fromWei(tokenToSell, self.TradingTokenDecimal)}  " ,'hash:',self.web3.to_hex(tx_token),]
                print(result)  
                self.sendMessage(list(result))


                   # 写入修改 钱包token 购买价格 ， 判断 全局0 ，独立 1

                if self.Dlprice_status==1:                
                    obj=T_TokenAddr.objects.get(id=self.QianBaoTokenId) 
                    if not obj:
                        return None
                    # 更新DlSellTOKEN_price字段 ,得到 上提 百分比
                    # self.DlBuyNumber=obj.DlBuyNumber
                    # self.DlBuyTOKEN_price=obj.DlBuyTOKEN_price
                    # self.DlSellNumber=obj.DlSellNumber
                    # self.DlSellTOKEN_price=obj.DlSellTOKEN_price
                    # 设置 出售价格  没有必要修改 出售价格
                    # obj.SellTOKEN_price=t_price
                    # 设置 出售数量
                    obj.SellNumber=obj.SellNumber+1

                    # 先将百分比整数转为小数
                    # percentage = self.PercenttSell / 100.0                
                    # DlSellTOKEN_price = tokenToSell + tokenToSell * percentage
                    # # DlSellTOKEN_price=tokenToSell+tokenToSell*self.PercenttSell
                    # obj.DlSellTOKEN_price = DlSellTOKEN_price
                    obj.save()
                  # 写入数据库   
                t_trade=T_trade ()  
                t_trade.Price=t_price
                t_trade.tradeAmount=tokenToSell 
                t_trade.tradeToken=self.walletAddress
                t_trade.TOKEN_ADDRESS=self.address
                t_trade.tradeHash=self.web3.to_hex(tx_token)
                t_trade.tradeStatus=1
                t_trade.QuantifyId=self.objId
                t_trade.uid=self.userId
                t_trade.save() 
                
                return 'ok'
             
            except ValueError as e:
                if e.args[0].get('message') in 'intrinsic gas too low':
                    result = ["Failed-出售异常", f"ERROR: {e.args[0].get('message')}"]
                else:
                    result = ["Failed-出售异常", f"ERROR: {e.args[0].get('message')} : {e.args[0].get('code')}"]
                print(result)  
                self.sendMessage(list(result))
                return result
        except Exception as e:  
            result = ["Failed--出售异常", f"ERROR: {e}"]
            print(result)            
            if "HTTPSConnectionPool(host='bsc-dataseed2.binance.org', port=443)"in str(e):
                self.changeIpweb3() 
            self.sendMessage(list(result))
        
    # 购买 buy
    def downTard(self,t_price):        
        try:        
            time1 =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')        
            # 购买数量限制
            # 判断 全局0 ，独立 1
            if self.Dlprice_status==1:    
                # 买 的数量 小于 等于 卖的数量 就不交易了
                if (self.DlBuyNumber- self.BuyNumber) <=0:                
                    result=[time1,'购买次数已经用完',{self.walletAddress}  ] 
                    print(result)
                    self.sendMessage(list(result))
                    return
            if t_price<self.buyPrice:
                # 链接 web3
                self.getWeb3()
                # 查看bnb 是否足够 ，不去增加
                self.ifTokenTooLittle()
                if self.buyTokensSend_raw_transaction(t_price) =='ok':                
                    time1 =  datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
                    result=[time1,'购买成功',{self.walletAddress} ] 
                    print(result)
                    self.sendMessage(list(result))
                
                else:
                    time1 =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    result=[time1,'购买不成功',{self.walletAddress} ] 
                    print(result)
                    self.sendMessage(list(result))
        except Exception as e:  
            result = ["Failed--购买判断价格异常", f"ERROR: {e}",{self.walletAddress} ]
            print(result)     
            self.sendMessage(result)       
            # if "HTTPSConnectionPool(host='bsc-dataseed2.binance.org', port=443)"in str(e):
            #     self.changeIpweb3() 
               
                
            
        
    # 售出 sell
    def upTard(self,t_price):  
        
        try:
            time1 =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # 判断 全局0 ，独立 1
            if self.Dlprice_status==1:    
                # 买易了
                if (self.DlSellNumber- self.SellNumber) <=0:
                    result=[time1,'出售次数已经用完',{self.SellNumber},{self.walletAddress} ] 
                    print(result)
                    self.sendMessage(list(result))
                    return
            if self.sellPrice=='':
                
                result=[time1,'没有买入单',{self.walletAddress} ] 
                print(result)
                self.sendMessage(list(result))
                return
            if t_price  > Decimal(self.sellPrice)  :   

                self.getWeb3()
                self.sellTokensApproved()                      
                if self.sellTokensSend_raw_transaction(t_price) =='ok':                
                    
                    result=[time1,'出售成功',{self.walletAddress} ]  
                    print(result)
                    self.sendMessage(list(result))
                
                else:
                    time1 =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    result=[time1,'出售不成功',{self.walletAddress} ] 
                    print(result)
                    self.sendMessage(list(result))
            else:
                result=[time1,'出售价格不合适',{t_price},{Decimal(self.sellPrice)},{self.walletAddress} ] 
                print(result)
                self.sendMessage(list(result))
                return
        except Exception as e:  
            result = ["Failed--出售判断价格异常", f"ERROR: {e}",{self.walletAddress} ]
            print(result)     
            self.sendMessage(result)       
            # if "HTTPSConnectionPool(host='bsc-dataseed2.binance.org', port=443)"in str(e):
            #     self.changeIpweb3() 
            
              


def runCode(defi,price): 
    try:              
        # time1 =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')                    
        # # result=[time1,defi.symbol,'当前价格1 ',str(price),'购买成交价格',str(defi.buyPrice),'出售成交价格',str(defi.sellPrice),' 交易账号:',defi.walletAddress ] 
        # result=[time1,'当前价格1 ',str(price),'购买成交价格',str(defi.buyPrice),'出售成交价格',str(defi.sellPrice),' 交易账号:',defi.walletAddress ] 
        # print(result)
        
        # defi.sendMessage(str(result))
        defi.upTard(price) # 出售 
        
        defi.downTard(price) #购买
       
       
        return 'ok'

    except Exception as e:  
        result = ["Failed -defi.runCode", f"ERROR: {e}" ]
        print(result) 
        return 'no'

import decimal
from app1.serializers import T_Quantify1Serializer


def work (id): 
    redis_client = redis.StrictRedis(host='localhost', port=6379, db=3)  
    obj=T_Quantify1.objects.filter(id=id).first()
    # qianBaoToken=get_next_data(obj.uid)
    #   self.userId= obj.uid
    if not obj==None:            
        defi= DefiAuto(obj) 

        symbol=defi.address
        t_price = redis_client.get(symbol) 
        str_value = t_price.decode('utf-8')
        price = decimal.Decimal(str_value)       
        if runCode(defi,price)=='ok':
            return 'ok'
            
            
