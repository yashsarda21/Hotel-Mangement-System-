from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class customer_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System ")
        self.root.geometry("1295x560+230+230")

        # __________variables of Mysql________________
        self.ref = StringVar()
        x = random.randint(1000, 10000)
        self.ref.set(str(x))

        self.Name = StringVar()
        self.Mother = StringVar()
        self.Gender = StringVar()
        self.post = StringVar()
        self.mobile = StringVar()
        self.nationality = StringVar()
        self.Idproof = StringVar()
        self.IDNumber = StringVar()
        self.Email = StringVar()
        self.Address = StringVar()


        label_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("Franklin Gothic Heavy", 20, "bold"), bg="black",fg="silver")
        label_title.place(x=0, y=0, width=1295, height=50)

        # ______________logo image_______________
        img1 = Image.open("hotell_logo.jfif")
        img1 = img1.resize((100, 50), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        label_img1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        label_img1.place(x=0, y=0, width=100, height=50)

        # ______________label frame__________________
        labelframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="customer details", padx=2, font=("times new roman", 25, "bold"))
        labelframe.place(x=5, y=50, width=405, height=490)

        # ______________________label and entries___________________
        # custref
        label = Label(labelframe, text="Cutomer Refrence", font=("times new roman", 12, "bold"), padx=2, pady=6 )
        label.grid(row=0, column=0)

        entry_ref = ttk.Entry(labelframe, width=23 ,textvariable=self.ref, font=("times new roman", 12, "bold"), state="readonly")
        entry_ref.grid(row=0, column=1)

        #cust name
        label_cust_name = Label(labelframe, text="Cutomer Name", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_cust_name.grid(row=1, column=0)

        entry_cust_name = ttk.Entry(labelframe, width=23, textvariable=self.Name, font=("times new roman", 12, "bold"))
        entry_cust_name.grid(row=1, column=1)

        #mother name
        label_mother_name = Label(labelframe, text="Mother Name", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_mother_name.grid(row=2, column=0)

        entry_mother_name = ttk.Entry(labelframe, width=23, textvariable=self.Mother, font=("times new roman", 12, "bold"))
        entry_mother_name.grid(row=2, column=1)

        #GENDEER BOX
        label_gender = Label(labelframe, text="Gender", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_gender.grid(row=3, column=0)

        gender_checkbox = ttk.Combobox(labelframe, textvariable=self.Gender, font=("times new roman", 12, "bold"), width=22, state="readonly")
        gender_checkbox["value"] = ("Male", "Female", "Other")
        gender_checkbox.current((0))
        gender_checkbox.grid(row=3, column=1)

        # postcode
        label_post = Label(labelframe, text="PostCode", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_post.grid(row=4, column=0)

        entry_post = ttk.Entry(labelframe, width=23, textvariable=self.post, font=("times new roman", 12, "bold"))
        entry_post.grid(row=4, column=1)

        # mobilenumber
        label_mobile_number = Label(labelframe, text="Mobile Number", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_mobile_number.grid(row=5, column=0)

        entry_mobile_number = ttk.Entry(labelframe, width=23, textvariable=self.mobile, font=("times new roman", 12, "bold"))
        entry_mobile_number.grid(row=5, column=1)

        # email
        label_email = Label(labelframe, text="Email", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_email.grid(row=6, column=0)

        entry_email = ttk.Entry(labelframe, width=23, textvariable=self.Email, font=("times new roman", 12, "bold"))
        entry_email.grid(row=6, column=1)

        #nationality

        label_nationality = Label(labelframe, text="Nationality", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_nationality.grid(row=7, column=0)
        nationality_checkbox = ttk.Combobox(labelframe, textvariable=self.nationality, font=("times new roman", 12, "bold"), width=22, state="readonly")
        nationality_checkbox["value"] = ("Indian", "American", "British", "Other")
        nationality_checkbox.current(0)
        nationality_checkbox.grid(row=7, column=1)

        #idproof
        label_IDproof = Label(labelframe, text="ID Proof",  font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_IDproof.grid(row=8, column=0)
        ID_checkbox = ttk.Combobox(labelframe, textvariable=self.Idproof, font=("times new roman", 12, "bold"), width=22, state="readonly")
        ID_checkbox["value"] = ("Adhar Card", "Pan Card", "Passport", "Other")
        ID_checkbox.current(0)
        ID_checkbox.grid(row=8, column=1)

        #ID number
        label_ID_number = Label(labelframe, text="ID Number", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_ID_number.grid(row=9, column=0)

        entry_ID_number = ttk.Entry(labelframe, width=23,  textvariable=self.IDNumber, font=("times new roman", 12, "bold"))
        entry_ID_number.grid(row=9, column=1)

        #address
        label_adress = Label(labelframe, text="Adress",  font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_adress.grid(row=10, column=0)

        entry_adress = ttk.Entry(labelframe, width=23, textvariable=self.Address, font=("times new roman", 12, "bold"))
        entry_adress.grid(row=10, column=1)

        # __________________buttons____________________

        btn_frame = Frame(labelframe, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=392, height=40)

        btnAdd = Button(btn_frame, text="Add", width=10, pady=4, font=("times new roman", 12, "bold"), bg="black", fg="silver", command=self.add_data)
        btnAdd.grid(row=0, column=0)

        btnUpdate = Button(btn_frame, text="Update", width=10, pady=4, font=("times new roman", 12, "bold"), bg="black", fg="silver", command=self.update)
        btnUpdate.grid(row=0, column=1)

        btndelete = Button(btn_frame, text="Delete", width=10, pady=4, font=("times new roman", 12, "bold"), bg="black",fg="silver", command=self.delete_data)
        btndelete.grid(row=0, column=2)

        btnReset = Button(btn_frame, text="Reset", width=10, pady=4, font=("times new roman", 12, "bold"), bg="black", fg="silver", command=self.reset)
        btnReset.grid(row=0, column=3)

        #____________tabel fram________________
        labelframe1 = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And search System", padx=2, font=("times new roman", 25, "bold"))
        labelframe1.place(x=435, y=50, width=860, height=490)

        label_search = Label(labelframe1, text="Search By:", font=("times new roman", 12, "bold"), bg="red", fg="white")
        label_search.grid(row=0, column=0, padx=2, pady=2)

        self.searchh = StringVar()
        search_checkbox = ttk.Combobox(labelframe1, textvariable=self.searchh, font=("times new roman", 12, "bold"), width=22, state="readonly")
        search_checkbox["value"] = ("MobileNumber", "Ref", "Nationality", "Name", "IDNumber")
        search_checkbox.current(0)
        search_checkbox.grid(row=0, column=1, padx=2, pady=2)

        self.txt_search = StringVar()
        entry_search = ttk.Entry(labelframe1,textvariable=self.txt_search, width=23, font=("times new roman", 12, "bold"))
        entry_search.grid(row=0, column=2, padx=2, pady=2)

        btnSearch = Button(labelframe1, command=self.search, text="Search", width=12, pady=4, font=("times new roman", 12, "bold"), bg="black", fg="silver")
        btnSearch.grid(row=0, column=3, padx=2, pady=2)

        btnshow = Button(labelframe1, text="Show All", width=15, command=self.fetch_data, pady=4, font=("times new roman", 12, "bold"), bg="black", fg="silver")
        btnshow.grid(row=0, column=4, padx=2, pady=2)

        #______________________show data table__________________________
        labeltableframe = LabelFrame(labelframe1, bd=2, relief=RIDGE, padx=2 ,font=("times new roman", 25, "bold"),)
        labeltableframe.place(x=0, y=50, width=840, height=350)

        scroll_x = ttk.Scrollbar(labeltableframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(labeltableframe, orient=VERTICAL)

        self.cust_details_table = ttk.Treeview(labeltableframe, column=("Ref", "Name", "Mother Name", "Gender", "Post", "Mobile", "Email", "Nationality", "ID Proof", "ID Number", "Address"),
                                               xscrollcommand=scroll_x.set,  yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("Ref", text="Refer No")
        self.cust_details_table.heading("Name", text="Name")
        self.cust_details_table.heading("Mother Name", text="Mother Name")
        self.cust_details_table.heading("Gender", text="Gender")
        self.cust_details_table.heading("Post", text="Post")
        self.cust_details_table.heading("Mobile", text="Mobile Number")
        self.cust_details_table.heading("Email", text="Email")
        self.cust_details_table.heading("Nationality", text="Nationality")
        self.cust_details_table.heading("ID Proof", text="ID Proof")
        self.cust_details_table.heading("ID Number", text="ID Number")
        self.cust_details_table.heading("Address", text="Address")

        self.cust_details_table["show"] = "headings"

        self.cust_details_table.column("Ref", width=110)
        self.cust_details_table.column("Name", width=110)
        self.cust_details_table.column("Mother Name", width=110)
        self.cust_details_table.column("Gender", width=110)
        self.cust_details_table.column("Post", width=110)
        self.cust_details_table.column("Mobile", width=110)
        self.cust_details_table.column("Email", width=110)
        self.cust_details_table.column("Nationality", width=110)
        self.cust_details_table.column("ID Proof", width=110)
        self.cust_details_table.column("ID Number", width=110)
        self.cust_details_table.column("Address", width=110)

        self.cust_details_table.pack(fill=BOTH, expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>", self.getdatafromtabletoboxes)
        self.fetch_data()


    def add_data(self):
        if self.mobile.get() == "" or self.Mother.get() == "":
            messagebox.showerror("ERROR", "All Fields are Required", parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(host="localhost", username="root", password="yashprem", database="yash123")
                myCursor = connection.cursor()
                myCursor.execute(("INSERT INTO customerss values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"), (
                    self.ref.get(),
                    self.Name.get(),
                    self.Mother.get(),
                    self.Gender.get(),
                    self.post.get(),
                    self.mobile.get(),
                    self.Email.get(),
                    self.nationality.get(),
                    self.Idproof.get(),
                    self.IDNumber.get(),
                    self.Address.get()
                ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("Success", "Customer has been added")
            except Exception as es:
                messagebox.showerror(("Warning", f"something went Wrong {str(es)}"), parent=self.root)

    def fetch_data(self):
        connection = mysql.connector.connect(host="localhost", username="root", password="yashprem", database="yash123")
        myCursor = connection.cursor()
        myCursor.execute("SELECT * FROM customerss")
        data = myCursor.fetchall()
        if len(data) != 0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in data:
                self.cust_details_table.insert("", END, values=i)
            connection.commit()
            connection.close()

    def getdatafromtabletoboxes(self, event=""):
        cursor_row = self.cust_details_table.focus()
        content = self.cust_details_table.item(cursor_row)
        row = content["values"]
        self.ref.set(row[0]),
        self.Name.set(row[1]),
        self.Mother.set(row[2]),
        self.Gender.set(row[3]),
        self.post.set(row[4]),
        self.mobile.set(row[5]),
        self.Email.set(row[6]),
        self.nationality.set(row[7]),
        self.Idproof.set(row[8]),
        self.IDNumber.set(row[9]),
        self.Address.set(row[10])

    def update(self):
        if self.mobile.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            connection = mysql.connector.connect(host="localhost", username="root", password="yashprem", database="yash123")
            myCursor = connection.cursor()
            myCursor.execute("update customerss set Name=%s, MotherName=%s, Gender=%s, post=%s, MobileNumber=%s, Email=%s, Nationality=%s, IDproof=%s, IDNumber=%s, Address=%s WHERE Ref=%s", (
                self.Name.get(),
                self.Mother.get(),
                self.Gender.get(),
                self.post.get(),
                self.mobile.get(),
                self.nationality.get(),
                self.Idproof.get(),
                self.IDNumber.get(),
                self.Email.get(),
                self.Address.get(),
                self.ref.get()
            ))
            connection.commit()
            self.fetch_data()
            connection.close()
            messagebox.showinfo("Update", "Customer details has been updated sucessfully", parent=self.root)

    def delete_data(self):
        delete = messagebox.askyesno("Hotel Sanagement System", "Do you want to delete this customer details?", parent=self.root)
        if delete > 0:
            connection1 = mysql.connector.connect(host="localhost", username="root", password="yashprem", database="yash123")
            myCursor = connection1.cursor()
            query = "delete from customerss where Ref=%s"
            value = (self.ref.get(),)
            myCursor.execute(query, value)
        else:
            if not delete:
                return
        connection1.commit()
        self.fetch_data()
        connection1.close()

    def reset(self):
        self.Name.set(""),
        self.Mother.set(""),
        self.post.set(""),
        self.mobile.set(""),
        self.IDNumber.set(""),
        self.Idproof.set(""),
        self.Email.set(""),
        self.Address.set("")
        x = random.randint(1000, 10000)
        self.ref.set(str(x))

    def search(self):
        connection1 = mysql.connector.connect(host="localhost", username="root", password="yashprem", database="yash123")
        myCursor = connection1.cursor()
        myCursor.execute(" SELECT * FROM customerss WHERE "+str(self.searchh.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows = myCursor.fetchall()
        if len(rows) != 0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("", END, values=i)
            connection1.commit()
        connection1.close()

if __name__ == '__main__':
    root = Tk()
    obj = customer_window(root)
    root.mainloop()
