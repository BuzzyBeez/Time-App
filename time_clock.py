import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as st
from datetime import datetime

# create the widnow and size and title.
window = tk.Tk()
window.geometry("450x450")
window.title("Time Clock")


""" these are the functions for the elements on the display """

# Display the current time at the top of the app
def headerClock():
    now = datetime.now()
    readable_time = now.strftime("\n%A\n%m/%d/%Y\n%I:%M:%S\n") # puts the date and time in a readable string.
    header.config(text=readable_time) # updates the label with readable time.
    window.after(1000, headerClock) # this refreshes the header function every second with the current time.
    return readable_time

# add the button to make a punch and write the time to a file.
def punch():
    times_file = open("Time_card_punches.txt", "a")
    tk.messagebox.showinfo("You Punch was accepted", headerClock())
    times_file.write(headerClock())
    times_file.close()

def showAll():
    get_file = open("Time_card_punches.txt", "r")
    get_lines = get_file.readlines()
    line_strings = ''
    for lines in get_lines:
        line_strings += lines
    return line_strings

def theBox():
    text_area = st.ScrolledText(window, width=50, height=80, font=("Times New Roman", 15))
    text_area.insert(tk.INSERT, showAll())
    text_area.pack()
    text_area.config(state="disabled")

""" these are the actual elements """

header = tk.Label(window, font=("Times New Roman", 33), pady=10, padx=10) # here we create the acutal label
punch_bttn = tk.Button(window, text="Punch", font=("TImes New Roman", 20), command=punch, pady=10) # create the button to take the punch
showAllBttn = tk.Button(window, text="See All Punches", font=("TImes New Roman", 20), command=theBox, pady=10, padx=10) # create the button to show all the punches


# run all the functions and pack all the elementes.
header.pack()
punch_bttn.pack()
headerClock()
showAllBttn.pack()
window.mainloop()






