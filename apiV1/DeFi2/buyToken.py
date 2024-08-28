# import config
import time


def buyTokensSend_raw_transaction(self,t_price):  
        try:
            tokenToSell=self.tokenToBuy # 购买数量            
            t_gas=self.web3.eth.gasPrice                            
            pancakeSwap_txn = self.contractPancake.functions.swapExactETHForTokens(0,
                [self.WBNB_Address,self.USDT_Address, self.TokenToSellAddress],
                self.walletAddress,
                (int(time.time() + 1000000))).build_transaction({
                'from': self.walletAddress,
                'value': tokenToSell,  # Amount of BNB
                'gas': 300000,
                'gasPrice': t_gas,
                'nonce': self.web3.eth.get_transaction_count(self.walletAddress)
            })                                                    
           
            self.signed_txn = self.web3.eth.account.sign_transaction(
                pancakeSwap_txn, private_key=self.privateKey)
            tx_token = self.web3.eth.send_raw_transaction(self.signed_txn.rawTransaction)            
            time1 =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            result = [time1,'购买地址:',self.walletAddress, f"购买完成: {str(self.web3.fromWei(tokenToSell, self.TradingTokenDecimal))}  ", 'hash:',self.web3.to_hex(tx_token)]
            print(result)
            # self.sendMessage(list(result))
            # self.sendMessage(str(result))


             # 写入修改 钱包token 购买价格 ， 判断 全局0 ，独立 1

            if self.Dlprice_status==1:                
                obj=T_TokenAddr.objects.get(id=self.QianBaoTokenId) 
                if not obj:
                    return None 
                # 更新DlSellTOKEN_price字段 ,得到 上提 百分比


                # self.DlBuyNumber=obj.DlBuyNumber
                # self.DlBuyTOKEN_price=obj.DlBuyTOKEN_price
                # self.DlSellNumber=obj.DlSellNumber
                # self.DlSellTOKEN_price=obj.DlSellTOKEN_price

                # 设置 购买价格
                obj.DlBuyTOKEN_price=tokenToSell
                # 设置 购买数量
                obj.DlBuyNumber=obj.DlBuyNumber+1

                # 先将百分比整数转为小数
                percentage = self.PercenttSell / Decimal('100.0')                
                DlSellTOKEN_price = tokenToSell + tokenToSell * percentage
                # DlSellTOKEN_price=tokenToSell+tokenToSell*self.PercenttSell
                obj.DlSellTOKEN_price = DlSellTOKEN_price
                obj.save() 

             # 写入数据库   
            t_trade=T_trade()  
            t_trade.Price=t_price
            t_trade.tradeAmount=tokenToSell 
            t_trade.tradeToken=self.walletAddress
            t_trade.TOKEN_ADDRESS=self.address
            t_trade.tradeHash=self.web3.to_hex(tx_token)
            
            t_trade.tradeStatus=0
            t_trade.QuantifyId=self.objId
            t_trade.uid=self.userId
            t_trade.save() 
          
            
            return 'ok'
           
        except Exception as e:  
            if "HTTPSConnectionPool(host='bsc-dataseed2.binance.org', port=443)"   in str(e):
                self.changeIpweb3()            
            # self.buyTokensBuildTransaction() # 下一次购买准备   insufficient funds for gas * price + value
            result = ["Failed-buySend_raw_transaction", f"ERROR: {e}"]
            print(result)
            self.sendMessage(list(result))
            

def buyTokens(**kwargs):






def buyTokens1(**kwargs):
    symbol = kwargs.get('symbol')
    web3 = kwargs.get('web3')
    walletAddress = kwargs.get('walletAddress')
    contractPancake = kwargs.get('contractPancake')
    TokenToBuyAddress = kwargs.get('TokenToSellAddress')
    WBNB_Address = kwargs.get('WBNB_Address')

    toBuyBNBAmount = input(f"Enter amount of BNB you want to buy {symbol}: ")
    toBuyBNBAmount = web3.toWei(toBuyBNBAmount, 'ether')

    pancakeSwap_txn = contractPancake.functions.swapExactETHForTokens(0,
                                                                      [WBNB_Address, TokenToBuyAddress],
                                                                      walletAddress,
                                                                      (int(time.time() + 10000))).build_transaction({
        'from': walletAddress,
        'value': toBuyBNBAmount,  # Amount of BNB
        'gas': 160000,
        'gasPrice': web3.toWei('5', 'gwei'),
        'nonce': web3.eth.get_transaction_count(walletAddress)
    })

    signed_txn = web3.eth.account.sign_transaction(pancakeSwap_txn, private_key=config.YOUR_PRIVATE_KEY)
    try:
        tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        result = [web3.to_hex(tx_token), f"Bought {web3.fromWei(toBuyBNBAmount, 'ether')} BNB of {symbol}"]
        return result
    except ValueError as e:
        if e.args[0].get('message') in 'intrinsic gas too low':
            result = ["Failed", f"ERROR: {e.args[0].get('message')}"]
        else:
            result = ["Failed", f"ERROR: {e.args[0].get('message')} : {e.args[0].get('code')}"]
        return result