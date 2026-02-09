# Uh so lowkey this might just be a zip bomb honestly
# But that's okay, right?
# Import TKInter module for use with the file dialog popup
import tkinter as tk
from tkinter import filedialog
# Import os library to make directories
import os
# Import platform module for checking OS
import platform
# Import shutil to make a zip
import shutil

def select_directory():
    global dir
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    print("Please only run this if you really know what you're doing, alright? I'm not responsible for you being a dipshit and bricking your pc")
    answer = str(input("Type Y to continue, otherwise the script will close. [Y/any] "))
    if answer == str("Y"):
        directory_path = filedialog.askdirectory()
        if platform.system() == "Linux":
            dir = directory_path + "/"
        root.destroy() # Close the hidden root window
        start_bomb()
        pass
    else:
        pass

def start_bomb():
    global dir
    os.makedirs(dir + "ZipBombPath")
    dir1 = dir + "ZipBombPath/"
    bomb1 = int(100)
    bomb1txt = str(bomb1)
    while bomb1 >= 1:
        os.makedirs(dir1 + bomb1txt)
        dir2 = dir1 + bomb1txt + "/"
        bomb2 = int(100)
        bomb2txt = str(bomb2)
        while bomb2 >= 1:
            os.makedirs(dir2 + bomb2txt)
            dir3 = dir2 + bomb2txt + "/"
            bomb3 = int(100)
            bomb3txt = str(bomb3)
            while bomb3 >= 1:
                os.makedirs(dir3 + bomb3txt)
                dir4 = dir3 + bomb3txt + "/"
                bomb4 = int(100)
                bomb4txt = str(bomb4)
                while bomb4 >= 1:
                    os.makedirs(dir4 + bomb4txt)
                    dir5 = dir4 + bomb4txt + "/"
                    bomb5 = int(100)
                    bomb5txt = str(bomb5)
                    while bomb5 >= 1:
                        os.makedirs(dir5 + bomb5txt)
                        dir6 = dir5 + bomb5txt + "/"
                        bomb6 = int(100)
                        bomb6txt = str(bomb6)
                        while bomb6 >= 1:
                            os.makedirs(dir6 + bomb6txt)
                            dir7 = dir6 + bomb6txt + "/"
                            bomb7 = int(100)
                            bomb7txt = str(bomb7)
                            while bomb7 >= 1:
                                os.makedirs(dir7 + bomb7txt)
                                dir8 = dir7 + bomb7txt + "/"
                                bomb8 = int(100)
                                bomb8txt = str(bomb8)
                                while bomb8 >= 1:
                                    os.makedirs(dir8 + bomb8txt)
                                    dir9 = dir8 + bomb8txt + "/"
                                    bomb9 = int(100)
                                    bomb9txt = str(bomb9)
                                    while bomb9 >= 1:
                                        os.makedirs(dir9 + bomb9txt)
                                        dir10 = dir9 + bomb9txt + "/"
                                        bomb10 = int(100)
                                        bomb10txt = str(bomb10)
                                        while bomb10 >= 1:
                                            os.makedirs(dir10 + bomb10txt)
                                            bomb10 = bomb10 - 1
                                            bomb10txt = str(bomb10)
                                        bomb9 = bomb9 - 1
                                        bomb9txt = str(bomb9)
                                    bomb8 = bomb8 - 1
                                    bomb8txt = str(bomb8)
                                bomb7 = bomb7 - 1
                                bomb7txt = str(bomb7)
                            bomb6 = bomb6 - 1
                            bomb6txt = str(bomb6)
                            pass
                        bomb5 = bomb5 - 1
                        bomb5txt = str(bomb5)
                    bomb4 = bomb4 - 1
                    bomb4txt = str(bomb4)
                bomb3 = bomb3 - 1
                bomb3txt = str(bomb3)
            bomb2 = bomb2 - 1
            bomb2txt = str(bomb2)
        bomb1 = bomb1 - 1
        bomb1txt = str(bomb1)
    shutil.make_archive("thebomb", 'zip', root_dir=dir, base_dir=dir1)
    pass

dir = str("nothin")
select_directory()
