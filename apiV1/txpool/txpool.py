from web3 import Web3

# 初始化Web3连接

bsc = "https://bsc-dataseed2.binance.org/"              

# self.web3 = Web3(Web3.HTTPProvider(bsc,request_kwargs=proxies)) 
w3 = Web3(Web3.HTTPProvider(bsc))

# 确保连接成功
if not w3.isConnected():
    print("Error: Not connected to Ethereum node!")
    exit()


while(1):
    # 获取txpool内容
    txpool_content = w3.geth.txpool.content()

    # 我们要查找的地址
    target_address = "0xC3Ad2B6ee371fDA1646090e86D96d8dBE372E329".lower()
    # swapExactETHForTokens方法签名的Keccak-256哈希的前4个字节
    # 注意: 这取决于具体的方法签名, 如果有不同的参数, 这可能会改变
    swap_exact_method_id = w3.sha3(text="swapExactETHForTokens(uint256,address[],address,uint256)").hex()[:10]
    # 过滤交易
    for tx in txpool_content['pending'].get(target_address, {}).values():
        if tx['to'] == target_address and tx['input'].startswith(swap_exact_method_id):
            print(tx)

    # 注意: 这个脚本只会在有pending的交易并且这些交易是swapExactETHForTokens的情况下打印输出.
