from tkinter import *
from PIL import Image, ImageTk
from customer import customer_window
from room import room_booking
from details import room_details

class hotelMangementSystem():
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System ")
        self.root.geometry("1550x800+0+0")

        #___________first image__________
        img1 = Image.open("hotel1.png")
        img1 = img1.resize((1550, 140), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        label_img1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        label_img1.place(x=0, y=0, width=1550, height=140)

        #______________logo image_______________
        img2 = Image.open("hotell_logo.jfif")
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        label_img2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        label_img2.place(x=0, y=0, width=230, height=140)

        #__________title name__________________
        label_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black", fg="silver")
        label_title.place(x=0, y=140, width=1550, height=50)

        #_____________creating a frame ____________________
        main_frame =Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        #________________MENU_______________________________
        label_title = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black",fg="silver")
        label_title.place(x=0, y=0, width=230, height=50)

        #______________menu frame__________________________
        button_frame = Frame(main_frame, bd=4, relief=RIDGE)
        button_frame.place(x=0, y=50, width=228, height=215)

        # __________________all the buttons on menu____________________
        customer_but = Button(button_frame, text="CUSTOMER", command=cust_details, font=("times new roman", 15, "bold"), bg="black", fg="silver", width=22, cursor="hand2")
        customer_but.grid(row=0, column=0, pady=1)
        room_but = Button(button_frame, text="ROOM",command=roombooking, font=("times new roman", 15, "bold"), bg="black",fg="silver", width=22, cursor="hand2")
        room_but.grid(row=1, column=0, pady=1)
        details_but = Button(button_frame, text="DETAILS", command=roomdetails, font=("times new roman", 15, "bold"), bg="black",fg="silver", width=22, cursor="hand2")
        details_but.grid(row=2, column=0, pady=1)
        report_but = Button(button_frame, text="REPORT", font=("times new roman", 15, "bold"), bg="black",fg="silver", width=22, cursor="hand2")
        report_but.grid(row=3, column=0, pady=1)
        logout_but = Button(button_frame, text="LOG OUT", font=("times new roman", 15, "bold"), bg="black", fg="silver", width=22, cursor="hand2")
        logout_but.grid(row=4, column=0, pady=1)

        #_________________main hotel centre image_________________
        img3 = Image.open("gettyimages-90565443-612x612.jpg")
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        label_img3 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        label_img3.place(x=225, y=0, width=1310, height=610)

        # _____________________bottom leftmost image___________________
        img4 = Image.open("focused_198841400-stock-photo-united-arab-emirates-dubai-burj.jpg")
        img4 = img4.resize((230, 210), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        label_img4 = Label(main_frame, image=self.photoimg4 , bd=4, relief=RIDGE)
        label_img4.place(x=0, y=266, width=230, height=170)

        img5 = Image.open("menu1.jfif")
        img5 = img5.resize((230, 190), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        label_img5 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        label_img5.place(x=0, y=420, width=230, height=190)

def cust_details():
    new_window = Toplevel(root)
    app = customer_window(new_window)

def roombooking():
    new_window = Toplevel(root)
    app = room_booking(new_window)

def roomdetails():
    new_window = Toplevel(root)
    app = room_details(new_window)

if __name__ == '__main__':
    root = Tk()
    obj = hotelMangementSystem(root)
    root.mainloop()