import smtplib
import ssl
from email.message import EmailMessage
from email_details import password, email_address, email_address1

# Define email sender and receiver
email_sender = email_address
email_password = password
email_receiver = email_address1

# Set the subject and body of the email
subject = 'My subject'
body = """
Email body
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
