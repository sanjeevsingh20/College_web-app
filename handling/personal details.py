from tkinter import *
from tkinter import ttk
from tkinter import messagebox as tmg
import mysql.connector
from PIL import ImageTk

import PIL.Image


def submit():
    try:
        if name.get() and phone.get() and age.get():
            #saving data into database
            db=mysql.connector.connect(host='localhost',user='root',password='@#Sanjukumar123',database='profile')
            mycur=db.cursor()
            mycur.execute('insert into registration values(%s,%s,%s,%s,%s,%s,%s,%s)',(name.get(),last.get(),phone.get(),add.get(),email.get(),age.get(),stra.get(),course.get()))
            db.commit()
         
         #confirmation message 
            tmg.showinfo('Sucessfully Registered',f"{name.get()} Your Are sucessfully registered to our course")
            print(name.get())
            root.destroy()
        else:
         tmg.showwarning('warning','Please fill mandatory entries marked with *')
    except:
        tmg.showerror("Error",'Please fill the details correctly')
root=Tk()
root.title("Registration")
root.configure(bg='powder blue')
f1=Frame(root)
f1.grid()
f2=Frame(root)
f2.grid()
f3=Frame(root,bg='powder blue')
f3.grid()
Label(f2,text='STUDENT SKILLS ENHANCEMENT PROGRAM',justify='center',font=('arial black',13,'bold'),anchor=E,bg='powder blue').grid(column=2)
photo=PIL.Image.open("/Users/91875/Documents/handling/du.png")

render =ImageTk.PhotoImage(photo)

img=Label(image=render)
img.grid(row=0,column=0)
str=StringVar
#entry of first name
name=Entry(f3,textvariable=str)
Label(f3,text='First Name*',bg='powder blue').grid(row=7,column=0)
name.grid(row=7,column=2,padx=5)

#entry opf last name 

last=Entry(f3,textvariable=str)
Label(f3,text='Last name',bg='powder blue').grid(row=7,column=6)
last.grid(row=7,column=7,padx=15)

#phone number 
phone=Entry(f3,textvariable=str)
Label(f3,text='Phone number*',bg='powder blue').grid(row=9,column=0)
phone.grid(row=9,column=2,pady=15,padx=5)

#email entry
email=Entry(f3,textvariable=str)
Label(f3,text='Email',bg='powder blue').grid(row=11,column=0)
email.grid(row=11,column=2,padx=5)

#gender 
stra=StringVar()
stra.set("None")
Label(f3,text='Gender',bg='powder blue').grid(row=13,column=0,pady=10)
Radiobutton(f3,text='Male',variable=stra,value='Male',bg='powder blue').grid(row=13,column=2)
Radiobutton(f3,text='Female',variable=stra,value='Female',bg='powder blue').grid(row=13,column=3)

#adress entry
add=Entry(f3,textvariable=str)
Label(f3,text='Address',bg='powder blue').grid(row=9,column=6)
add.grid(row=9,column=7,pady=15)


#asking age of a user 
age=ttk.Combobox(f3,textvariable=str)
Label(f3,text="Age*",bg='powder blue').grid(row=11,column=6)
age['values']=(15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40)
age.grid(row=11,column=7,pady=15)

#course selection 
course=ttk.Combobox(f3,textvariable=str)
Label(f3,text="select the course*",bg='powder blue',font=('helvetica',9,'bold')).grid(row=13,column=6)
course['values']=('C','C++','C#','CSS','HTML','JAVA','JAVASCRIPT','PYTHON')
course.grid(row=13,column=7,pady=15) 

#Creating submitting button

Button(f3,text="SUBMIT",command=submit,cursor='hand2').grid(row=16,column=4,pady=8)


root.mainloop()