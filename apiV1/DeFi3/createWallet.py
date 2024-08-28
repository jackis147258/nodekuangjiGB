from eth_account import Account
from web3 import Web3
import csv 

# 安装： pip3 install eth_account
#       pip3 install web3

def createNewETHWallet():
    wallets = []
    walletTokens = []

    for id in range(5):
        # 添加一些随机性
        account = Account.create('Random  Seed'+str(id))

        # 私钥
        privateKey = account._key_obj

        # 公钥
        publicKey = privateKey.public_key

        # 地址
        address = publicKey.to_checksum_address()
        
        walletToken={'token':privateKey,'ApprovedBuy':1,'ApprovedSell':0}
        walletTokens.append(walletToken)

        wallet = {
            "id": id,
            "address": address,
            "privateKey": privateKey,
            "publicKey": publicKey
        }
        wallets.append(wallet.values())

    return wallets,walletTokens


def saveETHWallet(jsonData):
    with open('walletsdk1.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["序号", "钱包地址", "私钥", "公钥"])
        csv_writer.writerows(jsonData)


if __name__ == "__main__":

    print("---- 开始创建钱包 ----")
    # 创建 1000 个随机钱包
    wallets,walletTokens = createNewETHWallet()
    
    for walletToken in walletTokens:        
        print(walletToken )
        print(',' )
         

    # 保存至 csv 文件
    saveETHWallet(wallets)
    print("---- 完成 ----")