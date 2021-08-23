from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime

class room_details:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System ")
        self.root.geometry("1295x560+230+230")

        self.floor = StringVar()
        self.roomno = StringVar()
        self.roomtype = StringVar()

        label_title = Label(self.root, text="ROOMS BOOKING floorDETAILS", font=("times new roman", 20, "bold"), bg="black", fg="silver")
        label_title.place(x=0, y=0, width=1295, height=50)

        # ______________logo image_______________
        img1 = Image.open("hotell_logo.jfif")
        img1 = img1.resize((100, 50), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        label_img1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        label_img1.place(x=0, y=0, width=100, height=50)

        # ______________label frame__________________
        labelframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="NEW ROOMS ADD", padx=2,
                                font=("times new roman", 25, "bold"))
        labelframe.place(x=5, y=50, width=555, height=350)

        label_floor = Label(labelframe, text="Floor", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_floor.grid(row=0, column=0)

        entryfloor = ttk.Entry(labelframe, textvariable=self.floor, width=18, font=("times new roman", 12, "bold"))
        entryfloor.grid(row=0, column=1, sticky=W, padx=20)

        label_roomno = Label(labelframe, text="Room No", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_roomno.grid(row=1, column=0)

        entryroomno = ttk.Entry(labelframe, textvariable=self.roomno, width=18, font=("times new roman", 12, "bold"))
        entryroomno.grid(row=1, column=1, sticky=W, padx=20)

        label_roomtype = Label(labelframe, text="Room Type", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_roomtype.grid(row=2, column=0)

        entryroomtype = ttk.Entry(labelframe,  textvariable=self.roomtype, width=18, font=("times new roman", 12, "bold"))
        entryroomtype.grid(row=2, column=1, sticky=W, padx=20)

        # __________________buttons____________________

        btn_frame = Frame(labelframe, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=230, width=392, height=40)

        btnAdd = Button(btn_frame, text="Add",command=self.add_data, width=10, pady=4,
                        font=("times new roman", 12, "bold"), bg="black",
                        fg="silver")
        btnAdd.grid(row=0, column=0)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, width=10, pady=4,
                           font=("times new roman", 12, "bold"), bg="black",
                           fg="silver")
        btnUpdate.grid(row=0, column=1)

        btndelete = Button(btn_frame, text="Delete",  command=self.delete_data, width=10, pady=4,
                           font=("times new roman", 12, "bold"), bg="black",
                           fg="silver")
        btndelete.grid(row=0, column=2)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, width=10, pady=4,
                          font=("times new roman", 12, "bold"), bg="black",
                          fg="silver")
        btnReset.grid(row=0, column=3)


        # ____________tabel fram________________
        labelframe1 = LabelFrame(self.root, bd=2, relief=RIDGE, text="show room details", padx=2,font=("times new roman", 25, "bold"))
        labelframe1.place(x=600, y=55, width=650, height=350)

        #______________scroll bar__________________________
        scroll_x = ttk.Scrollbar(labelframe1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(labelframe1, orient=VERTICAL)
        self.room_table = ttk.Treeview(labelframe1, column=(
        "Floor", "RoomNo", "RoomType"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Floor", text="Floor")
        self.room_table.heading("RoomNo", text="RoomNo")
        self.room_table.heading("RoomType", text="RoomType")

        self.room_table["show"] = "headings"

        self.room_table.column("Floor", width=110)
        self.room_table.column("RoomNo", width=110)
        self.room_table.column("RoomType", width=110)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.getdatafromtabletoboxes)
        self.fetch_data()

        # add button function______________
    def add_data(self):
        if self.roomno.get() == "" or self.roomtype.get() == "":
            messagebox.showerror("ERROR", "All Fields are Required", parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(host="localhost", username="root", password="yashprem",
                                                         database="yash123")
                myCursor = connection.cursor()
                myCursor.execute(("INSERT INTO customerroomdetails values(%s,%s,%s)"), (
                        self.floor.get(),
                        self.roomno.get(),
                        self.roomtype.get(),
                    ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("Success", "Room added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(("Warning", f"something went Wrong {str(es)}"), parent=self.root)

    def fetch_data(self):
        connection = mysql.connector.connect(host="localhost", username="root", password="yashprem", database="yash123")
        myCursor = connection.cursor()
        myCursor.execute("SELECT * FROM customerroomdetails")
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
        self.floor.set(row[0]),
        self.roomno.set(row[1]),
        self.roomtype.set(row[2])

    def update(self):
        if self.floor.get() == "":
            messagebox.showerror("Error", "Please valid floor number", parent=self.root)
        else:
            connection = mysql.connector.connect(host="localhost", username="root", password="yashprem", database="yash123")
            myCursor = connection.cursor()
            myCursor.execute("update customerroomdetails set Floor=%s, RoomType=%s WHERE RoomNo=%s", (
                self.floor.get(),
                self.roomtype.get(),
                self.roomno.get(),
            ))
            connection.commit()
            self.fetch_data()
            connection.close()
            messagebox.showinfo("Update", "Customer details has been updated sucessfully", parent=self.root)

    def delete_data(self):
        delete = messagebox.askyesno("Hotel management System", "Do you want to delete this customer details?", parent=self.root)
        if delete > 0:
            connection1 = mysql.connector.connect(host="localhost", username="root", password="yashprem", database="yash123")
            myCursor = connection1.cursor()
            query = "delete from customerroomdetails where RoomNo=%s"
            value = (self.roomno.get(),)
            myCursor.execute(query, value)
        else:
            if not delete:
                return
        connection1.commit()
        self.fetch_data()
        connection1.close()

    def reset(self):
        self.floor.set(""),
        self.roomno.set(""),
        self.roomtype.set("")


























if __name__ == '__main__':
    root = Tk()
    obj = room_details(root)
    root.mainloop()