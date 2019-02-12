import tkinter as tk
import sqlite3
from tkinter import  ttk
from tkinter import  messagebox
win3=tk.Tk()
#adding a label
    aLabel=ttk.Label(win3,  text="Admission no:")
    aLabel.grid(column=5,  row=5)
#adding another label
    aLabel=ttk.Label(win3,  text="Book no")
    aLabel.grid(column=5,  row=7)
#adding another label
    aLabel=ttk.Label(win3,  text="Issue date")
    aLabel.grid(column=5,  row=9)
#adding another label
    aLabel=ttk.Label(win3,  text="Return date")
    aLabel.grid(column=5,  row=11)

#adding textbox admission no
    stdadmno=tk.StringVar()
    stdadmno=ttk.Entry(win3,  width=12,  textvariable=stdadmno)
    stdadmno.grid(column=10,  row=5)
#adding text bookno
    book1=tk.StringVar()
    book1=ttk.Entry(win3, width=12,  textvariable=book1)
    book1.grid(column=10,  row=7)

#adding text issuedate
    issuedate=tk.StringVar()
    issuedate=ttk.Entry(win3, width=12,  textvariable=issuedate)
    issuedate.grid(column=10,  row=9)
    aLabel=ttk.Label(win3,  text="Format: yyyy-mm-dd")
    aLabel.grid(column=15,  row = 9)

#adding text returndate
    returndate=tk.StringVar()
    returndate=ttk.Entry(win3, width=12,  textvariable=returndate)
    returndate.grid(column=10,  row=11)
    aLabel=ttk.Label(win3,  text="Format: yyyy-mm-dd")
    aLabel.grid(column=15,  row = 11)


#function
    def cf():
        
        bnum1=book1.get()
        unum1=stdadmno.get()
        isdate=issuedate.get()
        rtdate=returndate.get()
        
        conn=sqlite3.connect("Library.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO STATUS(stdadmno, book1, issuedate, returndate)VALUES(?, ?, ?, ?);", (unum1,  bnum1, isdate, rtdate) )
        stdadmno.bind('<Return>', cf)
        book1.bind('<Return>',  cf)
        issuedate.bind('<Return>',  cf)
        returndate.bind('<Return>',  cf)
        conn.commit()
        conn.close()

        #conn1=sqlite3.connect("Library.db")
        #cur1=conn1.cursor()
        #cur1.execute("UPDATE BOOK SET status = 'Not_available' WHERE bookid=?", (bnum2))
        #bookid.bind('<Return>',  cf)
        #conn1.commit()
        #conn1.close()

        
        print(conn)
        messagebox.showinfo("SUCCESSFUL", "BOOK ISSUED!"  )
    #name.bind('<Return>', ef)
action=ttk.Button(win3,  text="Issue",  command=cf)
action.grid(column=15,  row=15)
win3.mainloop()
