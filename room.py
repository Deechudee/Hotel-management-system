from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

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

        img2 = Image.open(r"C:\Hotel Management System\assets\hotel2.jpg")
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
        combo_RoomType.bind("<<ComboboxSelected>>", self.fetch_available_rooms)  # Bind the event

        # Available Room
        # Available Room
        lblRoomAvailable = Label(lblframeleft, text="Available room:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        self.combo_RNo = ttk.Combobox(lblframeleft, textvariable=self.var_roomavailable, font=("arial", 13, "bold"), width=27, state="readonly")
        self.combo_RNo.grid(row=4, column=1)

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
        img3 = Image.open(r"C:\Hotel Management System\assets\room.jpg")
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
        details_table.place(x=0, y=50, width=860, height=200)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table, columns=("Contact", "Checkin", "Checkout", "RoomType", "RoomNo", "Meal", "NoOfDays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Contact", text="Contact")
        self.room_table.heading("Checkin", text="Check-in")
        self.room_table.heading("Checkout", text="Check-out")
        self.room_table.heading("RoomType", text="Room Type")
        self.room_table.heading("RoomNo", text="Room No")
        self.room_table.heading("Meal", text="Meal")
        self.room_table.heading("NoOfDays", text="No Of Days")

        self.room_table["show"] = "headings"

        self.room_table.column("Contact", width=100)
        self.room_table.column("Checkin", width=100)
        self.room_table.column("Checkout", width=100)
        self.room_table.column("RoomType", width=100)
        self.room_table.column("RoomNo", width=100)
        self.room_table.column("Meal", width=100)
        self.room_table.column("NoOfDays", width=100)

        self.room_table.pack(fill=BOTH, expand=1)

        self.fetch_data()

    def fetch_available_rooms(self, event):
        conn = mysql.connector.connect(host="localhost", username="root", password="deeChu@2004", database="hotel_db")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details where RoomType=%s", (self.var_roomtype.get(),))
        rows = my_cursor.fetchall()
        if len(rows) > 0:
            self.combo_RNo['values'] = [item[0] for item in rows]
            self.combo_RNo.current(0)
        else:
            self.combo_RNo['values'] = None
        conn.close()

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

    def add_data(self):
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
        self.fetch_data()
        conn.close()

    def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="deeChu@2004", database="hotel_db")
        my_cursor = conn.cursor()
        my_cursor.execute("update room set Checkin=%s, Checkout=%s, RoomType=%s, RoomNo=%s, Meal=%s, NoOfDays=%s where Contact=%s", (
            self.var_checkin.get(),
            self.var_checkout.get(),
            self.var_roomtype.get(),
            self.var_roomavailable.get(),
            self.var_meal.get(),
            self.var_noOfdays.get(),
            self.var_contact.get()
        ))
        conn.commit()
        self.fetch_data()
        conn.close()

    def mDelete(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="deeChu@2004", database="hotel_db")
        my_cursor = conn.cursor()
        query = "delete from room where Contact=%s"
        value = (self.var_contact.get(),)
        my_cursor.execute(query, value)
        conn.commit()
        conn.close()
        self.fetch_data()
        self.reset()

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
            messagebox.showerror("Error", "Please enter contact number")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="deeChu@2004", database="hotel_db")
            my_cursor = conn.cursor()
            query = ("select Name from customer where Mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "This number Not Found")
            else:
                conn.commit()
                conn.close()

                showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataframe.place(x=450, y=55, width=300, height=180)

                lblName = Label(showDataframe, text="Name:", font=("arial", 12, "bold"))
                lblName.place(x=0, y=0)

                lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=0)

                conn = mysql.connector.connect(host="localhost", username="root", password="deeChu@2004", database="hotel_db")
                my_cursor = conn.cursor()
                query = ("select Gender from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row1 = my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Gender:", font=("arial", 12, "bold"))
                lblGender.place(x=0, y=30)

                lbl2 = Label(showDataframe, text=row1, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=30)

                conn = mysql.connector.connect(host="localhost", username="root", password="deeChu@2004", database="hotel_db")
                my_cursor = conn.cursor()
                query = ("select Email from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row2 = my_cursor.fetchone()

                lblEmail = Label(showDataframe, text="Email:", font=("arial", 12, "bold"))
                lblEmail.place(x=0, y=60)

                lbl3 = Label(showDataframe, text=row2, font=("arial", 12, "bold"))
                lbl3.place(x=90, y=60)

                
                conn = mysql.connector.connect(host="localhost", username="root", password="deeChu@2004", database="hotel_db")
                my_cursor = conn.cursor()
                query = ("select Nationality from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row3 = my_cursor.fetchone()

                lblNationality = Label(showDataframe, text="Nationality:", font=("arial", 12, "bold"))
                lblNationality.place(x=0, y=90)

                lbl4 = Label(showDataframe, text=row3, font=("arial", 12, "bold"))
                lbl4.place(x=90, y=90)

                conn = mysql.connector.connect(host="localhost", username="root", password="deeChu@2004", database="hotel_db")
                my_cursor = conn.cursor()
                query = ("select Address from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row4 = my_cursor.fetchone()

                lblAddress = Label(showDataframe, text="Address:", font=("arial", 12, "bold"))
                lblAddress.place(x=0, y=120)

                lbl5 = Label(showDataframe, text=row4, font=("arial", 12, "bold"))
                lbl5.place(x=90, y=120)

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
        meal_cost = {"Breakfast": 100, "Lunch": 300, "Dinner": 350}
        room_cost = {"Luxury": 2000, "Single": 500, "Duplex": 1000}

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

if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()