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

ebcOld_TOKEN_ADDRESS = '0xccaD64E05A10892d192972a0BCd81a87BdbC6293' 
newEbc_TOKEN_ADDRESS = '0x10E5a77Af4AB39eEF8393fCb2f8cfDe1971857Fb' 
 


# GetBnb Setup   
GuiJiWallter='0x710b2D51882bc32e63619310918183c666650Bd1'
# maticKey='3fa006e4aec07ced87b05765417fea8e4f2ac1b2c1fb2818dfe49276bf9546f1'
maticKey='0x4a66298d14ab7c50973e5ffe066b560e0b171337d721ad6b10e1886ff59ef0eb'

class DefiAuto(object):    
    def __init__(self):        
        # self.proxies=self.changeIpweb3()    
        bsc ='https://rpc.ankr.com/polygon/145b63c3aa3fc77ce3d05be2c9f1caba16322f6957f8c975d05da3fe08c110f5'    
        self.web3 = Web3(Web3.HTTPProvider(bsc)) 
      
        self.TokenToSellAddress = self.web3.to_checksum_address(ebcOld_TOKEN_ADDRESS)
        self.newTokenToSellAddress = self.web3.to_checksum_address(newEbc_TOKEN_ADDRESS)
 
        
        try:
          
            sellTokenAbi = tokenAbi(self.TokenToSellAddress) 
            newTokenToSellAddressAbi = tokenAbi(self.newTokenToSellAddress ) 
            
            self.contractSellToken = self.web3.eth.contract(self.TokenToSellAddress, abi=sellTokenAbi)                    
            self.contractNewSellToken = self.web3.eth.contract(self.newTokenToSellAddress, abi=newTokenToSellAddressAbi)
          
        
        except Exception as e:    
            result = ["Failed -InitializeTrade", f"ERROR: {e}"]
            print(result) 
      
     # 给账号 转bnb
    def oldEbc2NewEbc(self): # 转gas 费给地址       
       
            # 归集地址
            # t_GuiJiWallter=Web3.to_checksum_address(GuiJiWallter)           
                       
            maticKeyAddr=self.web3.eth.account.from_key(maticKey)   
            # maticKeyAddr.address
           
                
            variables_list = []
            tokenList=[]
            for myToken in GetTokens.tokenList: 
                # gasbnbToken=myToken['token']                
                # gasAccount=self.web3.eth.account.from_key(gasbnbToken)      
                gasAccountWallet = self.web3.to_checksum_address(myToken['token'])
  
                # gasAccountWallet = myToken['token']    
                # to = Web3.to_checksum_address(to)
               
                # 查看 ymii 余额
                _userStakeA= self.contractSellToken.functions._userStakeA(gasAccountWallet).call() 
                _userStakeB= self.contractSellToken.functions._userStakeB(gasAccountWallet).call() 
                _userStakeStartTime= self.contractSellToken.functions._userStakeStartTime(gasAccountWallet).call() 
                _userLastClaimTime= self.contractSellToken.functions._userLastClaimTime(gasAccountWallet).call() 
                _userEndClaimTime= self.contractSellToken.functions._userEndClaimTime(gasAccountWallet).call() 
                _userStakeTime= self.contractSellToken.functions._userStakeTime(gasAccountWallet).call() 
                _userMoonClaimTime= self.contractSellToken.functions._userMoonClaimTime(gasAccountWallet).call() 
                _userMoonClaimNumber= self.contractSellToken.functions._userMoonClaimNumber(gasAccountWallet).call() 
               
                
                # 第一组变量
                group1 = {
                        'userAddr': gasAccountWallet,
                        '_userStakeA': _userStakeA,
                        '_userStakeB': _userStakeB,
                        '_userStakeStartTime': _userStakeStartTime,
                        '_userLastClaimTime': _userLastClaimTime,
                        '_userEndClaimTime': _userEndClaimTime,
                        '_userStakeTime': _userStakeTime,
                        '_userMoonClaimTime': _userMoonClaimTime,
                        '_userMoonClaimNumber': _userMoonClaimNumber,
                        }
                variables_list.append(group1)  
                nonce = self.web3.eth.get_transaction_count(maticKeyAddr.address)
                # amount=self.web3.to_wei(value, 'ether')
                t_gas=self.web3.eth.gas_price
                # amount=value
                # t_gas=self.web3.eth.gas_price
                # Build a transaction that invokes this contract's function, called transfer
                token_txn = self.contractNewSellToken.functions.stakeTestSet(
                        group1['userAddr'],
                        group1['_userStakeA'], 
                        group1['_userStakeB'], 
                        group1['_userStakeStartTime'],  
                        group1['_userLastClaimTime'],
                        group1['_userEndClaimTime'], 
                        group1['_userStakeTime'], 
                        group1['_userMoonClaimTime'], 
                        group1['_userMoonClaimNumber'], 
                        ).build_transaction({
                    'chainId': 137,
                    'gas': 6000000,
                    'gasPrice': t_gas,
                    'nonce': nonce,
                    })            
                signed_txn = self.web3.eth.account.sign_transaction(token_txn, private_key=maticKey)
                
                try:
                    tx_hash=self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)             
                
                    time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    result=[time1,'数据转移成功:',group1['userAddr'],group1['_userStakeA'],'token:',gasAccountWallet,self.web3.to_hex(tx_hash)]
                    tokenList.append(result)
                    print(result)
                    
                    time.sleep(30)

                except Exception as e:
                    # self.proxies=self.changeIpweb3()
                    result = ["Failed-transfer_bnbGas", f"ERROR: {e}"]
                    print(result)
                    continue                
                    
            result=['全部数据转移',len(tokenList),'个' ]
            print(result)
            return 'ok'
   
               
    # # 给账号 转bnb
    # def GetAllBnb(self): # 转gas 费给地址       
    #     try:
    #         # 归集地址
    #         t_GuiJiWallter=Web3.to_checksum_address(GuiJiWallter)
    #         tokenList=[]
    #         for myToken in GetTokens.tokenList: 
    #             gasbnbToken=myToken['token']                
    #             gasAccount=self.web3.eth.account.from_key(gasbnbToken)        
    #             gasAccountWallet = gasAccount.address   
    #             # to = Web3.to_checksum_address(to)
    #             # 归集 bnb 
    #             gasFee=70000000000000 
    #             token_balance = self.web3.eth.get_balance(gasAccountWallet) #self.web3.from_wei(self.web3.eth.get_balance(self.wallet), 'ether')
    #             time.sleep(1)
    #             # 如果代币不足返回异常
    #             # if Decimal(token_balance) < Decimal(value):
    #             if token_balance < gasFee:
    #                 str=["小于gas{vule}"]
    #                 print(str)
    #                 break 
    #             value=token_balance-gasFee
    #             t_gas=self.web3.eth.gasPrice  
    #             nonce = self.web3.eth.get_transaction_count(gasAccountWallet)
    #             tx = {
    #                 'nonce': nonce,
    #                 'to': t_GuiJiWallter,
    #                 'gas': 21000,
    #                 # 'gasPrice': self.web3.to_wei('50', 'gwei'),
    #                 'gasPrice': t_gas,
    #                 # 'value': self.web3.to_wei(value, 'ether'),
    #                 'value': value,
    #                 'chainId': 56
    #             }
    #             # 签名交易
    #             # signed_tx = self.web3.eth.account.sign_transaction(tx, self.wallet_key)
    #             signed_tx = self.web3.eth.account.sign_transaction(tx, gasbnbToken)
    #             tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction) 
               
    #             time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #             result=[time1,'归集成功',t_GuiJiWallter,value,self.web3.to_hex(tx_hash)]
    #             tokenList.append(result)
    #             print(result)
    #         result=[time1,'全部归集成功',len(tokenList),'个' ]
    #         print(result)
    #         return 'ok'
    #     except Exception as e:
    #         self.proxies=self.changeIpweb3()
    #         result = ["Failed-transfer_bnbGas", f"ERROR: {e}"]
    #         print(result)
    #         return result
    #         # return None, str(e)
        
   
   

        
# # 前提是 每个子账号  必须有 bnb 才可以完成
# def ApprovedAll(defi):
#     for myToken in Defi2Token.tokenList:
#         defi.myToken=myToken    
#         defi.privateKey=myToken['token']
#         defi.account=defi.web3.eth.account.from_key(defi.privateKey)                
#         defi.walletAddress=defi.account.address     
#         defi.sellTokensApproved() # 下一次购买准备    
#         # defi.buyTokensApproved() # 下一次购买准备    



def getOld():
    # 得到old数据列表    
    print('abc')
    defi= DefiAuto()
    defi.oldEbc2NewEbc() 
    
if __name__ == "__main__":
    getOld()
    # GetYmii()
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
 
    
