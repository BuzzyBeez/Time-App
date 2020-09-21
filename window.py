import tkinter as tk

class MakeWindow:
    """ This is a class to make the app diaplay"""

    def __init__(self):
        self.window = tk.Tk()
        self.window_size = self.window.geometry("450x450")
        self.window_title = self.window.title("Time Clock")

    def show_window(self):
        self.window.mainloop()