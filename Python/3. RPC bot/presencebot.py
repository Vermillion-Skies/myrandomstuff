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
    if x == str("1"): #School status
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
    elif x == str("2"): #Gaming status
        if y == str("d"):
            return("Gloria is gaming rn")
            pass
        elif y == str("s"):
            return("She may or may not be at the PC rn")
            pass
        elif y == str("i"):
            return("gaming")
            pass
        pass
    elif x == str("3"): #Relaxing status
        if y == str("d"):
            return("Gloria is doing nothing rn")
            pass
        elif y == str("s"):
            return("What a lazy ass bum")
            pass
        elif y == str("i"):
            return("lazybum")
            pass
        pass
    pass
stat = str(input("Enter status code: "))
appidl = getappid()
appid = appidl[0]
RPC = Presence(appid)
RPC.connect()
print("Bot is starting, attempting to connect...")
botconn = str("y")
starttime = time.time()
while botconn == str("y"):
    try:
        RPC.update(
            details=statcode(stat, "d"),
            state=statcode(stat, "s"),
            large_image=statcode(stat, "i"),
            #large_text="text to show when hovering over large image",
            #small_image="asset name for small image",
            #small_text="text to show when hovering over small image",
            start=starttime,
        )
        pass
    except Exception as e:
        print("An exception has occurred: " + e)
        botconn = str("n")
        pass
    time.sleep(15)