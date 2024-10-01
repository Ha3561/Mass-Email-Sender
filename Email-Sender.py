import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv
from tqdm import tqdm

TEMP_PASS = "mvmc pjju gdqp pzzc"

def send_email(smtp_server, sender_email, receiver_email, subject, body, attachment_path=None):
    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Add body to the email (plain text)
    message.attach(MIMEText(body, 'plain'))

    # Add attachment if provided
    if attachment_path:
        with open(attachment_path, 'rb') as attachment:
            print("Reading attachment...")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={attachment_path.split("/")[-1]}')
            print("Attaching file...")
            message.attach(part)

    # Send the email
    try:
        print(f"Sending email to {receiver_email}...")
        smtp_server.send_message(message)
        print(f"Email sent to {receiver_email}")
    except Exception as e:
        print(f"Failed to send email to {receiver_email}: {e}")

def main():
    # Email account info
    sender_email = "trijha.jhabua@gmail.com"
    sender_password = TEMP_PASS 

    # Get attachment file path
    attachment_path = "Trijha_Diwali Corporate Gifting.pdf"

    # Read the email body from the body.txt file once
    try:
        with open('body.txt', 'r', encoding='utf-8') as file:
            print("Reading the body...")
            email_body_template = file.read()
    except FileNotFoundError:
        print("Error: The file 'body.txt' was not found.")
        return

    # Read recipients from CSV
    csv_file_path = "senders_list.csv"

    try:
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header

            # Set up the SMTP server once
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp_server:
                smtp_server.starttls()
                smtp_server.login(sender_email, sender_password)

                # Use tqdm for progress tracking
                for row in tqdm(reader, desc="Sending Emails"):
                    receiver_email = row[0]  # Assumes email is the first column
                    name = row[1]  # Name is the second column
                    company = row[2]  # Company is the third column

                    # Personalize the subject
                    subject = f"Follow your Dreams, {name} at {company}"

                    # Personalize the body using the stored template
                    body = email_body_template.format(name=name, company=company)

                    # Send the personalized email
                    send_email(smtp_server, sender_email, receiver_email, subject, body, attachment_path)

    except FileNotFoundError:
        print(f"Error: The file {csv_file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
