from tkinter import Checkbutton, IntVar, StringVar, Tk, Frame, Label, Button, messagebox, ttk
from PIL import Image, ImageTk, ImageFilter
import mysql.connector
import os





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
        blurred_image = original_image.filter(ImageFilter.GaussianBlur(2))

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

        img1=Image.open(r"C:\Hotel Management System\assets\Login3.png")
        img1= img1.resize((100,45), Image.LANCZOS)
        self.photoimge1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimge1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=150,y=600,width=200)

        #### function declaration
    def register_data(self):
            if self.var_username.get()=="" or self.var_email.get()=="":
                 messagebox.showerror("Error","All fields are required")
            elif self.var_pass.get()!=self.var_confpass.get(): 
                 messagebox.showerror("Error","Password and Confirm Password must be same")
            elif self.var_check.get()==0: 
                 messagebox.showerror("Error","Please agree our terms and condition")
            else:
                conn = mysql.connector.connect(
                    host=os.getenv("DB_HOST"),
                    user=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASSWORD"),
                    database=os.getenv("DB_NAME")
)
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
    root = Tk()
    app = Register(root)
    root.mainloop()
