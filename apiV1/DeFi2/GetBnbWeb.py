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

import asyncio
from asgiref.sync import sync_to_async

 


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

    async def process_token(self, myToken, t_GuiJiWallter):
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
            result=[time1,'小于gas',gasFee,'token:',gasAccountWallet]
            # tokenList.append(result)
            print(result)
            return result
            # continue 
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
            # tokenList.append(result)
            print(result)
            return result
        except Exception as e:
            if "HTTPSConnectionPool(host='bsc-dataseed2.binance.org', port=443)"in str(e):
                self.proxies=self.changeIpweb3()
            #   self.proxies=self.changeIpweb3()
            result = ["Failed-transfer_bnbGas", f"ERROR: {e}"]
            print(result)
            return result                  


    # 给账号 转bnb
    async def GetAllBnb(self,userId,ImputationToken,T_TokenAddrList): # 转gas 费给地址       
       
        # 归集地址
        # t_GuiJiWallter=Web3.to_checksum_address(GuiJiWallter)
        t_GuiJiWallter=Web3.to_checksum_address(ImputationToken)    

            # 使用 asyncio.gather 并行处理每个 token
        results = await asyncio.gather(
            *[self.process_token(token, t_GuiJiWallter) for token in T_TokenAddrList]
        )

        
        # result='全部归集成功'+str(len(results))+'个' 
        print(results)
        return results
    




    # async def process_token_price(self, myToken, t_GuiJiWallter):
    async def process_token_price(self, myToken):        
        try:          
            gasAccountWallet=myToken.TOKEN_ADDRESS              
            # to = Web3.to_checksum_address(to)            
            token_balance = self.web3.eth.get_balance(gasAccountWallet) #self.web3.from_wei(self.web3.eth.get_balance(self.wallet), 'ether')
            time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            result=[time1,f"token:{gasAccountWallet}",'price',token_balance,]
            # tokenList.append(result)
            print(result)
            return result
        except Exception as e:
            if "HTTPSConnectionPool(host='bsc-dataseed2.binance.org', port=443)"in str(e):
                self.proxies=self.changeIpweb3()
            #   self.proxies=self.changeIpweb3()
            result = ["Failed-transfer_bnbGas", f"ERROR: {e}"]
            print(result)
            return result                  

    
     # 给账号 转bnb
    async def GetAllBnbPrice(self,userId,T_TokenAddrList): # 转gas 费给地址       
       
        # 归集地址
        # t_GuiJiWallter=Web3.to_checksum_address(GuiJiWallter)
        # t_GuiJiWallter=Web3.to_checksum_address(ImputationToken)    

            # 使用 asyncio.gather 并行处理每个 token
        results = await asyncio.gather(
            *[self.process_token_price(token) for token in T_TokenAddrList]
        )        
        # result='全部归集成功'+str(len(results))+'个' 
        print(results)
        return results
    
    
    async def process_tokenOther_price(self, myToken,contractSellToken):        
        try:          
            gasAccountWallet=myToken.TOKEN_ADDRESS              
            # to = Web3.to_checksum_address(to)           
            token_balance= contractSellToken.functions.balanceOf(gasAccountWallet).call() 
 
            # token_balance = self.web3.eth.get_balance(gasAccountWallet) #self.web3.from_wei(self.web3.eth.get_balance(self.wallet), 'ether')
            time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            result=[time1,f"token:{gasAccountWallet}",'price',token_balance,]
            # tokenList.append(result)
            print(result)
            return result
        except Exception as e:
            if "HTTPSConnectionPool(host='bsc-dataseed2.binance.org', port=443)"in str(e):
                self.proxies=self.changeIpweb3()
            #   self.proxies=self.changeIpweb3()
            result = ["Failed-transfer_bnbGas", f"ERROR: {e}"]
            print(result)
            return result   
        
    
       # 给账号 转bnb
    async def GetAllOtherPrice(self,userId,TokenAddress,T_TokenAddrList): # 转gas 费给地址    
        
        sellTokenAbi = tokenAbi(TokenAddress)
        contractSellToken = self.web3.eth.contract(TokenAddress, abi=sellTokenAbi)       
       
        # 归集地址
        # t_GuiJiWallter=Web3.to_checksum_address(GuiJiWallter)
        # t_GuiJiWallter=Web3.to_checksum_address(ImputationToken)    

            # 使用 asyncio.gather 并行处理每个 token
        results = await asyncio.gather(
            *[self.process_tokenOther_price(token,contractSellToken) for token in T_TokenAddrList]
        )        
        # result='全部归集成功'+str(len(results))+'个' 
        print(results)
        return results
   

        
