import matplotlib.pyplot as plt
import sys
import os

# 获取上一级目录路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from question1 import prediction_main_function as main
from question1 import model_process as process

from statsmodels.stats.outliers_influence import variance_inflation_factor

# 绘制未来三年预测的在校生人数
plt.figure(figsize=(10, 6))

plt.plot(main.future_predictions.index, main.future_predictions['义务教育在校生/万人'], label='义务教育在校生', marker='o')
plt.plot(main.future_predictions.index, main.future_predictions['高中教育在校生/万人'], label='高中教育在校生', marker='o')
plt.plot(main.future_predictions.index, main.future_predictions['高等教育在校生/万人'], label='高等教育在校生', marker='o')

plt.xlabel('年份')
plt.ylabel('在校生人数（万人）')
plt.title('未来三年吉林省各教育阶段在校生人数预测')
plt.legend()
plt.grid(True)
plt.show()