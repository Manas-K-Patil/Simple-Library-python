import tkinter as tk
import sqlite3
from tkinter import  ttk
from tkinter import  messagebox
win1=tk.Tk()
#adding a label
aLabel=ttk.Label(win1,  text="Book number")
aLabel.grid(column=0,  row=2)
#adding another label
aLabel=ttk.Label(win1,  text="Title")
aLabel.grid(column=0,  row=4)
#adding another label
aLabel=ttk.Label(win1,  text="Author")
aLabel.grid(column=0,  row=6)
#adding another label
aLabel=ttk.Label(win1,  text="book Isbn")
aLabel.grid(column=0,  row=8)
#adding another label
aLabel=ttk.Label(win1,  text="Publishers name")
aLabel.grid(column=0,  row=10)
#adding another label
aLabel=ttk.Label(win1,  text="Status")
aLabel.grid(column=0,  row=12)


#adding textbox book number
bookid=tk.StringVar()
bookid=ttk.Entry(win1,  width=12,  textvariable=bookid)
bookid.grid(column=2,  row=2)
#adding textbox title
title=tk.StringVar()
title=ttk.Entry(win1, width=12,  textvariable=title)
title.grid(column=2,  row=4)
#adding textbox author
author=tk.StringVar()
author=ttk.Entry(win1, width=12,  textvariable=author)
author.grid(column=2,  row=6)
#adding textbox book isbn
isbn=tk.StringVar()
isbn=ttk.Entry(win1, width=12,  textvariable=isbn)
isbn.grid(column=2,  row=8)

#adding textbox publishers name
publishername=tk.StringVar()
publishername=ttk.Entry(win1, width=12,  textvariable=publishername)
publishername.grid(column=2,  row=10)

#adding textbox status
status=tk.StringVar()
status=ttk.Entry(win1, width=12,  textvariable=status)
status.grid(column=2,  row=12)



#function
def af():
    unum1=bookid.get()
    name1=title.get()
    athr=author.get()
    isbn1=isbn.get()
    pub=publishername.get()
    state=status.get()

    conn=sqlite3.connect("Library.db")
    cur=conn.cursor()
    #cur.execute("SELECT * FROM FRUIT WHERE unum = ?", (unum1))
    #rows=cur.fetchall()
    #for column in rows:
        #print(column)
    #cur.execute("CREATE TABLE REMAINDER(number INTEGER PRIMARY KEY, date TEXT UNIQUE);")
    cur.execute("INSERT INTO BOOK(bookid, title, author, isbn, publishername, status)VALUES(?, ?, ?, ?, ?, ?);", (unum1,  name1, athr, isbn1, pub, state) )
    bookid.bind('<Return>',  af) 
    title.bind('<Return>',  af)
    author.bind('<Return>',  af)
    isbn.bind('<Return>',  af)
    publishername.bind('<Return>',  af)
    status.bind('<Return>',  af)
    conn.commit()
    conn.close() 
    print(conn)
    #messagebox.showwarning("Warning",  "Fruit exists")
    messagebox.showinfo("SUCCESSFULL!", "Book inserted")
#adding button
action=ttk.Button(win1, text="OK",  command=af)
action.grid(column=10, row=14)
win1.mainloop()
