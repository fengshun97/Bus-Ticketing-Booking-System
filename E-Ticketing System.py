from Tkinter import *
import TkMessageBox as tm
import time
from datetime import date

def Login(self):
    global entry1
    global entry2
    self.login=Tk()
    self.login.title('Ticket Booking System')

    self.userVar=StringVar()
    self.passVar=StringVar()
        
    frame=Frame(self.login)
    frame.pack()
    label=Label(frame,text='Username:')
    label.grid(row=0,sticky=W)
    label_1=Label(frame,text='Password:')
    label_1.grid(row=1,sticky=W)
        
    self.entry1=Entry(frame,textvariable=self.userVar,width=30)
    self.entry1.grid(row=0,column=1)
    self.entry2=Entry(frame,textvariable=self.passVar,width=30)
    self.entry2.grid(row=1,column=1)
        
    Login_Btn=Button(frame,text='Login',fg='brown',command=login_btn).grid(row=3,column=1,sticky=W)

    self.login.mainloop()

def login_btn(self):
    User=entry1.get()
    Pass=entry2.get()
    if not User:
        if not Pass:
            tm.showinfo('Ticket Booking System','Your username and password are missing!')
        else:
            tm.showinfo('Ticket Booking System','Your username is missing!')
    elif not Pass:
        tm.showinfo('Ticket Booking System','Your password is missing!')
    if User=='Alvin' and Pass=='abc123':
        self.login.destroy()
        ticketBuying()

def ticketBuying():
    #date and time
    today=date.today()

    time1 = ''
    clock = Label(root, font=('times', 12, 'bold'))
    clock.grid(row=1,column=4,sticky=E)
    def tick():
        global time1
        time2 = time.strftime('%H:%M:%S')
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
        clock.after(200, tick)
    tick()

    #Label
    label_1 = Label(root, text='Date:')
    label_2 = Label(root, text='Time:')
    label_3 = Label(root, text='Bus Company:',font=("Times", 12,"bold"))
    label_4 = Label(root, text='Destination',font=("Times", 12,"underline"))
    label_5 = Label(root, text='From:')
    label_6 = Label(root, text='To:')
    label_7 = Label(root, text='How many ticket(s) do you want?')
    label_8 = Label(root, text='Price:')
    label_9 = Label(root, text=today, font=('times', 12, 'bold'))
    label_10 = Label(root, text='Buy your ticket for when?')

    label_1.grid(row=1,column=0,sticky=W)
    label_2.grid(row=2,column=0,sticky=W)
    label_3.grid(row=3,column=0,sticky=W)
    label_4.grid(row=6,column=0,sticky=W)
    label_5.grid(row=7,column=0,sticky=W)
    label_6.grid(row=10,column=0,sticky=W)
    label_7.grid(row=13,column=0,sticky=W)
    label_8.grid(row=13,column=3,sticky=W)
    label_9.grid(row=0,column=4,sticky=E)
    label_10.grid(row=0,column=0,sticky=W)


    #Entry
    entry_1 = Entry(root,width=10)
    entry_2 = Entry(root,width=15)
    entry_3 = Entry(root,width=15)
    
    entry_1.grid(row=13,column=1)
    entry_2.grid(row=1,column=0)
    entry_3.grid(row=2,column=0)

    #Button
    but1 = Button(text='Cepat',fg='red')
    but2 = Button(text='Maju',fg='red')
    but3 = Button(text='Rapid',fg='red')
    but4 = Button(text='Khas',fg='red')
    but5 = Button(text='Bulan',fg='red')
    but6 = Button(text='Cyberia',fg='purple')
    but7 = Button(text='MMU',fg='purple')
    but8 = Button(text='Putrajaya Sentral',fg='purple')
    but9 = Button(text='The Arc',fg='purple')
    but10 = Button(text='Shaftbury',fg='purple')
    but11 = Button(text='Cyberia',fg='purple')
    but12 = Button(text='MMU',fg='purple')
    but13 = Button(text='Putrajaya Sentral',fg='purple')
    but14 = Button(text='The Arc',fg='purple')
    but15 = Button(text='Shaftbury',fg='purple')
    but16 = Button(text='OK',fg='blue')
    but17 = Button(text='Proceed to Payment',fg='blue')

    but1.grid(row=4,column=0,sticky=W)
    but2.grid(row=4,column=0)
    but3.grid(row=4,column=0,sticky=E)
    but4.grid(row=4,column=1)
    but5.grid(row=4,column=2)
    but6.grid(row=8,column=0,sticky=W)
    but7.grid(row=8,column=0)
    but8.grid(row=8,column=1,sticky=W)
    but9.grid(row=8,column=2)
    but10.grid(row=8,column=3)
    but11.grid(row=11,column=0,sticky=W)
    but12.grid(row=11,column=0)
    but13.grid(row=11,column=1,sticky=W)
    but14.grid(row=11,column=2)
    but15.grid(row=11,column=3)
    but16.grid(row=13,column=2,sticky=W)
    but17.grid(row=14,column=4)
        

Login(self)





