import tkinter as tk
import sqlite3
from tkinter import  ttk
from tkinter import  messagebox
win4=tk.Tk()
#adding a label
    aLabel=ttk.Label(win4,  text="Admission no:")
    aLabel.grid(column=5,  row=5)
    #adding another label
    aLabel=ttk.Label(win4,  text="Book number")
    aLabel.grid(column=5,  row=7)
    #adding another label
    aLabel=ttk.Label(win4,  text="Returned on")
    aLabel.grid(column=5,  row=9)
    aLabel=ttk.Label(win4,  text="Format: yyyy-mm-dd")
    aLabel.grid(column=15,  row = 9)




    #adding textbox admission no
    stdadmno=tk.StringVar()
    stdadmno=ttk.Entry(win4,  width=12,  textvariable=stdadmno)
    stdadmno.grid(column=10,  row=5)
    #adding text book number
    book1=tk.StringVar()
    book1=ttk.Entry(win4, width=12,  textvariable=book1)
    book1.grid(column=10,  row=7)

    #adding text returned on
    returnedon=tk.StringVar()
    returnedon=ttk.Entry(win4, width=12,  textvariable=returnedon)
    returnedon.grid(column=10,  row=9)

    

#function
    def df():
        snum1=stdadmno.get()
        bnum1=book1.get()
        date=returnedon.get()
        conn=sqlite3.connect("Library.db")
        cur=conn.cursor()
        cur.execute("UPDATE STATUS SET returnedon=? WHERE stdadmno=? AND book1=?", (date, snum1, bnum1))
        stdadmno.bind('<Return>', df)
        returnedon.bind('<Return>',  df)
        book1.bind('<Return>',  df)        
        conn.commit()
        conn.close()
        print(conn)
        messagebox.showinfo("SUCCESSFUL", "BOOK RETURNED!"  )
    #name.bind('<Return>', ef)
#button
action=ttk.Button(win4,  text="Return",  command=df)
action.grid(column=15,  row=15)
win4.mainloop()
