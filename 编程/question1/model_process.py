import prediction_main_function as main
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from statsmodels.stats.outliers_influence import variance_inflation_factor

#模型进一步检验

#这里以义务教育模型为例
#1.检查残差是否近似正态分布
resid = main.model_义务.resid  # 获取残差
sm.graphics.qqplot(resid, line='45', fit=True)
plt.title('义务教育残差 Q–Q 图')
plt.show()
#结果表示残差近似正态

#2.检查是否存在异方差
fitted = main.model_义务.fittedvalues
plt.scatter(fitted, resid)
plt.axhline(0, color='grey', linestyle='--')
plt.xlabel('拟合值')
plt.ylabel('残差')
plt.title('残差 vs. 拟合值')
plt.show()
#结果近似满足方差齐性

#3.自相关检验：检测残差序列中是否存在一阶自相关。
dw_stat = sm.stats.stattools.durbin_watson(resid)
print('Durbin–Watson 统计量：', dw_stat)
# 统计量接近2,无自相关

#4 线性关系检验，这里以人口自然增长率为例
sm.graphics.plot_ccpr(main.model_义务, '人口自然增长率/%')
plt.title('人口自然增长率对义务教育在校生的CCPR 图')
plt.show()
# 经检验，点云均绕直线分布，线性假设合理。

#筛选显著自变量
print(main.model_义务.summary())


#其余模型预测均同理。