from tkinter import Tk, Frame, Label, Button, ttk
from PIL import Image, ImageTk, ImageFilter
import subprocess


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # Open and blur the background image
        original_image = Image.open(r"C:\Users\deeks\OneDrive\Pictures\Saved Pictures\architecture-building-chairs-2034335.jpg")
        blurred_image = original_image.filter(ImageFilter.GaussianBlur(2))

        self.bg = ImageTk.PhotoImage(blurred_image)
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="white")
        frame.place(x=500, y=100, width=500, height=550)

        register_lbl = Label(frame, text="Registration", font=("times new roman", 20, "bold"), bg="lightblue", fg="white")
        register_lbl.place(x=20, y=20)

        # Username
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="white")
        username.place(x=50, y=105)

        self.username_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.username_entry.place(x=50, y=130, width=250)

        # Email
        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=50, y=185)

        self.txt_email = ttk.Entry(frame, font=("times new roman", 15))
        self.txt_email.place(x=50, y=210, width=250)

        # Password
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=265)

        self.txt_pswd = ttk.Entry(frame, font=("times new roman", 15), show="*")
        self.txt_pswd.place(x=50, y=290, width=250)

        # Confirm Password
        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=50, y=345)

        self.txt_confirm_pswd = ttk.Entry(frame, font=("times new roman", 15), show="*")
        self.txt_confirm_pswd.place(x=50, y=370, width=250)

        # Sign Up Button
        signup_btn = Button(frame, text="Sign Up", font=("times new roman", 15, "bold"), bg="green", fg="white", cursor="hand2", command=self.sign_up)
        signup_btn.place(x=150, y=450, width=200)

        # Login Redirect (Add this part)
        login_btn = Button(self.root, text="Already have an account? Login", font=("times new roman", 15, "bold"), fg="blue", bg="white", command=self.go_to_login)
        login_btn.place(x=650, y=680)

    def sign_up(self):
        # For now, you can validate fields and save data here (e.g., to a database).
        # After signing up, redirect to the login page.
        self.root.destroy()  # Close current window
        subprocess.run(["python", "login.py"])  # Open login.py

    def go_to_login(self):
        self.root.destroy()
        subprocess.run(["python", "login.py"])  # Open login.py


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
