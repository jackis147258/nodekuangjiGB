# Create your tasks here

# from demoapp.models import Widget

from celery import shared_task
import time
from apiV1.DeFi2 import DeFi2,celeryPrice,celeryBuySell,getTokenNewUser

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from celery.exceptions import MaxRetriesExceededError
from reg.ebcFenRun import FenRun,createEbcUser
from reg import ebcUserTiXian ,getTokenJiLu
import logging

logger = logging.getLogger(__name__)





@shared_task(bind=True, max_retries=5)
def taskQuantifyPrice(self,id):    
    try:
        celeryPrice.work(id)    
        return id 
    except Exception as general_exception:
        # 一般错误处理
        
        try:
            # 使用Celery的retry机制来重试任务
            self.retry(exc=general_exception,countdown=60)
        except MaxRetriesExceededError:
            result = ["Failed", f"ERROR-Exception: {str(MaxRetriesExceededError)}"]
            return result
        return ["Failed", f"ERROR: {str(general_exception)}"]

@shared_task(bind=True, max_retries=5)
def taskQuantifyBuySell(self,id):    
    try:
        celeryBuySell.work(id)    
        return id 
    except Exception as general_exception:
        # 一般错误处理        
        try:
            # 使用Celery的retry机制来重试任务
            self.retry(exc=general_exception,countdown=60)
        except MaxRetriesExceededError:
            result = ["Failed", f"ERROR-Exception: {str(MaxRetriesExceededError)}"]
            return result
        return ["Failed", f"ERROR: {str(general_exception)}"]
    

# @shared_task(bind=True, max_retries=5, default_retry_delay=60)  # 最多重试5次，每次重试间隔60秒
# @shared_task(bind=True,time_limit=None, max_retries=5)
@shared_task(bind=True, max_retries=5)
def taskQuantify(self,id):
    try:
        DeFi2.work(id)    
        return id
    except ValueError as e:    
        # result = ["Failed", f"ERROR: {e.args[0].get('message')} : {e.args[0].get('code')}"]
        
        try:
            # 使用Celery的retry机制来重试任务
            self.retry(exc=e,countdown=60)
        except MaxRetriesExceededError:
            result = ["Failed", f"ERROR-ValueError:{str(MaxRetriesExceededError)} "]
            return result
    except Exception as general_exception:
        # 一般错误处理
        
        try:
            # 使用Celery的retry机制来重试任务
            self.retry(exc=e,countdown=60)
        except MaxRetriesExceededError:
            # result = ["Failed", f"ERROR-Exception: {e.args[0].get('message')} : {e.args[0].get('code')}"]
            result = ["Failed", f"ERROR-Exception: {str(MaxRetriesExceededError)}"]
            return result
        return ["Failed", f"ERROR: {str(general_exception)}"]
        
        # return result


@shared_task
def mul(x, y):
    print(x * y)
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def token2sql(value):
    FenRun(value) 
    return 'ok'



@shared_task
def userStatusFenRun():
    try:                
        # 分润          
        FenRun() 
    except Exception as general_exception:
        # 一般错误处理     
        result = ["Failed-userStatusFenRun", f"ERROR-Exception: {str(general_exception)}"]
        logger.info(result )

        return result
        

# 调用 bsc链合约 中 新增的用户和他的上级关系 保存到档期系统的用户表中，同时返回，用户本次交易的投入金额 和投入时间。
@shared_task
def tokenNewUserList():
    try:                
        # 得到新用户信息        
        t_return=getTokenNewUser.work()    
        if t_return is not None:
            createEbcUser(t_return)      
            return '建立了新用户'  
        else:
            return '没有新用户信息' 
    except Exception as general_exception:
        # 一般错误处理        
      
        result = ["Failed", f"ERROR-Exception: {str(general_exception)}"]
        return result
        # return ["Failed", f"ERROR: {str(general_exception)}"]



@shared_task
def tokenNewUserList1():
    try:
        # getTokenJiLu.work()               
        # 得到新用户信息        
        t_return=getTokenJiLu.work()    
        if t_return is not None:
            createEbcUser(t_return)      
            return '建立了新用户'  
        else:
            return '没有新用户信息' 
    except Exception as general_exception:
        # 一般错误处理        
      
        result = ["Failed", f"ERROR-Exception: {str(general_exception)}"]
        return result
        # return ["Failed", f"ERROR: {str(general_exception)}"]
        
@shared_task
def userTiXianHashTask():
    try:                
        # 分润     
        result=ebcUserTiXian.userTiXianHash() 
        return result  
    except Exception as general_exception:
        # 一般错误处理     
        result = ["Failed-userStatusFenRun", f"ERROR-Exception: {str(general_exception)}"]
        logger.info(result )

        return result

@shared_task
def userTiXianTask():
    try:                
        # 分润     
        result=ebcUserTiXian.userTiXian() 
        return result
    except Exception as general_exception:
        # 一般错误处理     
        result = ["Failed-userStatusFenRun", f"ERROR-Exception: {str(general_exception)}"]
        logger.info(result )

        return result





    # web3_client = Web3Client()
    # event_filter = web3_client.create_event_filter()
    
    # while True:
    #     for event in event_filter.get_new_entries():
    #         process_deposit_event.delay(event)
    #     time.sleep(2)

# SECRET_KEY = ''


# @shared_task(bind=True, max_retries=5)
    
# def generate_hash_and_signature(user_address, amount):
#     timestamp = int(time.time())
#     data = f"{user_address}{amount}{timestamp}"
#     hash_value = hashlib.sha256(data.encode()).hexdigest()
#     signature = hmac.new(SECRET_KEY.encode(), data.encode(), hashlib.sha256).hexdigest()
#     return hash_value, signature, timestamp