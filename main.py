import time
from tkinter import *
from tkinter import Label


def time_current():
    a= time.strftime("%I:%M:%S %p")
    time_display.config(text=a)      #display time
    time_display.after(200, time_current)
tk_windows = Tk()
tk_windows.title("DIGI CLOCK")

# setting background & front color [label]

time_label = Label(tk_windows, text="Digital Clock", font=("consolas", "14", "bold"),
                   bg="#2C3C3F", fg="#CAF6FF")
time_label.pack()
time_display = Label(tk_windows, font=("radioland", 140, "bold", "italic"),
                     bg="#2C3C3F", fg="#CAF6FF")

time_display.pack()   #display in one single row
time_current()

tk_windows.mainloop()