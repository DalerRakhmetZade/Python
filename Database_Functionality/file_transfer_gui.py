from tkinter import *
import tkinter as tk
from tkinter import ttk

import file_transfer_main
import file_transfer_func

def load_gui(self):
    self.btn_from = tk.Button(self.master, width=15, height=12, background = '#ffffff', text='From:',
                              command = lambda: file_transfer_func.choose_from(self))
    self.btn_from.grid(row=1, column=0, rowspan=4, columnspan=2, padx=(7,0), pady=(45,10),sticky=W)
    self.btn_to = tk.Button(self.master, width=15, height=12, background = '#ffffff', text='To:',
                            command = lambda: file_transfer_func.choose_to(self))
    self.btn_to.grid(row=1, column=2, rowspan=4, columnspan=2, padx=(6,0), pady=(45,10),sticky=E)
    self.btn_transfer = tk.Button(self.master, width=30, height=2, background = '#5EAEEB', text='File Check',
                                  command = lambda: file_transfer_func.file_check(self))
    self.btn_transfer.grid(row=6, column=0, rowspan=2, columnspan=4, padx=(8,0), pady=(15,10))


    self.lbl_last_check = ttk.Label(self.master, background = '#ffe259', font=('Courier',9), text='Last Update:')
    self.lbl_last_check.grid(row=7, column=0, columnspan=4, rowspan=2, padx=(8,0), pady=(24,0), sticky=N)

    self.lr_time = StringVar()
    self.lr_time.set('XX-XX-XXXX XX:XX:XX XX')
    self.txt_last_run_time = ttk.Label(self.master, background = '#ffe259', font=('Courier',8), textvariable=self.lr_time)
    self.txt_last_run_time.grid(row=8, column=0, columnspan=4, padx=(8,0), pady=(5,10), sticky=N)

    self.logo = PhotoImage(file = 'logo.gif').subsample(14,14)
    ttk.Label(self.master, image = self.logo, background = '#ffe259').grid(row = 9, column = 2, padx=(30,0), pady=(0,10))

if __name__== "__main__":
    pass
