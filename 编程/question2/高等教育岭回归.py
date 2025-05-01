import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import RidgeCV
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error

df = pd.read_excel(r'F:\数模校赛\Mm\编程\数据集\第二题整合数据.xlsx')


# 选择自变量
X = df[['总户数/万户', '户均人口/人/户', '年末常驻总人口/万人', '出生率/%', '死亡率/%', '人口自然增长率/%', '城镇化率/%']]

# 选择因变量
y = df['高等教育在校生/万人']

# 标准化自变量
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
'''
# 检验标准化是否成功

# 计算每个特征的均值和标准差

means = pd.DataFrame(X_scaled, columns=X.columns).mean()
std_devs = pd.DataFrame(X_scaled, columns=X.columns).std()
print("均值：\n", means)
print("标准差：\n", std_devs)

# 经检验，均值接近0，标准差接近1，标准化成功。
'''
# 构建岭回归模型并交叉验证

# 定义α的取值范围
alphas = np.logspace(-3, 3, 100)

# 构建岭回归模型并进行交叉验证
ridge_cv = RidgeCV(alphas=alphas, store_cv_values=True)
ridge_cv.fit(X_scaled, y)

# 输出最佳α值
print(f"最佳 alpha 值: {ridge_cv.alpha_}")

# 模型评估

# 回归系数
coefficients = ridge_cv.coef_
print("回归系数:", coefficients)

# 模型评分（R²）
r2 = ridge_cv.score(X_scaled, y)
print(f"模型 R² 分数: {r2}")