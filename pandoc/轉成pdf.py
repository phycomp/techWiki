from streamlit import subheader, sidebar, session_state, radio as stRadio, columns as stCLMN, text_area, text_input, multiselect, toggle as stToggle #slider, dataframe, code as stCode, cache as stCache,
from pandas import DataFrame
from streamlit import image as stImage, markdown as stMarkdown, columns as stCLMN, container as stContainer
from stUtil import rndrCode
#from os import walk as osWalk
#from os.path import splitext    #basename, 
#from 遞廻 import rcrsvDIR
#from os.path import isdir
#from os import listdir
from mimetypes import guess_type#, read_mime_types    mimetypes.(path_file_to_upload)[
#from streamlit_pdf_viewer import pdf_viewer
from fhndlrUtil import 四欄文件, 三欄文件, pdfVWR
from base64 import b64encode
from pypandoc import convert_file as cnvrtFILE, convert_text as cnvrTXT
from pathlib import Path, PurePath

MENU, 表單=[], ['rndrMD', '檔案管理', 'mdTMPL']#, brwsrType, ['pdfViewr', 'PIC', 'VID'] #, '卦爻辭', '錯綜複雜', '二十四節氣'
mdFILE, MDs='dummy.md', ['configDverse.md', 'markdown-sample.md', 'sample.tex']
for ndx, Menu in enumerate(表單): MENU.append(f'{ndx}{Menu}')
with sidebar:
  menu=stRadio('表單', MENU, horizontal=True, index=1)
  #瀏覽=stRadio('瀏覽', brwsrType, key='browser', horizontal=True, index=0)
  md=stRadio('瀏覽', MDs, key='MD', horizontal=True, index=0)
  fmt=stRadio('轉換', ['rst', 'pdf', 'docx'], key='轉換', horizontal=True, index=0)

if menu==len(表單):
  pass
elif menu==MENU[0]:
  md=Path(md)
  根=Path(__file__).parent.parent
  rndrCode(根)
  #leftPane, rightPane=stCLMN([4, 6])
  #with leftPane:
  with open(根/md) as fin:
    outputINFO=fin.read()
    stMarkdown(outputINFO)
elif menu==MENU[2]:
  mdCntxt=text_area('寫作')
  leftPane, rightPane=stCLMN(2)
  with leftPane:
    if mdCntxt:
      output = cnvrTXT(mdCntxt, 'rst', format='md')
      with open(mdFILE, 'w') as fout:
        fout.write(output)
      rndrCode(output)
  with rightPane:
    with open(mdFILE, "rb") as fin:
      mdCntxt=fin.read()
      mdCntxt = cnvrTXT(mdCntxt, 'rst', format='latex')   #docbook, haddock, html, json, latex, markdown, markdown_github, markdown_mmd, markdown_phpextra, markdown_strict, mediawiki, native, opml, rst, textile
      rndrCode(mdCntxt)
      #base64PDF = b64encode(mdCntxt).decode('utf-8')
      #pdfPAGE = f'<iframe src="data:application/pdf;base64,{base64PDF}" width="800" height="800" type="application/pdf"></iframe>'
      #stMarkdown(pdfPAGE, unsafe_allow_html=True)
elif menu==MENU[1]:
  #with sidebar:
  if md:
    md=Path(md)
    base, fmt=md.stem, md.name
    #md.resolve()
    #base, ext=splitext(md)
    if fmt in ['pdf', 'docx']:
      with rightPane:
        output, ext=splitext(md)
        outfile=f'{output}.{fmt}'
        outputMD = pndcCnvrt(md, fmt, outputfile=outfile)
        with open(outfile, "rb") as f:
          base64PDF = b64encode(f.read()).decode('utf-8')
          pdfPAGE = f'<iframe src="data:application/pdf;base64,{base64PDF}" width="800" height="800" type="application/pdf"></iframe>'
          stMarkdown(pdfPAGE, unsafe_allow_html=True)
    elif fmt=='rst':
      outputMD = pndcCnvrt(md, fmt)
      rndrCode(outputMD)
      output = cnvrtFILE(md, 'rst', format='md')
    #with open(md) as fin: rndrCode(fin.read())
  #tblName='sutra'
  #sutraCLMN=queryCLMN(tblSchm='public', tblName=tblName, db='sutra')
  ##rndrCode(sutraCLMN)
  #fullQuery=f'''select {','.join(sutraCLMN)} from {tblName} where 章節~'中庸';'''
  #rsltQuery=runQuery(fullQuery, db='sutra')
  #rndrCode([fullQuery, rsltQuery])
  #rsltDF=session_state['rsltDF']=DataFrame(rsltQuery, index=None, columns=sutraCLMN)
  #rsltDF#[rsltDF['章節']=='中庸']
    #if count%3==2: stImage(fullName, caption=fullName)
    #[stImage(f'images/{fname}', caption=f'images/{fname}') for ndx, fname in enumerate(檔案) if ndx%3==2]
