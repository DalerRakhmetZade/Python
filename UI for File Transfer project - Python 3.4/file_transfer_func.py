import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
import shutil
import datetime
from datetime import timedelta
import time

import file_transfer_main
import file_transfer_gui


def center_window(self, w, h): 
    
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)

def choose_from(self):
  self.src = filedialog.askdirectory()
  print(self.src)

def choose_to(self):
  self.dst = filedialog.askdirectory()
  print(self.dst)




def file_check(self):
    files = os.listdir(self.src)
    print (files)
    for i in files:
        new_files = datetime.datetime.now() - datetime.timedelta(hours=24)
        mod_time = datetime.datetime.fromtimestamp(os.stat(self.src + '/' + i).st_mtime)
        if mod_time < new_files:
            shutil.move((self.src + '/' + i), self.dst + '/' + i)
            print(i + "\nhas been moved.\n")
   
    



