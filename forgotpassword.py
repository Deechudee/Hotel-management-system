import subprocess
from tkinter import Tk, Frame, Label, Button, ttk, messagebox
from PIL import Image, ImageTk, ImageFilter
import database  # Import the database functions

class ForgotPassword:
    def __init__(self, root):
        self.root = root
        self.root.title("Forgot Password")
        self.root.geometry("1600x900+0+0")

        # Open and blur the background image
        original_image = Image.open(r"C:\Users\deeks\OneDrive\Pictures\Saved Pictures\architecture-building-chairs-2034335.jpg")
        blurred_image = original_image.filter(ImageFilter.GaussianBlur(2))

        self.bg = ImageTk.PhotoImage(blurred_image)
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="white")
        frame.place(x=500, y=100, width=500, height=400)

        forgot_lbl = Label(frame, text="Forgot Password", font=("times new roman", 20, "bold"), bg="lightblue", fg="white")
        forgot_lbl.place(x=20, y=20)

        # Email
        email_lbl = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email_lbl.place(x=50, y=105)

        self.txt_email = ttk.Entry(frame, font=("times new roman", 15))
        self.txt_email.place(x=50, y=130, width=250)

        # New Password
        pswd_lbl = Label(frame, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd_lbl.place(x=50, y=185)

        self.txt_pswd = ttk.Entry(frame, font=("times new roman", 15), show="*")
        self.txt_pswd.place(x=50, y=210, width=250)

        # Confirm New Password
        confirm_pswd_lbl = Label(frame, text="Confirm New Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd_lbl.place(x=50, y=265)

        self.txt_confirm_pswd = ttk.Entry(frame, font=("times new roman", 15), show="*")
        self.txt_confirm_pswd.place(x=50, y=290, width=250)

        # Reset Password Button
        reset_btn = Button(frame, text="Reset Password", font=("times new roman", 15, "bold"), bg="green", fg="white", cursor="hand2", command=self.reset_password)
        reset_btn.place(x=150, y=350, width=200)

    def reset_password(self):
        # Get the email and new password
        email = self.txt_email.get()
        new_password = self.txt_pswd.get()
        confirm_password = self.txt_confirm_pswd.get()

        # Check if the email is valid and passwords match (for demonstration, email validation is just a simple check)
        if not email or not new_password or not confirm_password:
            messagebox.showerror("Error", "All fields are required!")
            return

        if new_password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        # Check if the email exists in the database using the database functions
        user = database.check_email_exists(email)

        if user:
            # Email exists, update the password using the database function
            database.update_password(email, new_password)

            messagebox.showinfo("Success", "Password successfully reset!")
            self.root.destroy()

            # Navigate to login page after reset
            subprocess.run(["python", "login.py"])  # Adjust the path to your login.py script

        else:
            messagebox.showerror("Error", "Email not found!")

if __name__ == "__main__":
    root = Tk()
    app = ForgotPassword(root)
    root.mainloop()
