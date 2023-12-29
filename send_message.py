from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from decouple import config
import csv
import os

# please disable the two verification code if this enable in your telegram account before using this software

api_id = config('api_id') # go to the my.telegram.org and API DEVEPLOMENT then copy the apt id and paste here
api_hash = config('api_hash') # go to the my.telegram.org and API DEVEPLOMENT then copy the apt hash and paste here
phone = config('phone') # enter the your account phone number + Countery code example:+251923481783

client = TelegramClient(phone, api_id, api_hash)
 
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))
 

async def main():
    # Now you can use all client methods listed below, like for example...
    await client.send_message('me', 'Hello to myself!')

with client:
    client.loop.run_until_complete(main())
       
print('Messages sent successfully.')