from streamlit import markdown, empty, number_input, button, toast, header, sidebar, set_page_config as pageConfig, columns as stCLMN
from streamlit_ace import st_ace
import time
#import pyautogui
pageConfig(page_title="Markdown編輯器", layout="wide", page_icon="💡")
markdown_table = """
## Markdown 語法參考

| 語法類型 | 說明             | 示例                             |
|----------|------------------|----------------------------------|
| 標題     | 創建標題         | `# 一級標題` `## 二級標題`        |
| 強調     | 斜體、粗體、刪除線 | `*斜體*` **粗體** `~~刪除線~~`    |
| 列表     | 無序和有序列表   | `- 項目1` `1. 第一項`            |
| 鏈接     | 插入鏈接         | `[標題](https://example.com)`   |
| 圖片     | 插入圖片         | `![替代文本](image-url.jpg)`     |
| 引用     | 引用文本         | `> 引用內容`                     |
| 代碼     | 顯示代碼         | ```python行內代碼```  |
| 分隔線   | 插入分隔線       | `---`                            |
| 任務列表 | 創建任務列表     | `- [x] 完成任務` `- [ ] 待完成`   |
| HTML元素 | 使用HTML元素     | `<div>HTML元素</div>`            |
| 轉義字符 | 轉義Markdown字符 | `\*這不是斜體\*`                 |
| 換行 | 隔開上下內容 | `在要隔開的內容之間輸入<br>`                |

<br>

## Markdown 表格語法示例

```markdown
| 表頭1 | 表頭2 | 表頭3 |
|-------|:-----:|------:|
| 左對齊 | 居中對齊 | 右對齊 |
| 文本   | 文本   | 文本  |
"""
with sidebar:
    markdown(markdown_table, unsafe_allow_html=True)
# 創建兩個并行的列
c1, c2, c3, c4, c5 = stCLMN([0.5,2,0.5,2,0.5])

# 添加全局CSS來改變一級和二級標題的樣式和代碼塊背景色
markdown("""<style>
h1, h2 { background-image: linear-gradient(to right, #00ccff, #1aff1a, #ffffff); border-radius: 3px; color: white !important; padding: 5px; }
pre { background-color: #E0FFF0 !important; }
</style>""", unsafe_allow_html=True)

# 使用左側列來獲取用戶輸入的Markdown文本
with c1:
    empty()
with c2:
    header("Markdown輸入")
    markdown_text=st_ace(language="markdown", value="", height=400, theme="monokai", show_gutter=True, key="markdown_editor")

with c3:
    empty()

# 使用右側列來顯示Markdown文本的渲染效果
with c4:
    header("操作區域")
    # 用戶提交內容後，顯示滾動幅度輸入框和復制按鈕
    # 默認隱藏復制區域的相關控件
    copy_button = None
    scroll_value = None
    # 當用戶提交內容後，顯示滾動幅度輸入框和復制按鈕
    if markdown_text:   # is not None
        # 設置向下滾動的幅度，用戶可以調整
        scroll_value = number_input('設置向下滾動的幅度（單位：行數）', min_value=1, value=10, step=1)
        copy_button = button('開始復制')

    # 如果已經設置了滾動值并且按下了復制按鈕，執行復制操作
    if copy_button:
        # 執行復制區域的函數
        # 定義復制區域的函數
        # 矩形區域的兩個頂點坐標
        first_point = (1012, 500)  # 左上角
        second_point = (1798, 500)  # 右上角
        def select_and_copy_area(scroll_amount):
            # 移動到第一個點并點擊以确保焦點在正确的窗口
            pyautogui.click(first_point)
            # 按下鼠標左鍵準備拖動
            pyautogui.mouseDown()
            time.sleep(0.2)  # 短暫延遲确保按鍵被注冊

            # 移動到第二個點，此處不改變y坐標
            pyautogui.moveTo(second_point[0], first_point[1])
            time.sleep(0.2)  # 短暫延遲以完成橫向選擇

            # 根據用戶輸入的滾動幅度計算滾動
            pyautogui.scroll(-scroll_amount * 100)  # 假設每行滾動100像素
            time.sleep(0.2)  # 短暫延遲以完成滾動

            # 松開鼠標左鍵完成選擇
            pyautogui.mouseUp()
            time.sleep(0.2)  # 短暫延遲以完成選擇操作

            # 執行 Ctrl+C 復制操作
            pyautogui.hotkey('ctrl', 'c')  # 對于 macOS 使用 'command', 'c'


        # 執行滾動并復制
        select_and_copy_area(scroll_value)
        toast("右側區域復制成功!")

    markdown(markdown_text, unsafe_allow_html=True)

with c5:
    empty()
