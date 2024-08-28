
from web3 import Web3

w3 = Web3(Web3.WebsocketProvider('wss://bsc.getblock.io/93184fd7-8180-48fb-aefc-3a8c3d0c111c/mainnet/'))

if not w3.isConnected():
    print("Error: Not connected to Ethereum node!")
    exit()

target_address = "0xC3Ad2B6ee371fDA1646090e86D96d8dBE372E329".lower()

target_address1 = "0x768a62a22b187EB350637e720ebC552D905c0331".lower()


# def handle_event(tx_obj):
#     tx_hash_hex = tx_obj['hash']
#     tx = w3.eth.getTransaction(tx_hash_hex)
#     if tx and tx['to'] == target_address:
#         print(f"Transaction {tx_hash_hex} is to {target_address}") 
        

from web3.exceptions import TransactionNotFound

SWAP_EXACT_TOKENS_FOR_ETH_SIGNATURE = w3.keccak(text="swapExactTokensForETH(uint256,uint256,address[],address,uint256)").hex()[:10]

def is_swap_exact_tokens_for_eth(tx):
    return tx['input'].startswith(SWAP_EXACT_TOKENS_FOR_ETH_SIGNATURE)


def parse_swap_exact_tokens_for_eth_input(input_data):
    # 跳过函数签名的前4个字节
    data = input_data[10:]

    # 提取amountIn (uint256占32个字节)
    token_to_sell = int(data[:64], 16)
    data = data[64:]

    # 跳过amountOutMin和deadline
    data = data[192:]

    # 获取路由数组的长度 (uint256)
    path_length = int(data[:64], 16)
    data = data[64:]

    # 提取TokenToSellAddress (第一个地址)
    token_to_sell_address = Web3.to_checksum_address('0x' + data[24:64])

    return token_to_sell, token_to_sell_address

def parse_swap_input(input_data):
    # 跳过前4个字节的函数签名
    data = input_data[10:]

    # 读取amountIn (uint256占32个字节)
    amount_in = int(data[:64], 16)

    # 跳过amountOutMin和deadline，进入path数组
    path_data = data[192:]

    # 获取地址数组的长度 (再次使用uint256)
    path_length = int(path_data[:64], 16)
    path_data = path_data[64:]

    # 第一个地址就是您要交易的代币地址
    token_address = Web3.to_checksum_address('0x' + path_data[24:64])

    return amount_in, token_address


def parse_input_for_path_and_amount(input_data):
    try:
        # 尝试提取代币数量 (uint256占32个字节)
        token_to_sell = int(input_data[:64], 16)
        data = input_data[64:]

        # 尝试获取路由数组的长度 (uint256)
        path_length = int(data[:64], 16)
        data = data[64:]

        # 提取第一个地址
        token_to_sell_address = None
        if path_length > 0:
            token_to_sell_address = Web3.to_checksum_address('0x' + data[24:64])

        return token_to_sell, token_to_sell_address
    except Exception as e:
        print(f"Error parsing input data: {e}")
        return None, None
    
# 估算gas 费用

def calculate_potential_fee(tx):
    gas_limit = tx['gas']
    max_fee_per_gas = tx['maxFeePerGas']

    return gas_limit * max_fee_per_gas

# def handle_event(tx_obj):
#     tx_hash_hex = tx_obj['hash']
#     try:
#         tx = w3.eth.getTransaction(tx_hash_hex)
#         if tx and tx['to'] == target_address:
#             print(f"Transaction {tx_hash_hex} is to {target_address}")
#     except TransactionNotFound:
#         print(f"Transaction {tx_hash_hex} was not found.")
        


def handle_event(tx_obj):
    tx_hash_hex = tx_obj['hash']
    try:
        tx = w3.eth.getTransaction(tx_hash_hex)
        
        # Ensure the transaction is of type 0x2 (EIP-1559)   
        # 估算gas 费用
        if tx['type'] == '0x2':
            potential_fee = calculate_potential_fee(tx)
            print(f"估算Gas费用 max fee of: {Web3.fromWei(potential_fee, 'ether')} ETH")
            # print(f"Transaction {tx_hash} has a potential max fee of: {Web3.fromWei(potential_fee, 'ether')} ETH")
            
        # if tx and tx['to'] == target_address:
        #     print(f"Transaction {tx_hash_hex} is to {target_address}")
        #     #  tx = w3.eth.getTransaction(tx_hash)
        #     if is_swap_exact_tokens_for_eth(tx):
        #         print(f"Found a swapExactTokensForETH transaction: {tx_hash}")
        #         amount_in, token_address = parse_swap_input(tx['input'])
        #         print(f"Swapped {amount_in} of token at address {token_address} in transaction {tx_hash}")
                
        if is_swap_exact_tokens_for_eth(tx):
            # print(f"Found a swapExactTokensForETH transaction: {tx_hash}")
            amount_in, token_address = parse_input_for_path_and_amount(tx['input'])
            if token_address==target_address1:
                print(f"找到地址 {target_address1 } of token at 数量 {amount_in}  ")
                # print(f"Swapped {amount_in} of token at address {token_address} in transaction {tx_hash}")
            
            
    except TransactionNotFound:
        print(f"Transaction {tx_hash_hex} was not found.")

import asyncio
transaction_filter = w3.eth.filter('pending') 
while True:
    try:

        for tx_hash in transaction_filter.get_new_entries():
            # print(tx_hash)
            handle_event(tx_hash)
            
            # tx = w3.eth.getTransaction(tx_hash)
            # if is_swap_exact_tokens_for_eth(tx):
            #     print(f"Found a swapExactTokensForETH transaction: {tx_hash}")
            #     amount_in, token_address = parse_swap_input(tx['input'])
            #     print(f"Swapped {amount_in} of token at address {token_address} in transaction {tx_hash}")
        
    except asyncio.TimeoutError:
        print("Timeout error while fetching new entries. Retrying...")
    except asyncio.CancelledError:
        print("The task was cancelled. Retrying...")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Retrying...")
 


