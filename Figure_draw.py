import matplotlib.pyplot as plt
import numpy as np

# ICLR

# # 句子统计
# labels = ['ICLR 2017', 'ICLR 2018', 'ICLR 2019', 'ICLR 2020', 'ICLR 2021', 'ICLR 2022', 'ICLR 2023', 'ICLR 2024']
# values = [15.7, 20.3, 22.4, 23.0, 25.6, 25.5, 24.6, 21.3]
#
# # 画柱状图
# plt.bar(labels, values, color='tab:orange')
# plt.xticks(fontsize=7)
# plt.xlabel('Year')
# plt.ylabel('Value')
# plt.savefig('iclr_sentence.png')
# # 显示图形
# plt.show()
#
#
# # 词数统计
# #labels = ['ICLR 2017', 'ICLR 2018', 'ICLR 2019', 'ICLR 2020', 'ICLR 2021', 'ICLR 2022', 'ICLR 2023', 'ICLR 2024']
# values = [479.1723084, 539.4932112, 565.2680598, 550.8129997, 478.3920548, 470.7306885, 431.1237263, 339.4706275]
# plt.bar(labels, values, color='cyan')
# plt.xticks(fontsize=7)
# plt.xlabel('Year')
# plt.ylabel('Value')
# plt.savefig('iclr_word.png')
# # 显示图形
# plt.show()
#
#
# # 提及方面句子数量
#
# labels = ['ICLR 2017', 'ICLR 2018', 'ICLR 2019', 'ICLR 2020', 'ICLR 2021', 'ICLR 2022', 'ICLR 2023', 'ICLR 2024']
# values = [8.791009216, 11.33949353, 10.32636769, 9.342631213, 8.297425978, 8.059403862, 7.430494905, 6.37917223]
# plt.bar(labels, values)
# plt.xticks(fontsize=7)
# plt.xlabel('Year')
# plt.ylabel('Value')
# plt.savefig('iclr_aspect_sent.png')
# # 显示图形
# plt.show()
#
#
# # 方面词频
# values = [223.7470892, 274.5449353, 254.4584018, 215.198992, 189.2758518, 182.761335, 168.9461426, 143.8471295]
# plt.bar(labels, values)
# plt.xticks(fontsize=7)
# # 显示图形
# plt.xlabel('Year')
# plt.ylabel('Value')
# plt.savefig('iclr_aspect_word.png')
# plt.show()
#
#
# 方面平均分布
# data = np.array([
#     [0.75834, 0.83712, 0.13952, 1.02336, 0.53471, 0.65621, 0.40654, 2.75434],  # 2017
#     [0.79367, 1.11972, 0.21470, 1.08624, 0.54403, 0.66776, 0.45670, 3.33406],  # 2018
#     [0.84614, 1.25840, 0.23992, 1.22586, 0.55647, 0.74727, 0.51763, 3.48678],  # 2019
#     [0.74498, 1.16828, 0.22214, 1.16530, 0.56137, 0.75167, 0.49635, 3.98616],  # 2020
#     [0.90954, 1.33568, 0.25643, 1.41067, 0.70238, 0.89790, 0.55344, 4.14381],  # 2021
#     [1.24834, 1.52845, 0.25875, 1.62041, 0.78227, 1.02387, 0.58958, 4.72873],  # 2022
#     [1.79122, 2.18761, 0.61013, 1.91051, 0.87683, 1.30857, 0.61105, 4.32495],  # 2023
#     [0.71158, 1.19416, 0.26298, 1.20503, 0.55680, 1.00886, 0.50636, 4.68946],  # 2024
# ])
#
# # 年份
# years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
#
# # 类别标签
# categories = ['originality', 'clarity', 'replicability', 'soundness', 'motivation', 'substance', 'meaningful_comparison', 'summary']
# fig, ax = plt.subplots(figsize=(14, 8))
#
# # Create bar width and positions
# bar_width = 0.1
# bar_positions = np.arange(len(categories))
#
# # Plot bars for each year
# for i, year in enumerate(years):
#     ax.bar(bar_positions + i * bar_width, data[i], bar_width, label=year)
#
# # Add labels, title, and legend
# ax.set_xlabel('Aspects')
# ax.set_ylabel('Value')
# ax.set_title('ICLR Distribution across 8 aspects over different years')
# ax.set_xticks(bar_positions + bar_width * (len(years) - 1) / 2)
# ax.set_xticklabels(categories)
# ax.legend(fontsize=12)
# plt.xticks(fontsize=10)
# plt.savefig('iclr_aspect.png')
# plt.show()
#
#
# # 方面情感极性分布
# data = np.array([
# [[0.40454,0.35381], [0.39956,0.39410], [0.42695,0.41919], [0.36483,0.38015], [0.46463,0.44491], [0.69351,0.55483], [0.93610,0.85512], [0.38863,0.32295]], # asp1
# [[0.34579,0.49132], [0.42795,0.69178], [0.48048,0.77792], [0.42315,0.74513], [0.53667,0.79901], [0.66667,0.86178], [1.17284,1.01476], [0.55491,0.63924]], # asp2
# [[0.00401,0.13551], [0.00655,0.20815], [0.00819,0.23174], [0.00908,0.21306], [0.01495,0.24148], [0.01753,0.24121], [0.09908,0.51105], [0.01798,0.24500]], # asp3
# [[0.41923,0.60414], [0.39338,0.69287], [0.44626,0.77960], [0.44086,0.72445], [0.54293,0.86774], [0.68130,0.93911], [0.88006,1.03044], [0.48393,0.72111]], # asp4
# [[0.39920,0.13551], [0.39410,0.14993], [0.38812,0.16835], [0.40411,0.15727], [0.52051,0.18187], [0.59224,0.19003], [0.64547,0.23136], [0.42733,0.12947]], # asp5
# [[0.15888,0.49733], [0.15648,0.51128], [0.18871,0.55856], [0.20161,0.55007], [0.26269,0.63521], [0.34046,0.68342], [0.49564,0.81293], [0.34898,0.65988]], # asp6
# [[0.03471,0.37183], [0.05131,0.40539], [0.04807,0.46956], [0.04999,0.44636], [0.06509,0.48836], [0.05330,0.53628], [0.07020,0.54084], [0.05556,0.45080]] # asp7
# ])
# # 年份
# years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
#
# # 类别标签
# categories = ['originality', 'clarity', 'replicability', 'soundness', 'motivation', 'substance', 'meaningful_comparison']
#
# # 绘制多线图
# plt.figure(figsize=(12, 6))
# colors = plt.cm.tab10(np.linspace(0, 1, len(categories)))
#
# # 绘制每个类别的正负极性变化
# for i in range(len(categories)):
#     plt.plot(years, data[i, :, 0], label=f'{categories[i]} Positive', linestyle='-', color=colors[i])
#     plt.plot(years, data[i, :, 1], label=f'{categories[i]} Negative', linestyle='--', color=colors[i])
#
# plt.xlabel('Year')
# plt.ylabel('Sentiment Polarity')
# plt.title('ICLR Sentiment Polarity Distribution from 2017 to 2024')
# plt.legend(bbox_to_anchor=(0.03, 1.0), loc='upper left', ncol=2, fontsize=10)
# plt.savefig('iclr_sentiment.png')
# plt.show()


