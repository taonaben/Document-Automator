# Custom Letter and Email Sender

This project is designed to automate the process of generating custom documents for companies stored in a CSV file and sending them via email. Each email will include the custom-generated letter and an additional attachment.

## Features

- Reads company information from a CSV file.
- Generates personalized letters using a DOCX template.
- Sends emails with the personalized letter and an additional attachment.
- Uses SMTP with SSL for secure email sending.

## Requirements

- Python 3.x
- `pandas` library
- `python-docx` library
- `smtplib` and `ssl` libraries (part of the Python Standard Library)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/custom-letter-email-sender.git
    cd custom-letter-email-sender
    ```

2. Install the required Python packages:
    ```sh
    pip install pandas python-docx
    ```

## Configuration

1. **CSV File**: Run the company.py to create a CSV file named `companies.csv` with the following structure and input company name and email in the following format:
    ```csv
    Company name,Email
    Company A,companyA@example.com
    Company B,companyB@example.com
    ```

2. **DOCX Template**: Create a DOCX file named `Cover Letter.docx` in the `letters` directory. Use placeholders like `[Company Name]` in the document where you want the company name to be inserted.

3. **Email Details**: Create a Python file named `email_details.py` in the project directory containing your email password, subject, body, and attachments:
   
## Usage

1. Place your CSV file at `C:\Users\taonb\PycharmProjects\Application letter Generator\venv\companies.csv`.
2. Place your DOCX template at `../letters/Cover Letter.docx`.
3. Run the script:
    ```sh
    python main.py
    ```
