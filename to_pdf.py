from fpdf import FPDF
import json 
import re 

def write_pdf():
    # get the general data
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    pdf = FPDF()
    pdf.add_page()

    # adding the title
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(40, 10, data['title'], ln=1, align='l')

    # adding the author
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, data['author'], ln=2, align='l')

    # adding the date 
    pdf.set_font('Arial', 'I', 16)
    pdf.cell(40, 10, data['date_update'], ln=3, align='l')

    # adding the content

    paragraph = data['content']
    paragraph_list = paragraph.split()

    paragraph = re.sub('\u2014', '', paragraph)
    paragraph = re.sub('\.', '\n', paragraph)
    pdf.write(5, paragraph)
    pdf.output('client-part/result.pdf', 'F')
    return "The PDF file was created"

write_pdf()
