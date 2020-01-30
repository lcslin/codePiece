import pandas as pd
import hashlib

def func_mask(x):
   tmp_x = ''
   for idx,i in enumerate(x):
      if idx > 0 and idx % 2 == 1:
         tmp_x = tmp_x + i
      else:
         tmp_x = tmp_x + 'X'
   return tmp_x

def func_md5(x):
   m = hashlib.md5()
   data = "G. T. Wang"

   # 先將資料編碼，再更新 MD5 雜湊值
   m.update(x.encode("utf-8"))

   h = m.hexdigest()
   return h


xls = pd.read_excel('2018貿易局補助展覽-mask.xls', dtype=str)
xls['name-encode'] = xls['公司/商號名稱'].apply(lambda x: func_mask(str(x)))
xls['ban-encode'] = xls['統一編號'].apply(lambda x: func_md5(str(x)))

xls.to_excel('output.xlsx')
