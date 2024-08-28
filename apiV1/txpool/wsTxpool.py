
from web3 import Web3

w3 = Web3(Web3.WebsocketProvider('wss://bsc.getblock.io/93184fd7-8180-48fb-aefc-3a8c3d0c111c/mainnet/'))

if not w3.isConnected():
    print("Error: Not connected to Ethereum node!")
    exit()

target_address = "0xC3Ad2B6ee371fDA1646090e86D96d8dBE372E329".lower()

target_address1 = "0x768a62a22b187EB350637e720ebC552D905c0331".lower() 

from web3.exceptions import TransactionNotFound 
 
 


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
        

def is_function_one(tx_input):    
    amount_in, token_address = parse_input_for_path_and_amount(tx_input['input'])
    if token_address==target_address1:
        print(f"找到地址 {target_address1 } of token at 数量 {amount_in}  ")
    
    return  '1'

def is_function_two(tx_input):
    amount_in, token_address = parse_input_for_path_and_amount(tx_input['input'])
    if token_address==target_address1:
        print(f"找到地址 {target_address1 } of token at 数量 {amount_in}  ")
    return '1'

def is_function_three(tx_input):
    amount_in, token_address = parse_input_for_path_and_amount(tx_input['input'])
    # amount_in, token_address = parse_input_for_path_and_amount(tx_input)
    if token_address==target_address1:
        print(f"找到地址 {target_address1 } of token at 数量 {amount_in}  ")
    return '1'

# 字典模拟switch-case结构
switch_dict = {
    "0x5ae401dc": is_function_one,
    "0x18cbafe5": is_function_two,   #Swap Exact Tokens For ETH
    "0x5f575529": is_function_three,
}

def check_function_signature(tx_input):
    # 使用get()方法从字典中提取对应的函数
    # 如果找不到匹配的键，则返回None
    tx_input['input']
    func = switch_dict.get(tx_input['input'][:10])
    
    # 如果找到了对应的函数，则执行它
    if func:
        return func(tx_input)
    else:
        return False


def handle_event(tx_obj):
    tx_hash_hex = tx_obj['hash']
    try:
        tx = w3.eth.getTransaction(tx_hash_hex) 
        # Ensure the transaction is of type 0x2 (EIP-1559)   
        # 估算gas 费用
        # if tx['type'] == '0x2':
        #     potential_fee = calculate_potential_fee(tx)
        #     print(f"估算Gas费用 max fee of: {Web3.fromWei(potential_fee, 'ether')} ETH")
            # print(f"Transaction {tx_hash} has a potential max fee of: {Web3.fromWei(potential_fee, 'ether')} ETH")
            
        # if tx and tx['to'] == target_address:
        #     print(f"Transaction {tx_hash_hex} is to {target_address}")
        #     #  tx = w3.eth.getTransaction(tx_hash)
        #     if is_swap_exact_tokens_for_eth(tx):
        #         print(f"Found a swapExactTokensForETH transaction: {tx_hash}")
        #         amount_in, token_address = parse_swap_input(tx['input'])
        #         print(f"Swapped {amount_in} of token at address {token_address} in transaction {tx_hash}")
                
        # if is_swap_exact_tokens_for_eth(tx):
        #     # print(f"Found a swapExactTokensForETH transaction: {tx_hash}")
        #     amount_in, token_address = parse_input_for_path_and_amount(tx['input'])
        #     if token_address==target_address1:
        #         print(f"找到地址 {target_address1 } of token at 数量 {amount_in}  ")
        #         # print(f"Swapped {amount_in} of token at address {token_address} in transaction {tx_hash}")
        # tx['input']
        check_function_signature(tx) 
            
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
 