#
# confidence = 1, asp
data = np.array([
    [0.28571, 1.42857, 0.28571, 0.57143, 0.42857, 0.00000, 0.00000, 1.28571], # 2017
    [0.26471, 0.76471, 0.20588, 0.55882, 0.29412, 0.23529, 0.08824, 2.32353], # 2018
    [0.42500, 1.20000, 0.12500, 0.85000, 0.47500, 0.25000, 0.10000, 2.15000], # 2019
    [0.55435, 1.01087, 0.04348, 0.80435, 0.58696, 0.34783, 0.13043, 3.04348], # 2021
    [0.94118, 1.52941, 0.17647, 0.94118, 0.58824, 0.52941, 0.11765, 3.00000], # 2022
    [0.94253, 1.42529, 0.20690, 0.96552, 0.39080, 0.50575, 0.18391, 2.48276], # 2023
    [0.41593, 0.90265, 0.07965, 0.70796, 0.47788, 0.52212, 0.14159, 3.52212] # 2024
])
# 年份
years = [2017, 2018, 2019, 2021, 2022, 2023, 2024]
data_T = np.array(data).T
# 类别标签
categories = ['originality', 'clarity', 'replicability', 'soundness', 'motivation', 'substance', 'meaningful_comparison', 'summary']
# 绘制堆积面积图
plt.figure(figsize=(10, 6))
for i, category in enumerate(categories):
    plt.plot(years, data_T[i], marker='o', label=category)
plt.grid(True)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Reviewer\'s Confidence Score is 1.')
plt.legend(loc='upper left', fontsize=12)
plt.xticks(years)
plt.savefig('iclr_aspect_conf1.png')
plt.show()



