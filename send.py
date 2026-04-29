import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import Tk

def send_confirmation_email(customer_email, booking_details):
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    
    # Create the email content
    subject = "Booking Confirmation"
    body = f"""
    Dear {booking_details['customer_name']},

    Thank you for booking with us! Here are your booking details:

    Room Type: {booking_details['room_type']}
    Check-in Date: {booking_details['check_in']}
    Check-out Date: {booking_details['check_out']}
    Total Price: {booking_details['total_price']}

    We look forward to welcoming you!

    Best regards,
    Hotel Management Team
    """

    # Set up the email server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = customer_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    server.send_message(msg)
    server.quit()

def book_room(self):
    # Assume you have collected booking details
    details_table = {
        'customer_name': self.txtuser.get(),
        'room_type': 'Deluxe Room',  # Example room type
        'check_in': '2023-10-01',  # Example check-in date
        'check_out': '2023-10-05',  # Example check-out date
        'total_price': '$500'  # Example total price
    }
    
    # Save booking details to the database (your existing code)
    # ...

    # Send confirmation email
    send_confirmation_email(self.txtuser.get(), details_table)

if __name__ == "__main__":
    root = Tk()
    app = send_confirmation_email(root)
    root.mainloop()
