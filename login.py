from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter
from tkinter import messagebox
from forgotpassword import ForgotPassword
from signup import Register
import mysql.connector
import time
import datetime
from hotel import HotelManagementSystem
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1650x800+0+0")



        # Open and blur the background image
        original_image = Image.open(r"C:\Hotel Management System\assets\login.jpg")
        blurred_image = original_image.filter(ImageFilter.GaussianBlur(2))

        self.bg = ImageTk.PhotoImage(blurred_image)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open(r"C:\Hotel Management System\assets\user.jpg")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(self.root, image=self.photoimg1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Login", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=135, y=100)

        username = Label(frame, text="Username", font=("times new roman", 20, "bold"), fg="white", bg="black")
        username.place(x=65, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=200, width=270)

        password = Label(frame, text="Password", font=("times new roman", 20, "bold"), fg="white", bg="black")
        password.place(x=65, y=230)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=270, width=270)

        img2=Image.open(r"C:\Hotel Management System\assets\R.png")
        img2= img2.resize((25, 25), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimg2, bg="black",borderwidth=0)
        lblimg2.place(x=650,y=333,width=25,height=25)

        img3=Image.open(r"C:\Hotel Management System\assets\img-2.png")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg3 = Label(self.root, image=self.photoimg3, bg="black",borderwidth=0)
        lblimg3.place(x=650,y=406,width=25,height=25)

        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=330,width=120,height=35)

        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=370,width=160)

        

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return

        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
)

        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM register WHERE username=%s AND password=%s", (
                               self.txtuser.get(),
                               self.txtpass.get()
         ))
        row = my_cursor.fetchone()

        if row is None:
            messagebox.showerror("Error", "Invalid Username & Password")
        else:
            # If login is successful, open the hotel management system directly
            messagebox.showinfo("Success", "Admin Login")
            self.new_window = Toplevel(self.root)  # Use `self.root` as the main parent window
            self.app = HotelManagementSystem(self.new_window)

        conn.commit()
        conn.close()
        

        







class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        ## variables
        self.var_username=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        

        

        # Open and blur the background image
        original_image = Image.open(r"C:\Hotel Management System\assets\login.jpg")
        blurred_image = original_image.filter(ImageFilter.GaussianBlur(3))

        self.bg = ImageTk.PhotoImage(blurred_image)
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="white")
        frame.place(x=500, y=100, width=500, height=650)

        register_lbl = Label(frame, text="Registration", font=("times new roman", 20, "bold"), bg="lightblue", fg="white")
        register_lbl.place(x=150, y=20)

        # Username
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="white",fg="black")
        username.place(x=110, y=105)

        self.username_entry = ttk.Entry(frame, textvariable=self.var_username,font=("times new roman", 15, "bold"))
        self.username_entry.place(x=110, y=130, width=250)

        ## Contact
        contact = Label(frame, text="Contact no", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=110, y=185)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact,font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=110, y=210, width=250)

        # Email
        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=110, y=265)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=110, y=290, width=250)

        # Password
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=110, y=345)

        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15), show="*")
        self.txt_pswd.place(x=110, y=370, width=250)

        # Confirm Password
        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=110, y=425)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15), show="*")
        self.txt_confirm_pswd.place(x=110, y=450, width=250)
        
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms and Conditions",font=("times new roman", 12, "bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=110,y=500)
  ####### Buttons
        img=Image.open(r"C:\Hotel Management System\assets\register.jpg")
        img = img.resize((100,40), Image.LANCZOS)
        self.photoimge=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimge,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=150,y=550,width=200)

        #### function declaration
    def register_data(self):
            if self.var_username.get()=="" or self.var_email.get()=="":
                 messagebox.showerror("Error","All fields are required")
            elif self.var_pass.get()!=self.var_confpass.get(): 
                 messagebox.showerror("Error","Password and Confirm Password must be same")
            elif self.var_check.get()==0: 
                 messagebox.showerror("Error","Please agree our terms and condition")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="deeChu@2004",database="hotel_db")
                my_cursor=conn.cursor()
                query=("select *from register where email=%s")
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row!=None:
                     messagebox.showerror("Error","User already exist, please try another email")
                else:
                     my_cursor.execute("insert into register values(%s,%s,%s,%s)",(
                                                                                   self.var_username.get(),
                                                                                   self.var_contact.get(),
                                                                                   self.var_email.get(),
                                                                                   self.var_pass.get()
                                                                                  ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully")
            
    

                    

        
       

if __name__ == "__main__":
   main()