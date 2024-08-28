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

 
from .web3_utils import Web3Client,listen_to_deposit_events
from .web3_tixian import listen_to_Withdrawal_events
from .nodeKjFenRun import fanTiXianTime

@shared_task
def listen_toDeposit ():
    listen_to_deposit_events()


# 提现
@shared_task
def listen_toWithdrawal ():
    listen_to_Withdrawal_events()

# 按小时 前 反提现
@shared_task
def fanTiXianTimeTask (t_house):    
    fanTiXianTime(t_house)


# @shared_task
# def process_deposit_event(event):
#     # Process the event (e.g., save to database, perform some action)
#     print(f"Processing Deposit Event: {event}")
#     user = event['args']['user']
#     amount = event['args']['amount']
#     # Add your processing logic here

# @shared_task
# def listen_to_deposit_events():
#     web3_client = Web3Client()
#     event_filter = web3_client.create_event_filter()
    
#     while True:
#         for event in event_filter.get_new_entries():
#             process_deposit_event.delay(event)
#         time.sleep(2)

# SECRET_KEY = ''


# @shared_task(bind=True, max_retries=5)
    
# def generate_hash_and_signature(user_address, amount):
#     timestamp = int(time.time())
#     data = f"{user_address}{amount}{timestamp}"
#     hash_value = hashlib.sha256(data.encode()).hexdigest()
#     signature = hmac.new(SECRET_KEY.encode(), data.encode(), hashlib.sha256).hexdigest()
#     return hash_value, signature, timestamp