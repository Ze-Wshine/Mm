import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 读取数据
df = pd.read_excel('数据集\第二题整合数据.xlsx')

# 筛选人口变量与在校生人数列
corr_data = df[['总户数/万户','户均人口/人/户','年末常驻总人口/万人','出生率/%', '死亡率/%', '人口自然增长率/%', '城镇化率/%',
                '义务教育在校生/万人', '高中教育在校生/万人', '高等教育在校生/万人']]

# 计算相关系数矩阵
corr_matrix = corr_data.corr()

# 可视化
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')

# 设置横坐标文字为水平显示并增加间距
plt.xticks(rotation=45, ha='right', fontsize=10)

# 手动调整边距，避免文字被截断
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)

plt.title("人口变量与在校生人数的相关性热力图")
plt.show()
