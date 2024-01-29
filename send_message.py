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
 

async def main(username, user_id, name):

    intro =[
    '''🚀 Vote for Excellence! 🚀

    Explore our Developers category proposals! 🌐🛠️

    Why us?''',
    '''⚙️Elevate Cardano with Us! ⚙️

    Discover our Developers category proposals impact! 🚀

    Why choose us?''',
    '''Unleash the potential of our Developers category proposals!

    Why support us?''',
    '''    ⚡ Revolutionize with Developers! ⚡

    Your vote matters in the Developers category! 🚀🌐

    Why us?''',
    '''Discover our Developers category proposals! 🚀🔍

    Why support us?''',
    '''Explore the Developers category! 🌐🛠️

    Why choose us?''',
    '''Your voice matters in the Developers category! 🚀🌐

    Why support us?''',
    '''Discover our Developers category proposals!

    Why choose us?''',
    '''    ⚡ Developers Unite for Cardano! ⚡

    Unleash the potential of our Developers category proposals! 🚀🌐

    Why support us?''',
    '''    🚀 Your Vote Powers Progress! 🚀

    Explore our Developers category proposals! 🌐🛠️

    Why us?''',
    '''    Your Vote, Your Cardano Legacy!

    Discover our Developers category proposals! 🚀🔍

    Why support us?''',
    '''Your voice matters in the Developers category! 🚀🌐

    Why us?'''
        ]
    success = [
    "🌟 Unmatched Success: 100K+ app downloads.",
    "✨ Stellar Track Record: 100K+ app downloads.",
    "💼 Proven Success: App triumph with 100K+ downloads.",
    "🏆 Proven Excellence: App with 100K+ downloads.",
    "✨ Unparalleled Success: App soaring with 100K+ downloads.",
    "🌟 Track Record: App triumph with 100K+ downloads.",
    "🏆 App Success: Soaring with 100K+ downloads.",
    "🌟 Unmatched Success: 100K+ app downloads.",
    "🏆 Proven Success: App soaring with 100K+ downloads.",
    "🌟 Unmatched Success: 100K+ app downloads.",
    "✨ Unparalleled Success: App soaring with 100K+ downloads.",
    "🏆 App Success: Soaring with 100K+ downloads."
        ]
    collaboration = [
    "🤝 Trusted Partner: Microsoft for Startups Founders Hub.",
    "🤝 Power of Collaboration: Microsoft for Startups Founders Hub.",
    "🤝 Collaborative Power: Microsoft for Startups Founders Hub alliance.",
    "🤝 Strategic Collaborator: Microsoft for Startups Founders Hub.",
    "🤝 Collaboration Dynamo: Partnered with Microsoft for Startups Founders Hub.",
    "🤝 Trusted Partner: Microsoft for Startups Founders Hub.",
    "🤝 Collaboration Dynamo: Microsoft for Startups Founders Hub ally.",
    "🤝 Trusted Collaborator: Microsoft for Startups Founders Hub.",
    "🤝 Collaborative Dynamo: Partnered with Microsoft for Startups Founders Hub.",
    "🤝 Trusted Collaborator: Microsoft for Startups Founders Hub.",
    "🤝 Collaboration Dynamo: Partnered with Microsoft for Startups Founders Hub.",
    "🤝 Collaboration Dynamo: Microsoft for Startups Founders Hub ally."
        ]
    experts = [
    "🔗 Blockchain Mastery: Deep Cardano expertise.",
    "🔐 Blockchain Experts: Proficient in Cardano tech.",
    "🔗 Blockchain Prowess: Cardano tech expertise.",
    "🔗 Blockchain Gurus: Experts in Cardano tech.",
    "🔐 Blockchain Whizzes: Mastery in Cardano tech.",
    "🔗 Blockchain Mastery: Deep Cardano expertise.",
    "🔗 Blockchain Gurus: Experts in Cardano tech.",
    "🔗 Blockchain Prowess: Deep Cardano expertise.",
    "🔗 Blockchain Mastery: Experts in Cardano tech.",
    "🔗 Blockchain Prowess: Deep Cardano expertise.",
    "🔐 Blockchain Whizzes: Mastery in Cardano tech.",
    "🔗 Blockchain Gurus: Experts in Cardano tech."
        ]
    ratting = [
    "🌟 Highly Rated: Community feedback supports our proposals!",
    "🌟 Community Choice: Our proposal received great reviews!",
    "🌟 Standout Performer: Our proposals earned high community ratings!",
    "🌟 Highly Acclaimed: Our proposals received top community ratings",
    "🌟 Community-Endorsed: Our proposals stands out with high ratings!",
    "🌟 Rated High: Our proposals earned praise during the community review stage!",
    "🌟 Ratings: Our proposals stood out during community review!",
    "🌟 Backed by the Community: Our proposals received high ratings in the review stage!",
    "🌟 Community Endorsement: Our proposals earned praise with outstanding reviews!",
    "🌟 Resonating Success: Our proposal received top reviews during the community stage!",
    "🌟 Recognized Excellence: Our proposal earned high community ratings during review!",
    "🌟 Community-Praised: Our proposal is a standout performer with high ratings!"

    ]
    revolution = [
        "💡 Focus: DevTools for 45%+ global websites.",
        "🌍 Revolution: DevTools for 45%+ global websites.",
        "🌟 Integration: DevTools for 45%+ global websites.",
        "💻 Evolution: DevTools for 45%+ global websites.",
        "💡 Transformation: DevTools for 45%+ global websites.",
        "💻 Revolution: DevTools for 45%+ global websites.",
        "💡 Evolution: DevTools for 45%+ global websites.",
        "💡 Focus: DevTools for 45%+ global websites.",
        "💻 Evolution: DevTools for 45%+ global websites.",
        "💡 Focus: DevTools for 45%+ global websites.",
        "💡 Transformation: DevTools for 45%+ global websites.",
        "💡 Evolution: DevTools for 45%+ global websites."
    ]
    signature = [
        '''Search "Esubalew" to locate our proposals quickly. Cast your vote and propel Cardano forward!''',
        '''Search "Esubalew" - Your vote is the catalyst! Easily find our proposals and ignite Cardano's progress!''',
        '''Your Vote, Your Impact! Search "Esubalew" - Locate our proposals easily and cast a vote that transforms Cardano!''',
        '''Navigate Change - Search "Esubalew" - Find our proposals with a simple search. Your vote steers Cardano's course!''',
        '''Easy Access, Big Impact! Search "Esubalew" - Discover our proposals effortlessly. Your vote shapes the destiny of Cardano!''',
        '''Search "Esubalew" to locate our proposals quickly. Cast your vote and propel Cardano forward!''',
        '''Search "Esubalew" - Explore our proposals with ease. Your vote is the catalyst for Cardano's growth!''',
        '''Search "Esubalew" - Access our proposals effortlessly. Every vote paves the way for a stronger Cardano!''',
        '''Search "Esubalew" - Make your vote count! Find us easily and fuel Cardano's evolution.''',
        '''Search "Esubalew" - Easily access our proposals! Cast your vote for a thriving Cardano.''',
        '''Search "Esubalew" to find our proposals easily. Your vote shapes Cardano's future! 🚀''',
        '''Search "Esubalew" for easy access to our proposals. Your vote fuels progress!'''
    ]


    selected_content = (random.choice(intro) + '\n'+
    
    random.choice(success) + '\n'+
     random.choice(collaboration) + '\n'+
     random.choice(experts) + '\n'+
     random.choice(ratting) + '\n'+
     random.choice(revolution)+ '\n'+

    '\n'+random.choice(signature)
    )

    print(f"user id data is {user_id}")
    # await client.send_message(int(user_id), f"Hello {name}, How are you?")
    # await client.send_message("me", selected_content, file='esubalew.jpeg')

    if username:
        await client.send_message(username, selected_content, file='esubalew.jpeg')

        with open('sent_to.txt', 'a') as file:
            file.write(f"\n({user_id}) {username} {name}")
    
        print(f"Messages sent successfully to {name} ({user_id})")
        
        # Generate a random sleep duration between 7 and 10 minutes
        # sleep_duration = random.uniform(7, 10)
        sleep_duration = random.uniform(7 * 60, 10 * 60)

        # Continue with the rest of your code after the sleep
        print("Slept for {:.2f} minutes.".format(sleep_duration / 60))

        # Sleep for the random duration
        time.sleep(sleep_duration)

    else:
        with open('sent_to.txt', 'a') as file:
            file.write(f"\n user_id={user_id} empty username!")

        print(f"Messages not sent due to empty username {name} ({user_id})")



def send_message(row_number, username, user_id, name):
    with client:
        client.loop.run_until_complete(main(username, user_id, name))
