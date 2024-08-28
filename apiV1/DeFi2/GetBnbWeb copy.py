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
from apiV1.DeFi2.abi import tokenAbi

from apiV1.DeFi2.decimalData import getTokenDecimal
# from abi import tokenAbi
# from decimalData import getTokenDecimal
import requests
import json
import  random 
# import GetTokens,Defi2Token
import datetime
from multiprocessing import Process

from app1.models import  T_TokenAddr  #保存 task id 以后删除
from cryptography.fernet import Fernet


 


# GetBnb Setup
# GuiJiWallter='0x710b2D51882bc32e63619310918183c666650Bd1'

class DefiAuto(object):
    
    def __init__(self):
        
        self.proxies=self.changeIpweb3()    
                        

    
      
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

        
    # def Firfox(self):
    #     self.options = Options()
    #     self.options.headless = True    
    #     self.driver = webdriver.Firefox(executable_path='/root/djangotokens/apiV1/DeFi2/geckodriver', options=self.options,proxy= self.proxiesFirfox)
        
    # 给账号 转bnb
    def GetAllBnb(self,userId,ImputationToken): # 转gas 费给地址       
       
            # 归集地址
            # t_GuiJiWallter=Web3.to_checksum_address(GuiJiWallter)
            t_GuiJiWallter=Web3.to_checksum_address(ImputationToken)     
            T_TokenAddrList=T_TokenAddr.objects.filter(uid=userId,status=1)  
            tokenList=[]
            # for myToken in GetTokens.tokenList: 
            for myToken in T_TokenAddrList: 
                
                t_gasbnbToken=myToken.TOKEN_private   

                # 创建Fernet对象    
                cipher_suite = Fernet('FRrgJ5KhZNgtdctTbQWV2-Xam9zZP-pdsUsLDDPg0pY=') 
                gasbnbToken = cipher_suite.decrypt(t_gasbnbToken).decode() 
                gasAccount=self.web3.eth.account.from_key(gasbnbToken)        
                gasAccountWallet = gasAccount.address   
                # to = Web3.to_checksum_address(to)
                # 归集 bnb 
                gasFee=70000000000000 
                token_balance = self.web3.eth.get_balance(gasAccountWallet) #self.web3.from_wei(self.web3.eth.get_balance(self.wallet), 'ether')
                time.sleep(1)
                # 如果代币不足返回异常                
                if token_balance < gasFee:
                    # str=[f"小于gas {gasFee}"]                    
                    time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    result=[time1,'小于gas',gasFee]
                    tokenList.append(result)
                    print(result)
                    continue 
                value=token_balance-gasFee
                print(token_balance)
                # value=token_balance-gasFee
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
                
                signed_tx = self.web3.eth.account.sign_transaction(tx, gasbnbToken)                
                try:
                    tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)                 
                    time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    result=[time1,'归集成功',t_GuiJiWallter,value,f"token:{gasAccountWallet}",self.web3.to_hex(tx_hash)]
                    tokenList.append(result)
                    print(result)
                except Exception as e:
                    self.proxies=self.changeIpweb3()
                    result = ["Failed-transfer_bnbGas", f"ERROR: {e}"]
                    print(result)
                    continue                  
                    
            result=['全部归集成功',len(tokenList),'个' ]
            print(result)
            return tokenList
     
        
   
   

        
# # 前提是 每个子账号  必须有 bnb 才可以完成
# def ApprovedAll(defi):
#     for myToken in Defi2Token.tokenList:
#         defi.myToken=myToken    
#         defi.privateKey=myToken['token']
#         defi.account=defi.web3.eth.account.from_key(defi.privateKey)                
#         defi.walletAddress=defi.account.address     
#         defi.sellTokensApproved() # 下一次购买准备    
#         # defi.buyTokensApproved() # 下一次购买准备
        
  # 给账号 转Ymii 或其他代币
    def GetAllYmii(self,userId,ImputationToken,TokenAddress): # 转gas 费给地址       
        
        sellTokenAbi = tokenAbi(TokenAddress)
        contractSellToken = self.web3.eth.contract(TokenAddress, abi=sellTokenAbi)    
    
        # 归集地址
        # t_GuiJiWallter=Web3.to_checksum_address(GuiJiWallter)
        
        t_GuiJiWallter=Web3.to_checksum_address(ImputationToken)     
        T_TokenAddrList=T_TokenAddr.objects.filter(uid=userId,status=1)  
        tokenList=[]
        # for myToken in GetTokens.tokenList: 
        for myToken in T_TokenAddrList:  
            # gasbnbToken=myToken.TOKEN_private #myToken['token']  
                
            t_gasbnbToken=myToken.TOKEN_private
            # 创建Fernet对象    
            cipher_suite = Fernet('FRrgJ5KhZNgtdctTbQWV2-Xam9zZP-pdsUsLDDPg0pY=') 
            gasbnbToken = cipher_suite.decrypt(t_gasbnbToken).decode() 
                        
            gasAccount=self.web3.eth.account.from_key(gasbnbToken)        
            gasAccountWallet = gasAccount.address   
            # to = Web3.to_checksum_address(to)
            # 归集 bnb 
            gasFee=70000000000000 
            
            # 查看 ymii 余额
            value= contractSellToken.functions.balanceOf(gasAccountWallet).call() 
            amount=value
            
            if value==0:            
                time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                result=[time1,'代币为0:',t_GuiJiWallter,amount,'token:',gasAccountWallet]
                tokenList.append(result)
                print(result)
                continue
                
            
            nonce = self.web3.eth.get_transaction_count(gasAccountWallet)
            # amount=self.web3.to_wei(value, 'ether')
            t_gas=self.web3.eth.gas_price
           
            # t_gas=self.web3.eth.gas_price
            # Build a transaction that invokes this contract's function, called transfer
            token_txn = contractSellToken.functions.transfer(self.web3.to_checksum_address(t_GuiJiWallter), amount,).build_transaction({
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
        return tokenList        
            
from django.contrib.auth.decorators import login_required
# 前提是 每个子账号  必须有 bnb 才可以完成
@login_required
def GetBnb(request,ImputationToken):
    acct=request.user   
    
    defi= DefiAuto()
    listToken=defi.GetAllBnb(acct.id,ImputationToken)
    return listToken
        
 
 
@login_required
def GetYmii(request,ImputationToken,TokenAddress):
    acct=request.user  
    defi= DefiAuto()
    listToken=defi.GetAllYmii(acct.id,ImputationToken,TokenAddress)
    return listToken
   