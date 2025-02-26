title: 使用 Pandoc 將 Markdown 轉為 PDF 文件
author: Sam Chuang
date: "2020-01-13"
CJKmainfont: "華康魏碑體"
documentclass:
    - ctexart
---

感謝 Will 保哥 這篇文章的啟蒙

介紹好用工具：Pandoc ( 萬用的文件轉換器 )

## 準備環境
 * 安裝 Pandoc : 功能強的萬用文件轉換器
 * 安裝 MiKTeX : 在 Pandoc 轉檔時會自動安裝缺少的套件 (例如處理中文字就需要 cjk 套件)
 * YAML metadata 區塊
 * 在 markdown 開頭寫 YAML metadata 區塊，依此區塊用到的不同參數，會對應 template 格式檔而輸出至文件指定的位置，如：頁首、頁尾、字體格式等。


title: 使用 Pandoc 將 Markdown 轉為 PDF 文件
author: Sam Chuang
date: "2020-01-13"
CJKmainfont: "Microsoft YaHei Mono"

YAML metadata 參數
### CJKmainfont
指定中文字型檔，預設為 SourceSansPro-Bold.otf 字型 (不支援中文字)
若文件內有中文字，必須在 YAML metadata 區塊加上中文字型的指定，否則會轉檔失敗。
準確一點的說法：指定的字型檔必須包含文件內所有用到的字元
也就是，若輸入 Unicode 的 emoji 字元，而字型檔內沒有此 emoji 字元，一樣會出錯。

參考資料

Pandoc with Chinese

YAML metadata 其他參數
官方文件 (Pandoc User’s Guide - Templates)

執行 Pandoc 指令轉檔
在 Terminal 或 PowerShell 或 CMD 輸入 Pandoc 指令

Linux pandoc 'example.md' -o 'example.pdf' --latex-engine=xelatex --toc --toc-depth=4
Windows pandoc 'example.md' -o 'example.pdf' --pdf-engine=xelatex --toc --toc-depth=4
#### 指令參數說明
 * -o 'example.pdf' 輸出檔名
 * --latex-engine=xelatex 或 --pdf-engine=xelatex 指定 LaTeX engine 使用 xelatex 製作 PDF
 * --toc 用 markdown 的標題在 PDF 內產生 Table of Contents 目錄，同時加上頁碼和連結
 * --toc-depth=NUMBER Table of Contents 目錄要包含多少層的 markdown 標題 NUMBER 可設定的值為 1~6 (預設為 3)
指令參數參考
官方文件 (Pandoc User’s Guide - Options)
Pandoc 官網轉換各種文件的範例
輸出樣式
預設樣式
執行轉檔指令沒有指定 template 樣式會以預設格式輸出，預設格式不會針對 markdown 每個語法去對應不同字型、顏色、格式，因此輸出的文件版面不美觀，甚至可能會遇到中文段落的文字不會自動換行，或超出版面的問題，最顯而易見的是邊界空白區就佔了將近版面 40%。

使用 LaTeX template 自訂樣式
可依需求自行撰寫 LaTeX template 的樣式檔，輸出時只要指定使用此樣式檔，只要樣式檔沒寫錯，就會照我們預期的版面樣式輸出。

若想自訂樣式檔，可參考 LaTeX template 的寫法

Using Markdown Templates
官方文件 (Pandoc User’s Guide - Variables for LaTeX)
使用 Eisvogel LaTeX template 樣式
自製 LaTeX template 樣式輸出的格式最完美，但也是最曠日費時的做法，人生短暫，我們可以使用別人寫好現成的 LaTex template，把省下的時間用來創造更美好的事物，這裡選用開源專案的 Eisvogel LaTeX template。

下載 Eisvogel LaTex template
Eisvogel LaTex template

解壓縮 Zip

