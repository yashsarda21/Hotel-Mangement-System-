from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime

class room_booking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System ")
        self.root.geometry("1295x560+230+230")

        # variables
        self.contact = StringVar()
        self.checkout = StringVar()
        self.checkin = StringVar()
        self.room = StringVar()
        self.roomavailable= StringVar()
        self.meal = StringVar()
        self.noofdays = StringVar()
        self.paidtax = StringVar()
        self.actaltotal = StringVar()
        self.totalcost = StringVar()

        label_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 20, "bold"), bg="black", fg="silver")
        label_title.place(x=0, y=0, width=1295, height=50)

        # ______________logo image_______________
        img1 = Image.open("hotell_logo.jfif")
        img1 = img1.resize((100, 50), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        label_img1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        label_img1.place(x=0, y=0, width=100, height=50)

        # ______________label frame__________________
        labelframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Booking", padx=2, font=("times new roman", 25, "bold"))
        labelframe.place(x=5, y=50, width=405, height=490)

        # custref
        label_conatact = Label(labelframe, text="Cutomer Contact", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_conatact.grid(row=0, column=0)

        entry_contact = ttk.Entry(labelframe, textvariable=self.contact, width=18 , font=("times new roman", 12, "bold"))
        entry_contact.grid(row=0, column=1, sticky=W)

        fetch_btn = Button(labelframe, text="fetch data", font=("times new roman", 12, "bold"),command=self.fetch_btn, width=8, bg="black", fg="silver")
        # fetch_btn.grid(row=0, column=2)
        fetch_btn.place(x=282, y=0)
        #check In
        label_check_in = Label(labelframe, text="Check In", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_check_in.grid(row=1, column=0)

        entry_check_in = ttk.Entry(labelframe, textvariable=self.checkin, width=23, font=("times new roman", 12, "bold"))
        entry_check_in.grid(row=1, column=1)
        #check out
        label_check_out = Label(labelframe, text="Check Out", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_check_out.grid(row=2, column=0)

        entry_check_out = ttk.Entry(labelframe, textvariable=self.checkout, width=23, font=("times new roman", 12, "bold"))
        entry_check_out.grid(row=2, column=1)
        #Room type
        label_roomtype = Label(labelframe, text="Room type", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_roomtype.grid(row=3, column=0)

        room_checkbox = ttk.Combobox(labelframe, textvariable=self.room, font=("times new roman", 12, "bold"), width=22, state="readonly")
        room_checkbox["value"] = ("Single", "Double", "Luaxry")
        room_checkbox.current((0))
        room_checkbox.grid(row=3, column=1)

        #available room
        label_available_room = Label(labelframe, text="Available Room", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_available_room.grid(row=4, column=0)

        entry_available_room = ttk.Entry(labelframe, textvariable=self.roomavailable,  width=23, font=("times new roman", 12, "bold"))
        entry_available_room.grid(row=4, column=1)

        #meal
        label_Meal = Label(labelframe, text="Meal", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_Meal.grid(row=5, column=0)

        entry_Meal = ttk.Entry(labelframe, width=23,textvariable=self.meal,  font=("times new roman", 12, "bold"))
        entry_Meal.grid(row=5, column=1)

        # no of days
        label_No_of_days = Label(labelframe, text="No of days", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_No_of_days.grid(row=6, column=0)

        entry_No_of_days = ttk.Entry(labelframe,textvariable=self.noofdays,  width=23, font=("times new roman", 12, "bold"))
        entry_No_of_days.grid(row=6, column=1)

        #paid tax
        label_Paid_tax = Label(labelframe, text="Paid tax", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_Paid_tax.grid(row=7, column=0)

        entry_Paid_tax = ttk.Entry(labelframe, textvariable=self.paidtax, width=23, font=("times new roman", 12, "bold"))
        entry_Paid_tax.grid(row=7, column=1)

        #sub total
        label_Total = Label(labelframe, text="Total", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_Total.grid(row=8, column=0)

        entry_Total = ttk.Entry(labelframe, width=23,textvariable=self.actaltotal,  font=("times new roman", 12, "bold"))
        entry_Total.grid(row=8, column=1)

        # total cost
        label_Totalcost = Label(labelframe, text="Total cost", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_Totalcost.grid(row=9, column=0)

        entry_Totalcost = ttk.Entry(labelframe, textvariable=self.totalcost,  width=23, font=("times new roman", 12, "bold"))
        entry_Totalcost.grid(row=9, column=1)

        # bill button
        bill_btn = Button(labelframe, text="Bill",command=self.totalcostofcustomer, width=10, pady=4, font=("times new roman", 12, "bold"), bg="black",
                          fg="silver")
        bill_btn.grid(row=10, column=0, sticky=W)

        # __________________buttons____________________

        btn_frame = Frame(labelframe, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=392, height=40)


        btnAdd = Button(btn_frame, text="Add", command= self.add_data,  width=10, pady=4, font=("times new roman", 12, "bold"), bg="black",
                        fg="silver")
        btnAdd.grid(row=0, column=0)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, width=10, pady=4, font=("times new roman", 12, "bold"), bg="black",
                           fg="silver")
        btnUpdate.grid(row=0, column=1)

        btndelete = Button(btn_frame, text="Delete", command=self.delete_data, width=10, pady=4, font=("times new roman", 12, "bold"), bg="black",
                           fg="silver")
        btndelete.grid(row=0, column=2)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, width=10, pady=4, font=("times new roman", 12, "bold"), bg="black",
                          fg="silver")
        btnReset.grid(row=0, column=3)

        # bed image
        img1 = Image.open("bed.jpg")
        img1 = img1.resize((500, 240), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        label_img1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        label_img1.place(x=760, y=55, width=500, height=240)


        # ____________tabel fram________________
        labelframe1 = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And search System", padx=2,font=("times new roman", 25, "bold"))
        labelframe1.place(x=435, y=280, width=860, height=260)

        label_search = Label(labelframe1, text="Search By:", font=("times new roman", 12, "bold"), bg="red", fg="white")
        label_search.grid(row=0, column=0, padx=2, pady=2)

        self.searchh = StringVar()
        search_checkbox = ttk.Combobox(labelframe1, textvariable=self.searchh, font=("times new roman", 12, "bold"),width=22, state="readonly")
        search_checkbox["value"] = ("Contact", "Room",)
        search_checkbox.current(0)
        search_checkbox.grid(row=0, column=1, padx=2, pady=2)

        self.txt_search = StringVar()
        entry_search = ttk.Entry(labelframe1, textvariable=self.txt_search, width=23,font=("times new roman", 12, "bold"))
        entry_search.grid(row=0, column=2, padx=2, pady=2)

        btnSearch = Button(labelframe1, text="Search", command=self.searchbar, width=12, pady=4,font=("times new roman", 12, "bold"), bg="black", fg="silver")
        btnSearch.grid(row=0, column=3, padx=2, pady=2)

        btnshow = Button(labelframe1, text="Show All", command=self.fetch_data, width=15, pady=4, font=("times new roman", 12, "bold"), bg="black", fg="silver")
        btnshow.grid(row=0, column=4, padx=2, pady=2)

        # ______________________show data table__________________________
        labeltableframe = LabelFrame(labelframe1, bd=2, relief=RIDGE, padx=2, font=("times new roman", 25, "bold"))
        labeltableframe.place(x=0, y=50, width=840, height=170)

        scroll_x = ttk.Scrollbar(labeltableframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(labeltableframe, orient=VERTICAL)

        self.room_table = ttk.Treeview(labeltableframe, column=("Contact", "CheckIn", "CheckOut", "Room", "RoomAvailable", "Meal", "noOfdays","TotalCost"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Contact", text="Contact")
        self.room_table.heading("CheckIn", text="CheckIn")
        self.room_table.heading("CheckOut", text="Checkout")
        self.room_table.heading("Room", text="Room")
        self.room_table.heading("RoomAvailable", text="RoomAvailable")
        self.room_table.heading("Meal", text="Meal")
        self.room_table.heading("noOfdays", text="noOfdays")
        self.room_table.heading("TotalCost", text="TotalCost")

        self.room_table["show"] = "headings"

        self.room_table.column("Contact", width=110)
        self.room_table.column("CheckIn", width=110)
        self.room_table.column("CheckOut", width=110)
        self.room_table.column("Room", width=110)
        self.room_table.column("RoomAvailable", width=110)
        self.room_table.column("Meal", width=110)
        self.room_table.column("noOfdays", width=110)
        self.room_table.column("TotalCost", width=110)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.getdatafromtabletoboxes)
        self.fetch_data()



    # add button function______________
    def add_data(self):
        if self.contact.get() == "" or self.checkin.get() == "":
            messagebox.showerror("ERROR", "All Fields are Required", parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(host="localhost", username="root", password="yashprem",
                                                         database="yash123")
                myCursor = connection.cursor()
                myCursor.execute(("INSERT INTO room_detals values(%s,%s,%s,%s,%s,%s,%s,%s)"), (
                    self.contact.get(),
                    self.checkout.get(),
                    self.checkin.get(),
                    self.room.get(),
                    self.roomavailable.get(),
                    self.meal.get(),
                    self.noofdays.get(),
                    self.totalcost.get()
                ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("Success", "Room details has been added", parent=self.root)
            except Exception as es:
                messagebox.showerror(("Warning", f"something went Wrong {str(es)}"), parent=self.root)

    def fetch_data(self):
        connection = mysql.connector.connect(host="localhost", username="root", password="yashprem", database="yash123")
        myCursor = connection.cursor()
        myCursor.execute("SELECT * FROM room_detals")
        data = myCursor.fetchall()
        if len(data) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in data:
                self.room_table.insert("", END, values=i)
            connection.commit()
            connection.close()

    def getdatafromtabletoboxes(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]
        self.contact.set(row[0])
        self.checkout.set(row[1])
        self.checkin.set(row[2])
        self.room.set(row[3])
        self.roomavailable.set(row[4])
        self.meal.set(row[5])
        self.noofdays.set(row[6])
        self.totalcost.set(row[7])

    def update(self):
        if self.contact.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            connection = mysql.connector.connect(host="localhost", username="root", password="yashprem",
                                                 database="yash123")
            myCursor = connection.cursor()
            myCursor.execute(
                "update room_detals set CheckIn=%s, CheckOut=%s, Room=%s, RoomAvailable=%s, Meal=%s, noOfdays=%s, TotalCost=%s WHERE Contact=%s",
                (
                    self.checkin.get(),
                    self.checkout.get(),
                    self.room.get(),
                    self.roomavailable.get(),
                    self.meal.get(),
                    self.noofdays.get(),
                    self.totalcost.get(),
                    self.contact.get(),
                ))
            connection.commit()
            self.fetch_data()
            connection.close()
            messagebox.showinfo("Update", "Room details has been updated sucessfully", parent=self.root)

    def delete_data(self):
        delete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer details?",
                                     parent=self.root)
        if delete > 0:
            connection1 = mysql.connector.connect(host="localhost", username="root", password="yashprem",
                                                  database="yash123")
            myCursor = connection1.cursor()
            query = "delete from room_detals where Contact=%s"
            value = (self.contact.get(),)
            myCursor.execute(query, value)
        else:
            if not delete:
                return
        connection1.commit()
        self.fetch_data()
        connection1.close()

    def reset(self):
        self.contact.set(""),
        self.checkin.set(""),
        self.checkout.set(""),
        self.room.set(""),
        self.roomavailable.set(""),
        self.noofdays.set(""),
        self.totalcost.set(""),
        self.paidtax.set(""),
        self.actaltotal.set(""),
        self.totalcost.set("")


    def fetch_btn(self):
        if self.contact.get() == "":
            messagebox.showerror("Error", "contact number is required", parent=self.root)
        else:
            connection = mysql.connector.connect(host="localhost", username="root", password="yashprem",database="yash123")
            myCursor = connection.cursor()
            query = ("select Name from customerss where MobileNumber=%s")
            value = (self.contact.get(),)
            myCursor.execute(query, value)
            row = myCursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "this number is not found", parent=self.root)
            else:
                connection.commit()
                connection.close()

            showdata_frame = Frame(self.root, bd=4, relief=RIDGE, padx=2)
            showdata_frame.place(x=455, y=55, width=300, height=220)
            # _______________name______________
            lbl_name =Label(showdata_frame, text="   Name: ", font=("times new roman", 17, "bold"))
            lbl_name.grid(row=0, column=0)
            lbl_name_1 = Label(showdata_frame, text=row, font=("times new roman", 17, "bold"))
            lbl_name_1.grid(row=0, column=1)
            # ______________gender______________________
            connection = mysql.connector.connect(host="localhost", username="root", password="yashprem",database="yash123")
            myCursor = connection.cursor()
            query = ("select Gender from customerss where MobileNumber=%s")
            value = (self.contact.get(),)
            myCursor.execute(query, value)
            row = myCursor.fetchone()

            lbl_gender =Label(showdata_frame, text="   Gender: ", font=("times new roman", 17, "bold"))
            lbl_gender.grid(row=1, column=0)
            lbl_gender_1 = Label(showdata_frame, text=row, font=("times new roman", 17, "bold"))
            lbl_gender_1.grid(row=1, column=1)

            # ______________email_________________
            connection = mysql.connector.connect(host="localhost", username="root", password="yashprem",database="yash123")
            myCursor = connection.cursor()
            query = ("select Email from customerss where MobileNumber=%s")
            value = (self.contact.get(),)
            myCursor.execute(query, value)
            row = myCursor.fetchone()

            lbl_email =Label(showdata_frame, text="   Email: ", font=("times new roman", 17, "bold"))
            lbl_email.grid(row=2, column=0)
            lbl_email_1 = Label(showdata_frame, text=row, font=("times new roman", 17, "bold"))
            lbl_email_1.grid(row=2, column=1)
            # __________________natinality__________________
            connection = mysql.connector.connect(host="localhost", username="root", password="yashprem",
                                                 database="yash123")
            myCursor = connection.cursor()
            query = ("select Nationality from customerss where MobileNumber=%s")
            value = (self.contact.get(),)
            myCursor.execute(query, value)
            row = myCursor.fetchone()

            lbl_Nationality = Label(showdata_frame, text="   Nationality: ", font=("times new roman", 17, "bold"))
            lbl_Nationality.grid(row=3, column=0)
            lbl_Nationality_1 = Label(showdata_frame, text=row, font=("times new roman", 17, "bold"))
            lbl_Nationality_1.grid(row=3, column=1)

            # ________________address_________________________
            connection = mysql.connector.connect(host="localhost", username="root", password="yashprem",database="yash123")
            myCursor = connection.cursor()
            query = ("select Address from customerss where MobileNumber=%s")
            value = (self.contact.get(),)
            myCursor.execute(query, value)
            row = myCursor.fetchone()

            lbl_Address =Label(showdata_frame, text="   Address: ", font=("times new roman", 17, "bold"))
            lbl_Address.grid(row=4, column=0)
            lbl_Address_1 = Label(showdata_frame, text=row, font=("times new roman", 17, "bold"))
            lbl_Address_1.grid(row=4, column=1)

    def totalcostofcustomer(self):
        inDate = self.checkin.get()
        outDAte  = self.checkout.get()
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDAte = datetime.strptime(outDAte, "%d/%m/%Y")
        self.noofdays.set(abs(outDAte-inDate).days)
        if self.meal.get()=="Breakfast" and self.room.get() == "Single":
            q1 = float(500)
            q2 = float(1000)
            q3 = float(self.noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            tax = "Rs." + str("%.2f"%((q5)*0.30))
            actualtotal = "Rs." + str("%.2f" % (q5))
            totalcost = "Rs." + str("%.2f"%((q5)*0.30+(q5)))
            self.paidtax.set(tax)
            self.actaltotal.set(actualtotal)
            self.totalcost.set(totalcost)


    # searching perticular customer
    def searchbar(self):
        connection1 = mysql.connector.connect(host="localhost", username="root", password="yashprem", database="yash123")
        myCursor = connection1.cursor()
        myCursor.execute(" SELECT * FROM room_detals WHERE " + str(self.searchh.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        rows = myCursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            connection1.commit()
        connection1.close()


if __name__ == '__main__':
    root = Tk()
    obj = room_booking(root)
    root.mainloop()