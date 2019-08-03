import pandas as pd

df = pd.read_csv("C:\Mine\Github\Python\CDNOW.csv")
#将读取的文件进行每列标识
df2 = df[['1','2','3','4','5','6','7','8']]
df2