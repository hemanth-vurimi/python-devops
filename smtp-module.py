import smtplib
from email.message import EmailMessage
import psutil

def send_email():
    SMTP_SERVER = "smtp.gmail.com"
    PORT = 587

    sender = "hemanth3560@gmail.com"
    receiver = "hemanthvurimi60@gmail.com"
    password = "wtbw tpjm ikws bwbr"   # Gmail app password

    msg = EmailMessage()
    msg["Subject"] = "DevOps Alert: Test Email"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("This is a memory usage alert from Python DevOps script")

    server = smtplib.SMTP(SMTP_SERVER, PORT)
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)
    server.quit()

    print("Email sent successfully")

memory_usage = psutil.virtual_memory().percent
if memory_usage > 80:
    print(f"Warning: Memory usage is at {memory_usage}%")
    send_email()

