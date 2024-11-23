from tkinter import Tk, Label, Frame, Button, Checkbutton, IntVar
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")


        self.bg=ImageTk.PhotoImage(file=r"C:\Users\deeks\OneDrive\Pictures\Saved Pictures\architecture-building-chairs-2034335.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\deeks\OneDrive\Pictures\Saved Pictures\4326noregEMETE.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1 = Label(self.root, image=self.photoimg1, bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started", font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        username=lbl=Label(frame,text="Username", font=("times new roman",20,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=200,width=270)
        
        password=lbl=Label(frame,text="Password", font=("times new roman",20,"bold"),fg="white",bg="black")
        password.place(x=70,y=230)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=270,width=270)

    
        img2=Image.open(r"C:\Users\deeks\OneDrive\Pictures\Saved Pictures\R.png")
        img2= img2.resize((25, 25), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimg2, bg="black",borderwidth=0)
        lblimg2.place(x=650,y=333,width=25,height=25)

        img3=Image.open(r"C:\Users\deeks\OneDrive\Pictures\Saved Pictures\img-2.png")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg3 = Label(self.root, image=self.photoimg3, bg="black",borderwidth=0)
        lblimg3.place(x=650,y=406,width=25,height=25)

        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=330,width=120,height=35)

        registerbtn=Button(frame,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=370,width=160)

        registerbtn=Button(frame,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=400,width=160)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="deechu" and self.txtpass.get()=="2004":
            messagebox.showinfo("Success","Welcome to our Hotel")
        else:
            messagebox.showerror("Invalid","Invalid Username & Password")        

        




if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
    