from django.test import TestCase

# Create your tests here.
from .web3_utils import Web3Client
import time

 
def process_deposit_event(event):
    # Process the event (e.g., save to database, perform some action)
    print(f"Processing Deposit Event: {event}")
    user = event['args']['user']
    amount = event['args']['amount']
    # Add your processing logic here

 
def listen_to_deposit_events():
    web3_client = Web3Client()
    event_filter = web3_client.create_event_filter()
    
    while True:
        for event in event_filter.get_new_entries():
            process_deposit_event.delay(event)
        time.sleep(2)
print('dddd')
listen_to_deposit_events()
