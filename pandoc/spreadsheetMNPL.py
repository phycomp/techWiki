from pandas import DataFrame
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb
from streamlit import spinner as stSpinner, set_page_config, title, subheader, text_input, multiselect, button, warning, success, download_button, error, write as stWrite

MENU, 表單=[], ['六十四卦', '先後天', '卦爻辭', '錯綜複雜', '二十四節氣']
for ndx, Menu in enumerate(表單): MENU.append(f'{ndx}{Menu}')
with sidebar:
  menu=stRadio('表單', MENU, horizontal=True, index=0)
  srch=text_input('搜尋', '')
if menu==len(表單):
  pass
elif menu==MENU[1]:
  tblName='sutra'
  sutraCLMN=queryCLMN(tblSchm='public', tblName=tblName, db='sutra')
  #rndrCode(sutraCLMN)
  fullQuery=f'''select {','.join(sutraCLMN)} from {tblName} where 章節~'中庸';'''
  rsltQuery=runQuery(fullQuery, db='sutra')
  #rndrCode([fullQuery, rsltQuery])
  rsltDF=session_state['rsltDF']=DataFrame(rsltQuery, index=None, columns=sutraCLMN)
  rsltDF#[rsltDF['章節']=='中庸']
elif menu==MENU[0]:
  sutraCLMN=['章節', '內容']
  rsltQuery=runQuery(f'''select {','.join(sutraCLMN)} from ;''', db='fiveClass')
  rsltDF=session_state['rsltDF']=DataFrame(rsltQuery, columns=sutraCLMN, index=None)
  sutraDF=session_state['rsltDF']=DataFrame([['', '']], columns=sutraCLMN, index=[0])
  DF[DF.fiveClass.str.contains('', case=False)]
  cols = ["col1", "col2"]
  df = DataFrame.from_records([{k: 0.0 for k in cols} for _ in range(25)])
  excel_data = to_excel(df)
  file_name = "excel.xlsx"
  download_button( f"Click to download {file_name}", excel_data, file_name, f"text/{file_name}", key=file_name)

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.save()
    processed_data = output.getvalue()
    return processed_data
df_xlsx = to_excel(df)
download_button(label='📥 Download Current Result', data=df_xlsx , file_name= 'df_test.xlsx')

def to_excel(df: pd.DataFrame):
    in_memory_fp = BytesIO()
    df.to_excel(in_memory_fp)
    # Write the file out to disk to demonstrate that it worked.
    in_memory_fp.seek(0, 0)
    return in_memory_fp.read()