# confidence = 2, asp
data = np.array([
    [0.49020, 0.96078, 0.11765, 0.66667, 0.43137, 0.31373, 0.21569, 1.68627], # 2017
    [0.60769, 1.36923, 0.20769, 0.89231, 0.50769, 0.47692, 0.31538, 3.13846], # 2018
    [0.64364, 1.34545, 0.20000, 0.84727, 0.46182, 0.54909, 0.29818, 2.89818], # 2019
    [0.65991, 1.33541, 0.15133, 1.09828, 0.55226, 0.64275, 0.34945, 3.62871], # 2021
    [1.03528, 1.60429, 0.25767, 1.38037, 0.68405, 0.81902, 0.44479, 3.93712], # 2022
    [1.43035, 2.12243, 0.48094, 1.57991, 0.81452, 0.93622, 0.37243, 3.78519], # 2023
    [0.58237, 1.15323, 0.21947, 1.01555, 0.50461, 0.75115, 0.34850, 4.24539] # 2024
])
# 年份
years = [2017, 2018, 2019, 2021, 2022, 2023, 2024]
data_T = np.array(data).T
# 类别标签
categories = ['originality', 'clarity', 'replicability', 'soundness', 'motivation', 'substance', 'meaningful_comparison', 'summary']
# 绘制堆积面积图
plt.figure(figsize=(10, 6))
for i, category in enumerate(categories):
    plt.plot(years, data_T[i], marker='o', label=category)
plt.grid(True)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Reviewer\'s Confidence Score is 2.')
plt.legend(loc='upper left', fontsize=12)
plt.xticks(years)
plt.savefig('iclr_aspect_conf2.png')
plt.show()



# confidence = 3, asp
data = np.array([
    [0.66150, 0.87597, 0.14729, 1.01809, 0.52455, 0.56072, 0.35401, 2.77003], # 2017
    [0.72254, 1.21098, 0.22688, 0.99277, 0.52168, 0.59538, 0.38295, 3.48121], # 2018
    [0.71590, 1.20743, 0.21872, 1.15093, 0.55529, 0.64084, 0.41889, 3.36965], # 2019
    [0.81755, 1.39766, 0.22633, 1.29336, 0.69732, 0.81665, 0.45807, 3.99128], # 2021
    [1.29766, 1.62467, 0.20223, 1.49538, 0.75278, 0.83708, 0.39924, 5.16671], # 2022
    [1.69969, 2.24305, 0.59157, 1.86589, 0.87510, 1.22593, 0.51670, 4.30969], # 2023
    [0.66357, 1.22163, 0.25488, 1.17096, 0.55806, 0.92434, 0.41668, 4.68006] # 2024
])
# 年份
years = [2017, 2018, 2019, 2021, 2022, 2023, 2024]
data_T = np.array(data).T
# 类别标签
categories = ['originality', 'clarity', 'replicability', 'soundness', 'motivation', 'substance', 'meaningful_comparison', 'summary']
# 绘制堆积面积图
plt.figure(figsize=(10, 6))
for i, category in enumerate(categories):
    plt.plot(years, data_T[i], marker='o', label=category)
plt.grid(True)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Reviewer\'s Confidence Score is 3.')
plt.legend(loc='upper left', fontsize=12)
plt.xticks(years)
plt.savefig('iclr_aspect_conf3.png')
plt.show()


# confidence = 4, asp
data = np.array([
    [0.79104, 0.83085, 0.13682, 1.03856, 0.52861, 0.69279, 0.41294, 2.81468], # 2017
    [0.80661, 1.10784, 0.21136, 1.14522, 0.57369, 0.73616, 0.47520, 3.40834], # 2018
    [0.92094, 1.29563, 0.24979, 1.31119, 0.56939, 0.80193, 0.53827, 3.62868], # 2019
    [0.93285, 1.31902, 0.27289, 1.49590, 0.72319, 0.95600, 0.57944, 4.29320], # 2021
    [1.20488, 1.49609, 0.27940, 1.70005, 0.81460, 1.09048, 0.66232, 4.58641], # 2022
    [1.86685, 2.18796, 0.63853, 1.99496, 0.89722, 1.38725, 0.66073, 4.44665], # 2023
    [0.75396, 1.19822, 0.27098, 1.25817, 0.57119, 1.07618, 0.55662, 4.80149] # 2024
])
# 年份
years = [2017, 2018, 2019, 2021, 2022, 2023, 2024]
data_T = np.array(data).T
# 类别标签
categories = ['originality', 'clarity', 'replicability', 'soundness', 'motivation', 'substance', 'meaningful_comparison', 'summary']
# 绘制堆积面积图
plt.figure(figsize=(10, 6))
for i, category in enumerate(categories):
    plt.plot(years, data_T[i], marker='o', label=category)
plt.grid(True)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Reviewer\'s Confidence Score is 4.')
plt.legend(loc='upper left', fontsize=12)
plt.xticks(years)
plt.savefig('iclr_aspect_conf4.png')

plt.show()



