Automatic Email Sender
This Python script allows you to send emails to multiple recipients using the smtplib library. You can customize the email subject, body, and even attach files if needed.

Prerequisites
Python 3.12
Gmail account (for using Gmail SMTP server)
Installation
Clone the repository or download the script directly.
Make sure you have Python installed on your system.
Install the required libraries using pip:
bash
Copy code
pip install smtplib
Usage
Run the script:
bash
Copy code
python email_sender.py
Enter your Gmail credentials, email subject, body, and attachment path (if any) when prompted.
Enter the email addresses of recipients (comma-separated) when prompted.
Example
Sending an email with attachment to multiple recipients:

bash
Copy code
Enter your email: your_email@gmail.com
Enter your email password:
Enter email subject: Invitation to Event
Enter email body: Join us for an Exciting Event!
Enter attachment file path (leave blank if none): /path/to/attachment.pdf
Enter email addresses of recipients (comma-separated): recipient1@example.com, recipient2@example.com
Notes
Make sure to enable less secure app access in your Gmail settings if you're using a Gmail account for sending emails.
The script uses HTML format for the email body by default. You can modify the body_template variable in the script to customize the email template.
 

Feel free to customize this README according to your specific needs and preferences!
