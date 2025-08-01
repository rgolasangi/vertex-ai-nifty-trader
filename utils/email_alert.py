import smtplib
from email.mime.text import MIMEText

def send_email_report(subject, body, to_email):
    print(f"Sending email to {to_email} with subject '{subject}'")
