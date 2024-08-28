
import json
import requests
from web3 import Web3
# import config
from .abi import tokenAbi
# from config import EbcContractTokenAddress
from decouple import config

 
def userTuichu(username):
    
    try:
        # 合约地址和 ABI
        # pancakeRouterAddress = config.EbcState_ADDRESS 
        pancakeRouterAddress = config('EbcState_ADDRESS', default='')
        pancakeAbi = tokenAbi(pancakeRouterAddress)  # 合约 ABI
        # owner 账户的私钥  0xBB8f45851f2c7EE4c03961E9D1Fb1E2C13AE82B8
        # owner_private_key = "13276bf700ca50688c13b3c55337dcbcebcea653d1fb49303a991c6a241cdb2d"
        owner_private_key = config('TOKEN_private', default='')
        # 初始化 Web3 连接
        # bsc = "https://rpc.ankr.com/bsc/174ba138f2cbc5773ef292c0e0a941ec3f23246439e9f0b8d7bec242a67f8c20"  #免费
        bsc=config('BSC', default='')
    
        web3 = Web3(Web3.HTTPProvider(bsc))
        if not web3.is_connected(): 
            print("Not Connected to BSC wait...")    
            return 'Not Connected to BSC'
           

        # 实例化合约
        contractPancake = web3.eth.contract(address=pancakeRouterAddress, abi=pancakeAbi)
        
        # address = '0xbb8f45851f2c7ee4c03961e9d1fb1e2c13ae82b8'
        username = web3.to_checksum_address(username)

        # 要调用的合约方法
        method_to_call = contractPancake.functions.ownerSetUserStakeAB0(username)  # 传入 username 参数

        # owner 账户地址
        gasAccount=web3.eth.account.from_key(owner_private_key)        
        # gasAccountWallet = gasAccount.address   
        # to = Web3.to_checksum_address(to)
        owner_address =web3.to_checksum_address(gasAccount.address)  #"0xBB8f45851f2c7EE4c03961E9D1Fb1E2C13AE82B8"

        # 获取当前 nonce
        nonce = web3.eth.getTransactionCount(owner_address)
        
        # 获取当前建议的 gas 价格
        gas_price = web3.eth.gas_price

        # 构建交易
        transaction = method_to_call.build_transaction({
            'gas': 700000,  # 适当设置 gas
            'gasPrice': gas_price,  # 适当设置 gasPrice
            'from': owner_address,
            'nonce': nonce,
        })

        # 签署交易
        signed_transaction = web3.eth.account.sign_transaction(transaction, owner_private_key)

        # 发送交易
        transaction_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

        # 等待交易确认
        web3.eth.waitForTransactionReceipt(transaction_hash)
        
        result = ["ok-userTuichu", f"msg:成功退出 "]
        print(result)            
        return  result
    
    except Exception as e:  
        # self.buyTokensBuildTransaction() # 下一次购买准备
        result = ["Failed-userTuichu", f"ERROR: {e}"]
        print(result)
        return  result
    
    