將裡面的 [eisvogel.tex](https://github.com/Wandmalfarbe/pandoc-latex-template/releases/download/2.4.2/Eisvogel-2.4.2.tar.gz) 複製到 pandoc templates 目錄，並改名為 eisvogel.latex，pandoc templates 的路徑為


Unix、Linux、macOS : /Users/USERNAME/.local/share/pandoc/templates/ 或 /Users/USERNAME/.pandoc/templates/

Windows : C:\Users\USERNAME\AppData\Roaming\pandoc\templates\

如果目錄不存在，請自己建立

使用 Eisvogel LaTeX template
在 Terminal 或 PowerShell 或 CMD 輸入 Pandoc 指令

Linux pandoc 'example.md' -o 'example.pdf' --latex-engine=xelatex --toc --from markdown --template eisvogel --listings
Windows pandoc 'example.md' -o 'example.pdf' --pdf-engine=xelatex --toc --from markdown --template eisvogel --listings
指令參數說明 (使用 template)
--from markdown 指定來源為 markdown 格式
--template eisvogel 指定要使用的 template 樣式檔 此例會到 Template 預設目錄 找eisvogel.latex
--listings 用來處理 LaTeX code block 的 listings 套件
指令參數參考資料
## 如何使用 pandoc 和 LaTeX 製作漂亮的 pdf
Eisvogel - A pandoc LaTeX template to convert markdown files to PDF or LaTeX.
4. Eisvogel LaTeX template 透過 YAML metadata 使用自訂變數 (進階用法)
Eisvogel LaTeX template 有預留參數，可透過 markdown 的 YAML metadata 自訂變數傳入 template

在 YAML metadata 設定 template 預留的自訂變數，可在不修改 template 檔的情況下調整輸出版面

例如輸出時加入封面、指定各種 markdown 語法對應的字型格式設定、…等

YAML metadata 使用自訂變數參考資料
Eisvogel GitHub Repo 說明 - Custom Template Variables

範例
點擊範例檔名連結可下載範例檔

若下載的範例原始檔沒看到 YAML metadata 區塊內容，就是被網站平台給過濾掉了 。
YAML metadata 設定方式可參考：YAML metadata 區塊
範例1 (不使用 template)
執行指令

pandoc "example.txt" -o "example.pdf" --pdf-engine=xelatex --toc --toc-depth=4
結果 (不使用 template)

example.txt 是 markdown 來源檔

example.pdf 是輸出的 PDF 檔
此範例未指定 template 樣式檔，使用預設輸出 ，雖然已將中文內容轉成 PDF 文件，也包含有 Table of Contents 目錄、頁碼與文章標題的書籤連結，但轉換出來的版面不完美。

範例2 (使用 Eisvogel template 格式)
執行指令

pandoc "example.txt" -o "example_with_template.pdf" --pdf-engine=xelatex --toc --toc-depth=4 --from markdown --template eisvogel --listings
--template eisvogel 指定使用 Eisvogel template 樣式檔

結果 (使用 Eisvogel template 格式)

example.txt 是 markdown 來源檔，同範例1的markdown 檔

example_with_template.pdf 是輸出的 PDF 檔
轉換出來的版面很完美。

範例3 (使用 Eisvogel template + YAML metadata)
製做封面底圖並存為 PDF 檔：background1.pdf

在 YAML metadata 增加 template 預留的參數，啟用封面，並指定封面檔


title: 使用 Pandoc 將 Markdown 轉為 PDF 文件
author: Sam Chuang
date: "2020-01-13"
CJKmainfont: "Microsoft YaHei Mono"
subject: "Pandoc 轉檔教學"
keywords: [Markdown, Pandoc]
titlepage: true,
titlepage-rule-color: "360049"
titlepage-background: "background1.pdf"

執行指令

同範例2的指令

pandoc "example_with_template_titlepage.txt" -o "example_with_template_titlepage.pdf" --pdf-engine=xelatex --toc --toc-depth=4 --from markdown --template eisvogel --listings
結果 (使用 Eisvogel template + YAML metadata)

example_with_template_titlepage.txt 是 markdown 來源檔

example_with_template_titlepage.pdf 是輸出的 PDF 檔
轉換出來的內容有附封面，更精致了。

其他參考資料
Pandoc’s Markdown 語法 (中文翻譯)
Pandoc - Markdown 基本語法介紹
Pandoc - Markdown 轉 PDF 格式