# confidence = 5, asp
data = np.array([
    [0.87149, 0.75502, 0.13655, 1.06827, 0.59438, 0.77510, 0.51807, 2.79518], # 2017
    [0.94012, 0.98603, 0.20958, 1.13772, 0.51896, 0.65669, 0.56886, 3.04391], # 2018
    [0.91346, 1.20192, 0.26202, 1.23678, 0.55649, 0.83894, 0.69832, 3.51442], # 2019
    [1.11014, 1.29062, 0.30807, 1.50218, 0.70611, 0.98419, 0.73937, 4.19847], # 2021
    [1.40909, 1.34897, 0.33651, 1.75000, 0.76833, 1.38783, 0.90616, 4.45308], # 2022
    [2.00332, 2.10000, 0.64360, 1.93460, 0.85592, 1.48768, 0.84455, 4.27915], # 2023
    [0.78704, 1.13591, 0.29316, 1.24536, 0.53418, 1.19044, 0.69854, 4.62189] # 2024
])
# 年份
years = [2017, 2018, 2019, 2021, 2022, 2023, 2024]
data_T = np.array(data).T
# 类别标签
categories = ['originality', 'clarity', 'replicability', 'soundness', 'motivation', 'substance', 'meaningful_comparison', 'summary']
# 绘制堆积面积图
plt.figure(figsize=(10, 6))
for i, category in enumerate(categories):
    plt.plot(years, data_T[i], marker='o', label=category)
plt.grid(True)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Reviewer\'s Confidence Score is 5.')
plt.legend(loc='upper left', fontsize=12)
plt.xticks(years)
plt.savefig('iclr_aspect_conf5.png')
plt.show()




# confidence sentiment distribution
# 定义年份和数据
years = [2017, 2018, 2019, 2021, 2022, 2023, 2024]


confidence_scores = [1, 2, 3, 4, 5]
positive_polarity = [
    [1.28571,1.39216,1.80362,1.79229,1.71486], # 2017
    [1.00000,1.88462,1.89595,1.91373,1.54491], # 2018
    [2.02500,1.83636,2.01211,2.06056,1.78606], # 2019
    [2.02174,2.05460,2.49564,2.43890,2.29389], # 2021
    [2.05882,2.83742,3.24201,3.02162,2.65836], # 2022
    [2.48276,3.89809,4.44792,4.35934,3.95261], # 2023
    [1.71681,2.05472,2.30580,2.32486,2.17701] # 2024
]
negative_polarity = [
    [1.71429,1.80392,2.33850,2.63930,3.00402], # 2017
    [1.41176,2.49231,2.75723,3.14234,3.47305], # 2018
    [1.40000,2.50909,2.89588,3.62658,3.92188], # 2019
    [1.45652,2.73479,3.21130,3.84040,4.34678], # 2021
    [2.76471,3.38804,3.36704,4.22619,5.24853], # 2022
    [2.13793,3.83871,4.57002,5.27415,5.91706], # 2023
    [1.53097,2.52016,2.90431,3.36045,3.70763] # 2024
]

# 置信分数年份变化
# 转置数据以便按置信度分数绘图
positive_polarity_transposed = list(zip(*positive_polarity))
negative_polarity_transposed = list(zip(*negative_polarity))

# 创建图形和坐标轴
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

# 绘制正向极性
for i, score in enumerate(confidence_scores):
    ax[0].plot(years, positive_polarity_transposed[i], marker='o', label=f'Confidence Score {score}')

# 绘制负向极性
for i, score in enumerate(confidence_scores):
    ax[1].plot(years, negative_polarity_transposed[i], marker='o', label=f'Confidence Score {score}')

# 添加标题和标签
ax[0].set_title('Positive Polarity over Years')
ax[0].set_xlabel('Years')
ax[0].set_ylabel('Positive Polarity')
ax[0].legend(fontsize=12)

ax[1].set_title('Negative Polarity over Years')
ax[1].set_xlabel('Years')
ax[1].set_ylabel('Negative Polarity')
ax[1].legend(fontsize=12)
ax[0].xaxis.set_major_locator(plt.MaxNLocator(integer=True))
ax[1].xaxis.set_major_locator(plt.MaxNLocator(integer=True))
# 显示图表
plt.tight_layout()
plt.savefig('iclr_sentiment_conf.png')
plt.show()
#
#
# confidence sentence
# 定义年份和数据
years = [2017, 2018, 2019, 2021, 2022, 2023, 2024] # 2017年到2024年
confidence_scores = [1, 2, 3, 4, 5]
sentence_counts = [
    [11.57143,11.88235,14.66925,15.88433,17.34538],
    [9.76471,15.90000,19.04046,21.04889,21.74451],
    [10.75000,16.59273,19.46005,23.83137,25.21875],
    [13.70652,18.80343,23.05500,26.88279,28.94438],
    [11.17647,19.35276,23.68648,26.48474,29.16789],
    [10.41379,18.47067,22.93006,26.23257,27.03223],
    [11.81416,16.63018,20.05105,22.60190,23.61241]
]

