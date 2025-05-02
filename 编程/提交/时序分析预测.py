import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm #用于时间序列建模及统计分析
import scipy.stats as st  # 用于 Shapiro-Wilk 正态性检验

from statsmodels.stats.diagnostic import acorr_ljungbox  # Ljung-Box 检验
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_squared_error, mean_absolute_error#评估模型性能

# 设置中文字体
plt.rcParams['font.family'] = ['Microsoft YaHei'] 

# 原始数据
data = {
    'year': list(range(2015, 2024)),
    'exp': [597.52, 643.98, 658.67, 686.65, 677.74, 720.48, 709.2, 748.41, 835.33]
}
df = pd.DataFrame(data) #创建数据框

# 设置时间索引
df['date'] = pd.to_datetime(df['year'], format='%Y')
df.set_index('date', inplace=True)

# 取单列作为序列
series = df['exp']

# 构建模型
model = ExponentialSmoothing(
    series,
    trend='add',
    damped_trend=True,
    seasonal=None
)

# 拟合模型（自动估计平滑参数）
fit = model.fit(optimized=True)

'''
# 建模用

# 获取趋势（b_t）和水平（ℓ_t）估计值
# 水平估计值
level_estimates = fit.level

# 趋势估计值
trend_estimates = fit.trend

# 打印水平和趋势估计
print("水平估计 (ℓ_t):")
print(level_estimates)

print("趋势估计 (b_t):")
print(trend_estimates)

result_df = pd.DataFrame({
    'year': df.index.year,
    '水平估计 (ℓ_t)': level_estimates,
    '趋势估计 (b_t)': trend_estimates
})

print(result_df)
'''
'''
#建模用

#检验模型拟合程度是否达标

# 1.拟合值与残差
fitted_vals = fit.fittedvalues
residuals = series - fitted_vals

# 2.计算 RMSE、mae、mape
rmse = np.sqrt(mean_squared_error(series, fitted_vals))
mae  = mean_absolute_error(series, fitted_vals)
mape = np.mean(np.abs((series - fitted_vals) / series)) * 100
print(f"RMSE: {rmse:.2f} 亿元")
print(f"MAE: {mae:.2f} 亿元")
print(f"MAPE: {mape:.2f}%")
#该指标很低，表示拟合和预测结果非常优秀。

# 3.Q–Q 图
sm.qqplot(residuals, line='s')
plt.title('残差 Q–Q 图')
plt.show()
#数据点大致落在参考直线附近，正态性成立。

# 4.Ljung–Box 检验
max_lag = min(10, len(residuals) - 1)
lb_df = acorr_ljungbox(residuals, lags=[max_lag], return_df=True)
lb_stat = float(lb_df['lb_stat'].iloc[0])
lb_pvalue = float(lb_df['lb_pvalue'].iloc[0])

print(f"Ljung–Box 检验 (lag={max_lag})")
print(f"  检验统计量: {lb_stat:.4f}")
print(f"  p-value:       {lb_pvalue:.4f}")

# 判断
if lb_pvalue > 0.05:
    print("→ 残差不显著自相关（可视为白噪声）")
else:
    print("→ 残差存在自相关，需要进一步建模或调整")

#结果为不显著自相关，符合要求。

# 5.残差图与分布图
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(residuals.index.year, residuals, marker='o')
plt.axhline(0, linestyle='--', color='red')
plt.title('残差时间序列')
plt.xlabel('年份')
plt.ylabel('残差（亿元）')

plt.subplot(1, 2, 2)
plt.hist(residuals, bins=8, edgecolor='k')
plt.title('残差分布直方图')
plt.xlabel('残差（亿元）')
plt.ylabel('频数')
plt.tight_layout()
plt.show()
#残差图无明显异常。

#6. Shapiro–Wilk 正态性检验
shapiro_stat, shapiro_p = st.shapiro(residuals)
print("\nShapiro–Wilk 正态性检验")
print(f"  检验统计量: {shapiro_stat:.4f}")
print(f"  p-value:       {shapiro_p:.4f}")

if shapiro_p > 0.05:
    print("→ 残差近似正态分布")
else:
    print("→ 残差偏离正态分布，可能需要变换或其他模型")
# 残差符合正态分布，满足假设。
'''
# 预测未来3年
forecast = fit.forecast(3)
forecast.index = pd.to_datetime([2024, 2025, 2026], format='%Y')

print("\n未来三年年度预测：")
print(forecast)


'''# 可视化结果
plt.figure(figsize=(10, 6))
plt.plot(series.index.year, series, 'o-', label='历史经费')
plt.plot(fitted_vals.index.year, fitted_vals, 'r--', label='拟合经费')
plt.plot(forecast.index.year, forecast, 'g-o', label='预测经费')
plt.xlabel('年份')
plt.ylabel('教育经费（亿元）')
plt.title('双指数平滑：吉林省教育经费拟合与预测')
plt.legend()
plt.grid(True)
plt.show()
'''


