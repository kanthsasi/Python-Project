from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database
db=Database("Employee.db")
root=Tk()
root.title("Employee Management System")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

name=StringVar()
age=StringVar()
doj=StringVar()
email=StringVar()
gender=StringVar()
contact=StringVar()
# Entries Frame
entries_frame=Frame(root,bg="#535c68")
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame,text="Employee Management System",font=("Calibri",18,"bold"),bg="#535c68",fg="white")
title.grid(row=0,columnspan=2,padx=10,pady=20)


lblName=Label(entries_frame,text="Name",font=("Calibri",16),bg="#535c68",fg="white")
lblName.grid(row=1,column=0,padx=10,pady=10,sticky="w")
#For Empty WhiteBox
txtName=Entry(entries_frame,textvariable=name,font=("Calibri",16),width=30)
txtName.grid(row=1,column=1,sticky="w")

lblAge=Label(entries_frame,text="Age",font=("Calibri",16),bg="#535c68",fg="white")
lblAge.grid(row=1,column=2,padx=10,pady=10,sticky="w")
txtAge=Entry(entries_frame,textvariable=age,font=("Calibri",16),width=30)
txtAge.grid(row=1,column=3,sticky="w")

lbldoj=Label(entries_frame,text="D.O.J",font=("Calibri",16),bg="#535c68",fg="white")
lbldoj.grid(row=3,column=0,padx=10,pady=10,sticky="w")
txtdoj=Entry(entries_frame,textvariable=doj,font=("Calibri",16),width=30)
txtdoj.grid(row=3,column=1,sticky="w")

lblemail=Label(entries_frame,text="Email.id",font=("Calibri",16),bg="#535c68",fg="white")
lblemail.grid(row=3,column=2,padx=10,pady=10,sticky="w")
txtemail=Entry(entries_frame,textvariable=email,font=("Calibri",16),width=30)
txtemail.grid(row=3,column=3,sticky="w")

lblgender=Label(entries_frame,text="Gender",font=("Calibri",16),bg="#535c68",fg="white")
lblgender.grid(row=5,column=0,padx=10,pady=10,sticky="w")
comboGender=ttk.Combobox(entries_frame,textvariable=gender,font=("Calibri",16),width=28,state="readonly")
comboGender['values']=("Male","Female","Others")
comboGender.grid(row=5,column=1,sticky="w")

lblcontact=Label(entries_frame,text="Contact.no",font=("Calibri",16),bg="#535c68",fg="white")
lblcontact.grid(row=5,column=2,padx=10,pady=10,sticky="w")
txtcontact=Entry(entries_frame,textvariable=contact,font=("Calibri",16),width=30)
txtcontact.grid(row=5,column=3,sticky="w")

lbladdress=Label(entries_frame,text="Address",font=("Calibri",16),bg="#535c68",fg="white")
lbladdress.grid(row=7,column=0,sticky="w")
txtaddress=Text(entries_frame,width=72,height=5,font=("Calibri",16))
txtaddress.grid(row=7,column=1,columnspan=3,sticky="w")

def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data["values"]
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtaddress.delete(1.0, END)
    txtaddress.insert(END,row[7])


def displayAll():
    tv.delete(*tv.get_children())
    for rows in db.fetch():
        tv.insert("",END,values=rows)

def add_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtdoj.get() == "" or txtemail.get() == "" or comboGender.get() == "" or txtcontact.get() == "" or txtaddress.get(
            1.0, END) == "":
        messagebox.showerror("Error in Input","Please fill all the Details")
        return
    db.insert(txtName.get(),txtAge.get(), txtdoj.get(),txtemail.get(),comboGender.get(),txtcontact.get(),txtaddress.get(
            1.0, END))
    messagebox.showinfo("Success","Record Inserted")
    Clear_employee()
    displayAll()

def edit_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtdoj.get() == "" or txtemail.get() == "" or comboGender.get() == "" or txtcontact.get() == "" or txtaddress.get(
            1.0, END) == "":
        messagebox.showerror("Error in Input","Please fill all the Details")
        return
    db.update(row[0],txtName.get(),txtAge.get(), txtdoj.get(),txtemail.get(),comboGender.get(),txtcontact.get(),txtaddress.get(
            1.0, END))
    messagebox.showinfo("Success","Record Updated")
    Clear_employee()
    displayAll()

def delete_employee():
    db.remove(row[0])
    Clear_employee()
    displayAll()

def Clear_employee():
    name.set("")
    age.set("")
    doj.set("")
    email.set("")
    gender.set("")
    contact.set("")
    txtaddress.delete(1.0,END)

btn_frame=Frame(entries_frame,bg="#535c68")
btn_frame.grid(row=8,column=0,columnspan=4,padx=10,pady=10,sticky="w")
btnAdd=Button(btn_frame,command=add_employee,text="Add Details",width=15,font=("Calibri",16,"bold"),bg="#16a085",fg="white")
btnAdd.grid(row=9,column=0)
btnEdit=Button(btn_frame,command=edit_employee,text="Update Details",width=15,font=("Calibri",16,"bold"),bg="#2980b9",fg="white")
btnEdit.grid(row=9,column=3,padx=10)
btnDelete=Button(btn_frame,command=delete_employee,text="Delete Details",width=15,font=("Calibri",16),bg="red",fg="white")
btnDelete.grid(row=9,column=4,padx=10)
btnClear=Button(btn_frame,command=Clear_employee,text="Clear Details",width=15,font=("Calibri",16),bg="black",fg="white")
btnClear.grid(row=9,column=5,padx=10)

#Table Frame
tree_frame=Frame(root,bg="#ecf0f1")
tree_frame.place(x=0,y=430,width=1300,height=520)
style=ttk.Style()
#modify the font of the body
style.configure("mystyle.Treeview",font=("Calibri",15),rowheight=50)
#modify the font of the headings
style.configure("mystyle.Treeview.Heading",font=("Calibri",15))
tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=5)
tv.heading("2",text="Name")
tv.heading("3",text="Age")
tv.column("3",width=10)
tv.heading("4",text="D.O.J")
tv.column("4",width=80)
tv.heading("5",text="Email")
tv.heading("6",text="Gender")
tv.column("6",width=80)
tv.heading("7",text="Contact")
tv.heading("8",text="Address")
tv["show"]="headings"
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)
root.mainloop()
