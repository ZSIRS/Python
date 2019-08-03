import pandas as pd
import numpy as np

#numpy加载文件
data = np.loadtxt('C:\Mine\Github\Python\CDNOW.txt')
#numpy以小数点后两位，不足的不补零，存入，以逗号分隔符进行分割
np.savetxt('NOW.txt',data,fmt='%.2f',delimiter=',')
data1 = pd.read_csv('C:\Mine\Github\Python\NOW.txt')
data1.to_csv('NOW.csv')