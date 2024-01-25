from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
# from decouple import config
import csv
import os

import time
import random


# please disable the two verification code if this enable in your telegram account before using this software

api_id = "17972956" #config('api_id') # go to the my.telegram.org and API DEVEPLOMENT then copy the apt id and paste here
api_hash = "bd3957fc220456845947aef0b56d8775" #config('api_hash') # go to the my.telegram.org and API DEVEPLOMENT then copy the apt hash and paste here
phone = "+251985287648" #config('phone') # enter the your account phone number + Countery code example:+251923481783

client = TelegramClient(phone, api_id, api_hash)
 
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))
 

async def main(user_id, name):

    print(f"user id data is {user_id}")
    await client.send_message(int(user_id), f"Hello {name}, How are you?")



def send_message(row_number, user_id, name):
    with client:
        client.loop.run_until_complete(main(user_id, name))

    print(f"Messages sent successfully to {name} ({user_id})")


    # Generate a random sleep duration between 7 and 10 minutes
    sleep_duration = random.uniform(7, 10)
    # sleep_duration = random.uniform(7 * 60, 10 * 60)

    # Continue with the rest of your code after the sleep
    print("Slept for {:.2f} minutes.".format(sleep_duration / 60))

    # Sleep for the random duration
    time.sleep(sleep_duration)

