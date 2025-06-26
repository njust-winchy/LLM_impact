import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ICLR_list = ['ICLR_2017', 'ICLR_2018', 'ICLR_2019', 'ICLR_2020', 'ICLR_2021', 'ICLR_2022', 'ICLR_2023', 'ICLR_2024']
NIPS_list = ['NIPS_2016','NIPS_2017','NIPS_2018','NIPS_2019','NIPS_2021','NIPS_2022','NIPS_2023']
column_names_1 = ['COCA_Academic_Frequency_AW', 'COCA_Academic_Bigram_Frequency', 'COCA_Academic_Trigram_Frequency']
column_names_2 = ['advcl_per_cl', 'nsubj_per_cl', 'mark_per_cl', 'aux_per_cl', 'dobj_per_cl']

ICLR = [[], [], []]
ICLR_2 = [[], [], [], [], []]
NIPS = [[], [], []]
NIPS_2 = [[], [], [], [], []]

for venue in ICLR_list:
    file_name_1 = 'TAALES/$venue_index_coverage.csv'
    file_name_1 = file_name_1.replace('$venue', venue)
    df = pd.read_csv(file_name_1, usecols=column_names_1)
    column_means = df.mean()
    for idx, num in enumerate(column_means):
        ICLR[idx].append(num)

    file_name_2 = 'TAASSC/$venue.csv'
    file_name_2 = file_name_2.replace('$venue', venue)
    df = pd.read_csv(file_name_2, usecols=column_names_2)
    column_means = df.mean()
    for idx, num in enumerate(column_means):
        ICLR_2[idx].append(num)

for venue in NIPS_list:
    file_name_1 = 'TAALES/$venue_index_coverage.csv'
    file_name_1 = file_name_1.replace('$venue', venue)
    df = pd.read_csv(file_name_1, usecols=column_names_1)
    column_means = df.mean()
    for idx, num in enumerate(column_means):
        NIPS[idx].append(num)

    file_name_2 = 'TAASSC/$venue.csv'
    file_name_2 = file_name_2.replace('$venue', venue)
    df = pd.read_csv(file_name_2, usecols=column_names_2)
    column_means = df.mean()
    for idx, num in enumerate(column_means):
        NIPS_2[idx].append(num)

# 数据
years = np.arange(2017, 2025)
labels = [
    'COCA_Academic_Frequency_AW',
    'COCA_Academic_Bigram_Frequency',
    'COCA_Academic_Trigram_Frequency'
]
data = ICLR

# 绘制图形
plt.figure(figsize=(10, 6))

for i, label in enumerate(labels):
    plt.plot(years, data[i], marker='o', label=label)

# 设置图形标题和标签
plt.title('Trend of Lexical Sophistication (ICLR 2017-2024)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Values', fontsize=12)
plt.xticks(years)  # 显示每一年的标记
plt.legend(loc='upper left', fontsize=12)
plt.grid(True)

# 展示图形
plt.tight_layout()
plt.savefig('ICLR_Lexical.png')
plt.show()

years = np.arange(2017, 2025)
labels = ['advcl_per_cl', 'nsubj_per_cl', 'mark_per_cl', 'aux_per_cl', 'dobj_per_cl']
data = ICLR_2

# 绘制图形
plt.figure(figsize=(10, 6))

for i, label in enumerate(labels):
    plt.plot(years, data[i], marker='o', label=label)

# 设置图形标题和标签
plt.title('Trend of Syntactic Sophistication and Complexity (ICLR 2017-2024)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Values', fontsize=12)
plt.xticks(years)  # 显示每一年的标记
plt.legend(loc='upper left', fontsize=12)
plt.grid(True)

# 展示图形
plt.tight_layout()
plt.savefig('ILCR_Syntactic.png')
plt.show()


years = [2016, 2017, 2018, 2019, 2021, 2022, 2023]
labels = [
    'COCA_Academic_Frequency_AW',
    'COCA_Academic_Bigram_Frequency',
    'COCA_Academic_Trigram_Frequency'
]
data = NIPS

# 绘制图形
plt.figure(figsize=(10, 6))

for i, label in enumerate(labels):
    plt.plot(years, data[i], marker='o', label=label)

# 设置图形标题和标签
plt.title('Trend of Lexical Sophistication (NeurIPS 2016-2023)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Values', fontsize=12)
plt.xticks(years)  # 显示每一年的标记
plt.legend(loc='upper left', fontsize=12)
plt.grid(True)

# 展示图形
plt.tight_layout()
plt.savefig('NIPS_Lexical.png')
plt.show()



years = [2016, 2017, 2018, 2019, 2021, 2022, 2023]
labels = ['advcl_per_cl', 'nsubj_per_cl', 'mark_per_cl', 'aux_per_cl', 'dobj_per_cl']
data = NIPS_2

# 绘制图形
plt.figure(figsize=(10, 6))

for i, label in enumerate(labels):
    plt.plot(years, data[i], marker='o', label=label)

# 设置图形标题和标签
plt.title('Trend of Syntactic Sophistication and Complexity (NeurIPS 2016-2023)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Values', fontsize=12)
plt.xticks(years)  # 显示每一年的标记
plt.legend(loc='upper left', fontsize=12)
plt.grid(True)

# 展示图形
plt.tight_layout()
plt.savefig('NIPS_Syntactic.png')
plt.show()