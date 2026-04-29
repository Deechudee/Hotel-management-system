import os
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox
import mysql.connector

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # Variables
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noOfdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        # Title
        lbl_title = Label(self.root, text="Room Booking Details", font=("times new roman", 30, "bold"), bg="black", fg="lightblue", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        img2 = Image.open(r"D:\Hotel Management System\assets - Copy\hotel2.jpg")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        lblframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room booking Details", font=("arial", 12, "bold"), padx=2)
        lblframeleft.place(x=5, y=50, width=425, height=490)

        # Customer Contact
        lbl_cust_contact = Label(lblframeleft, text="Customer Contact", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        enty_contact = ttk.Entry(lblframeleft, textvariable=self.var_contact, font=("arial", 13, "bold"), width=20)
        enty_contact.grid(row=0, column=1, sticky=W)

        # Fetch Data Button
        btnFetchData = Button(lblframeleft, command=self.Fetch_contact, text="Fetch Data", font=("arial", 8, "bold"), bg="black", fg="gold", width=8)
        btnFetchData.place(x=345, y=4)

        # Check-in Date
        check_in_date = Label(lblframeleft, text="Check in date", font=("arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        txtcheck_in_date = ttk.Entry(lblframeleft, textvariable=self.var_checkin, font=("arial", 13, "bold"), width=29)
        txtcheck_in_date.grid(row=1, column=1)

        # Check-out Date
        lbl_Check_out_date = Label(lblframeleft, text="Check out date", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_Check_out_date.grid(row=2, column=0, sticky=W)
        txt_Check_out_date = ttk.Entry(lblframeleft, textvariable=self.var_checkout, font=("arial", 13, "bold"), width=29)
        txt_Check_out_date.grid(row=2, column=1)

        # Room Type
        label_RoomType = Label(lblframeleft, text="Room Type:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="deeChu@2004", database="hotel_db")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide = [item[0] for item in my_cursor.fetchall()]  # Fetching room types

        combo_RoomType = ttk.Combobox(lblframeleft, textvariable=self.var_roomtype, font=("arial", 13, "bold"), width=27, state="readonly")
        combo_RoomType["values"] = ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)
        
        

        # Available Room
        lblRoomAvailable = Label(lblframeleft, text="Available room:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        txtRoomAvailable = ttk.Entry(lblframeleft, textvariable=self.var_roomavailable, font=("arial", 13, "bold"), width=29)
        txtRoomAvailable.grid(row=4, column=1)

        my_cursor.execute("select RoomNo from details")
        rows = [item[0] for item in my_cursor.fetchall()]  # Fetching available room numbers

        combo_RoomNo = ttk.Combobox(lblframeleft, textvariable=self.var_roomavailable, font=("arial", 13, "bold"), width=27, state="readonly")
        combo_RoomNo["values"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)

        # Meal
        lblMeal = Label(lblframeleft, text="Meal:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)
        txtMeal = ttk.Entry(lblframeleft, textvariable=self.var_meal, font=("arial", 13, "bold"), width=29)
        txtMeal.grid(row=5, column=1)

        # No of Days
        lblNoOfDays = Label(lblframeleft, text="No of Days:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(lblframeleft, textvariable=self.var_noOfdays, font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=6, column=1)

        # Paid Tax
        lblPaidTax = Label(lblframeleft, text="Paid Tax:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPaidTax.grid(row=7, column=0, sticky=W)
        txtPaidTax = ttk.Entry(lblframeleft, textvariable=self.var_paidtax, font=("arial", 13, "bold"), width=29)
        txtPaidTax.grid(row=7, column=1)

        # Sub Total
        lblSubTotal = Label(lblframeleft, text="Sub Total:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblSubTotal.grid(row=8, column=0, sticky=W)
        txtSubTotal = ttk.Entry(lblframeleft, textvariable=self.var_actualtotal, font=("arial", 13, "bold"), width=29)
        txtSubTotal.grid(row=8, column=1)

        # Total Cost
        lblTotalCost = Label(lblframeleft, text="Total Cost:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblTotalCost.grid(row=9, column=0, sticky=W)
        txtTotalCost = ttk.Entry(lblframeleft, textvariable=self.var_total, font=("arial", 13, "bold"), width=29)
        txtTotalCost.grid(row=9, column=1)

        # Bill Button
        btnBill = Button(lblframeleft, text="Bill", command=self.total, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)

        # Button Frame
        btn_frame = Frame(lblframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.mDelete, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # Right Image
        img3 = Image.open(r"D:\Hotel Management System\assets - Copy\room.jpg")
        img3 = img3.resize((520, 220), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg.place(x=760, y=55, width=520, height=220)

        # Table Frame for Search System
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", font=("arial", 12, "bold"), padx=2, pady=6)
        Table_Frame.place(x=435, y=280, width=860, height=260)

        lblSearchBy = Label(Table_Frame, font=("arial", 12, "bold"), text="Search by:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_Search["values"] = ("Contact", "Room")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, font=("arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search", command=self.search, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All", command=self.fetch_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        # Show Data Table
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)
        self.room_table = ttk.Treeview(details_table, column=("contact", "checkin", "checkout", "roomtype", "roomavailable", "meal", "noOfdays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Check-in")
        self.room_table.heading("checkout", text="Check-out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noOfdays", text="NoOfdays")

        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noOfdays", width=100)
        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="deeChu@2004", database="hotel_db")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_contact.get(),
                    
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noOfdays.get()
                ))
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Room Booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="deeChu@2004", database="hotel_db")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noOfdays.set(row[6])

    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="deeChu@2004", database="hotel_db")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set contact=%s, check_in=%s, check_out=%s, roomtype=%s, meal=%s, noOfdays=%s where Room=%s", (
                self.var_contact.get(),
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_meal.get(),
                self.var_noOfdays.get(),
                self.var_roomavailable.get(),
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Room details updated successfully", parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this room details?", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="deeChu@2004", database="hotel_db")
            my_cursor = conn.cursor()
            query = "delete from room where Room=%s"
            value = (self.var_roomavailable.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            conn.close()

    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noOfdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

    def Fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please Enter Contact number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="deeChu@2004", database="hotel_db")
            my_cursor = conn.cursor()
            query = ("select Name from customer where Mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "This is Not Found", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataframe.place(x=455, y=55, width=300, height=180)

                lblName = Label(showDataframe, text="Name:", font=("arial", 12, "bold"))
                lblName.place(x=0, y=0)

                lbl = Label(showDataframe, text=row[0], font=("arial", 12, "bold"))
                lbl.place(x=90, y=0)

                # Fetch additional customer details
                self.fetch_customer_details(showDataframe)

    def fetch_customer_details(self, showDataframe):
        details = ["Gender", "Email", "Nationality", "Address"]
        for index, detail in enumerate(details):
            conn = mysql.connector.connect(host="localhost", username="root", password="deeChu@2004", database="hotel_db")
            my_cursor = conn.cursor()
            query = f"select {detail} from customer where Mobile=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lblDetail = Label(showDataframe, text=f"{detail}:", font=("arial", 12, "bold"))
            lblDetail.place(x=0, y=30 + index * 30)

            lblValue = Label(showDataframe, text=row[0] if row else "N/A", font=("arial", 12, "bold"))
            lblValue.place(x=90, y=30 + index * 30)

            conn.close()

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="deeChu@2004", database="hotel_db")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from room where " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        self.var_noOfdays.set(abs(outDate - inDate).days)

        # Calculate total based on meal and room type
        meal_cost = {"Breakfast": 300, "Lunch": 500}
        room_cost = {"Luxury": 700, "Single": 700, "Duplex": 1000}

        if self.var_meal.get() in meal_cost and self.var_roomtype.get() in room_cost:
            q1 = meal_cost[self.var_meal.get()]
            q2 = room_cost[self.var_roomtype.get()]
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs." + str("%.2f" % (q5 * 0.1))
            ST = "Rs." + str("%.2f" % (q5))
            TT = "Rs." + str("%.2f" % (q5 + (q5 * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

    # Method to fetch available room types
    def fetch_room_types(self):
        try:
            conn = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
)
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT DISTINCT RoomType FROM details")  # Fetch distinct RoomType values
            room_types = my_cursor.fetchall()
            self.combo_RoomType['values'] = [room[0] for room in room_types]
            conn.close()
        except Exception as es:
           messagebox.showerror("Error", f"Error fetching room types: {str(es)}", parent=self.root)

#


if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()