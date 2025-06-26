import json

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr
with open('AI_ICLR_2024.json') as f:
    ana_data = json.load(f)

score = []
confidence_score = []
summary = []
motivation = []
substance = []
replicability = []
originality = []
soundness = []
clarity = []
meaningful_comparison = []
for d in ana_data:
    score.append(int(d['score'][0]))
    confidence_score.append(int(d['confidence'][0]))
    summary.append(d['aspect'][0])
    motivation.append(d['aspect'][1])
    substance.append(d['aspect'][2])
    replicability.append(d['aspect'][3])
    originality.append(d['aspect'][4])
    soundness.append(d['aspect'][5])
    clarity.append(d['aspect'][6])
    meaningful_comparison.append(d['aspect'][7])
# 示例数据
data = {
    'Score': score,
    'Summary': summary,
    'Motivation': motivation,
    'Substance': substance,
    'Replicability': replicability,
    'Originality': originality,
    'Soundness': soundness,
    'Clarity': clarity,
    'Meaningful_comparison': meaningful_comparison
}

df = pd.DataFrame(data)

# 计算相关性
for col in df.columns[1:]:
    s = df[col]
    corr, p_value = spearmanr(df['Score'], df[col])
    print(f"Correlation between Score and {col}: {corr:.2f}, p-value: {p_value:.3f}")

# 设置图形大小
plt.figure(figsize=(20, 10))

# 选择要绘制的列
columns_to_plot = ['Summary', 'Motivation', 'Substance', 'Replicability',
                   'Originality', 'Soundness', 'Clarity', 'Meaningful_comparison']

# 创建两行四列的子图布局
fig, axes = plt.subplots(2, 4, figsize=(20, 10))

# 绘制每个方面的散点图
for i, col in enumerate(columns_to_plot):
    row = i // 4  # 计算当前图的位置（行）
    col_idx = i % 4  # 计算当前图的位置（列）
    sns.regplot(x=col, y='Score', data=df, ax=axes[row, col_idx])
    axes[row, col_idx].set_title(f'{col}')

# 调整布局
plt.tight_layout()
plt.suptitle('Scatter plots of Score vs Aspects Mentioned', y=1.02, fontsize=16)
#plt.savefig('iclr_score.png')
plt.show()


data = {
    'Confidence_Score': confidence_score,
    'Summary': summary,
    'Motivation': motivation,
    'Substance': substance,
    'Replicability': replicability,
    'Originality': originality,
    'Soundness': soundness,
    'Clarity': clarity,
    'Meaningful_comparison': meaningful_comparison
}

df = pd.DataFrame(data)

# 计算相关性
for col in df.columns[1:]:
    corr, p_value = spearmanr(df['Confidence_Score'], df[col])
    print(f"Correlation between Confidence Score and {col}: {corr:.2f}, p-value: {p_value:.3f}")

# 设置图形大小
plt.figure(figsize=(20, 10))

# 选择要绘制的列
columns_to_plot = ['Summary', 'Motivation', 'Substance', 'Replicability',
                   'Originality', 'Soundness', 'Clarity', 'Meaningful_comparison']

# 创建两行四列的子图布局
fig, axes = plt.subplots(2, 4, figsize=(20, 10))

# 绘制每个方面的散点图
for i, col in enumerate(columns_to_plot):
    row = i // 4  # 计算当前图的位置（行）
    col_idx = i % 4  # 计算当前图的位置（列）
    sns.regplot(x=col, y='Confidence_Score', data=df, ax=axes[row, col_idx])
    axes[row, col_idx].set_title(f'{col}')

# 调整布局
plt.tight_layout()
plt.suptitle('Scatter plots of Confidence Score vs Aspects Mentioned', y=1.02, fontsize=16)
#plt.savefig('iclr_conf.png')
plt.show()