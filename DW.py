import time
import tkinter as tk
from tkinter import *

root=Tk()
root.title("Real-time Digital Clock")
clock_frame=Label(root,font=('times',100,'italic'),bg='black',fg='red')
clock_frame.pack(fill='both',expand=1)
def ticks(time1=""):
    # Get the current local time from the system
    time2= time.strftime('%A\n%S:%M:%I\n%D')
    # if the time string has changes, update it
    if time2 != time1:
        time1=time2
        clock_frame.config(text=time2)
        # calls itself every 100 millisecond to update
        clock_frame.after(100,ticks)

def set_alarm():
    global hour_entry
    global minute_entry
    global hour
    global minute
    global LM
    global LH
    global confirm_alarm

def get_time():
    current_time = time.strftime("06:00:00")
    set_alarm()

ticks()
mainloop()
