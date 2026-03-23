from pypresence import Presence
import time
import os
import sys
def getappid():
    try:
        with open("pbcred.txt", "r") as file:
            return(file.read().splitlines())
            pass
        pass
    except:
        print("Error getting app ID.")
        return("fail")
        pass
    pass
appidl = getappid()
appid = appidl[0]
RPC = Presence(appid)
RPC.connect()
print("Bot is starting, attempting to connect...")
while True:
    try:
        RPC.update(
            details="Gloria is testing an RPC bot",
            state="RPC state test",
            start=time.time()
        )
        pass
    except Exception as e:
        print("An exception has occurred: " + e)
        pass
    time.sleep(15)