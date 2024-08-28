
import json
import requests
from web3 import Web3
import config
from .abi import tokenAbi
from .models import payToken
from config import EbcContractTokenAddress
from apiV1.DeFi2.ebcTiXian import dfEbcTixian,txhash ,DefiAuto
from .  import ebcFenRun  ,ebcUserTuichu
import time
import logging
from django.contrib.auth import get_user_model

User = get_user_model()
from typing import Optional


# def sqlChuLi(t_payToken,t_re):
#     # 第一次 t_re传值 保存 hash 等数据 ，第二次 主要是扣出 没有扣的费用
#     if t_re is not None and t_re != "":         
#         t_payToken.TxHash=t_re['txhash']  #hash 地址
#         t_payToken.hashInfo=t_re['hashInfo'] #hash 信息 成功失败
#         t_payToken.Remark+="-提现成功"
#         # t_payToken.save() 
#         # if ebcFenRun.tiXianOksql(t_payToken.amount,t_payToken.tiXianWallter):
#         # t_payToken.Remark+="-减少数据成功"
#         t_payToken.status=3  #已转
#         t_payToken.save() 
#         print("包含成功转入")
#         return {'valid': True, 'message': '包含成功转入'}
#         # else:
#         #     t_payToken.Remark+="-减少数据失败"
#         #     t_payToken.save() 
#         #     return {'valid': False, 'message': '减少数据失败'}
 
        
  
def TiXianJiLuChuLi(t_payToken):    
    contractTokenAddress=EbcContractTokenAddress
    # 进入支付
    # 判断 支付过 因为时间 没找到 就，测试 现在如果找到了 。就直接处理 数据库部分
    # if "Transaction with hash: not found" in t_payToken.Remark: 
    #     if txhash(t_payToken)[0]==3:            
    #         t_payToken.Remark+="-提现成功"
    #         t_payToken.status=1  #已转
    #         t_payToken.save()            
    #         return {'valid': True, 'message': '处理完成'}
    
    defi= DefiAuto()
    # results="执行中请等待。。。"
    t_re = defi.ebcTixianGo(int(t_payToken.amount),t_payToken.tiXianWallter,contractTokenAddress)
    
    # t_re=dfEbcTixian(int(t_payToken.amount),t_payToken.tiXianWallter,contractTokenAddress)        
    if  t_re['status']==1 :  
        
        t_payToken.TxHash=t_re['txhash']  #hash 地址
        # t_payToken.hashInfo=t_re['hashInfo'] #hash 信息 成功失败
        t_payToken.Remark+="-得到hash"
        t_payToken.status=t_re['status']  #已转
        t_payToken.save() 
        return {'valid': True, 'message': '得到hash,status状态1'}
     
        # sqlChuLi(t_payToken,t_re)
    else:
        t_payToken.Remark+=''.join(t_re)
        t_payToken.status=0  #失败
        t_payToken.save() 
        # return JsonResponse({'valid': False, 'message': t_re})
    
    
    
def userTiXian():
    try:
        logging.info(f"userTiXian start....: ")   
        contractTokenAddress=EbcContractTokenAddress
        defi= DefiAuto()
        payToken_records = payToken.objects.filter(status=0)
        if payToken_records.exists():  # 检查记录集合是否有数据
            for t_payToken in payToken_records:
                try:
                    time.sleep(5)
                    t_re = defi.ebcTixianGo(int(t_payToken.amount),t_payToken.tiXianWallter,contractTokenAddress)    
                    # t_re=dfEbcTixian(int(t_payToken.amount),t_payToken.tiXianWallter,contractTokenAddress)        
                    if  t_re['status']==1 :                          
                        t_payToken.TxHash=t_re['txhash']  #hash 地址
                        # t_payToken.hashInfo=t_re['hashInfo'] #hash 信息 成功失败
                        t_payToken.Remark+="-得到hash"
                        t_payToken.status=1  #已转
                        t_payToken.save() 
                        # return {'valid': True, 'message': '得到hash,status状态1'}
                    
                        # sqlChuLi(t_payToken,t_re)
                    else:
                        t_payToken.Remark+=''.join(t_re)
                        t_payToken.status=0  #失败
                        t_payToken.save()   
                except Exception as e:
                    # 捕获异常并输出错误信息
                    print(f"userTiXian{t_payToken.id}: {e}")
                    logging.error(f"userTiXian  {e}: ")   
                
            result = ["ok-提现", f"msg:得到hash "]
            print(result)            
            return True , result
          
        else:
            result = ["ok-提现", f"msg:没有提现记录 "]
            print(result)           
            logging.info(f"ok-提现", f"msg:没有提现记录 ")   
            return True , result
        
     
    
    except Exception as e:  
        # self.buyTokensBuildTransaction() # 下一次购买准备
        result = ["Failed-userTuichu", f"ERROR: {e}"]
        logging.error(f"Failed-userTuichu", f"ERROR: {e}") 
        print(result)
        
    
