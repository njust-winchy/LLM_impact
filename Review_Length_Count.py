import json
import os
import nltk
import numpy
from tqdm import tqdm
# total_length, every_aspect_sentence_length, average number of aspect, different score
asp_label = ['originality', 'clarity', 'replicability', 'soundness', 'motivation', 'substance', 'meaningful', 'summary']
sentiment = ['positive', 'negative']

word_len_list = []
asp_sent_list = []
sent_len_list = []
asp_word_list = []
aspect_list = []
sentiment_list = []
confidence_asp_list = []
confidence_sentiment_list = []
confidence_sentence_list = []
confidence_word_list = []
confidence_count = numpy.zeros(5)
save_dict = {}


def rev_count(venue_name):
    with open(venue_name + '.json') as f:
        data = json.load(f)
        for da in tqdm(data):
            for rev in da['rev']:
                asp_count = numpy.zeros(8)
                confidence_word = numpy.zeros(5)
                confidence_sentence = numpy.zeros(5)
                sentiment_distribution = numpy.zeros([7, 2])
                confidence_asp_distribution = numpy.zeros([8, 5])
                confidence_sentiment_distribution = numpy.zeros([5, 2])
                sent_len = len(rev['rev_with_aspects'])
                word_len = 0
                asp_sent_count = 0
                asp_word_count = 0
                for rev_sent in rev['rev_with_aspects']:
                    sentence = rev_sent[-1]
                    word_len += len(nltk.word_tokenize(sentence))
                    if 'O' in rev_sent and len(rev_sent)>2:
                        # 方面句子的数量
                        asp_sent_count += 1
                        # 方面句子长度统计
                        asp_word_count += len(nltk.word_tokenize(rev_sent[-1]))
                    elif 'O' not in rev_sent or len(rev_sent) > 2:
                        # 方面句子的数量
                        asp_sent_count += 1
                        # 方面句子长度统计
                        asp_word_count += len(nltk.word_tokenize(rev_sent[-1]))
                    for x in rev_sent:
                        asp_sp = x.split('_')
                        if asp_sp[0] in asp_label:
                            if 'confidence' in rev:
                                # 不同置信分数提及方面的次数
                                confidence = int(rev['confidence'][0]) - 1
                                confidence_asp_distribution[asp_label.index(asp_sp[0]), confidence] += 1
                                if asp_sp[0] != 'summary':
                                    # 不同置信分数情感分布次数
                                    confidence_sentiment_distribution[confidence, sentiment.index(asp_sp[-1])] += 1
                            # 提及各个方面的次数
                            asp_count[asp_label.index(asp_sp[0])] += 1
                            # 方面情感极性统计
                            if x != 'summary':
                                sentiment_distribution[asp_label.index(asp_sp[0]), sentiment.index(asp_sp[-1])] += 1
                if 'confidence' in rev:
                    confidence = int(rev['confidence'][0]) - 1
                    # 不同置信分数词统计
                    confidence_word[confidence] += word_len
                    # 不同置信分数句子统计
                    confidence_sentence[confidence] += sent_len
                    confidence_count[confidence] += 1
                # 句子数量统计
                sent_len_list.append(sent_len)
                # 词的数量统计
                word_len_list.append(word_len)
                # 方面句子数量统计
                asp_sent_list.append(asp_sent_count)
                # 方面句子长度统计
                asp_word_list.append(asp_word_count)
                # 方面数量统计
                aspect_list.append(asp_count)
                # 情感极性分布
                sentiment_list.append(sentiment_distribution)
                if 'confidence' in rev:
                    # 置信分数方面统计
                    confidence_asp_list.append(confidence_asp_distribution)
                    # 置信分数情感极性分布
                    confidence_sentiment_list.append(confidence_sentiment_distribution)
                    # 置信分数句子统计
                    confidence_sentence_list.append(confidence_sentence)
                    # 置信分数词统计
                    confidence_word_list.append(confidence_word)

    sentence_len = sum(sent_len_list) / len(sent_len_list)
    word_length = sum(word_len_list) / len(word_len_list)
    asp_sentence = sum(asp_sent_list) / len(asp_sent_list)
    asp_word_length = sum(asp_word_list) / len(asp_word_list)
    aspect_count = numpy.sum(aspect_list, axis=0) / len(aspect_list)
    aspect_sentiment_count = numpy.sum(sentiment_list, axis=0) / len(sentiment_list)
    confidence_aspect_count = numpy.divide(numpy.sum(confidence_asp_list, axis=0), confidence_count)
    confidence_sentiment_count = numpy.divide(numpy.sum(confidence_sentiment_list, axis=0).T, confidence_count).T
    confidence_sentence_count = numpy.divide(numpy.sum(confidence_sentence_list, axis=0), confidence_count)
    confidence_word_count = numpy.divide(numpy.sum(confidence_word_list, axis=0), confidence_count)
    save_dict['sentence_len'] = sentence_len
    save_dict['word_length'] = word_length
    save_dict['asp_sentence'] = asp_sentence
    save_dict['asp_word_length'] = asp_word_length
    save_dict['aspect_count'] = aspect_count
    save_dict['aspect_sentiment_count'] = aspect_sentiment_count
    save_dict['confidence_aspect_count'] = confidence_aspect_count
    save_dict['confidence_sentiment_count'] = confidence_sentiment_count
    save_dict['confidence_sentence_count'] = confidence_sentence_count
    save_dict['confidence_word_count'] = confidence_word_count
    return save_dict
res = rev_count('ICLR_2024')
# no_ai = [80346,20433,24303,11330,33848,35578,43630,11341]
#  #NIPS [12587,3172,3648,492,2437,4110,3069,1052]
# ai = [21981,4516,5721,808,4129,5958,4706,1758]
#  #NIPS [46013,8445,9917,2158,9293,14540,14168,4546]
#
# def calculate_proportions(numbers):
#     total = sum(numbers)
#     proportions = [number / total for number in numbers]
#     return proportions
#
#
# # 示例使用
#
# proportions = calculate_proportions(no_ai)
#
# for number, proportion in zip(no_ai, proportions):
#     print(f"{number}: {proportion * 100:.2f}%")
#
# print('\n')
# proportions = calculate_proportions(ai)
#
# for number, proportion in zip(ai, proportions):
#     print(f"{number}: {proportion * 100:.2f}%")
