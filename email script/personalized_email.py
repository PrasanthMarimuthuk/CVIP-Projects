import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

def send_email(sender_email, sender_password, recipient_email, subject, body):
    # Set up the SMTP server
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(sender_email, sender_password)

    # Create message container - the correct MIME type is multipart/alternative
    msg = MIMEMultipart('alternative')
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the body of the email
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    smtp_server.sendmail(sender_email, recipient_email, msg.as_string())

    # Close SMTP connection
    smtp_server.quit()

def main():
    # Email credentials
    sender_email = 'prasanth.m.1107@gmail.com'
    sender_password = 'sheu fwgv vffo zbwm'

    # Load recipient data from CSV
    with open('recipients.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipient_email = row['Email']
            recipient_name = row['Name']
            # Customize email body for each recipient
            subject = f'Hello, {recipient_name}!'
            body = f'Dear {recipient_name},\n\nThis is a personalized email just for you.It is a email script created using smtplib and email extension using python.\n\nBest regards,\n Prasanth M'
            
            # Send the email
            send_email(sender_email, sender_password, recipient_email, subject, body)
            print(f"Email sent to {recipient_email}")

if __name__ == "__main__":
    main()
