from dbUtil import runQuery
from pandas import DataFrame
from streamlit import text_input, dataframe, columns as stColumns, write as stWrite, info as stInfo
from streamlit import sidebar, session_state, line_chart, slider
from streamlit import text_input, text_area
tchwkCLMN=['id', '主旨', '內容']

MENU, 表單=[], ['tchwk', '搜尋', '更新', '資料驗證', '搜索內容', '輸入or更新']	#, '錯綜複雜', '二十四節氣'
for ndx, Menu in enumerate(表單): MENU.append(f'{ndx}{Menu}')
with sidebar:
  menu=stRadio('表單', MENU, horizontal=True, index=0)
  srch=text_input('搜尋', '')
if menu==len(表單):
  pass
elif menu==MENU[1]:
  #from 眼科.折線圖 import plotSght#, cnvrtDF, cnvrtLOG
  #tchwkCLMN=session_state['tchwkCLMN']

  keyTerm=text_input('搜索關鍵字')   #32567127
  if keyTerm.find('<->')!=-1:
    fullQuery=f'''select {','.join(tchwkCLMN)} from isc8381."TechwikiMnpltn" where to_tsvector(主旨)@@to_tsquery('{keyTerm}') or to_tsvector(內容)@@to_tsquery('{keyTerm}') limit 10;'''
  else:
    fullQuery=f'''select {','.join(tchwkCLMN)} from isc8381."TechwikiMnpltn" where 主旨~*'{keyTerm}' or 內容~*'{keyTerm}' limit 10;'''
  qryRslt=runQuery(fullQuery, db='tchwk') #[v[0] for v in ]
  qryDF=DataFrame(data=qryRslt , columns=tchwkCLMN, index=None)
  dataframe(qryDF)
  #qryDF.主旨
elif menu==MENU[2]:
  tid=text_input('更新')
  if tid:
    fullQuery=f'''select 主旨, 內容 from isc8381."TechwikiMnpltn" where id='{tid}';'''#, db='tchwk'runQuery() [v[0] for v in ]
    qryRslt=runQuery(fullQuery, db='tchwk') #[v[0] for v in ]
    qryDF=DataFrame(data=qryRslt , columns=['主旨', '內容'])
    dataframe(qryDF)
    leftPane, rightPane=stColumns([1, 10])
    主旨=leftPane.text_area('主旨', qryDF.主旨.str.cat())
    內容=rightPane.text_area('內容', qryDF.內容.str.cat())
    if 主旨 and 內容:
      主旨=主旨.replace("'", "@")
      內容=內容.replace("'", "@")
      fullQuery=f'''update isc8381."TechwikiMnpltn" set 主旨='{主旨}', 內容='{內容}' where id='{tid}';'''#, db='tchwk'runQuery() [v[0] for v in ]
      runQuery(fullQuery, db='tchwk', commitType='update')
elif menu==MENU[-1]:
  tblName='TechwikiMnpltn'
  clmnQuery=f'''select column_name from information_schema.columns WHERE table_schema = 'isc8381' AND table_name = '{tblName}';'''
  session_state['tchwkCLMN']=tchwkCLMN=runQuery(clmnQuery, db='tchwk', commitType='insert')
  主旨=text_input('主旨')
  內容=text_area('內容')
  if 主旨 and 內容:
    fullQuery=f'''insert into isc8381."{tblName}" (主旨, 內容) values('{主旨}', '{內容}');'''
    qryRslt=runQuery(fullQuery, db='tchwk', commitType='insert')
    tchwkDF=DataFrame(columns=tchwkCLMN, data=qryRslt)
    dataframe(tchwkDF)
    #stWrite(qryRslt)
  #qryRslt=runQuery(f'select * from "OLAP".視力手術 where ~'{keyTerm}'limit 50;', db='bdtest')
  #dataframe(qryRslt)
  #stWrite(qryRslt)#DataFrame(data=qryRslt))
  #dataframe()
elif menu==MENU[0]:
  #from 眼科 import 折線圖
  '''
  try:
    sghtInfo=session_state['sghtInfo']
  except:
    fin=open('rsltSight.csv')
    sghtInfo=session_state['sghtInfo']=fin.read()
  session_state['sghtInfo']=sghtInfo

  '''

  #from 眼科 import 折線圖
  #from streamlit.components.v1 import html
  #from 眼科.折線圖 import cnvrtDF, plotSght
  from pandas import DataFrame, set_menu
  from streamlit import markdown, dataframe, number_input
  from dbUtil import runQuery
  set_menu('display.max_colwidth', 400)
  noTchwk=number_input('要抓取n紀錄', 100)
  #markdown('<style>div[role=radiogroup]{flex-direction:row; flex-wrap:wrap; justify-content:space-between;}</style>', unsafe_allow_html=True)
  try:
    #fullQuery=f'''select 主旨, 內容 from isc8381."TechwikiMnpltn" limit 10;'''
    #TCHWKs=runQuery(fullQuery, db='tchwk')
    TCHWKs=session_state['TCHWKs']
    dkjkf
  except:
    #eyeHISTs=open('eyeHISTs').read().split(',')
    if noTchwk:
      TCHWKs=runQuery(f'''select {','.join(tchwkCLMN)} from isc8381."TechwikiMnpltn" limit {noTchwk};''', db='tchwk') #[v[0] for v in ]
      session_state['TCHWKs']=TCHWKs
  qryDF=DataFrame(data=TCHWKs, columns=tchwkCLMN, index=None)
  dataframe(qryDF)
  #max_colwidth
  totalTchwk=len(TCHWKs)
  lastPage=10
  noPerPage = totalTchwk // lastPage
  midPage=lastPage//2
  spcfcPg=slider('第幾頁', min_value=1, max_value=lastPage, value=midPage)
  Prev, _ , Next = stColumns([1, 10, 1])
  #pgNmbr=None
  if spcfcPg:
    pass
    #pgNmbr=session_state['pgNmbr']=spcfcPg
    #pgNmbr=session_state.get('pgNmbr')
    #if not pgNmbr: pgNmbr=0
    #stWrite(dFrame)

  try: pgNmbr=session_state['pgNmbr']
  except: pass#session_state['pgNmbr']=pgNmbr
  if Next.button("Next"):
    if pgNmbr + 1 > lastPage: pgNmbr = 1
    else: pgNmbr += 1
    session_state['pgNmbr']=pgNmbr
  if Prev.button("Previous"):
    if pgNmbr - 1 < 0: pgNmbr = lastPage
    else: pgNmbr -= 1
    session_state['pgNmbr']=pgNmbr
  #print('pgNmbr', pgNmbr)
  stWrite(pgNmbr, 'spcfcPg', spcfcPg)
  if pgNmbr==1:
    tchwkSPAN=TCHWKs[:noPerPage]
  elif pgNmbr==lastPage:
    tchwkSPAN=TCHWKs[noPerPage*(lastPage-1):]
  else:
    tchwkSPAN=TCHWKs[noPerPage*(pgNmbr-1):noPerPage*pgNmbr]
  dataframe(tchwkSPAN)
  #eyeMem=eyeHISTs[pgNmbr*ptntPerPage:pgNmbr*ptntPerPage+ptntPerPage]
elif menu==MENU[2]:
  from 眼科.rtrvIVI import rtrvIVI
  from pandas import read_csv
  #df=read_csv('IVILOAE.csv', delimiter='\x06', dtype='str')
  #df.apply(rtrvIVI, axis=1)
elif menu==MENU[3]:
  from 眼科.資料驗證 import dataIntegrity
  dataIntegrity()
