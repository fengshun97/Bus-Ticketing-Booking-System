from Tkinter import *

root=Tk()

label_1= Label(root, text='Date:')
label_2= Label(root, text='Time:')
label_3= Label(root, text='Reciept Number:')
label_4= Label(root, text='Depart:')
label_5= Label(root, text='Destination:')
label_6= Label(root, text='Number of ticket:')
label_7= Label(root, text='Total Price:')
label_8= Label(root, text='*Please reach your destination on time, the bus will arrive in 15 minutes.*')

label_1.grid(row=0,column=1,sticky=W)
label_2.grid(row=1,column=1,sticky=W)
label_3.grid(row=2,column=1,sticky=W)
label_4.grid(row=3,column=1,sticky=W)
label_5.grid(row=4,column=1,sticky=W)
label_6.grid(row=5,column=1,sticky=W)
label_7.grid(row=6,column=1,sticky=W)
label_8.grid(row=7,column=1,sticky=W)



root.mainloop()
