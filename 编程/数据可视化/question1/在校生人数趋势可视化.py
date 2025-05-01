import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 读取Excel数据
df = pd.read_excel(r'F:\数模校赛\Mm\编程\数据集\在校生人数历史数据.xls',sheet_name='17-10',engine='xlrd')

# 设置图表大小
plt.figure(figsize=(10, 6))

# 绘制各教育阶段的折线图
plt.plot(df['年份'], df['义务教育在校生'], marker='o', label='义务教育')
plt.plot(df['年份'], df['高中教育在校生'], marker='s', label='高中教育')
plt.plot(df['年份'], df['高等教育在校生'], marker='^', label='高等教育')

# 添加标题和标签
plt.title('吉林省各教育阶段在校生人数变化趋势')
plt.xlabel('年份')
plt.ylabel('在校生人数（人）')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()