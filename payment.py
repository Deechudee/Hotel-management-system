# payment.py

from tkinter import *
from tkinter import messagebox

class PaymentWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Payment")
        self.root.geometry("400x300")

        # Payment details
        self.amount_label = Label(self.root, text="Amount:", font=("Arial", 14))
        self.amount_label.pack(pady=10)

        self.amount_entry = Entry(self.root, font=("Arial", 14))
        self.amount_entry.pack(pady=10)

        self.card_label = Label(self.root, text="Card Number:", font=("Arial", 14))
        self.card_label.pack(pady=10)

        self.card_entry = Entry(self.root, font=("Arial", 14))
        self.card_entry.pack(pady=10)

        self.pay_button = Button(self.root, text="Pay", command=self.process_payment, font=("Arial", 14), bg="green", fg="white")
        self.pay_button.pack(pady=20)

    def process_payment(self):
        amount = self.amount_entry.get()
        card_number = self.card_entry.get()

        if not amount or not card_number:
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be greater than zero")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        # Here you would typically integrate with a payment gateway
        # For demonstration, we will just show a success message
        messagebox.showinfo("Success", f"Payment of ${amount:.2f} processed successfully!")

if __name__ == "__main__":
    root = Tk()
    app = PaymentWindow(root)
    root.mainloop()