from fpdf import FPDF
import json 
import re 

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
r = data['content']
r  = re.sub('\u2014', '', r)
# l = re.sub('\.', '\n', r)

pdf.set_font('Arial', "", 12)
pdf.cell(400, 10, r, ln=4, align='l')

pdf.output('client-part/test.pdf', 'F')
