from tkinter import Tk, Label, Frame, Button, ttk
from PIL import Image, ImageTk, ImageFilter
from tkinter import messagebox


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1650x800+0+0")

        # Open and blur the background image
        original_image = Image.open(r"C:\Users\deeks\OneDrive\Pictures\Saved Pictures\WhatsApp Image 2024-11-28 at 12.11.18 PM.jpeg")
        blurred_image = original_image.filter(ImageFilter.GaussianBlur(2))  # Adjust blur radius as needed

        self.bg = ImageTk.PhotoImage(blurred_image)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open(r"C:\Users\deeks\OneDrive\Pictures\Saved Pictures\user.jpg")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(self.root, image=self.photoimg1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        username = lbl = Label(frame, text="Username", font=("times new roman", 20, "bold"), fg="white", bg="black")
        username.place(x=40, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=200, width=270)

        password = lbl = Label(frame, text="Password", font=("times new roman", 20, "bold"), fg="white", bg="black")
        password.place(x=40, y=230)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=270, width=270)

        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"),
                          bd=3, relief="ridge", fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=330, width=120, height=35)

        lbl = Label(frame, text="Don't have account?", font=("times new roman", 14, "bold"), bg="black", fg="white")
        lbl.place(x=90, y=370)

        signupbtn = Button(frame, text=" Sign Up", font=("times new roman", 10, "bold"),
                           borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black",
                           command=self.open_register)
        signupbtn.place(x=70, y=400, width=200)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "deechu" and self.txtpass.get() == "2004":
            messagebox.showinfo("Success", "Welcome to our Hotel")
        else:
            messagebox.showerror("Invalid", "Invalid Username & Password")

    def open_register(self):
        self.root.destroy()  
        root = Tk()
        app = Register(root)  
        root.mainloop()


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # Open and blur the background image
        original_image = Image.open(r"C:\Users\deeks\OneDrive\Pictures\Saved Pictures\architecture-building-chairs-2034335.jpg")
        blurred_image = original_image.filter(ImageFilter.GaussianBlur(10))

        self.bg = ImageTk.PhotoImage(blurred_image)
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="white")
        frame.place(x=20, y=100, width=500, height=550)

        register_lbl = Label(frame, text="Registration", font=("times new roman", 20, "bold"), bg="lightblue", fg="white")
        register_lbl.place(x=20, y=20)

        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="white")
        username.place(x=50, y=105)

        self.username_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.username_entry.place(x=50, y=130, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=50, y=185)

        self.txt_email = ttk.Entry(frame, font=("times new roman", 15))
        self.txt_email.place(x=50, y=210, width=250)

        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=265)

        self.txt_pswd = ttk.Entry(frame, font=("times new roman", 15), show="*")
        self.txt_pswd.place(x=50, y=290, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=50, y=345)

        self.txt_confirm_pswd = ttk.Entry(frame, font=("times new roman", 15), show="*")
        self.txt_confirm_pswd.place(x=50, y=370, width=250)


if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()