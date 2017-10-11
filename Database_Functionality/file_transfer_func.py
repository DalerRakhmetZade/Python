import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
import shutil
import datetime
from datetime import timedelta
import time
import sqlite3

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
            update_last_run_time(self,currentTime)
            print(i + "\nhas been moved.\n")
   
def create_db(self):
    conn = sqlite3.connect('last_check_time.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_last_check( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_month INT, \
            col_day INT, \
            col_year INT, \
            col_hour INT, \
            col_min INT, \
            col_sec INT \
            );")
        conn.commit()
    conn.close()
    first_check(self)
    
def first_check(self):
    conn = sqlite3.connect('last_check_time.db')
    with conn:
        cur = conn.cursor()
        cur, count = count_records(cur)
        if count > 0:
            get_last_run(self,cur)
    

def count_records(cur):
    count = ""
    cur.execute("SELECT COUNT(*) FROM tbl_last_check")
    count = cur.fetchone()[0]
    return cur, count

def get_last_run(self,cur):
    cur.execute("SELECT *, MAX(ID) FROM tbl_last_check   GROUP BY ID ORDER BY ID DESC")
    lr = cur.fetchall()[0]
    last_run = '{}-{}-{} {}:{}:{}'.format(str(lr[1]).zfill(2),str(lr[2]).zfill(2),lr[3],str(lr[4]).zfill(2),str(lr[5]).zfill(2),str(lr[6]).zfill(2))
    self.lr_time.set(last_run)

    
currentTime = datetime.datetime.now()

def update_last_run_time(self,currentTime):
    conn = sqlite3.connect('last_check_time.db')
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_last_check (col_month,col_day,col_year,col_hour,col_min,col_sec)\
                    VALUES(?,?,?,?,?,?)",(currentTime.month,currentTime.day,currentTime.year,currentTime.hour,currentTime.minute,currentTime.second))
    create_db(self)



if __name__ == "__main__":
    pass

