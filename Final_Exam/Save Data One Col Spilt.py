import pandas as pd

#需要拆分的列必须有标签
name = ['number']
#pandas读取文件
data = pd.read_csv('C:\Mine\Github\Python\CDNOW.txt')
#将‘number’列以空格为标识符进行拆分
data1 = data['number'].str.split(' ',expand=True)
data1.to_csv('CDNOW.csv')