import io
from pathlib import Path
from docx2txt2 import extract_text as xtrctTXT, extract_images as xtrctIMG, process as docPrcss
from streamlit import sidebar, radio as stRadio, text_input

MENU, 表單=[], ['轉換DOC', '轉換ODT']	#, '錯綜複雜', '二十四節氣'
for ndx, Menu in enumerate(表單): MENU.append(f'{ndx}{Menu}')
with sidebar:
  menu=stRadio('表單', MENU, horizontal=True, index=0)
  來源=text_input('來源')
  目的=text_input('目的')
  #menu=stRadio('表單', MENU, horizontal=True, index=0)
if menu==len(表單):
  pass
elif menu==MENU[1]:
  tblName='sutra'
elif menu==MENU[0]:
  if 來源 and 目的:
    cntxt = xtrctTXT(來源)
    rndrCode(cntxt)
    cntxtSlide = xtrctSlide(來源)
    rndrCode(cntxtSlide)
    imgPath = xtrctIMG(來源, 目的)
    rndrCode(imgPath)
def imgXtrct():
  cntxt = xtrctTXT("path/to/my.docx")
  imgPath = xtrctIMG("path/to/my.docx", 目的)
  # actual Paths
  docx_path = Path(__file__).parent / "my.docx"
  image_out = Path(__file__).parent / "my" / "images"
  image_out.mkdir(parents=True)

  text2 = xtrctTXT(docx_path)
  image_paths2 = xtrctIMG(docx_path, image_out)

def byteStream(): # bytestreams
  docx_bytes = b"..."
  bytes_io = io.BytesIO(docx_bytes)
  text3 = xtrctTXT(bytes_io)
  image_paths3 = xtrctIMG(bytes_io, "path/to/images/out")
  #We also support the process method as the original docx2txt exposed.


  text = docPrcss("path/to/my.docx")

  # Image output paths are discarded in this example
  text = docPrcss("path/to/my.docx", "path/to/images/out")
  #Compatability & Motivation
  #docx2txt2 provides a superset of all data returned by docx2txt with some caveats (below), so the below is true:

def main():
  import docx2txt
  import docx2txt2

  orig_content = docx2txt.process("my/file.docx").split()
  new_content = docx2txt2.process("my/file.docx").split()
  assert all(orig in new_content for orig in orig_content)
