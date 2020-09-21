import tkinter as tk

from window import MakeWindow
from get_time import GettingTime
from display_elements import DisplayElems

class ButtonFunctions:

    def __init__(self):
        self.window = MakeWindow()
        self.time = GettingTime()
        self.header = DisplayElems
        # self.times_file = open("Time_card_punches.txt", "a")
        # self.popUp = tk.messagebox.showinfo("You Punch was accepted", headerClock())


    def header_clock(self):
        self.header.config(text=self.time.time_stamp)
        self.window.window.after(1000, header_clock)
        return self.time.time_stamp