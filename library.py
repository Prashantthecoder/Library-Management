from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from tkinter import messagebox
import tkinter
import datetime


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")


        # ==============================================variable==================================================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.name_var=StringVar()
        self.fathername_var=StringVar()
        self.address_var=StringVar()
        self.pincode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.bookname_var=StringVar()
        self.auther_var=StringVar()
        self.borroweddate_var=StringVar()
        self.duedate_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.finalprice_var=StringVar()


        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="light green", fg="green",
                         bd=20, relief=RIDGE, font=("times new roman", 50, "bold", "italic"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)


        frame = Frame(self.root, bd=20, relief=RIDGE,
                      padx=20, bg="light green")
        frame.place(x=0, y=100, width=1370, height=400)


        # ==============Data Frame Left=============================
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="light green", fg="green",
                                   bd=10, relief=RIDGE, font=("times new roman", 12, "bold", "italic"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)
        DataFrameLeft.place(x=0, y=2, width=700, height=350)



        lblMember = Label(DataFrameLeft, font=("times new roman", 12, "bold", "italic"),
                          text="Member Type", padx=2, pady=6, bg="light green", fg="green")
        lblMember.grid(row=0, column=0, sticky=W)
        comMember = ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=(
            "times new roman", 19, "bold"), width=15, state="readonly")
        comMember['value'] = ("-------Select-------","Admin staff", "Lecturer", "Student")
        comMember.current(0)
        comMember.grid(row=0, column=1)

        lblPRN_No = Label(DataFrameLeft, font=("times new roman", 12, "bold", "italic"),
                          text="PRN NO.", padx=2, pady=6, bg="light green", fg="green")
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",16,"bold"),textvariable=self.prn_var,width=20)
        txtPRN_No.grid(row=1,column=1)

        lblId_No = Label(DataFrameLeft, font=("times new roman", 12, "bold", "italic"),
                          text="ID NO.", padx=2, pady=6, bg="light green", fg="green")
        lblId_No.grid(row=2, column=0, sticky=W)
        txtId_No=Entry(DataFrameLeft,font=("times new roman",16,"bold"),textvariable=self.id_var,width=20)
        txtId_No.grid(row=2,column=1)

        lblName = Label(DataFrameLeft, font=("times new roman", 12, "bold", "italic"),
                          text="Name", padx=2, pady=6, bg="light green", fg="green")
        lblName.grid(row=3, column=0, sticky=W)
        txtName=Entry(DataFrameLeft,font=("times new roman",16,"bold"),textvariable=self.name_var,width=20)
        txtName.grid(row=3,column=1)

        lblFather_Name = Label(DataFrameLeft, font=("times new roman", 12, "bold", "italic"),
                          text="Father Name", padx=2, pady=6, bg="light green", fg="green")
        lblFather_Name.grid(row=4, column=0, sticky=W)
        txtFather_Name=Entry(DataFrameLeft,font=("times new roman",16,"bold"),textvariable=self.fathername_var,width=20)
        txtFather_Name.grid(row=4,column=1)

        lblAddress = Label(DataFrameLeft, font=("times new roman", 12, "bold", "italic"),
                          text="Address", padx=2, pady=6, bg="light green", fg="green")
        lblAddress.grid(row=5, column=0, sticky=W)
        txtAddress=Entry(DataFrameLeft,font=("times new roman",16,"bold"),textvariable=self.address_var,width=20)
        txtAddress.grid(row=5,column=1)

        lblPincode = Label(DataFrameLeft, font=("times new roman", 12, "bold", "italic"),
                          text="Pincode", padx=2, pady=6, bg="light green", fg="green")
        lblPincode.grid(row=6, column=0, sticky=W)
        txtPincode=Entry(DataFrameLeft,font=("times new roman",16,"bold"),textvariable=self.pincode_var,width=20)
        txtPincode.grid(row=6,column=1)

        lblMobile_No = Label(DataFrameLeft, font=("times new roman", 12, "bold", "italic"),
                          text="Mobile NO.", padx=2, pady=6, bg="light green", fg="green")
        lblMobile_No.grid(row=7, column=0, sticky=W)
        txtMobile_No=Entry(DataFrameLeft,font=("times new roman",16,"bold"),textvariable=self.mobile_var,width=20)
        txtMobile_No.grid(row=7,column=1)

        lblBook_ID = Label(DataFrameLeft, font=("times new roman", 12, "bold", "italic"),
                          text="Book ID", padx=2, pady=6, bg="light green", fg="green")
        lblBook_ID.grid(row=0, column=2, sticky=W)
        txtBook_ID=Entry(DataFrameLeft,font=("times new roman",16,"bold"),textvariable=self.bookid_var,width=20)
        txtBook_ID.grid(row=0,column=3)

        lblBook_Name = Label(DataFrameLeft, font=("times new roman", 12, "bold", "italic"),
                          text="Book Name", padx=2, pady=6, bg="light green", fg="green")
        lblBook_Name.grid(row=1, column=2, sticky=W)
        txtBook_Name=Entry(DataFrameLeft,font=("times new roman",16,"bold"),textvariable=self.bookname_var,width=20)
        txtBook_Name.grid(row=1,column=3)

        lblAuthor_Name = Label(DataFrameLeft, font=("times new roman", 12, "bold", "italic"),
                          text="Auther Name", padx=2, pady=6, bg="light green", fg="green")
        lblAuthor_Name.grid(row=2, column=2, sticky=W)
        txtAuthor_Name=Entry(DataFrameLeft,font=("times new roman",16,"bold"),textvariable=self.auther_var,width=20)
        txtAuthor_Name.grid(row=2,column=3)

        lblDate_Borrowed = Label(DataFrameLeft, font=("times new roman", 12, "bold", "italic"),
                          text="Borrowed Date", padx=2, pady=6, bg="light green", fg="green")
        lblDate_Borrowed.grid(row=3, column=2, sticky=W)
        txtDate_Borrowed=Entry(DataFrameLeft,font=("times new roman",16,"bold"),textvariable=self.borroweddate_var,width=20)
        txtDate_Borrowed.grid(row=3,column=3)

        lblDate_Due = Label(DataFrameLeft, font=("times new roman", 12, "bold", "italic"),
                          text="Due Date", padx=2, pady=6, bg="light green", fg="green")
        lblDate_Due.grid(row=4, column=2, sticky=W)
        txtDate_Due=Entry(DataFrameLeft,font=("times new roman",16,"bold"),textvariable=self.duedate_var,width=20)
        txtDate_Due.grid(row=4,column=3)

        lblDays_on_Book = Label(DataFrameLeft, font=("times new roman", 12, "bold", "italic"),
                          text="Days on Book", padx=2, pady=6, bg="light green", fg="green")
        lblDays_on_Book.grid(row=5, column=2, sticky=W)
        txtDays_on_Book=Entry(DataFrameLeft,font=("times new roman",16,"bold"),textvariable=self.daysonbook_var,width=20)
        txtDays_on_Book.grid(row=5,column=3)

        lblLate_Return_Fine = Label(DataFrameLeft, font=("times new roman", 12, "bold", "italic"),
                          text="Late Return Fine", padx=2, pady=6, bg="light green", fg="green")
        lblLate_Return_Fine.grid(row=6, column=2, sticky=W)
        txtLate_Return_Fine=Entry(DataFrameLeft,font=("times new roman",16,"bold"),textvariable=self.latereturnfine_var,width=20)
        txtLate_Return_Fine.grid(row=6,column=3)

        lblActual_Price = Label(DataFrameLeft, font=("times new roman", 12, "bold", "italic"),
                          text="Actual Price", padx=2, pady=6, bg="light green", fg="green")
        lblActual_Price.grid(row=7, column=2, sticky=W)
        txtActual_Price=Entry(DataFrameLeft,font=("times new roman",16,"bold"),textvariable=self.finalprice_var,width=20)
        txtActual_Price.grid(row=7,column=3)



        # ===============Data Frame Right============================
        DataFrameRight = LabelFrame(frame, text="Book Details", bg="light green", fg="green",
                                    bd= 10, relief=RIDGE, font=("times new roman", 12, "bold", "italic"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)
        DataFrameRight.place(x=700, y=2, width=600, height=350)

        self.txtBox=Text(DataFrameRight, font=("times new roman",12,"bold","italic"),width=40,height=15,padx=3, pady=6)
        self.txtBox.grid(row=0,column=2,padx=5)

        listScrooolbar=Scrollbar(DataFrameRight)
        listScrooolbar.grid(row=0,column=1,sticky="ns")

        listBooks=["A Secular Agenda","A Suitable Boy","Akbarnama","An idealist View of Life","Arion and the Dolphin","Arthashastra","Ashtadhyayi","Autobiography of an Unknown Indian","A Reveolutionary Life","Ain - i - Akbari","Ajatshatru","Anandmath","Area of Darkness","Broken Wings","Bunch of Old Letters","Bride for the Sahib and Other Stories","By God's Decree","Chandalika","Conquest of Self","Chitra	","Court Dancer","Crescent Moon","Convenient Action:Gujarat's Response to Climate Change","Devadas	Sarat","Durgesh Nandini	Bankim","Dharmashastra"]

        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="A Secular Agenda"):
                self.bookid_var.set("BKID5455")
                self.bookname_var.set("A Secular Agenda")
                self.auther_var.set("Prashant Yadav")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.finalprice_var.set("Rs.500")

            elif(x=="A Suitable Boy"):
                self.bookid_var.set("BKID0055")
                self.bookname_var.set("A Suitable Boy")
                self.auther_var.set("Himanshu Sharma")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.15")
                self.finalprice_var.set("Rs.400")

            elif(x=="Akbarnama"):
                self.bookid_var.set("BKID10564")
                self.bookname_var.set("Akbarnama")
                self.auther_var.set("Bhanu Tyagi")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.20")
                self.finalprice_var.set("Rs.300")

            elif(x=="An idealist View of Life"):
                self.bookid_var.set("BKID85855")
                self.bookname_var.set("An idealist View of Life")
                self.auther_var.set("Vishu Yadav")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.finalprice_var.set("Rs.700")

            elif(x=="Arion and the Dolphin"):
                self.bookid_var.set("BKID0055")
                self.bookname_var.set("Arion and the Dolphin")
                self.auther_var.set("Prashant")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borroweddate_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.15")
                self.finalprice_var.set("Rs.600")


        listBox=Listbox(DataFrameRight,font=("times new roman",12,"bold","italic"),width=25,height=15)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=5)	
        listScrooolbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)


        # ==============Button Frames================================
        framebutton = Frame(self.root, bd=20, relief=RIDGE,
                            padx=20, bg="light green")
        framebutton.place(x=0, y=480, width=1370, height=74)

        btnAddData=Button(framebutton,command=self.add_data,text="Add Data",font=("times new roman",12,"bold","italic"),width=22,height=0,bg="lightgreen",fg="black")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(framebutton,command=self.showData,text="Show Data",font=("times new roman",12,"bold","italic"),width=22,height=0,bg="lightgreen",fg="black")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(framebutton,command=self.update,text="Update",font=("times new roman",12,"bold","italic"),width=22,height=0,bg="lightgreen",fg="black")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(framebutton,command=self.delete,text="Delete",font=("times new roman",12,"bold","italic"),width=22,height=0,bg="lightgreen",fg="black")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(framebutton,command=self.reset,text="Reset",font=("times new roman",12,"bold","italic"),width=22,height=0,bg="lightgreen",fg="black")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(framebutton,command=self.iExit,text="Exit",font=("times new roman",12,"bold","italic"),width=22,height=0,bg="lightgreen",fg="black")
        btnAddData.grid(row=0,column=5)



        # ===============Information================================
        framedetails = Frame(self.root, bd=20, relief=RIDGE,
                             padx=2, bg="light green")
        framedetails.place(x=0, y=535, width=1370, height=210)

        xscroll=ttk.Scrollbar(framedetails,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(framedetails,orient=VERTICAL)

        self.library_table=ttk.Treeview(framedetails,column=("MemberType","PRNNo.","Title","Name","FatherName","Address","PinCode","Mobile","BookID","BookName","Auther","BorrowedDate","DueDate","Days","LateReturnFine","FinalPrice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("MemberType",text="Member Type")
        self.library_table.heading("PRNNo.",text="PRN NO.")
        self.library_table.heading("Title",text="Title")
        self.library_table.heading("Name",text="Name")
        self.library_table.heading("FatherName",text="Father Name")
        self.library_table.heading("Address",text="Address")
        self.library_table.heading("PinCode",text="Pin Code")
        self.library_table.heading("Mobile",text="Mobile NO.")
        self.library_table.heading("BookID",text="Book ID")
        self.library_table.heading("BookName",text="Book Name")
        self.library_table.heading("Auther",text="Auther Name")
        self.library_table.heading("BorrowedDate",text="Borrowed Date")
        self.library_table.heading("DueDate",text="Due Date")
        self.library_table.heading("Days",text="Days")
        self.library_table.heading("LateReturnFine",text="Late Return Fine")
        self.library_table.heading("FinalPrice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("MemberType",width=100)
        self.library_table.column("PRNNo.",width=100)
        self.library_table.column("Title",width=100)
        self.library_table.column("Name",width=100)
        self.library_table.column("FatherName",width=100)
        self.library_table.column("Address",width=100)
        self.library_table.column("PinCode",width=100)
        self.library_table.column("Mobile",width=100)
        self.library_table.column("BookID",width=100)
        self.library_table.column("BookName",width=100)
        self.library_table.column("Auther",width=100)
        self.library_table.column("BorrowedDate",width=100)
        self.library_table.column("DueDate",width=100)
        self.library_table.column("Days",width=100)
        self.library_table.column("LateReturnFine",width=100)
        self.library_table.column("FinalPrice",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Password",database="sys")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.member_var.get(),
                                                                                                        self.prn_var.get(),
                                                                                                        self.id_var.get(),
                                                                                                        self.name_var.get(),
                                                                                                        self.fathername_var.get(),
                                                                                                        self.address_var.get(),
                                                                                                        self.pincode_var.get(),
                                                                                                        self.mobile_var.get(),
                                                                                                        self.bookid_var.get(),
                                                                                                        self.bookname_var.get(),
                                                                                                        self.auther_var.get(),
                                                                                                        self.borroweddate_var.get(),
                                                                                                        self.duedate_var.get(),
                                                                                                        self.daysonbook_var.get(),
                                                                                                        self.latereturnfine_var.get(),
                                                                                                        self.finalprice_var.get(),
                                                                                                        ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success","Member has been inserted successfully")

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Password",database="sys")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set MemberType=%s,ID=%s,Name=%s,FatherName=%s,Address=%s,Pincode=%s,MobileNo=%s,BookID=%s,BookName=%s,AutherName=%s,BorrowedDate=%s,DueDate=%s,DaysonBook=%s,LateReturnFine=%s,ActualPrice=%s where PRNNo=%s",(
                                                                                                        self.member_var.get(),
                                                                                                        self.id_var.get(),
                                                                                                        self.name_var.get(),
                                                                                                        self.fathername_var.get(),
                                                                                                        self.address_var.get(),
                                                                                                        self.pincode_var.get(),
                                                                                                        self.mobile_var.get(),
                                                                                                        self.bookid_var.get(),
                                                                                                        self.bookname_var.get(),
                                                                                                        self.auther_var.get(),
                                                                                                        self.borroweddate_var.get(),
                                                                                                        self.duedate_var.get(),
                                                                                                        self.daysonbook_var.get(),
                                                                                                        self.latereturnfine_var.get(),
                                                                                                        self.finalprice_var.get(),
                                                                                                        self.prn_var.get()
                                                                                                        ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been Updated")
                                                                                                

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Password",database="sys")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cuesor_row=self.library_table.focus()
        content=self.library_table.item(cuesor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.name_var.set(row[3]),
        self.fathername_var.set(row[4]),
        self.address_var.set(row[5]),
        self.pincode_var.set(row[6]),
        self.mobile_var.set(row[7]),
        self.bookid_var.set(row[8]),
        self.bookname_var.set(row[9]),
        self.auther_var.set(row[10]),
        self.borroweddate_var.set(row[11]),
        self.duedate_var.set(row[12]),
        self.daysonbook_var.set(row[13]),
        self.latereturnfine_var.set(row[14]),
        self.finalprice_var.set(row[15])
    
    def showData(self):
        self.txtBox.insert(END, "Member Type\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END, "PRN No.\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END, "ID No.\t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END, "Name\t\t"+ self.name_var.get() + "\n")
        self.txtBox.insert(END, "Father Name\t\t"+ self.fathername_var.get() + "\n")
        self.txtBox.insert(END, "Address\t\t"+ self.address_var.get() + "\n")
        self.txtBox.insert(END, "Pin Code\t\t"+ self.pincode_var.get() + "\n")
        self.txtBox.insert(END, "Mobile No.\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "Book ID\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END, "Book Name\t\t"+ self.bookname_var.get() + "\n")
        self.txtBox.insert(END, "Auther\t\t"+ self.auther_var.get() + "\n")
        self.txtBox.insert(END, "Borrowed Date\t\t"+ self.borroweddate_var.get() + "\n")
        self.txtBox.insert(END, "Due Date\t\t"+ self.duedate_var.get() + "\n")
        self.txtBox.insert(END, "Days On Book\t\t"+ self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END, "Late Return Fine\t\t"+ self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END, "Final Price\t\t"+ self.finalprice_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.name_var.set(""),
        self.fathername_var.set(""),
        self.address_var.set(""),
        self.pincode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.bookname_var.set(""),
        self.auther_var.set(""),
        self.borroweddate_var.set(""),
        self.duedate_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.finalprice_var.set(""),
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library management System","Do You want to exit")
        if iExit>0:
            self.root.destroy()
            return


    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":           
            messagebox.showerror("Error","First Select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Password",database="sys")
            my_cursor=conn.cursor()
            query="delete from library where PRNNo=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been Successfully deleted")


if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
