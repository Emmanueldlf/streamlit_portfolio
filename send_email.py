from dotenv import load_dotenv
import os
import smtplib, ssl

def send_email(message):

    load_dotenv()

    username = os.environ.get("gmail_username")
    password = os.environ.get("gmail_password")

    host = "smtp.gmail.com"
    port = 465

    receiver = "emmanuel.delaforestdivonne@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
