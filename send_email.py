import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "conacheantonio13@gmail.com"
    password = os.getenv("EMAIL_PASSWORD")

    receiver = "conacheantonio13@gmail.com"
    myContext = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=myContext) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
