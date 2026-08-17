# Imports urllib to download the images
import urllib.request
# Imports TKInter for directory selection
import tkinter as tk
from tkinter import filedialog
#imports platform library for OS detection
import platform
# Imports Shutil to copy files
import shutil
# Imports OS to remove files
import os

def select_directory():
    global dir
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    directory_path = filedialog.askdirectory()
    if platform.system() == "Linux":
        dir = directory_path + "/"
    root.destroy() # Close the hidden root window
    pass

print("Welcome to the cheese script!")
answer = str(input("Press enterto select what directory to download the cheese to"))
dir = str("nothin")
select_directory()
answer = int(input("How much cheese do you want?"))
total = answer
current = int(0)
urllib.request.urlretrieve("https://raw.githubusercontent.com/Vermillion-Skies/myrandomstuff/refs/heads/main/Python/2.%20Cheese%20Image%20Downloader/cheese.jpg", dir + "cheesebase.jpg")
src = str(dir + "cheesebase.jpg")
current = current + 1
while current <= total:
    shutil.copyfile(src, dir + "cheese" + str(current) + ".jpg")
    current = current + 1
os.remove(src)
print("Enjoy the cheese!")
answer = str(input("Press enter to exit"))