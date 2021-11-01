import requests, threading, time
from colorama import Fore
import os
from itertools import cycle
import random
from colored import fg, attr

a = fg('#a005ed')
b = attr('reset')

def Spammer(webhook, name, message):
  avatars = cycle(["https://media.discordapp.net/attachments/778720320035094550/808181516483166228/ec35695c38b97ea470a3d8761930f5d7.png", "https://preview.redd.it/nx4jf8ry1fy51.gif?format=png8&s=a5d51e9aa6b4776ca94ebe30c9bb7a5aaaa265a6", "https://icon-library.com/images/yellow-discord-icon/yellow-discord-icon-15.jpg"])
  while True:
    json = {
        "username": name,
        "avatar_url": next(avatars),
        "author": {
                "icon_url": None
                },
            "description": str(message)       
    }
    while True:
        r = requests.post(webhook, json=json)
        if "retry_after" in r.text:
            print(f"{a}>{b} ratelimited sleeping for {a}{r.json()['retry_after']}{b} secs.")
            time.sleep(r.json()['retry_after'])
        elif r.status_code == 204:
            print(f"{a}>{b} Sent Webhook")
        else:
            pass

if __name__ == "__main__":
    os.system('cls & title Discord Webhook Spammer')
    web = input(f"{a}>{b} Webhook Url{a}:{b} ")
    nme = input(f"{a}>{b} Webhook Name{a}:{b} ")
    des = input(f"{a}>{b} Webhook Description{a}:{b} ")
    amount = int(input(f"{a}>{b} Amount{a}:{b} "))
    while True:
        for i in range(amount):
            threading.Thread(target=Spammer, args=(web, nme, des,)).start()
