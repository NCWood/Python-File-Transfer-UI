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

import fTransfer_main
import fTransfer_func


def load_gui(self):
        

    #<Buttons>===================================================================================================
    self.srcBrowseBtn = tk.Button(self.master, text = 'Browse', width = 6, command=lambda: varS.set(fTransfer_func.browseSrcFile(self)))
    self.srcBrowseBtn.grid(row = 2, column = 0, columnspan = 4, padx = (10,0), pady = (0,0), sticky = 'nesw')

    self.dstBrowseBtn = tk.Button(self.master, text = 'Browse', width = 6, command=lambda: varD.set(fTransfer_func.browseDstFile(self)))
    self.dstBrowseBtn.grid(row = 2, column = 6, columnspan = 4, padx = (0,10), pady = (0,0), sticky = 'nesw')

    self.copyBtn = tk.Button(self.master, text = 'Copy', width = 6, command=lambda: fTransfer_func.dailyTransfer(self))
    self.copyBtn.grid(row = 3, column = 4, padx = (10,10), pady = (20,0), sticky = 'nesw')
    #</Buttons>==========================================================================

    #<Labels>===================================================
    self.labelSrc = tk.Label(self.master, text = 'Source Folder')
    self.labelSrc.grid(row = 0, column = 0, padx = (10,0), pady = (10,0), sticky = 'nw')

    self.labelDst = tk.Label(self.master, text = 'Destination Folder')
    self.labelDst.grid(row = 0, column = 6, padx = (0,10), pady = (10,0), sticky = 'nw')
    #</Labels>=========================================================================

    #<Entries>=====================================
    varS = StringVar()
    self.entrySrc = tk.Entry(self.master, textvariable = varS)
    self.entrySrc.grid(row = 1, column = 0, columnspan = 4, padx=(10,0), pady=(0,0), sticky = 'nesw')

    varD = StringVar()
    self.entryDst = tk.Entry(self.master, textvariable = varD)
    self.entryDst.grid(row = 1, column = 6, columnspan = 4, padx=(0,10), pady=(0,0), sticky = 'nesw')
    #</Entries>======================================================================================



   
if __name__ == "__main__":
    pass
