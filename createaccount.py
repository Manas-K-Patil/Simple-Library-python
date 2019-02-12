import tkinter as tk
import sqlite3
from tkinter import  ttk
from tkinter import  messagebox
win2=tk.Tk()
#adding a label
aLabel=ttk.Label(win2,  text="Admission no")
aLabel.grid(column=0,  row=2)
#adding another label
aLabel=ttk.Label(win2,  text="Name")
aLabel.grid(column=0,  row=4)
#adding another label
aLabel=ttk.Label(win2,  text="Branch")
aLabel.grid(column=0,  row=6)
#adding another label
aLabel=ttk.Label(win2,  text="Semester")
aLabel.grid(column=0,  row=8)
#adding another label
aLabel=ttk.Label(win2,  text="Valid upto")
aLabel.grid(column=0,  row=10)


#adding textbox book number
admissionno=tk.StringVar()
admissionno=ttk.Entry(win2,  width=12,  textvariable=admissionno)
admissionno.grid(column=2,  row=2)
#adding textbox title
name=tk.StringVar()
name=ttk.Entry(win2, width=12,  textvariable=name)
name.grid(column=2,  row=4)
#adding textbox author
branch=tk.StringVar()
branch=ttk.Entry(win2, width=12,  textvariable=branch)
branch.grid(column=2,  row=6)
#adding textbox book isbn
sem=tk.StringVar()
sem=ttk.Entry(win2, width=12,  textvariable=sem)
sem.grid(column=2,  row=8)

#adding textbox publishers name
validity=tk.StringVar()
validity=ttk.Entry(win2, width=12,  textvariable=validity)
validity.grid(column=2,  row=10)





#function
def bf():
    num=admissionno.get()
    name1=name.get()
    bran=branch.get()
    sem1=sem.get()
    val=validity.get()
    
    conn=sqlite3.connect("Library.db")
    cur=conn.cursor()
    #cur.execute("SELECT * FROM FRUIT WHERE unum = ?", (unum1))
    #rows=cur.fetchall()
    #for column in rows:
        #print(column)
    #cur.execute("CREATE TABLE REMAINDER(number INTEGER PRIMARY KEY, date TEXT UNIQUE);")
    cur.execute("INSERT INTO STUDENT(admissionno, name, branch, sem, validity)VALUES(?, ?, ?, ?, ?);", (num,  name1, bran, sem1, val) )
    admissionno.bind('<Return>',  bf) 
    name.bind('<Return>',  bf)
    branch.bind('<Return>',  bf)
    sem.bind('<Return>',  bf)
    validity.bind('<Return>',  bf)
    conn.commit()
    conn.close() 
    print(conn)
    #messagebox.showwarning("Warning",  "Fruit exists")
    messagebox.showinfo("SUCCESSFULL!", "Account created")
#adding button
action=ttk.Button(win2, text="OK",  command=bf)
action.grid(column=10, row=14)
win2.mainloop()
