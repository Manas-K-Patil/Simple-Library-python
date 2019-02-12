import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import  messagebox
#window creation
win=tk.Tk()
win.geometry("500x500")
win.resizable(0, 0)
aLabel=ttk.Label(win,  text="LIBRARY MANAGEMENT SYSTEM")
aLabel.grid(column=10,  row=10)

#add book details
#function1
def af():
    win1=tk.Tk()
    win1.geometry("500x500")
    win1.resizable(0, 0)
#adding a label
    aLabel=ttk.Label(win1,  text="Book number")
    aLabel.grid(column=5,  row=5)
#adding another label
    aLabel=ttk.Label(win1,  text="Title")
    aLabel.grid(column=5,  row=6)
#adding another label
    aLabel=ttk.Label(win1,  text="Author")
    aLabel.grid(column=5,  row=9)
#adding another label
    aLabel=ttk.Label(win1,  text="book Isbn")
    aLabel.grid(column=5,  row=11)
#adding another label
    aLabel=ttk.Label(win1,  text="Publishers name")
    aLabel.grid(column=5,  row=13)



#adding textbox book number
    bookid=tk.StringVar()
    bookid=ttk.Entry(win1,  width=12,  textvariable=bookid)
    bookid.grid(column=10,  row=5)
#adding textbox title
    title=tk.StringVar()
    title=ttk.Entry(win1, width=12,  textvariable=title)
    title.grid(column=10,   row=6)
#adding textbox author
    author=tk.StringVar()   
    author=ttk.Entry(win1, width=12,  textvariable=author)
    author.grid(column=10,  row=9)
#adding textbox book isbn
    isbn=tk.StringVar()
    isbn=ttk.Entry(win1, width=12,  textvariable=isbn)
    isbn.grid(column=10,  row=11)

#adding textbox publishers name
    publishername=tk.StringVar()
    publishername=ttk.Entry(win1, width=12,  textvariable=publishername)
    publishername.grid(column=10,  row=13)






#function
    def mf():
        unum1=bookid.get()
        name1=title.get()
        athr=author.get()
        isbn1=isbn.get()
        pub=publishername.get()
        

        conn=sqlite3.connect("Library.db")
        cur=conn.cursor()
    #cur.execute("SELECT * FROM FRUIT WHERE unum = ?", (unum1))
    #rows=cur.fetchall()
    #for column in rows:
        #print(column)
    #cur.execute("CREATE TABLE REMAINDER(number INTEGER PRIMARY KEY, date TEXT UNIQUE);")
        cur.execute("INSERT INTO BOOK(bookid, title, author, isbn, publishername)VALUES(?, ?, ?, ?, ?);", (unum1,  name1, athr, isbn1, pub) )
        bookid.bind('<Return>',  mf) 
        title.bind('<Return>',  mf)
        author.bind('<Return>', mf)
        isbn.bind('<Return>',  mf)
        publishername.bind('<Return>',  mf)
        conn.commit()
        conn.close() 
        print(conn)
    #messagebox.showwarning("Warning",  "Fruit exists")
        messagebox.showinfo("SUCCESSFULL!", "Book inserted")
 #adding button
    action=ttk.Button(win1, text="OK",  command=mf)
    action.grid(column=20, row=20)
    win1.mainloop()

#add student details
def bf():
    win2=tk.Tk()
    win2.geometry("500x500")
    win2.resizable(0, 0)
#adding a label
    aLabel=ttk.Label(win2,  text="Admission no")
    aLabel.grid(column=5,  row=5)
#adding another label
    aLabel=ttk.Label(win2,  text="Name")
    aLabel.grid(column=5,  row=7)
#adding another label
    aLabel=ttk.Label(win2,  text="Branch")
    aLabel.grid(column=5,  row=9)
#adding another label
    aLabel=ttk.Label(win2,  text="Semester")
    aLabel.grid(column=5,  row=11)
#adding another label
    aLabel=ttk.Label(win2,  text="Valid upto")
    aLabel.grid(column=5,  row=13)


#adding textbox admission no
    admissionno=tk.StringVar()
    admissionno=ttk.Entry(win2,  width=12,  textvariable=admissionno)
    admissionno.grid(column=10,  row=5)
#adding textbox name
    name=tk.StringVar()
    name=ttk.Entry(win2, width=12,  textvariable=name)
    name.grid(column=10,  row=7)
#adding textbox branch
    branch=tk.StringVar()
    branch=ttk.Entry(win2, width=12,  textvariable=branch)
    branch.grid(column=10,  row=9)
#adding textbox semester
    sem=tk.StringVar()
    sem=ttk.Entry(win2, width=12,  textvariable=sem)
    sem.grid(column=10,  row=11)

#adding textbox validity
    validity=tk.StringVar()
    validity=ttk.Entry(win2, width=12,  textvariable=validity)
    validity.grid(column=10,  row=13)





#function
    def mf():
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
        admissionno.bind('<Return>',  mf) 
        name.bind('<Return>',  mf)
        branch.bind('<Return>',  mf)
        sem.bind('<Return>',  mf)
        validity.bind('<Return>',  mf)
        conn.commit()
        conn.close() 
        print(conn)
    #messagebox.showwarning("Warning",  "Fruit exists")
        messagebox.showinfo("SUCCESSFULL!", "Account created")

#adding button
    action=ttk.Button(win2, text="OK",  command=mf)
    action.grid(column=20, row=20)
    win2.mainloop()

#issue a book
#function

