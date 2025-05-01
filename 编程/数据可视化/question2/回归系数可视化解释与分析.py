import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.family'] = ['Microsoft YaHei'] 

# 自变量列表
features = ['总户数/万户', '户均人口/人/户', '年末常驻总人口/万人', '出生率/%', '死亡率/%', '人口自然增长率/%', '城镇化率/%']

# 每个教育阶段的回归系数
coefficients = {
    '义务教育': [1.36237545,-0.76108142,0.72580112,0.86518521,-4.59615731,2.68445279,-1.01133629],
    '高中教育': [-9.81822526,-21.39015532,2.61268947,-3.34902391,-1.52426451,-1.24476645,-13.90889883],
    '高等教育': [0.14246691,-0.74066172,-1.14935177,-1.89201401,1.57749638,-1.80882007,1.12196887]
}

# 绘制条形图
fig, ax = plt.subplots(figsize=(10, 6))

# 为每个教育阶段绘制条形
width = 0.2  # 每个条形的宽度
x = np.arange(len(features))

for i, (education, coef) in enumerate(coefficients.items()):
    ax.bar(x + i * width, coef, width=width, label=education)

ax.set_xticks(x + width)
ax.set_xticklabels(features, rotation=45, ha="right")
ax.set_ylabel('回归系数')
ax.set_title('不同教育阶段自变量回归系数比较')
ax.legend()

plt.tight_layout()
plt.show()