# 定义X轴位置
bar_width = 0.15
x = np.arange(len(years))

# 创建图形
fig, ax = plt.subplots(figsize=(14, 7))

# 绘制柱状图
for i in range(len(confidence_scores)):
    ax.bar(x + i * bar_width, [row[i] for row in sentence_counts], bar_width, label=f'Confidence Score {confidence_scores[i]}')

# 添加标题和标签
ax.set_title('Number of Sentences by Confidence Score (1-5) in 2017-2024 (except 2020)')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Sentences')
ax.set_xticks(x + 2 * bar_width)
ax.set_xticklabels(years, fontsize=10)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1, fontsize=12)

# 显示图形
plt.tight_layout()
plt.savefig('iclr_sentence_conf.png')
plt.show()

# confidence word
# 定义年份和数据
years = [2017, 2018, 2019, 2021, 2022, 2023, 2024] # 2017年到2024年
confidence_scores = [1, 2, 3, 4, 5]
word_counts = [
    [263.42857,259.35294,315.01034,348.98632,365.30924],
    [207.50000,336.59231,403.77746,446.86341,464.90020],
    [213.35000,346.25455,407.82486,503.08495,525.45192],
    [298.64130,410.51950,501.95071,581.74955,606.43730],
    [288.58824,431.89571,523.06488,592.02101,635.23167],
    [236.33333,413.64956,511.71351,573.21453,570.76398],
    [280.82301,388.20565,459.29088,504.11676,509.64401]
]

# 定义X轴位置
bar_width = 0.15
x = np.arange(len(years))

# 创建图形
fig, ax = plt.subplots(figsize=(14, 7))

# 绘制柱状图
for i in range(len(confidence_scores)):
    ax.bar(x + i * bar_width, [row[i] for row in word_counts], bar_width, label=f'Confidence Score {confidence_scores[i]}')

# 添加标题和标签
ax.set_title('Number of words by Confidence Score (1-5) in 2017-2024 (except 2020)')
ax.set_xlabel('Year')
ax.set_ylabel('Number of words')
ax.set_xticks(x + 2 * bar_width)
ax.set_xticklabels(years, fontsize=10)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1, fontsize=12)

# 显示图形
plt.tight_layout()
plt.savefig('iclr_word_conf.png')

plt.show()

