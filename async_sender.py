import asyncio
import csv
from email.message import EmailMessage
import aiosmtplib
from tqdm import tqdm

TEMP_PASS = "mvmc pjju gdqp pzzc"

async def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path=None):
    # Create the email message
    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.set_content(body)

    # Add attachment if provided
    if attachment_path:
        with open(attachment_path, 'rb') as attachment:
            message.add_attachment(attachment.read(), maintype='application', subtype='octet-stream', filename=attachment_path.split("/")[-1])

    try:
        await aiosmtplib.send(message, hostname="smtp.gmail.com", port=587, username=sender_email, password=sender_password, starttls=True)
        print(f"Email sent to {receiver_email}")
    except Exception as e:
        print(f"Failed to send email to {receiver_email}: {e}")

async def main():
    # Email account info
    sender_email = "trijha.jhabua@gmail.com"
    sender_password = TEMP_PASS

    # Get attachment file path
    attachment_path = "Trijha_Diwali Corporate Gifting.pdf"

    # Read the email body from the body.txt file once
    try:
        with open('body.txt', 'r', encoding='utf-8') as file:
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

            tasks = []
            for row in reader:
                receiver_email = row[0]  # Email
                name = row[1]  # Name
                company = row[2]  # Company

                # Personalize the subject
                subject = f"Follow your Dreams, {name} at {company}"

                # Personalize the body
                body = email_body_template.format(name=name, company=company)

                # Create a task for sending the email
                tasks.append(send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path))

            # Display progress bar
            for task in tqdm(asyncio.as_completed(tasks), total=len(tasks)):
                await task  # Wait for all tasks to complete

    except FileNotFoundError:
        print(f"Error: The file {csv_file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
