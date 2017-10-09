from tkinter import *
import tkinter as tk

import file_transfer_gui
import file_transfer_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(255,375)
        self.master.maxsize(255,375)
        file_transfer_func.center_window(self,255,375)
        self.master.title("File Tranfer")
        self.master.configure(bg="#ffe259")
        self.master.protocol("WM_DELETE_WINDOW", lambda: file_transfer_func.ask_quit(self))
        arg = self.master

        file_transfer_gui.load_gui(self)


if __name__== "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
