from docx import Document
import pandas as pd



def fill_letter(letter_path, output_path, data):
    doc = Document(letter_path)

    for paragraph in doc.paragraphs:
        for key, value in data.items():
            if key in paragraph.text:
                paragraph.text = paragraph.text.replace(key, value)
                for run in paragraph.runs:
                    run.text = run.text.replace(key, value)

    doc.save(output_path)

def generate_letter_from_csv(csv_path, letter_path):
    df = pd.read_csv(csv_path)
    for idx, row in df.iterrows():
        data = {
            '[Company Name]': row['Company name'],
        }

        output_path = f"Cover letter for {row['Company name']}.docx"
        fill_letter(letter_path, output_path, data)


if __name__ == '__main__':

    csv_path = r'C:\Users\taonb\PycharmProjects\Application letter Generator\venv\companies.csv'
    letter_path = '../letters/Cover Letter.docx'
    generate_letter_from_csv(csv_path,letter_path)
    print(f'letters printed')