def mf():
    win3=tk.Tk()
    win3.geometry("500x500")
    win3.resizable(0, 0)
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
        print(conn)
        messagebox.showinfo("SUCCESSFUL", "BOOK ISSUED!"  )
    #name.bind('<Return>', ef)
#button
    action=ttk.Button(win3,  text="Issue",  command=cf)
    action.grid(column=20,  row=20)
    win3.mainloop()

#update book table after issue
def vf():
    win7=tk.Tk()
    win7.geometry("500x500")
    win7.resizable(0, 0)
#adding a label
    aLabel=ttk.Label(win7,  text="Bookid")
    aLabel.grid(column=5,  row=5)

#adding textbox bookid
    bookid=tk.StringVar()
    bookid=ttk.Entry(win7,  width=12,  textvariable=bookid)
    bookid.grid(column=10,  row=5)



#function
    def cf():
        
        bnum=bookid.get()
        conn=sqlite3.connect("Library.db")
        cur=conn.cursor()
        cur.execute("UPDATE BOOK SET status='Not_available' WHERE bookid=?", (bnum, ))
        #bookid.bind('<Return>',  cf)
        conn.commit()
        conn.close()
        print(conn)
        messagebox.showinfo("SUCCESSFUL", "Table updated!"  )
    #name.bind('<Return>', ef)
#button
    action=ttk.Button(win7,  text="Update",  command=cf)
    action.grid(column=20,  row=20)
    win7.mainloop()


#return a  book
#function

def ef():
    win4=tk.Tk()
    win4.geometry("500x500")
    win4.resizable(0, 0)

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
    action.grid(column=20,  row=20)
    win4.mainloop()


#update book table after return
def nf():
    win8=tk.Tk()
    win8.geometry("500x500")
    win8.resizable(0, 0)
#adding a label
    aLabel=ttk.Label(win8,  text="Bookid")
    aLabel.grid(column=5,  row=5)

#adding textbox bookid
    bookid=tk.StringVar()
    bookid=ttk.Entry(win8,  width=12,  textvariable=bookid)
    bookid.grid(column=10,  row=5)



#function
    def cf():
        
        bnum=bookid.get()
        
        conn=sqlite3.connect("Library.db")
        cur=conn.cursor()
        cur.execute("UPDATE BOOK SET status='available' WHERE bookid=?", (bnum, ))
        bookid.bind('<Return>',  cf)
        conn.commit()
        conn.close()
        print(conn)
        messagebox.showinfo("SUCCESSFUL", "Table updated!"  )
    #name.bind('<Return>', ef)
#button
    action=ttk.Button(win8,  text="Update",  command=cf)
    action.grid(column=20,  row=20)
    win8.mainloop()

#view book details
#function

def ff():
    win5=tk.Tk()
    win5.geometry("700x750")
    win5.resizable(0, 0)

    #adding a label
    aLabel=ttk.Label(win5,  text="Book number")
    aLabel.grid(column=5,  row=3)
   

    #adding textbox book no
    bookid=tk.StringVar()
    bookid=ttk.Entry(win5,  width=12,  textvariable="bookid")
    bookid.grid(column=7,  row=3)
    
    

#function
    def df():
        bnum=bookid.get()
        conn=sqlite3.connect("Library.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM BOOK WHERE bookid = ?", (bnum, ))
        for row in cur.fetchall():
            s=row
        bookid.bind('<Return>',  df)
        conn.commit()
        conn.close()
        print(conn) 
        aLabel=ttk.Label(win5,  text=s)
        aLabel.grid(column=1, row=10)
   
#button
    action=ttk.Button(win5,  text="View",  command=df)
    action.grid(column=11,  row=5)
    win5.mainloop()




#view student details
#function

def gf():
    win6=tk.Tk()
    win6.geometry("700x700")
    win6.resizable(0, 0)

    #adding a label
    aLabel=ttk.Label(win6,  text="Admission no")
    aLabel.grid(column=10,  row=3)
   

    #adding textbox book no
    admissionno=tk.StringVar()
    admissionno=ttk.Entry(win6,  width=12,  textvariable="admissionno")
    admissionno.grid(column=12,  row=3)
    
    

#function
    def df():
        num=admissionno.get()
        conn=sqlite3.connect("Library.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM STUDENT WHERE admissionno = ?", (num, ))
        for row in cur.fetchall():
            s=row
        admissionno.bind('<Return>',  df)
        conn.commit()
        conn.close()
        print(conn)
        aLabel=ttk.Label(win6,  text=s)
        aLabel.grid(column=5, row=10)
   
#button
    action=ttk.Button(win6,  text="View",  command=df)
    action.grid(column=14,  row=5)
    win6.mainloop()








#Button1
action=ttk.Button(win,  text="Insert book",  command=af)
action.grid(column=15,  row=15)

#Button2
action=ttk.Button(win,  text="Create an account",  command=bf)
action.grid(column=15,  row=17)

#Button3
action=ttk.Button(win,  text="Issue book",  command=mf)
action.grid(column=15,  row=19)

#Button update
action=ttk.Button(win,  text="Update table",  command=vf)
action.grid(column=17,  row=19)

#Button4
action=ttk.Button(win,  text="Return book",  command=ef)
action.grid(column=15,  row=21)
#Button update
action=ttk.Button(win,  text="Update table",  command=nf)
action.grid(column=17,  row=21)


#Button 5
action=ttk.Button(win,  text="View Book Details",  command=ff)
action.grid(column=15,  row=23)

#Button4
action=ttk.Button(win,  text="View student details",  command=gf)
action.grid(column=15,  row=25)

win.mainloop()

    
