from web3 import Web3
import json
import time
import os
import logging
# from django.conf import settings
from decimal import Decimal
from threading import Timer
import tokens
from threading import Thread
from multiprocessing import Process
from abi import tokenAbi
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests

class PayEthOrToken(object):
    
    def __init__(self,wallet_key):
        # 设置web3
        # bsc = "https://bsc-dataseed1.binance.org/"      
        # self.web3 = Web3(Web3.HTTPProvider(bsc))     
        self.proxies=self.changeIpweb3()   
        # token合约地址
        # self.contract_address = '0x55d398326f99059fF775485246999027B3197955' #usdt
        self.contract_address = '0x768a62a22b187EB350637e720ebC552D905c0331' #ymii
        # 主钱包地址
        self.account=self.web3.eth.account.from_key(wallet_key)        
        self.wallet = self.account.address        
        # 钱包的私钥
        self.wallet_key = wallet_key
        # 合约的abi test.json 是eth的abi json文件，可以在eth区块链浏览器上获得
        # with open('ymii.json', 'r') as f:
        # path1='D:\dk\github\dk38\ymiiTools\ymii.json'
        # with open(path1, 'r') as f:
        #     self.abi = json.loads(f.read())
        # 生成合约
        self.abi = tokenAbi(self.contract_address, self.driver)
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=self.abi)
        # 代币简写
        self.token_name = 'ymii'
        toAddr='0x16c62dD94E7594b2Fcf90663FB5ed4C5eac30220'
        self.to=toAddr
        self.litte=10000000000000000
        self.gasYmii=80000
        self.gasBnb=21000
        
        self.changeIpFirfox()
        self.Firfox()
        
        # self.token_name = 'usdt'
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

    def transfer_usdt(self,gasbnb):       
        try:
            
            to=self.to
            value= self.contract.functions.balanceOf(self.wallet).call()  
            #  value= self.contract.functions.balanceOf(self.wallet).call()  
            if value<self.litte:
                return "小于1"
            
            self.transfer_bnbGas(gasbnb)
             
            nonce = self.web3.eth.get_transaction_count(self.wallet)
            # amount=self.web3.to_wei(value, 'ether')
            t_gas=self.web3.eth.gas_price
             
            # 测算 gas 量
            # estimate = self.web3.eth.estimate_gas({
            #     'to':   to, 
            #     'from': self.wallet, 
            #     'value': value})
            # gasBnb=estimate*t_gas
            # t_gas=70000000000000
            # gasBnb= 70000000000000*3
            # self.transfer_bnbGas(gasBnb)
            
            amount=value
            t_gas=self.web3.eth.gas_price
            # Build a transaction that invokes this contract's function, called transfer
            token_txn = self.contract.functions.transfer(self.web3.to_checksum_address(to), amount,).build_transaction({
                'chainId': 56,
                'gas': self.gasYmii,
                'gasPrice': t_gas,
                'nonce': nonce,
                })            
            signed_txn = self.web3.eth.account.sign_transaction(token_txn, private_key=self.wallet_key)
            tx_hash=self.web3.eth.send_raw_transaction(signed_txn.rawTransaction) 
            return self.web3.to_hex(tx_hash), 'pay success' 
        except Exception as e:
            logging.error(f'转账{self.token_name}代币时发生异常：{e}')
            logging.exception(e)
            return None, str(e)

    
    def transfer_bnbGas(self,gasbnb): # 转gas 费给地址       
        try:
            gasbnbToken='9c94be624fc0b0527dfd0db70c0b70d4180e290e30e9c13f688a01fe84e4a5be'
            gasAccount=self.web3.eth.account.from_key(gasbnbToken)        
            gasAccountWallet = gasAccount.address  
            
            value=gasbnb
            
            # to = Web3.to_checksum_address(to)
            to=Web3.to_checksum_address(self.wallet)
            
            # estimate = self.web3.eth.estimate_gas({
            #     'to':   to, 
            #     'from': gasAccountWallet, 
            #     'value': value})
            # gasBnb=estimate*t_gas
            
            
            t_gas=self.web3.eth.gas_price
            # nonce = self.web3.eth.get_transaction_count(self.wallet)
            
            nonce = self.web3.eth.get_transaction_count(gasAccountWallet)
            tx = {
                'nonce': nonce,
                'to': to,
                'gas': self.gasBnb,
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
            return self.web3.to_hex(tx_hash), 'pay success'
        except Exception as e:
            logging.error(f'转账eth时发生异常：{e}')
            logging.exception(e)
            return None, str(e)
        

   
            

def main():    
    # b="0"
    # print("输入2开始继续")
    # b = input("input:")  
    while 1:
        gasB=70000000000000*4
        t_i=0        
        for colour in tokens.colours:  
            t_i=t_i+1                    
            # 处理 转账  bnb 进入  ymii 转出                
            locals()['PayEthOrToken_'+str(t_i)] = PayEthOrToken(colour)
            re=locals()['PayEthOrToken_'+str(t_i)].transfer_usdt(gasB)
            print(re)    

if __name__ == '__main__':    
    main()

    
   
    