# # 前提是 每个子账号  必须有 bnb 才可以完成
# def ApprovedAll(defi):
#     for myToken in Defi2Token.tokenList:
#         defi.myToken=myToken    
#         defi.privateKey=myToken['token']
#         defi.account=defi.web3.eth.account.from_key(defi.privateKey)                
#         defi.walletAddress=defi.account.address     
#         defi.sellTokensApproved() # 下一次购买准备    
#         # defi.buyTokensApproved() # 下一次购买准备


    async def process_tokenYmii(self, myToken, t_GuiJiWallter,contractSellToken):
        t_gasbnbToken=myToken.TOKEN_private   
        # tokenList=[]
        # for myToken in GetTokens.tokenList: 
        # for myToken in T_TokenAddrList:  
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
            # tokenList.append(result)
            print(result)
            return result
            
        
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
            # tokenList.append(result)
            print(result)
            return result
        except Exception as e:
            if "HTTPSConnectionPool(host='bsc-dataseed2.binance.org', port=443)"in str(e):
                self.proxies=self.changeIpweb3()
            #   self.proxies=self.changeIpweb3()
            result = ["Failed-transfer_bnbGas", f"ERROR: {e}"]
            print(result)
            return result                

        
  # 给账号 转Ymii 或其他代币
    async def GetAllYmii(self,userId,ImputationToken,TokenAddress,T_TokenAddrList): # 转gas 费给地址       
        
        sellTokenAbi = tokenAbi(TokenAddress)
        contractSellToken = self.web3.eth.contract(TokenAddress, abi=sellTokenAbi)    
    
        # 归集地址
        # t_GuiJiWallter=Web3.to_checksum_address(GuiJiWallter)
        
        t_GuiJiWallter=Web3.to_checksum_address(ImputationToken)     
        # T_TokenAddrList=T_TokenAddr.objects.filter(uid=userId,status=1)  


        results = await asyncio.gather(
            *[self.process_tokenYmii(token, t_GuiJiWallter,contractSellToken) for token in T_TokenAddrList]
        )

        # result=['全部归集成功',len(results),'个' ]
        # result='全部归集成功'+str(len(results))+'个' 
        print(results)
        return results
                
        # result=['全部归集成功',len(tokenList),'个' ]
        # print(result)
        # return tokenList        
            
from django.contrib.auth.decorators import login_required
# 前提是 每个子账号  必须有 bnb 才可以完成
@login_required
def GetBnb(request,ImputationToken,token_private_list):
    acct=request.user   
    
    defi= DefiAuto()
    

    # T_TokenAddrList=T_TokenAddr.objects.filter(uid=acct.id,status=1) 
    # token_private_list = [obj  for obj in T_TokenAddrList]

    results = asyncio.run(defi.GetAllBnb(acct.id, ImputationToken,token_private_list))

    return results
        
 
 
@login_required
def GetYmii(request,ImputationToken,TokenAddress,token_private_list):
    acct=request.user  
    defi= DefiAuto()

    # T_TokenAddrList=T_TokenAddr.objects.filter(uid=acct.id,status=1)  
    # token_private_list = [obj  for obj in T_TokenAddrList]



    results = asyncio.run(defi.GetAllYmii(acct.id,ImputationToken,TokenAddress,token_private_list))

    
    # listToken=defi.GetAllYmii(acct.id,ImputationToken,TokenAddress,token_private_list)
    return results



@login_required
def GetBnbPrice(request,token_private_list):
    acct=request.user       
    defi= DefiAuto()
    # T_TokenAddrList=T_TokenAddr.objects.filter(uid=acct.id,status=1) 
    # token_private_list = [obj  for obj in T_TokenAddrList]
    results = asyncio.run(defi.GetAllBnbPrice(acct.id, token_private_list))
    return results

@login_required
def GetOtherPrice(request,tokenAddress,token_private_list):
    acct=request.user       
    defi= DefiAuto()
    # T_TokenAddrList=T_TokenAddr.objects.filter(uid=acct.id,status=1) 
    # token_private_list = [obj  for obj in T_TokenAddrList]
    results = asyncio.run(defi.GetAllOtherPrice(acct.id, tokenAddress,token_private_list))
    return results

@login_required
def GetTokenAddress(request,TOKEN_private):
    # acct=request.user       
    try:
        defi= DefiAuto()
                # 创建Fernet对象    
        cipher_suite = Fernet('FRrgJ5KhZNgtdctTbQWV2-Xam9zZP-pdsUsLDDPg0pY=') 
        gasbnbToken = cipher_suite.decrypt(TOKEN_private).decode() 
        gasAccount=defi.web3.eth.account.from_key(gasbnbToken)        
        gasAccountWallet = gasAccount.address  
    except Exception as e:
        if "HTTPSConnectionPool(host='bsc-dataseed2.binance.org', port=443)"in str(e):
            defi.proxies=defi.changeIpweb3()
        #   self.proxies=self.changeIpweb3()
        result = ["Failed-transfer_bnbGas", f"ERROR: {e}"]
        print(result)
        return result           
        
    # results = asyncio.run(defi.GetAllOtherPrice(acct.id, tokenAddress,token_private_list))
    return gasAccountWallet




   