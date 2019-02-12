import tkinter as tk
from tkinter import ttk
#window creation
win=tk.Tk()
win.geometry("300x150")
#function1
def af():
    win1=tk.Tk()
    win1.mainloop()
#function2
def bf():
    win2=tk.Tk()
    win2.mainloop()
#function3
def cf():
    win3=tk.Tk()
    win3.mainloop()
#function4
def df():
    win4=tk.Tk()
    win4.mainloop()
#function5
def vf():
    win5=tk.Tk()
    win5.mainloop()

#Button1
action=ttk.Button(win,  text="Insert book",  command=af)
action.grid(column=0,  row=0)
#Button2
action=ttk.Button(win,  text="create an account",  command=bf)
action.grid(column=0,  row=2)
#Button3
action=ttk.Button(win,  text="Issue book",  command=cf)
action.grid(column=0,  row=4)
#Button4
action=ttk.Button(win,  text="Return book",  command=df)
action.grid(column=0,  row=8)
#Button5
action=ttk.Button(win,  text="View details",  command=vf)
action.grid(column=0,  row=12)
win.mainloop()
