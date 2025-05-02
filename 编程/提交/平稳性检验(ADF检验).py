#导入必要库
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
import os
print(os.getcwd())


plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 读取Excel数据
df = pd.read_excel(r'数据集\在校生人数历史数据.xlsx', sheet_name='17-10', engine='xlrd')



# 定义ADF函数
def adf_test(series, label):
    result = adfuller(series)
    print(f"\n【{label}】ADF检验统计量: {result[0]}")
    print(f"{label}的p值: {result[1]}")
    if result[1] < 0.05:
        print(f"→ {label} 是平稳的")
    else:
        print(f"→ {label} 是非平稳的")

#执行ADF检验
adf_test(df['义务教育在校生'], '义务教育')
adf_test(df['高中教育在校生'], '高中教育')
adf_test(df['高等教育在校生'], '高等教育')

#最终结果为义务教育和高等教育为非平稳，故对义务教育和高等教育在校生进行一阶差分。
df['义务教育差分'] = df['义务教育在校生'].diff()
adf_test(df['义务教育差分'].dropna(), '义务教育一阶差分')

df['高等教育差分'] = df['高等教育在校生'].diff()
adf_test(df['高等教育差分'].dropna(), '高等教育一阶差分')

#一阶差分后高等教育仍然非平稳，故不适合用时间序列方法做本题。

