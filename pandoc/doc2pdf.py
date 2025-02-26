from docx import Document
from PyPDF2 import PdfReader
from markdown import markdown
from subprocess import run as sbprcssRUN

def docx2markdown(input_file, output_file):
  doc = Document(input_file)
  paragraphs = [p.text for p in doc.paragraphs]
  markdown_text='\n'.join(paragraphs)
  with open(output_file, 'w', encoding='utf-8') as f:
    f.write(markdown_text)
  print('Conversion successful!')

def convert_pdf_to_markdown(input_file, output_file):
  with open(input_file, 'rb') as f:
    pdf_reader = PdfReader(f)
    text=''
    for page in pdf_reader.pages:
      text += page.extract_text()
    mdText = markdown(text)
  with open(output_file, 'w', encoding='utf-8') as f:
    f.write(mdText)
  print('Conversion successful')

def convert2markdown(input_file, output_file):
  try:
    sbprcssRUN(['pandoc', '-s', input_file, '-o', output_file])
    print('Conversion successful!')
  except FileNotFoundError:
    print('Pandoc is not installed or not in the system path.')
  except Exception as e:
    print('An error occurred during conversion:', str(e))

def main():
  input_file = 'input.docx' # Replace with the path to your Word document or PDF file
  output_file = 'output.md' # Replace with the desired output Markdown file
  if input_file.endswith('.docx'): convert_docx_to_markdown(input_file, output_file)
  elif input_file.endswith('.pdf'): convert_pdf_to_markdown(input_file, output_file)
  else: print('Unsupported file format.')
  convert2markdown(input_file, output_file)
