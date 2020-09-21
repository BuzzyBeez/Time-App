import tkinter as tk
from get_time import GettingTime
from window import MakeWindow


class DisplayElems:

    def __init__(self):
        # Header displaying the Date and time
        self.time_header = GettingTime()
        self.the_date = self.time_header.time_stamp()
        self.header = tk.Label(text=self.the_date, font=("Times New Roman", 22))

        # Buttons
        self.window = MakeWindow()
        self.punch_bttn = tk.Button(self.window.window, text="Punch", command=punch, pady=10)