# NIPS
#
# # 句子统计
# labels = ['NIPS 2016', 'NIPS 2017', 'NIPS 2018', 'NIPS 2019', 'NIPS 2021', 'NIPS 2022', 'NIPS 2023']
# values = [17.59220861, 17.7985574446161, 21.884207033842, 18.9515636021631, 23.5673408518967, 22.6672797676669, 21.1208885373409]
#
# # 画柱状图
# plt.bar(labels, values, color='tab:orange')
# plt.xticks(fontsize=10)
# plt.xlabel('Year')
# plt.ylabel('Value')
# plt.savefig('NIPS_sentence.png')
# # 显示图形
# plt.show()
#
# # 词数统计
# labels = ['NIPS 2016', 'NIPS 2017', 'NIPS 2018', 'NIPS 2019', 'NIPS 2021', 'NIPS 2022', 'NIPS 2023']
# values = [383.297518064718, 383.063884595569, 478.542468480424, 402.557959087702, 529.55093671358, 515.822362052274, 494.525410322325]
# plt.bar(labels, values, color='cyan')
#
# plt.xticks(fontsize=10)
# plt.xlabel('Year')
# plt.ylabel('Value')
# plt.savefig('NIPS_word.png')
#
# # 显示图形
# plt.show()
#
# # 提及方面句子数量
# labels = ['NIPS 2016', 'NIPS 2017', 'NIPS 2018', 'NIPS 2019', 'NIPS 2021', 'NIPS 2022', 'NIPS 2023']
#
# values = [7.22871504869619, 7.06646058732612, 8.48009289980093, 6.92076181518927, 9.35501910709292, 9.17386253630203, 9.01773119767978]
# plt.bar(labels, values)
# plt.xticks(fontsize=10)
# plt.xlabel('Year')
# plt.ylabel('Value')
# plt.savefig('NIPS_aspect_sent.png')
# # 显示图形
# plt.show()
# #
# #
# # 方面词频
# values = [171.771599120326, 163.18134981968, 197.21400132714, 154.32024453327, 230.733059931028, 226.917231364956, 235.718014633181]
# plt.bar(labels, values)
# plt.xticks(fontsize=10)
# plt.xlabel('Year')
# plt.ylabel('Value')
# plt.savefig('NIPS_aspect_word.png')
# # 显示图形
# plt.show()
#
# 方面平均分布
# data = np.array([
#     [0.66478, 1.05184, 0.15269, 0.94345, 0.51084, 0.49513, 0.28118, 3.99717],  # 2016
#     [0.64863,1.07316,0.13189,0.94333,0.53426,0.45956,0.31942,3.67903],  # 2017
#     [0.82614,1.35999,0.18912,1.18248,0.65627,0.62210,0.36729,4.13935],  # 2018
#     [0.95391,1.41853,0.16671,1.14860,0.67834,0.55772,0.38796,2.42464],  # 2019
#     [0.98714,1.41523,0.18669,1.33330,0.74443,0.77854,0.45466,4.69979],  # 2021
#     [0.87018,1.32749,0.20862,1.40019,0.68006,0.95963,0.44008,4.46341],  # 2022
#     [0.70622,1.25021,0.23571,1.31178,0.61057,0.98530,0.44427,4.90271]  # 2023
# ])
#
# # 年份
# years = [2016, 2017, 2018, 2019, 2021, 2022, 2023]
#
# # 类别标签
# categories = ['originality', 'clarity', 'replicability', 'soundness', 'motivation', 'substance', 'meaningful_comparison', 'summary']
# fig, ax = plt.subplots(figsize=(14, 8))
#
# # Create bar width and positions
# bar_width = 0.1
# bar_positions = np.arange(len(categories))
#
# # Plot bars for each year
# for i, year in enumerate(years):
#     ax.bar(bar_positions + i * bar_width, data[i], bar_width, label=year)
#
# # Add labels, title, and legend
# ax.set_xlabel('Aspects')
# ax.set_ylabel('Value')
# ax.set_title('NeurIPS Distribution across 8 categories over different years')
# ax.set_xticks(bar_positions + bar_width * (len(years) - 1) / 2, fontsize=10)
# ax.set_xticklabels(categories)
# ax.legend(fontsize=12)
# plt.savefig('NIPS_aspect.png')
# plt.show()
#
# # 方面情感极性分布
# data = np.array([
# [[0.44298,0.22180], [0.43946,0.20917], [0.55740,0.26875], [0.64378,0.31013], [0.64256,0.34458], [0.54685,0.32333], [0.46127,0.24494]], # asp1
# [[0.52152,0.53032], [0.57651,0.49665], [0.72163,0.63835], [0.84858,0.56995], [0.80157,0.61366], [0.72265,0.60484], [0.68295,0.56727]], # asp2
# [[0.00880,0.14389], [0.00979,0.12210], [0.01659,0.17253], [0.01787,0.14884], [0.02097,0.16572], [0.01830,0.19032], [0.02017,0.21554]], # asp3
# [[0.48822,0.45523], [0.53581,0.40752], [0.67352,0.50896], [0.66541,0.48319], [0.74313,0.59018], [0.71530,0.68490], [0.61796,0.69382]], # asp4
# [[0.41282,0.09802], [0.44101,0.09325], [0.54512,0.11115], [0.56313,0.11521], [0.60537,0.13906], [0.52652,0.15353], [0.48131,0.12926]], # asp5
# [[0.15960,0.33553], [0.14374,0.31582], [0.20372,0.41838], [0.19116,0.36656], [0.32715,0.45139], [0.39138,0.56825], [0.35640,0.62890]], # asp6
# [[0.04461,0.23657], [0.06131,0.25811], [0.07001,0.29728], [0.10275,0.28521], [0.10607,0.34859], [0.07909,0.36099], [0.06704,0.37723]] # asp7
# ])
# # 年份
# years = [2016, 2017, 2018, 2019, 2021, 2022, 2023]
# colors = plt.cm.tab10(np.linspace(0, 1, len(categories)))
# # 类别标签
# categories = ['originality', 'clarity', 'replicability', 'soundness', 'motivation', 'substance', 'meaningful_comparison']
#
# # 绘制多线图
# plt.figure(figsize=(12, 6))
#
# # 绘制每个类别的正负极性变化
# for i in range(len(categories)):
#     plt.plot(years, data[i, :, 0], label=f'{categories[i]} Positive', linestyle='-', color=colors[i])
#     plt.plot(years, data[i, :, 1], label=f'{categories[i]} Negative', linestyle='--', color=colors[i])
#
# plt.xlabel('Year')
# plt.ylabel('Sentiment Polarity')
# plt.title('NeurIPS Sentiment Polarity Distribution from 2016 to 2023')
# plt.legend(bbox_to_anchor=(0.03, 1.0), loc='upper left', ncol=2, fontsize=10)
# plt.xticks(years, fontsize=10)
# plt.savefig('NIPS_sentiment.png')
# plt.show()


