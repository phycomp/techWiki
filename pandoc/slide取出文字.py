#!/usr/bin/env python
from odf import text, teletype
from odf.opendocument import load as odfLoad
from glob import glob
from os.path import splitext

FILEs=glob('*.docx')
for fname in FILEs:
  textdoc = odfLoad(fname)  #"your.odt"
  base, ext=splitext(fname)
  allParas = textdoc.getElementsByType(text.P)
  out=teletype.extractText(allParas[0])
  with open(f'{base}.raw', 'w') as fout:
    fout.write(out)
#***********************************************************
#!/usr/bin/env python
import aspose.slides as slides

#Instatiate Presentation class that represents a ODP file
with slides.Presentation("pres.odp") as pptxPresentation:
    # Get an Array of ITextFrame objects from all slides in the ODP
    textFramesPPTX = slides.util.SlideUtil.get_all_text_frames(pptxPresentation, True)
    # Loop through the Array of TextFrames
    for i in range(len(textFramesPPTX)): # Loop through paragraphs in current ITextFrame
      for para in textFramesPPTX[i].paragraphs:
        # Loop through portions in the current IParagraph
        for port in para.portions:
          print(port.text) # Display text in the current portion
          print(port.portion_format.font_height) # Display font height of the text
          if port.portion_format.latin_font != None:
            print(port.portion_format.latin_font.font_name) # Display font name of the text
