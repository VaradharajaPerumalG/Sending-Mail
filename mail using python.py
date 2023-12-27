import smtplib
import ssl

from_email = input('Enter your email:')
app_password = input('Enter your app password:')

port = 465
context = ssl.create_default_context()
to_email = input('Enter to email:')
subject = input("Enter subject:")
body = input("Enter body:")
message = f"""\
Subject: {subject}

{body}"""


with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
    server.login(from_email, app_password)
    print("Connection establised successfully...")
    server.sendmail(from_email, to_email, message)
    print("Your email is successfully sent...")
