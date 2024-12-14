import random
from tkinter import BOTH, BOTTOM, END, HORIZONTAL, RIDGE, RIGHT, VERTICAL, W, X, Y, Button, Entry, Frame, StringVar, Tk, Label
from tkinter import ttk
from tkinter.ttk import LabelFrame, Style
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

class CustomerWin:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        self.var_ref=StringVar()
        x=random.randint(1000,10000)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_cust_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        

        # Title Label
        lbl_title = Label(
            self.root,
            text="ADD CUSTOMER DETAILS",
            font=("times new roman", 18, "bold"),
            bg="black",
            fg="gold"
        )
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Image
        img2 = Image.open(r"C:\Hotel Management System\assets\hotel2.jpg")  # Replace with your path
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief="ridge")
        lblimg.place(x=5, y=2, width=100, height=40)

        # Create a Style for LabelFrame
        style = Style()
        style.configure(
            "Custom.TLabelframe.Label",
            font=("times new roman", 12, "bold"),
            foreground="black"
        )

        # LabelFrame for Customer Details
        labelFrameLeft = LabelFrame(
            self.root,
            relief="ridge",
            text="Customer Details",
            style="Custom.TLabelframe"
        )
        labelFrameLeft.place(x=5, y=50, width=425, height=490)

        # ==== Labels and Entry ====
        lbl_cust_ref = Label(labelFrameLeft, text="Customer Ref", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        entry_ref = Entry(labelFrameLeft,textvariable=self.var_ref,state="readonly" ,width=29, font=("times new roman", 13, "bold"))
        entry_ref.grid(row=0, column=1, padx=10)

        cname = Label(labelFrameLeft, font=("arial", 12, "bold"), text="Customer Name:", padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        textcname = ttk.Entry(labelFrameLeft,textvariable=self.var_cust_name, font=("arial", 13, "bold"), width=29)
        textcname.grid(row=1, column=1)

        lblmname = Label(labelFrameLeft, font=("arial", 12, "bold"), text="Mother Name:", padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)
        txtmname = ttk.Entry(labelFrameLeft,textvariable=self.var_cust_mother, font=("arial", 13, "bold"), width=29)
        txtmname.grid(row=2, column=1)

        label_gender = Label(labelFrameLeft, font=("arial", 12, "bold"), text="Gender:", padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(labelFrameLeft,textvariable=self.var_gender, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        lblPostCode = Label(labelFrameLeft, font=("arial", 12, "bold"), text="PostCode:", padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)
        txtPostCode = ttk.Entry(labelFrameLeft, textvariable=self.var_post,font=("arial", 13, "bold"), width=29)
        txtPostCode.grid(row=4, column=1)

        lblMobile = Label(labelFrameLeft, font=("arial", 12, "bold"), text="Mobile:", padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)
        txtMobile = ttk.Entry(labelFrameLeft, textvariable=self.var_mobile,font=("arial", 13, "bold"), width=29)
        txtMobile.grid(row=5, column=1)

        lblEmail = Label(labelFrameLeft, font=("arial", 12, "bold"), text="Email:", padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)
        txtEmail = ttk.Entry(labelFrameLeft,textvariable=self.var_email, font=("arial", 13, "bold"), width=29)
        txtEmail.grid(row=6, column=1)

        lblNationality = Label(labelFrameLeft, font=("arial", 12, "bold"), text="Nationality:", padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)

        combo_Nationality = ttk.Combobox(labelFrameLeft,textvariable=self.var_nationality, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_Nationality["value"] = ("British", "American", "Indian")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7, column=1)

        lblIdProof = Label(labelFrameLeft, font=("arial", 12, "bold"), text="Id Proof Type:", padx=2, pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)

        combo_id = ttk.Combobox(labelFrameLeft,textvariable=self.var_id_proof, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_id["value"] = ("AdharCard", "VoterID", "DrivingLicense")
        combo_id.current(0)
        combo_id.grid(row=8, column=1)

        lblIdNumber = Label(labelFrameLeft, font=("arial", 12, "bold"), text="Id Number:", padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        txtIdNumber = ttk.Entry(labelFrameLeft, textvariable=self.var_id_number,font=("arial", 13, "bold"), width=29)
        txtIdNumber.grid(row=9, column=1)

        lblAddress = Label(labelFrameLeft, font=("arial", 12, "bold"), text="Address:", padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)
        txtAddress = ttk.Entry(labelFrameLeft,textvariable=self.var_address, font=("arial", 13, "bold"), width=29)
        txtAddress.grid(row=10, column=1)

        # Button Frame
        btn_frame = Frame(labelFrameLeft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add",command=self.add_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=8)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame,command=self.update, text="Update", font=("arial", 12, "bold"), bg="black", fg="gold", width=8)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, command=self.mDelete,text="Delete", font=("arial", 12, "bold"), bg="black", fg="gold", width=8)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, command=self.reset,text="Reset", font=("arial", 12, "bold"), bg="black", fg="gold", width=12)
        btnReset.grid(row=0, column=3, padx=1)

        # Table Frame
        Table_Frame = LabelFrame(
            self.root,
            relief="ridge",
            text="View Details And Search System",
            style="Custom.TLabelframe"
        )
        Table_Frame.place(x=435, y=50, width=860, height=490)  # Adjusted x-coordinate for better alignment

        lblSearchBy = Label(Table_Frame, font=("arial", 12, "bold"), text="Search By:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search = ttk.Combobox(Table_Frame,textvariable=self.search_var, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("Mobile", "Ref No", "Name")  # Add more options as needed
        combo_search.current(0)  # Set default value
        combo_search.grid(row=0, column=1,padx=2)

        self.txt_search=StringVar()

        # Add a text entry field for search input
        txt_search = ttk.Entry(Table_Frame,textvariable=self.txt_search, font=("arial", 13, "bold"), width=24)
        txt_search.grid(row=0, column=2, padx=2)

        # Add a search button
        btn_search = Button(Table_Frame,command=self.search, text="Search", font=("arial", 12, "bold"), bg="black", fg="gold", width=10)
        btn_search.grid(row=0, column=3, padx=1)

        # Add a "Show All" button
        btn_Showall = Button(Table_Frame,command=self.fetch_data, text="Show All", font=("arial", 12, "bold"), bg="black", fg="gold", width=8)
        btn_Showall.grid(row=0, column=4,padx=1)

        # Create a Frame for the Table
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=359) 

        # Create Scrollbars
        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        # Create Treeview Widget
        self.Cust_Details_Table = ttk.Treeview(details_table, columns=("ref", 'name', "mother", "gender", "post", "mobile", "email", "nationality", "idproof", "idnumber", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        self.Cust_Details_Table.pack(fill="both", expand=1)

        # Configure Scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)
        self.Cust_Details_Table.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)


        # Configure Treeview Columns
        self.Cust_Details_Table["show"] = "headings" 

        self.Cust_Details_Table.heading("ref", text="Ref")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("mother", text="Mother")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("post", text="PostCode")
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("idproof", text="ID Proof")
        self.Cust_Details_Table.heading("idnumber", text="ID Number")
        self.Cust_Details_Table.heading("address", text="Address")

        # Set column widths (adjust as needed)
        self.Cust_Details_Table.column("ref", width=100)
        self.Cust_Details_Table.column("name", width=150)
        self.Cust_Details_Table.column("mother", width=150)
        self.Cust_Details_Table.column("gender", width=80)
        self.Cust_Details_Table.column("post", width=100)
        self.Cust_Details_Table.column("mobile", width=120)
        self.Cust_Details_Table.column("email", width=200)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("idproof", width=100)
        self.Cust_Details_Table.column("idnumber", width=150)
        self.Cust_Details_Table.column("address", width=200)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    
    def add_data(self):
      if self.var_mobile.get() == "" or self.var_cust_mother.get() == "":
        messagebox.showerror("Error", "All fields are required")
      else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="deeChu@2004",
                database="hotel_db"
            )
            my_cursor = conn.cursor()
            
            # Correct INSERT statement
            my_cursor.execute(
                "INSERT INTO customer (Ref,Name, Mother, Gender, PostCode, Mobile, Email, Nationality, Idproof, Idnumber, Address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    self.var_ref.get(),       # Ref (INT)
                    self.var_cust_name.get(),     # Name (VARCHAR)
                    self.var_cust_mother.get(),   # Mother (VARCHAR)
                    self.var_gender.get(),        # Gender (VARCHAR)
                    self.var_post.get(),          # PostCode (VARCHAR)
                    self.var_mobile.get(),        # Mobile (VARCHAR)
                    self.var_email.get(),         # Email (VARCHAR)
                    self.var_nationality.get(),   # Nationality (VARCHAR)
                    self.var_id_proof.get(),      # Idproof (VARCHAR)
                    self.var_id_number.get(),     # Idnumber (VARCHAR)
                    self.var_address.get()        # Address (VARCHAR)
                )
            )
            
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Customer has been added", parent=self.root)
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)


    def fetch_data(self):
                 conn=mysql.connector.connect(host="localhost",username="root",password="deeChu@2004",database="hotel_db")  # type: ignore
                 my_cursor=conn.cursor()
                 my_cursor.execute("select * from customer")
                 rows=my_cursor.fetchall()
                 if len(rows)!=0:  # type: ignore
                       self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                       for i in rows:  # type: ignore
                             self.Cust_Details_Table.insert("",END,values=i)

                       conn.commit()
                 conn.close()

    def get_cursor(self,event=""):
          cursor_row=self.Cust_Details_Table.focus()
          content=self.Cust_Details_Table.item(cursor_row) # type: ignore
          row=content["values"]

          self.var_ref.set(row[0]),
          self.var_cust_name.set(row[1]),
          self.var_cust_mother.set(row[2]),
          self.var_gender.set(row[3]),
          self.var_post.set(row[4]),
          self.var_mobile.set(row[5]),
          self.var_email.set(row[6]),
          self.var_nationality.set(row[7]),
          self.var_id_proof.set(row[8]),
          self.var_id_number.set(row[9]),
          self.var_address.set(row[10]),  
    
    def update(self):
        if self.var_cust_name.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
               conn=mysql.connector.connect(host="localhost",username="root",password="deeChu@2004",database="hotel_db")
               my_cursor=conn.cursor()
               my_cursor.execute("update customer set Name=%s, Mother=%s, Gender=%s, PostCode=%s, Mobile=%s, Email=%s, Nationality=%s, Idproof=%s, Idnumber=%s, Address=%s where Ref=%s",(
                     # Ref (INT)
                    self.var_cust_name.get(),     # Name (VARCHAR)
                    self.var_cust_mother.get(),   # Mother (VARCHAR)
                    self.var_gender.get(),        # Gender (VARCHAR)
                    self.var_post.get(),          # PostCode (VARCHAR)
                    self.var_mobile.get(),        # Mobile (VARCHAR)
                    self.var_email.get(),         # Email (VARCHAR)
                    self.var_nationality.get(),   # Nationality (VARCHAR)
                    self.var_id_proof.get(),      # Idproof (VARCHAR)
                    self.var_id_number.get(),     # Idnumber (VARCHAR)
                    self.var_address.get() ,
                    self.var_ref.get()                       )
            )
            
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("Update","New Room details has been updated  successfully",parent=self.root)


    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this room details",parent=self.root)
        if mDelete>0:
               conn=mysql.connector.connect(host="localhost",username="root",password="deeChu@2004",database="hotel_db")
               my_cursor=conn.cursor()
               query="delete from customer where Ref=%s"
               value=(self.var_ref.get(),)
               my_cursor.execute(query,value)
        else:
               if not mDelete:
                   return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
             self.var_ref.set(""),
             self.var_cust_name.set(""),
             self.var_cust_mother.set(""),
             self.var_gender.set(""),
             self.var_post.set(""),
             self.var_mobile.set(""),
             self.var_email.set(""),
             self.var_nationality.set(""),
             self.var_id_proof.set(""),
             self.var_id_number.set(""),
             self.var_address.set(""),
             
             x=random.randint(1000,9999)
             self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="deeChu@2004",database="hotel_db")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
if __name__ == "__main__":
    root = Tk()
    app = CustomerWin(root)
    root.mainloop()
