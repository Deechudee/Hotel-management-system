import mysql.connector
from tkinter import *
from tkinter import messagebox, ttk
from tkinter import *
from PIL import Image, ImageTk


class Staff:
    def __init__(self, root):
        self.root = root
        self.root.title("Staff Management System")
        self.root.geometry("1295x550+230+220")

        # Variables
        self.var_staff_id = StringVar()
        self.var_staff_name = StringVar()
        self.var_contact = StringVar()
        self.var_position = StringVar()
        self.var_shift = StringVar()
        self.var_department = StringVar()
        self.var_salary = StringVar()
        self.var_gender = StringVar()

        # Title
        lbl_title = Label(self.root, text="Staff Management System", font=("Arial", 20, "bold"), bg="black", fg="lightblue")
        lbl_title.pack(side=TOP, fill=X)

        img2 = Image.open(r"C:\Hotel Management System\assets\hotel2.jpg")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        # Entry Frame
        frame = Frame(self.root, bd=5, relief=RIDGE, padx=10, pady=10)
        frame.place(x=7, y=50, width=425, height=495)

        lbl_staff_id = Label(frame, text="Staff ID:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_staff_id.grid(row=0, column=0, sticky=W)
        txt_staff_id = Entry(frame, textvariable=self.var_staff_id, font=("arial", 13, "bold"), width=20)
        txt_staff_id.grid(row=0, column=1, padx=10, pady=5)

        lbl_staff_name = Label(frame, text="Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_staff_name.grid(row=1, column=0, sticky=W)
        txt_staff_name = Entry(frame, textvariable=self.var_staff_name, font=("Arial", 12))
        txt_staff_name.grid(row=1, column=1, padx=10, pady=5)

        lbl_contact = Label(frame, text="Contact:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_contact.grid(row=2, column=0, sticky=W)
        txt_contact = Entry(frame, textvariable=self.var_contact, font=("Arial", 12))
        txt_contact.grid(row=2, column=1, padx=10, pady=5)

        lbl_position = Label(frame, text="Position:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_position.grid(row=3, column=0, sticky=W)
        txt_position = Entry(frame, textvariable=self.var_position, font=("Arial", 12))
        txt_position.grid(row=3, column=1, padx=10, pady=5)

        lbl_shift = Label(frame, text="Shift:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_shift.grid(row=4, column=0, sticky=W)
        txt_shift = Entry(frame, textvariable=self.var_shift, font=("Arial", 12))
        txt_shift.grid(row=4, column=1, padx=10, pady=5)

        lbl_department = Label(frame, text="Department:",font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_department.grid(row=5, column=0, sticky=W)
        txt_department = Entry(frame, textvariable=self.var_department, font=("Arial", 12))
        txt_department.grid(row=5, column=1, padx=10, pady=5)

        lbl_salary = Label(frame, text="Salary:",font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_salary.grid(row=6, column=0, sticky=W)
        txt_salary = Entry(frame, textvariable=self.var_salary, font=("Arial", 12))
        txt_salary.grid(row=6, column=1, padx=10, pady=5)

        lbl_gender = Label(frame, text="Gender:",font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_gender.grid(row=7, column=0, sticky=W)
        txt_gender = Entry(frame, textvariable=self.var_gender, font=("Arial", 12))
        txt_gender.grid(row=7, column=1, padx=10, pady=5)

        # Buttons
        btn_frame = Frame(self.root, bd=5, relief=RIDGE, padx=10, pady=10)
        btn_frame.place(x=5, y=450, width=425, height=50)

        btn_add = Button(btn_frame, text="Add", font=("Arial", 12), command=self.add_staff, bg="black", fg="gold")
        btn_add.grid(row=0, column=0, padx=10)

        btn_update = Button(btn_frame, text="Update", font=("Arial", 12), command=self.update_staff, bg="black", fg="gold")
        btn_update.grid(row=0, column=1, padx=10)

        btn_delete = Button(btn_frame, text="Delete", font=("Arial", 12), command=self.delete_staff, bg="black", fg="gold")
        btn_delete.grid(row=0, column=2, padx=10)

        btn_clear = Button(btn_frame, text="Clear", font=("Arial", 12), command=self.clear, bg="black", fg="gold")
        btn_clear.grid(row=0, column=3, padx=10)

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
        combo_Search["values"] = ("Contact", "Name")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, font=("arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search", command=self.search, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All", command=self.fetch_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)


        # Staff Table
        table_frame = Frame(self.root, bd=5, relief=RIDGE)
        table_frame.place(x=435, y=350, width=860, height=200)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.staff_table = ttk.Treeview(table_frame, columns=("id", "name", "contact", "position", "shift", "department", "salary", "gender"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.staff_table.xview)
        scroll_y.config(command=self.staff_table.yview)

        self.staff_table.heading("id", text="Staff ID")
        self.staff_table.heading("name", text="Name")
        self.staff_table.heading("contact", text="Contact")
        self.staff_table.heading("position", text="Position")
        self.staff_table.heading("shift", text="Shift")
        self.staff_table.heading("department", text="Department")
        self.staff_table.heading("salary", text="Salary")
        self.staff_table.heading("gender", text="Gender")

        self.staff_table["show"] = "headings"

        self.staff_table.pack(fill=BOTH, expand=1)
        self.staff_table.bind("<ButtonRelease-1>", self.get_cursor)

    def add_staff(self):
        if self.var_staff_id.get() == "" or self.var_staff_name.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="deeChu@2004", database="hotel_db")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO staff (id, name, contact, position, shift, department, salary, gender) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_staff_id.get(),
                    self.var_staff_name.get(),
                    self.var_contact.get(),
                    self.var_position.get(),
                    self.var_shift.get(),
                    self.var_department.get(),
                    self.var_salary.get(),
                    self.var_gender.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Staff added successfully")
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="deeChu@2004", database="hotel_db")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM staff")
            rows = my_cursor.fetchall()
            if rows:
                self.staff_table.delete(*self.staff_table.get_children())
                for row in rows:
                    self.staff_table.insert("", END, values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def get_cursor(self, event):
        cursor_row = self.staff_table.focus()
        contents = self.staff_table.item(cursor_row)
        row = contents['values']
        self.var_staff_id.set(row[0])
        self.var_staff_name.set(row[1])
        self.var_contact.set(row[2])
        self.var_position.set(row[3])
        self.var_shift.set(row[4])
        self.var_department.set(row[5])
        self.var_salary.set(row[6])
        self.var_gender.set(row[7])

    def update_staff(self):
        if self.var_staff_id.get() == "":
            messagebox.showerror("Error", "Please select a staff member to update")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="deeChu@2004", database="hotel_db")
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE staff SET name=%s, contact=%s, position=%s, shift=%s, department=%s, salary=%s, gender=%s WHERE id=%s", (
                    self.var_staff_name.get(),
                    self.var_contact.get(),
                    self.var_position.get(),
                    self.var_shift.get(),
                    self.var_department.get(),
                    self.var_salary.get(),
                    self.var_gender.get(),
                    self.var_staff_id.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Staff updated successfully")
                self.clear()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def delete_staff(self):
        if self.var_staff_id.get() == "":
            messagebox.showerror("Error", "Please select a staff member to delete")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="deeChu@2004", database="hotel_db")
                my_cursor = conn.cursor()
                my_cursor.execute("DELETE FROM staff WHERE id=%s", (self.var_staff_id.get(),))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Staff deleted successfully")
                self.clear()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def clear(self):
        self.var_staff_id.set("")
        self.var_staff_name.set("")
        self.var_contact.set("")
        self.var_position.set("")
        self.var_shift.set("")
        self.var_department.set("")
        self.var_salary.set("")
        self.var_gender.set("")

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="deeChu@2004", database="hotel_db")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from staff where " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.staff_table.delete(*self.staff_table.get_children())
            for i in rows:
                self.staff_table.insert("", END, values=i)
            conn.commit()
        conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = Staff(root)
    root.mainloop()
