#=========================================================#
# Python 3.5.2                                            #
#                                                         #
# Create UI that will allow user to choose folders/files  #
# and copy them to destination folder.                    #
#                                                         #
# Author: Nicholas Wood (nicholas.cameron.wood@gmail.com) #     
#                                                         #
#======================={nWc}=============================#

from tkinter import *
import tkinter as tk
import shutil
import os
from os import path
import datetime
from datetime import datetime, date, time, timedelta

import fTransfer_main
import fTransfer_gui

# yesterday
aDayOld = datetime.now() - timedelta(hours = 24)

#=============================
def centerWindow(self, w, h):                                                    
    # get screen width and height                                                 
    screen_width = self.master.winfo_screenwidth()                                
    screen_height = self.master.winfo_screenheight()                              
    # calculate x and y coords to center app                                      
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def askQuit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)
#==================


def browseSrcFile(self):
    self.fSrc = filedialog.askdirectory(initialdir="/",title='Please select a source folder')
    print ('Source File: ', self.fSrc)
    return self.fSrc
 
    

def browseDstFile(self):
    self.fDst = filedialog.askdirectory(initialdir="/",title='Please select a destination folder')
    print ('Destination File: ', self.fDst)
    return self.fDst


def dailyTransfer(self):
    for root, dirs, files in os.walk(self.fSrc):
        for txtfile in files:
            path = os.path.join(root, txtfile)
            st = os.stat(path)
            mtime = datetime.fromtimestamp(st.st_mtime)
            ctime = datetime.fromtimestamp(st.st_ctime)
            if mtime > aDayOld and txtfile.endswith('.txt'):
                shutil.copy(os.path.join(self.fSrc, txtfile), os.path.join(self.fDst, txtfile))
            elif ctime > aDayOld and txtfile.endswith('.txt'): 
                shutil.copy(os.path.join(self.fSrc, txtfile), os.path.join(self.fDst, txtfile))
                
    print('Files successfully copied!')       





if __name__ == "__main__":
    pass
                
