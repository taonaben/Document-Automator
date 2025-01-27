from docx import Document
import pandas as pd
import smtplib
import ssl
from email.message import EmailMessage
from email_details import password, email_address, email_body, email_subject, attachment
import os

def fill_letter(letter_path, output_path, data):
    doc = Document(letter_path)

    for paragraph in doc.paragraphs:
        for key, value in data.items():
            if key in paragraph.text:
                paragraph.text = paragraph.text.replace(key, value)
                for run in paragraph.runs:
                    run.text = run.text.replace(key, value)

    doc.save(output_path)

def send_email_with_attachment(email_sender, email_password, email_receiver, subject, body, attachment_paths):
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    for attachment_path in attachment_paths:
        with open(attachment_path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(attachment_path)
        em.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

def generate_letter_and_send_emails(csv_path, letter_path, email_sender, email_password):
    df = pd.read_csv(csv_path)
    for idx, row in df.iterrows():
        company_name = row['Company name']
        email_receiver = row['Email address']

        data = {
            '[Company Name]': company_name,
        }

        output_path = f"Cover letter for {company_name}.docx"
        fill_letter(letter_path, output_path, data)

        subject = email_subject
        body = email_body
        attachment_paths = [output_path, attachment]

        send_email_with_attachment(email_sender, email_password, email_receiver, subject, body, attachment_paths)

        print(f'Email for {company_name} sent')
        print('------------------------------')

if __name__ == '__main__':
    csv_path = r'C:\Users\taonb\PycharmProjects\Application letter Generator\venv\companies.csv'
    letter_path = '../letters/Cover Letter.docx'
    email_sender = email_address
    email_password = password

    generate_letter_and_send_emails(csv_path, letter_path, email_sender, email_password)
    print(f'\n\nLetters sent')
