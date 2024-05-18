from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import time
from datetime import *
import random
import mysql.connector as mysql

#Title of the project
root=Tk()
root.title("Attendence project")
root.geometry("1920x1080")
label=Label(root,text="CLOUD BASED ATTEDENCE SYSTEM",font=("arial","20","italic","bold"))
label.pack()

'''#adding  background
img =ImageTk.PhotoImage(Image.open("1680773950166.jpg"))
panel = Label(root, image=img)
panel.pack(side = "bottom", fill="both", expand="yes")'''

menubar=Menu(root)
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file)

    #components of menubar
file.add_command(label="New file!",command=None)
file.add_command(label="open",command=None)
file.add_command(label="Save",command=None)
file.add_separator()
def hi3():                   #destroy the screen
    root.destroy()

file.add_command(label="Exit",command=hi3)

    #adding edit bar


root.configure(menu=menubar)
edit=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=edit)
edit.add_command(label="Cut",command=None)
edit.add_command(label="Copy",command=None)
edit.add_command(label="Paste",command=None)
edit.add_separator()

    #adding options of help button

help_=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=help_)
help_.add_command(label="license",command=None)
help_.add_command(label="contact",command=None)
help_.add_command(label="about us",command=None)
help_.add_separator()
help_.add_command(label="About Tk",command=None)


    #Student name button
name=StringVar()
name1=Label(root,text="Name",font=("",18,"")).place(x=80,y=80)
name2=Entry(root,font=("","18",""),textvariable=name).place(x=250,y=80)

    #Roll number
roll=StringVar()
roll1=Label(root,text="Roll Number",font=("",18,"")).place(x=80,y=170)
roll2=Entry(root,font=("","18",""),textvariable=roll).place(x=250,y=170)

    # Time in of the student
time=StringVar()
time1=Label(root,text="Time in",font=("",18,"")).place(x=80,y=250)
time2=Entry(root,font=("","18",""),textvariable=time).place(x=250,y=250)

    #Date
date=StringVar()
date1=Label(root,text="Date",font=("",18,"")).place(x=80,y=330)
date2=Entry(root,font=("",'18',""),textvariable=date).place(x=250,y=330)#

    #id card using radiobutton
id_card=StringVar()
id_card1=Label(root,text="Id_card",font=("",18,"")).place(x=80,y=410)
id_card2=Checkbutton(root,text="Yes",font=("",18,""),variable=id_card1,onvalue=1,offvalue=0,height=1,width=2).place(x=270,y=410)
id_card3=Checkbutton(root,text="No",font=("",18,""),variable=id_card1,onvalue=0,offvalue=1,height=1,width=2).place(x=350,y=410)

    # Shoe weared using checkbox
shoe=StringVar()
shoe1=Label(root,text="Shoe",font=("",18,"")).place(x=80,y=490)
shoe2=Checkbutton(root,text="Yes",font=("",18,""),variable=shoe1,onvalue=0,offvalue=1,height=1,width=2).place(x=270,y=490)
shoe3=Checkbutton(root,text="No",font=("",18,""),variable=shoe1,onvalue=1,offvalue=0,height=1,width=2).place(x=350,y=490)

    #Total present
presents=StringVar()
present1=Label(root,text="Total present",font=("","18",""))
present1.place(x=600,y=80)
present2=Entry(root,font=("","18",""),textvariable=presents)
present2.place(x=800,y=80)

    #Absent members
absents=StringVar()
absent1=Label(root,text="Total Absent",font=("","18",""))
absent1.place(x=600,y=150)
absent2=Entry(root,font=("","18",""),textvariable=absents)
absent2.place(x=800,y=150)

    #save button

def process():
        import mysql.connector as mysql
        mydb= mysql.connect(host="localhost",user="root",password="1234",database="clg",auth_plugin="mysql_native_password")
        mycursor=mydb.cursor()
        mycursor.execute("insert into entry(Name_, Roll_no, Time_in, Date_, Id_Card, Shoe, Total_present, Total_abseent) values(%s,%s,%s,%s,%s,%s,%s,%s)",[name.get(), roll.get(), time.get(), date.get(), id_card.get(), shoe.get(), presents.get(), absents.get()] )
        print("Details are saved sucessfully")
        mydb.commit()
label=Button(root,text="Save",font=("ariel","18","italic","bold"),activeforeground="red",activebackground="black",command=process)
label.place(x=1270,y=710)

    #exit button
def hiii():                     #destroy the screen
    messagebox.showerror("Askquestion","Are you sure?")
    root.destroy()
exits=Button(root,text="Cancel",font=("ariel","18","italic","bold"),activeforeground="red",activebackground="black", command=hiii)
exits.place(x=1410,y=710)

 
    #clock
def clock():
    bb=datetime.now()
    current=bb.strftime("%H:%M:%S")
    label1["text"]=current
    root.after(1000,clock)
    
   #time
label1=Label(root,font=("article 30"),fg="black")
label1.place(x=1200,y=5)
clock()
text1=Label(root,text="Time",font=("","18",""))
text1.place(x=1250,y=70)

    #Ai&Ds dept
dept=StringVar()
dept1=Label(root,text="-- AI&DS DEPT STUDENTS --",font=("","22",""),fg="red")
dept1.place(x=1100,y=330)
dept2=Label(root,text="Number of Boys: 35\nNumber of Girls:  10 ",font=("","18",""))
dept2.place(x=1140,y=370)
dept3=Label(root,text="Total Strength:",font=("","18",""))
dept3.place(x=1140,y=460)
dept3=Label(root,text=" 45",font=("","18",""))
dept3.place(x=1330,y=460)
dept4=Label(root,text="-----",font=("","18",""))
dept4.place(x=1330,y=430)

