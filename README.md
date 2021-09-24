# moe-hakkadict 教育部臺灣客家語常用詞辭典資料

辭典文字內容以創用CC「姓名標示─禁止改作」3.0臺灣授權條款釋出，使用時請遵守條款規範，毋須另外申請授權。資料內容包含本辭典主詞目、詞性、詞目索引、所有腔別音讀、釋義、近義詞、反義詞及對應國語詞等欄位內容。

- `調值資料_raw/` 中的 .ods、.pdf 檔案，為教育部提供原始資料；.csv 檔案透過 LibreOffice 產生。
- `調型資料/` 中的 .csv檔案，是利用 `轉做調型資料.py` 轉換產生，調值與調型對應參考《客語能力認證基本詞彙》書中之說明，饒平腔以新竹地區為準。
- `調值資料_uni/` 及`調型資料/` 中的造字均轉換為Unicode，除了「⿺皮卜」字無Unicode，暫時以IDS組字符號呈現。
- 造字碼與Unicode對應參考 [豆腐烏專案](https://github.com/tauhu-tw/tauhu-oo) 的 [本土語言外字表](https://docs.google.com/spreadsheets/d/1RPN_4sVAYlHaMchak1wwf2dpNKRcLil7WFHkB1ZGVuE)。
