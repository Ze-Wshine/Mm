import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 读取数据
df = pd.read_excel('F:\数模校赛\Mm\编程\数据集\第二题整合数据.xlsx')

# 筛选人口变量与在校生人数列
corr_data = df[['总户数/万户','户均人口/人/户','年末常驻总人口/万人','出生率/%', '死亡率/%', '人口自然增长率/%', '城镇化率/%',
                '义务教育在校生/万人', '高中教育在校生/万人', '高等教育在校生/万人']]

# 计算相关系数矩阵
corr_matrix = corr_data.corr()

# 可视化
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("人口变量与在校生人数的相关性热力图")
plt.show()
