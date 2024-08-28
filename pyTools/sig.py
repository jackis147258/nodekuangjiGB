from web3 import Web3

from eth_account import Account
from eth_account.messages import encode_defunct

from Crypto.Hash import keccak
import eth_abi

def generate_hash(sender_address, amount, timestamp):
    # 确保地址是小写，且包含 "0x" 前缀
    sender_address = sender_address.lower()
    print(sender_address)
    t_GuiJiWallter=Web3.to_checksum_address(sender_address)   
    print(t_GuiJiWallter)
 


    
    # 使用 eth_abi 编码数据
    encoded_data = eth_abi.encode(['address', 'uint256', 'uint256'], [t_GuiJiWallter, amount, timestamp])
    
    # 使用 Keccak256 进行哈希
    hasher = keccak.new(digest_bits=256)
    hasher.update(encoded_data)
    message_hash = hasher.digest()
    message_hash_hex = message_hash.hex()

      # 使用生成的私钥
    private_key = '0x9ba61124ddeb2c0c444ac5b643833bf24421d97eed3c9ede44a771319054bc9d'
    signed_message = Account.sign_message(encode_defunct(hexstr=message_hash_hex), private_key)

    signature = signed_message.signature.hex()
    print(signature)



    return message_hash_hex

# 示例调用  0x5B38Da6a701c568545dCfcB03FcB875f56beddC4   0x606adb6c2b7d415e0fd58b7d9cff6b71e5139ceb
message_hash_hex = generate_hash('0x9e1322e3Ca57fFf1EEaDC2B30F666BbAA5595350', 100, 1616161616)
print(message_hash_hex)