# confidence = 1, asp
data = np.array([
    [0.62000,1.38000,0.09000,0.80000,0.54000,0.29000,0.18000,3.41000], # 2021
    [0.51807,1.19277,0.12048,0.89759,0.45181,0.39759,0.18675,3.27711], # 2022
    [0.39114,0.99631,0.12177,1.04797,0.45756,0.64207,0.23616,3.76015] # 2023
])
# 年份
years = [2021, 2022, 2023]
data_T = np.array(data).T
# 类别标签
categories = ['originality', 'clarity', 'replicability', 'soundness', 'motivation', 'substance', 'meaningful_comparison', 'summary']
# 绘制堆积面积图
plt.figure(figsize=(10, 6))
for i, category in enumerate(categories):
    plt.plot(years, data_T[i], marker='o', label=category)
plt.grid(True)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Reviewer\'s Confidence Score is 1.')
plt.legend(loc='upper left', fontsize=12)
plt.xticks(years, fontsize=10)
plt.savefig('NIPS_aspect_conf1.png')
plt.show()



# confidence = 2, asp
data = np.array([
    [0.71365,1.33680,0.11721,1.10386,0.63501,0.49852,0.29674,4.09199], # 2021
    [0.68107,1.31075,0.14720,1.18808,0.62617,0.69860,0.26168,3.96963], # 2022
    [0.56839,1.23024,0.17173,1.15729,0.53419,0.76292,0.32371,4.30395] # 2023
])
# 年份
years = [2021, 2022, 2023]
data_T = np.array(data).T
# 类别标签
categories = ['originality', 'clarity', 'replicability', 'soundness', 'motivation', 'substance', 'meaningful_comparison', 'summary']
# 绘制堆积面积图
plt.figure(figsize=(10, 6))
for i, category in enumerate(categories):
    plt.plot(years, data_T[i], marker='o', label=category)
plt.grid(True)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Reviewer\'s Confidence Score is 2.')
plt.legend(loc='upper left', fontsize=12)
plt.xticks(years, fontsize=10)
plt.savefig('NIPS_aspect_conf2.png')
plt.show()


# confidence = 3, asp
data = np.array([
    [0.91783,1.45864,0.16490,1.31219,0.73896,0.68306,0.39687,4.68334], # 2021
    [0.83398,1.34012,0.17997,1.33175,0.67048,0.83231,0.38895,4.40011], # 2022
    [0.65730,1.29644,0.21196,1.30562,0.60302,0.88073,0.37615,4.90080] # 2023
])
# 年份
years = [2021, 2022, 2023]
data_T = np.array(data).T
# 类别标签
categories = ['originality', 'clarity', 'replicability', 'soundness', 'motivation', 'substance', 'meaningful_comparison', 'summary']
# 绘制堆积面积图
plt.figure(figsize=(10, 6))
for i, category in enumerate(categories):
    plt.plot(years, data_T[i], marker='o', label=category)
plt.grid(True)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Reviewer\'s Confidence Score is 3.')
plt.legend(loc='upper left', fontsize=12)
plt.xticks(years, fontsize=10)
plt.savefig('NIPS_aspect_conf3.png')
plt.show()



# confidence = 4, asp
data = np.array([
    [1.05384,1.42667,0.20861,1.39695,0.76920,0.84601,0.48128,4.80413], # 2021
    [0.91263,1.34061,0.23897,1.46799,0.70545,1.05666,0.48875,4.62284], # 2022
    [0.75476,1.24389,0.25469,1.34603,0.63207,1.05715,0.48433,5.04710] # 2023
])
# 年份
years = [2021, 2022, 2023]
data_T = np.array(data).T
# 类别标签
categories = ['originality', 'clarity', 'replicability', 'soundness', 'motivation', 'substance', 'meaningful_comparison', 'summary']
# 绘制堆积面积图
plt.figure(figsize=(10, 6))
for i, category in enumerate(categories):
    plt.plot(years, data_T[i], marker='o', label=category)
plt.grid(True)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Reviewer\'s Confidence Score is 4.')
plt.legend(loc='upper left', fontsize=12)
plt.xticks(years, fontsize=10)
plt.savefig('NIPS_aspect_conf4.png')
plt.show()

# confidence = 5, asp
data = np.array([
    [1.09038,1.28285,0.20418,1.29456,0.73222,0.97071,0.62427,4.74728], # 2021
    [1.01000,1.26455,0.23545,1.57909,0.68091,1.25455,0.57909,4.56273], # 2022
    [0.82433,1.18813,0.30267,1.35846,0.63323,1.25460,0.62493,4.98872] # 2023
])
# 年份
years = [2021, 2022, 2023]
data_T = np.array(data).T
# 类别标签
categories = ['originality', 'clarity', 'replicability', 'soundness', 'motivation', 'substance', 'meaningful_comparison', 'summary']
# 绘制堆积面积图
plt.figure(figsize=(10, 6))
for i, category in enumerate(categories):
    plt.plot(years, data_T[i], marker='o', label=category)