def userTiXianHash():
    try: 
        
        defi= DefiAuto()        
        payToken_records = payToken.objects.filter(status=1)
        # print("Web3 版本:", defi.web3.__version__)

        if payToken_records.exists():  # 检查记录集合是否有数据
            for record in payToken_records:                
                          
                    # Txhash = defi.isTxhash(record.TxHash)   
                    
                try:        
                    receipt = defi.web3.eth.getTransactionReceipt(record.TxHash) 
                    if receipt['status'] == 1:
                        record.hashInfo='hashOk' #hash 信息 成功失败         
                        record.Remark+="-提现成功"
                        record.status=3  #已转
                        record.save()            
                    else:
                        # status = 2  #hash 返回失败            
                        # revert_reason='ok'
                        # try:
                        #     revert_reason = defi.web3.toText(receipt['logs'][0]['data']).decode('latin-1', 'replace')
                        # except UnicodeDecodeError:
                        #     revert_reason = "no"
                                                        
                        record.hashInfo='hash返回 Status:fail' #hash 信息 成功失败
                        record.Remark+="-hash不成功 " 
                        record.status=2    
                        record.save()  
                        logging.error(f"{record.id} hash返回 Status:fail {record.TxHash}")                

                except Exception as e:
                    if "not found."  in str(e):
                        record.hashInfo=str(e)   
                        print(f"userTiXianHash {record.id}: {e}")
                        if record.Remark is  None:
                            record.Remark=""
                        record.Remark+="-hashTransactionNotFound,重新处理"
                        record.status=0  #已转
                        record.save()
                        continue                                                     
                            # 捕获异常并输出错误信息
                    print(f"userTiXianHash {record.id}: {e}")
                    logging.error(f"userTiXianHash {record.id}: {e}") 
                    
        
        
        
                    
                
                # elif Txhash[0]==2:  
                #     t_user = User.objects.filter(id=record.uidB).first()
                #     if t_user:
                #         # t_user.userStakesBfanHuan+=record.amount
                #         # t_user.save()                                                
                #         # record.Remark+="-hash不成功-已返还userStakesBfanHuan:"+str(record.amount)
                #         record.Remark+="-hash不成功 " 
                #         record.status=4
                #     else:
                #         record.status=2  #hash不成功
                #         record.Remark+="-hash不成功,用户不存在"
                #     # 退回EBC                             
                #     record.hashInfo=Txhash[1] #hash 信息 成功失败
                #     # record.hashInfo=Txhash[1] #hash 信息 成功失败 
                #     record.save()            
                # else:
                #     record.Remark+="-hash不成功,重新处理"
                #     record.status=0  #已转
                #     record.save()            
                    
                    # return {'valid': False, 'message': 'hash不成功'}   
                          
            result = ["userTiXianHash 处理完毕" ]
            print(result)            
            return True , result
          
        else:
            result = ["userTiXianHash  ,没有记录 "]
            print(result)            
            return True , result
        
     
    
    except Exception as e:  
        # self.buyTokensBuildTransaction() # 下一次购买准备
        result = ["Failed-userTuichu", f"ERROR: {e}"]
        print(result)
        
    
    