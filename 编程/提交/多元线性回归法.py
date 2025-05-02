#导入必要库

import pandas as pd
import statsmodels.api as sm #回归分析和统计建模库
import numpy as np
pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.max_rows', None)     # 显示所有行


from statsmodels.stats.outliers_influence import variance_inflation_factor

df = pd.read_excel(r'数据集\第一题整合数据.xlsx',sheet_name='1',engine='openpyxl')

# 自变量与因变量准备

# 自变量矩阵 X
features = [
    '出生率/%','死亡率/%','人口自然增长率/%','城镇化率/%',
    '年末常驻总人口/万人','义务教育学校数','高中教育学校数','高等教育学校数'
]
X = df[features]

# 添加常数项（截距）
X = sm.add_constant(X)

# 因变量
y义务 = df['义务教育在校生/万人']
y高中 = df['高中教育在校生/万人']
y高等 = df['高等教育在校生/万人']

#使用最小二乘法（OLS）对三个阶段的在校生人数分别建立回归模型并估计其参数

# 义务教育模型
model_义务 = sm.OLS(y义务, X).fit()

# 高中教育模型
model_高中 = sm.OLS(y高中, X).fit()

# 高等教育模型
model_高等 = sm.OLS(y高等, X).fit()
# 进行预测
# 先进行未来三年自变量的线性预测。
# 提取年份
years = np.arange(len(df))  # 如果你的年份是按行排列的，可以用索引代替

# 自变量列表
features = [
    '出生率/%','死亡率/%','人口自然增长率/%','城镇化率/%',
    '年末常驻总人口/万人','义务教育学校数','高中教育学校数','高等教育学校数'
]
'''
# 论文建模用
print(model_义务.params)  # 输出义务教育模型的回归系数β
print(model_高中.params)  # 输出高中教育模型的回归系数β
print(model_高等.params)  # 输出高等教育模型的回归系数β
'''
# 储存未来三年预测结果
future_data = {}

# 对每个变量做线性拟合并外推三年
for feature in features:
    y = df[feature].values
    X = sm.add_constant(years)
    model = sm.OLS(y, X).fit()
    
    # 预测未来三年
    future_years = np.array([len(df), len(df)+1, len(df)+2])
    X_future = sm.add_constant(future_years)
    y_pred = model.predict(X_future)
    
    future_data[feature] = y_pred

# 构造未来三年的 DataFrame
df_future = pd.DataFrame(future_data)
df_future.index = [f'Year_{i}' for i in range(1, 4)]
'''
# 论文建模用
print("未来三年预测的自变量：")
print(df_future)
'''

# 预测目标变量
future_X = sm.add_constant(df_future[features])

# 义务教育在校生人数预测
y_pred_义务 = model_义务.predict(future_X)

# 高中教育在校生人数预测
y_pred_高中 = model_高中.predict(future_X)

# 高等教育在校生人数预测
y_pred_高等 = model_高等.predict(future_X)

# 合并预测结果
future_predictions = pd.DataFrame({
    '义务教育在校生/万人': y_pred_义务,
    '高中教育在校生/万人': y_pred_高中,
    '高等教育在校生/万人': y_pred_高等
})

# 设置索引为Year_1, Year_2, Year_3
future_predictions.index = ['Year_1', 'Year_2', 'Year_3']
print("未来三年预测的在校生人数：")
print(future_predictions)








