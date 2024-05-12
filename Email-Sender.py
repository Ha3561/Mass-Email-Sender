import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path=None):
    # Set up the SMTP server
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(sender_email, sender_password)

    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Add body to the email
    message.attach(MIMEText(body, 'html'))

    # Add attachment if provided
    if attachment_path:
        attachment = open(attachment_path, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {attachment_path.split("/")[-1]}')
        message.attach(part)

    # Send the email
    smtp_server.send_message(message)

    # Close the SMTP server
    smtp_server.quit()

def main():
    # Input from the terminal
    sender_email = input("Enter your email: ")
    sender_password = input("Enter your email password: ")
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")
    attachment_path = input("Enter attachment file path (leave blank if none): ")

    # List of recipients
    recipients_input = input("Enter email addresses of recipients (comma-separated): ")
    recipients = [email.strip() for email in recipients_input.split(',')]

    for receiver_email in recipients:
        send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path)
        print(f"Email sent to {receiver_email}")

if __name__ == "__main__":
    main()
