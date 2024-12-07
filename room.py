from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        lbl_title = Label(self.root, text="Room Booking Details",font=("times new roman",40,"bold"), bg="black", fg="lightblue",bd=4,relief=RIDGE)
        lbl_title.place(x=100, y=140, width=1295, height=50)

        
        img2 = Image.open(r"C:\Users\deeks\OneDrive\Pictures\Saved Pictures\WhatsApp Image 2024-11-28 at 12.11.18 PM (1).jpeg")
        img2 = img2.resize((230, 140), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        lblframeleft = LabelFrame(self.root,bd=2,relief=RIDGE, text="Room booking Details",font=("arial",12,"bold"),padx=2 )
        lblframeleft.place(x=0, y=220, width=425, height=490)

        lbl_cust_contact= Label(lblframeleft, text="Customer Contact",font=("arial",12,"bold"), padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        enty_contact= ttk.Entry(lblframeleft,font=("arial",13,"bold"), width=20)
        enty_contact.grid(row=0,column=1,sticky=W)

        #fetch data
        btnFetchData=Button(lblframeleft,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=345,y=4)


        #check in Date
        check_in_date= Label(lblframeleft, text="Check in date",font=("arial",12,"bold"), padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date= ttk.Entry(lblframeleft,font=("arial",13,"bold"), width=29)
        txtcheck_in_date.grid(row=1,column=1)

        #check out Date
        lbl_Check_out_date= Label(lblframeleft, text="Check out date",font=("arial",12,"bold"), padx=2,pady=6)
        lbl_Check_out_date.grid(row=2,column=0,sticky=W)
        txt_Check_in_date= ttk.Entry(lblframeleft,font=("arial",13,"bold"), width=29)
        txt_Check_in_date.grid(row=2,column=1)

        #Room type
       # Room type
        label_RoomType = Label(lblframeleft, text="Room Type:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)

        combo_RoomType = ttk.Combobox(lblframeleft, font=("arial", 13, "bold"), width=27, state="readonly")
        combo_RoomType["values"] = ("Single", "Double", "Luxury")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        
        #Available room
        lblRoomAvailable= Label(lblframeleft, text="Available room:",font=("arial",12,"bold"), padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        txtRoomAvailable= ttk.Entry(lblframeleft,font=("arial",13,"bold"), width=29)
        txtRoomAvailable.grid(row=4,column=1)

        #Meal
        lblMeal= Label(lblframeleft, text="Meal:",font=("arial",12,"bold"), padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal= ttk.Entry(lblframeleft,font=("arial",13,"bold"), width=29)
        txtMeal.grid(row=5,column=1)

        #No of days
        lblNoOfDays= Label(lblframeleft, text="No of Days:",font=("arial",12,"bold"), padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays= ttk.Entry(lblframeleft,font=("arial",13,"bold"), width=29)
        txtNoOfDays.grid(row=6,column=1)

        #Paid tax
        lblNoOfDays= Label(lblframeleft, text="Paid Tax:",font=("arial",12,"bold"), padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        txtNoOfDays= ttk.Entry(lblframeleft,font=("arial",13,"bold"), width=29)
        txtNoOfDays.grid(row=7,column=1)

        #Sub total
        lblNoOfDays= Label(lblframeleft, text="Sub total:",font=("arial",12,"bold"), padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)
        txtNoOfDays= ttk.Entry(lblframeleft,font=("arial",13,"bold"), width=29)
        txtNoOfDays.grid(row=8,column=1)

        # Total cost
        lblIdNumber= Label(lblframeleft, text="Total Cost:",font=("arial",12,"bold"), padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber= ttk.Entry(lblframeleft,font=("arial",13,"bold"), width=29)
        txtIdNumber.grid(row=9,column=1)

        #Bill button
        btnBill=Button(lblframeleft,text="Bill",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)


        #button
        btn_frame=Frame(lblframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Upadate",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        # tabel frame search system
        










if __name__ == "__main__":
    root = Tk()
    obj=Roombooking(root)
    root.mainloop()