plt.grid(True)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Reviewer\'s Confidence Score is 5.')
plt.legend(loc='upper left', fontsize=12)
plt.xticks(years, fontsize=10)
plt.savefig('NIPS_aspect_conf5.png')
plt.show()


# confidence sentiment distribution
# 定义年份和数据
years = [2021, 2022, 2023]


confidence_scores = [1, 2, 3, 4, 5]
positive_polarity = [
    [2.22000,2.82789,3.23253,3.35237,3.15397], # 2021
    [1.92771,2.51402,2.92606,3.11116,3.31455], # 2022
    [2.07011,2.31763,2.65979,2.77321,2.81899] # 2023
]
negative_polarity = [
    [1.68000,1.87389,2.43991,2.83018,3.04519], # 2021
    [1.83735,2.39953,2.65151,3.09991,3.28909], # 2022
    [1.82288,2.43085,2.67144,2.99970,3.36736] # 2023

]
# 置信分数年份变化
# 转置数据以便按置信度分数绘图
positive_polarity_transposed = list(zip(*positive_polarity))
negative_polarity_transposed = list(zip(*negative_polarity))

# 创建图形和坐标轴
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

# 绘制正向极性
for i, score in enumerate(confidence_scores):
    ax[0].plot(years, positive_polarity_transposed[i], marker='o', label=f'Confidence Score {score}')

# 绘制负向极性
for i, score in enumerate(confidence_scores):
    ax[1].plot(years, negative_polarity_transposed[i], marker='o', label=f'Confidence Score {score}')

# 添加标题和标签
ax[0].set_title('Positive Polarity over Years')
ax[0].set_xlabel('Years')
ax[0].set_ylabel('Positive Polarity')
ax[0].legend(fontsize=12)

ax[1].set_title('Negative Polarity over Years')
ax[1].set_xlabel('Years')
ax[1].set_ylabel('Negative Polarity')
ax[1].legend(fontsize=12)
ax[0].xaxis.set_major_locator(plt.MaxNLocator(integer=True))
ax[1].xaxis.set_major_locator(plt.MaxNLocator(integer=True))
# 显示图表
plt.tight_layout()
plt.savefig('NIPS_sentiment_conf.png')
plt.show()


# confidence sentence
# 定义年份和数据
years = [2021, 2022, 2023]
confidence_scores = [1, 2, 3, 4, 5]
sentence_counts = [
    [14.72000,17.37240,22.03102,24.95677,26.37657],
    [12.87952,18.00350,21.03265,24.50065,25.39273],
    [11.94834,16.29331,20.26529,22.47263,23.67478]
]

# 定义X轴位置
bar_width = 0.15
x = np.arange(len(years))

# 创建图形
fig, ax = plt.subplots(figsize=(14, 7))

# 绘制柱状图
for i in range(len(confidence_scores)):
    ax.bar(x + i * bar_width, [row[i] for row in sentence_counts], bar_width, label=f'Confidence Score {confidence_scores[i]}')

# 添加标题和标签
ax.set_title('Number of Sentences by Confidence Score (1-5) in 2021-2023')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Sentences')
ax.set_xticks(x + 2 * bar_width)
ax.set_xticklabels(years, fontsize=10)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1, fontsize=12)

# 显示图形
plt.tight_layout()
plt.savefig('NIPS_sentence_conf.png')
plt.show()

# confidence word
# 定义年份和数据
years = [2021, 2022, 2023] # 2017年到2024年
confidence_scores = [1, 2, 3, 4, 5]
word_counts = [
    [322.20000,398.53412,500.28200,560.34794,574.88536],
    [311.02410,418.36565,483.39202,558.27682,549.76818],
    [291.36531,395.60866,484.59289,521.48478,528.62611]
]

# 定义X轴位置
bar_width = 0.15
x = np.arange(len(years))

# 创建图形
fig, ax = plt.subplots(figsize=(14, 7))

# 绘制柱状图
for i in range(len(confidence_scores)):
    ax.bar(x + i * bar_width, [row[i] for row in word_counts], bar_width, label=f'Confidence Score {confidence_scores[i]}')

# 添加标题和标签
ax.set_title('Number of words by Confidence Score (1-5) in 2021-2023')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Sentences')
ax.set_xticks(x + 2 * bar_width)
ax.set_xticklabels(years)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1, fontsize=12)

# 显示图形
plt.tight_layout()
plt.savefig('NIPS_word_conf.png')
plt.show()
