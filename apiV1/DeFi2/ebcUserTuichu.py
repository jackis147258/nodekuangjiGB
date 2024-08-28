
import json
import requests
from web3 import Web3
import config
from abi import tokenAbi
 
def userTuichu(username):
    # 合约地址和 ABI
    pancakeRouterAddress = config.EbcState_ADDRESS 
    pancakeAbi = tokenAbi(pancakeRouterAddress)  # 合约 ABI
    # owner 账户的私钥  0xBB8f45851f2c7EE4c03961E9D1Fb1E2C13AE82B8
    owner_private_key = "13276bf700ca50688c13b3c55337dcbcebcea653d1fb49303a991c6a241cdb2d"
    account=web3.eth.account.from_key(owner_private_key)                
    # walletAddress=account.address 
    # 初始化 Web3 连接
    bsc = "https://rpc.ankr.com/bsc/174ba138f2cbc5773ef292c0e0a941ec3f23246439e9f0b8d7bec242a67f8c20"  #免费
 
    web3 = Web3(Web3.HTTPProvider(bsc))

    # 实例化合约
    contractPancake = web3.eth.contract(address=pancakeRouterAddress, abi=pancakeAbi)

    # 要调用的合约方法
    method_to_call = contractPancake.functions.ownerSetUserStakeAB0(username)  # 传入 username 参数

    # owner 账户地址
    owner_address = account.address 

    # 获取当前 nonce
    nonce = web3.eth.getTransactionCount(owner_address)

    # 构建交易
    transaction = method_to_call.build_transaction({
        'gas': 2000000,  # 适当设置 gas
        'gasPrice': web3.toWei('50', 'gwei'),  # 适当设置 gasPrice
        'from': owner_address,
        'nonce': nonce,
    })

    # 签署交易
    signed_transaction = web3.eth.account.sign_transaction(transaction, owner_private_key)

    # 发送交易
    transaction_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

    # 等待交易确认
    web3.eth.waitForTransactionReceipt(transaction_hash)