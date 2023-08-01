import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(address, title, content):
    # Your Gmail credentials (Replace with your Gmail email and password)
    gmail_email = "laozishixs@gmail.com"
    gmail_password = "nhnsqqlcuilosaig"

    # Email content
    sender = gmail_email
    receiver = address
    subject = title
    message = content

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Upgrade the connection to a secure TLS connection

        # Log in to your Gmail account
        server.login(gmail_email, gmail_password)

        # Send the email
        server.sendmail(sender, receiver, msg.as_string())

        print("Email sent successfully!")

        # Close the connection
        server.quit()
    except Exception as e:
        print("Error sending email:", e)

# Example usage:
# send_email("laozishixs@gmail.com", "Test Email", "This is a test email sent from Python!")
