# -*- coding: utf-8 -*-
# ebc 体现功能
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
from decimal import Decimal
from app1.models import  T_TokenAddr  #保存 task id 以后删除
from cryptography.fernet import Fernet

import asyncio
from asgiref.sync import sync_to_async

from reg.ebcFenRun import tiXianOksql
from decouple import config
import threading
import logging


# GetBnb Setup
# GuiJiWallter='0x710b2D51882bc32e63619310918183c666650Bd1'

class DefiAuto(object):
    
    def __init__(self):        
        self.proxies=self.changeIpweb3()     
        self.nonce_lock = threading.Lock()
  
    def changeIpweb3(self):
        # proxies=self.changeIp()        
        # bsc = "https://bsc-dataseed2.binance.org/"              
        # # self.web3 = Web3(Web3.HTTPProvider(bsc))        
        # self.web3 = Web3(Web3.HTTPProvider(bsc,request_kwargs=proxies)) 
        
        
            # 初始化 Web3 连接
        bsc =config('BSC', default='')  #"https://rpc.ankr.com/bsc/174ba138f2cbc5773ef292c0e0a941ec3f23246439e9f0b8d7bec242a67f8c20"  #免费
    
        self.web3 = Web3(Web3.HTTPProvider(bsc))
        # self.web3.is_connected()
        
        t_num=0
        while not self.web3.is_connected(): 
            if t_num>2:
                break
            t_num=t_num+1
            time.sleep(1)
            print("Not Connected to BSC wait  TiXian...")            
            self.proxies=self.changeIpweb3()        
        print("Connected to BSC")        
        return self.web3
    
    # def changeIp(self):
        
    #     # ips='http://api.haiwaiip.com/api/pull?token=c10a444f7800613d326178a5e18e224c&num='+str(1)+'&format=json&protocol=http&country=sg&state=&city=&ip_type=datacenter&sep=3&area='
    #     ips='http://api.haiwaiip.com/api/pull?token=809fca7ecb467aafc033528723789277&num=1&format=json&protocol=http&country=sg&state=&city=&ip_type=datacenter&sep=2&area='
    #     resp = requests.get(ips) 

    #     data = resp.text

    #     data_dict = json.loads(data)   
        
    #     proxy = data_dict['data'][0]
    
    #     proxies={"proxies":{'https' : proxy, 'http' : proxy }}
        
    #     return proxies
    
    
    
    def isTxhash(self,tx_hash):        
        try:        
            receipt = self.web3.eth.getTransactionReceipt(tx_hash) 
            if receipt['status'] == 1:
                status = 3 #hash 返回成功
                revert_reason='ok'
            else:
                status = 2  #hash 返回失败            
                # revert_reason='ok'
                try:
                    revert_reason = self.web3.toText(receipt['logs'][0]['data']).decode('latin-1', 'replace')
                except UnicodeDecodeError:
                    revert_reason = "no"
        
        except Exception as e:
                    # 捕获异常并输出错误信息
            print(f"userTiXianHash  : {e}")
                


        # revert_reason = self.web3.toText(receipt['logs'][0]['data'])
        result=[status,revert_reason]
        return result
    
    def get_nonce(self, gas_account_wallet):
        with self.nonce_lock:
            nonce = self.web3.eth.get_transaction_count(gas_account_wallet)
        return nonce
        
    
        
 

    # 给t_GuiJiWallter  账号转代币
    def process_tokenYmii(self,amount,t_GuiJiWallter,contractSellToken):         
        amount = Decimal(amount) * Decimal('1000000000000000000')        
        amount = int(amount)  
        # t_TOKEN_private=config('TOKEN_private', default=''),      
        
        
        t_TOKEN_private = config('TOKEN_private', default='')
        gasAccount = self.web3.eth.account.from_key(bytes.fromhex(t_TOKEN_private))
 
   
        # gasAccount=self.web3.eth.account.from_key(my_bytes)        
        gasAccountWallet = gasAccount.address   
        # to = Web3.to_checksum_address(to)
        # 归集 bnb 
        gasFee=70000000000000 
        
        # 查看  余额
        value= contractSellToken.functions.balanceOf(gasAccountWallet).call() 
        # amount=value
        
        if value<amount:            
            time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            result = {'time': time1, 
                        'status': 0, #返回hash
                        'tokenAdress':t_GuiJiWallter,
                        'amount':amount,
                        # 'hashInfo':isTxhash[1],
                        # 'txhash':self.web3.to_hex(tx_hash),
                        }    
             
            # result=[time1,'代币不足:',t_GuiJiWallter,':',value]
            # tokenList.append(result)
            print(result)
            return result
            
        nonce = self.get_nonce(gasAccountWallet)

        # nonce = self.web3.eth.get_transaction_count(gasAccountWallet)
        # amount=self.web3.to_wei(value, 'ether')
        t_gas=self.web3.eth.gas_price    
        gas_limit = 700000  # 适当调整 Gas 上限，根据合约的复杂性和执行情况  3000000000
    
     
        maxPriorityFeePerGas = self.web3.eth.max_priority_fee
        max_priority_fee_half = self.web3.eth.max_priority_fee // 2

        
        token_txn = contractSellToken.functions.transfer(self.web3.to_checksum_address(t_GuiJiWallter), amount,).build_transaction({
        # token_txn = contractSellToken.functions.transfer(self.web3.to_checksum_address(t_GuiJiWallter), amount,).build_transaction({
        'chainId': 56,
        'gas': gas_limit,
        # 'gasPrice': t_gas,
        'nonce': nonce,
        'maxFeePerGas': t_gas + max_priority_fee_half,
        'maxPriorityFeePerGas': max_priority_fee_half,
        })            
        signed_txn = self.web3.eth.account.sign_transaction(token_txn, private_key=t_TOKEN_private) 
        try: 
            tx_hash=self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            time.sleep(2)
            time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            result = {'time': time1, 
                            'status': 1, #返回hash
                            'tokenAdress':t_GuiJiWallter,
                            'amount':amount,
                            # 'hashInfo':isTxhash[1],
                            'txhash':self.web3.to_hex(tx_hash),
                            }    
            
            # isTxhash=self.isTxhash(tx_hash)
            # if isTxhash[0]== 'Success':
            #     result = {'time': time1, 
            #                    'status': True,
            #                    'tokenAdress':t_GuiJiWallter,
            #                    'amount':amount,
            #                    'hashInfo':isTxhash[1],
            #                    'txhash':self.web3.to_hex(tx_hash),
            #                    }
            #     # result=[time1,'转入失败:',isTxhash[1],t_GuiJiWallter,amount,'token:',self.web3.to_hex(tx_hash)]                
            # else:
            #     result = {'time': time1, 
            #                 'status': False,
            #                 'tokenAdress':t_GuiJiWallter,
            #                 'amount':amount,
            #                 'hashInfo':isTxhash[1],
            #                 'txhash':self.web3.to_hex(tx_hash),
            #                 }                 
            print(result)
            return result
        except Exception as e:
            if "HTTPSConnectionPool(host='bsc-dataseed2.binance.org', port=443)"in str(e):
                self.proxies=self.changeIpweb3()
            #   self.proxies=self.changeIpweb3()
            result = [False,"Failed-zhuanZhang", f"ERROR: {e}"]
             # 记录异常信息到日志中
            logging.error(f"Err:userTiXian: {e}")
            # logging.info(f"userTiXian start....: ")   
            print(result)
            # return result                

 
     
    # 给账号 转Ymii 或其他代币
    def ebcTixianGo(self,amount,tiXianWallter,contractTokenAddress): # 转gas 费给地址       
        Web3.to_checksum_address
        sellTokenAbi = tokenAbi(contractTokenAddress)
        contractSellToken = self.web3.eth.contract(contractTokenAddress, abi=sellTokenAbi)
        t_tiXianWallter=Web3.to_checksum_address(tiXianWallter)            
        results =self.process_tokenYmii(amount, t_tiXianWallter,contractSellToken)
        # results = await asyncio.gather(
        #     self.process_tokenYmii(amount, t_GuiJiWallter,contractSellToken) 
        # )
        # results = await asyncio(
        #     self.process_tokenYmii(amount, t_tiXianWallter,contractSellToken) 
        # )

        # result=['全部归集成功',len(results),'个' ]
        # result='全部归集成功'+str(len(results))+'个' 
        # print(results)
        return results
                
        # result=['全部归集成功',len(tokenList),'个' ]
        # print(result)
        # return tokenList        
        
# @login_required
def dfEbcTixian(amount,tiXianWallter,contractTokenAddress):
   
    try:
        defi= DefiAuto() 
        results = defi.ebcTixianGo(amount,tiXianWallter,contractTokenAddress)
        return results
         

    except Exception as e:
        if "HTTPSConnectionPool(host='bsc-dataseed2.binance.org', port=443)"in str(e):
            defi.proxies=defi.changeIpweb3()
        #   self.proxies=self.changeIpweb3()
        result = ["Failed-transfer_bnbGas", f"ERROR: {e}"]
        print(result)
        return result           
        


# @login_required
def txhash(txhash):   
    try:
        defi= DefiAuto()
        # results="执行中请等待。。。"
        results = defi.isTxhash(txhash)
        return results
         

    except Exception as e:
        if "HTTPSConnectionPool(host='bsc-dataseed2.binance.org', port=443)"in str(e):
            defi.proxies=defi.changeIpweb3()
        #   self.proxies=self.changeIpweb3()
        result = ["Failed-transfer_bnbGas", f"ERROR: {e}"]
        print(result)
        return result   