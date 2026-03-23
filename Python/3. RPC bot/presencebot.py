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
def statcode(x, y):
    if x == str("1"):
        if y == str("d"):
            return("Gloria is at class rn")
            pass
        elif y == str("s"):
            return("She may be slow to respond, please be patient")
            pass
        elif y == str("i"):
            return("schoolimg")
            pass
        pass
    pass
appidl = getappid()
appid = appidl[0]
RPC = Presence(appid)
RPC.connect()
stat = str(input("Enter status code: "))
print("Bot is starting, attempting to connect...")
botconn = str("y")
while botconn == str("y"):
    try:
        RPC.update(
            details=statcode(stat, "d"),
            state=statcode(stat, "s"),
            large_image=statcode(stat, "i"),
            start=time.time()
        )
        pass
    except Exception as e:
        print("An exception has occurred: " + e)
        botconn = str("n")
        pass
    time.sleep(15)