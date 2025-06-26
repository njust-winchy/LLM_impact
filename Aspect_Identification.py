import os
import json
from tqdm import tqdm
from nltk.tokenize import sent_tokenize, word_tokenize
from tagger.annotator import Annotator
annotator = Annotator('tagger/labels.txt', 'F:\code\confidence score-master\seqlab_final', 'gpu')
ir_str = 'F:\code\LLM_impact\$insert'
#ir_list = ['ICLR_2021', 'ICLR_2022', 'ICLR_2024', 'NIPS_2021', 'NIPS_2022', 'NIPS_2023']
#ir_list = ['ICLR_2023']
ir_list = ['ICLR_2020']
# for ir in ir_list:
#     if ir == 'ICLR_2021' or ir == 'ICLR_2022' or ir == 'NIPS_2021':
#         conf = 'confidence_score'
#         rate = 'rating_score'
#     elif ir == 'ICLR_2023':
#         conf = 'Confidence'
#         rate = 'Recommendation'
#     else:
#         conf = 'confidence'
#         rate = 'rating'
#     final_list = []
#     list_dir = os.listdir(ir_str.replace('$insert', ir))
#     for l in tqdm(list_dir):
#         re_list = os.listdir(ir_str.replace('$insert', ir) + '\\' + l)
#         prior = ir_str.replace('$insert', ir) + '\\' + l + '\\'
#         for file in tqdm(re_list):
#             final_dict = {}
#             with open(prior + file) as f:
#                 reviews = json.load(f)
#             f.close()
#             decision = reviews['Decision:']
#             save_rev = []
#             for rev in reviews['reviews']:
#                 save_dict = {}
#                 review_text = rev['review_text']
#                 token_text = sent_tokenize(review_text)
#                 rev_list = []
#                 for t in token_text:
#                     asp_list = []
#                     asp_text = annotator.annotate(t)
#                     for sample in asp_text:
#                         asp_list.append(sample[1])
#                     asp = list(set(asp_list))
#                     asp.append(t)
#                     rev_list.append(asp)
#                 save_dict['rev_with_aspects'] = rev_list
#                 save_dict['rating'] = rev[rate]
#                 save_dict['confidence'] = rev[conf]
#                 save_rev.append(save_dict)
#             final_dict['decision'] = decision
#             final_dict['rev'] = save_rev
#             final_list.append(final_dict)
#     with open(ir + '.json', 'w') as f:
#         json.dump(final_list, f)

# NIPS
file_list = os.listdir('F:\code\ReviewAdvisor-main\dataset')
prior = 'F:\code\ReviewAdvisor-main\dataset\$insert\$insert_paper\\'
prior_2 = 'F:\code\ReviewAdvisor-main\dataset\$insert\$insert_review\\'
ir2_list = ['NIPS_2016', 'NIPS_2017', 'NIPS_2018', 'NIPS_2019']
for f in ir_list:
    fina_list = []
    if f in ir_list:
        if f == 'ICLR_2020':
            rev_list = os.listdir(prior_2.replace('$insert', f))
            for rev_f in tqdm(rev_list):
                with open(prior_2.replace('$insert', f) + rev_f) as fp:
                    rev = json.load(fp)
                paper = rev_f.split('_review')[0]
                with open(prior.replace('$insert', f) + paper + '_paper.json') as p:
                    paper = json.load(p)
                decision = paper['decision']
                fina_dict = {}
                save_rev = []
                for r in rev['reviews']:
                    save_dict = {}
                    review_text = r['review']
                    token_text = sent_tokenize(review_text)
                    revv_list = []
                    for t in token_text:
                        asp_list = []
                        asp_text = annotator.annotate(t)
                        for sample in asp_text:
                            asp_list.append(sample[1])
                        asp = list(set(asp_list))
                        asp.append(t)
                        revv_list.append(asp)
                    save_dict['rev_with_aspects'] = revv_list
                    save_dict['rating'] = r['rating']
                    save_rev.append(save_dict)
                fina_dict['decision'] = decision
                fina_dict['rev'] = save_rev
                fina_list.append(fina_dict)
        if f == 'NIPS_2016':
            rev_list = os.listdir(prior_2.replace('$insert', f))
            fina_list = []
            for rev_f in tqdm(rev_list):
                with open(prior_2.replace('$insert', f) + rev_f) as fp:
                    rev = json.load(fp)
                fp.close()
                paper = rev_f.split('_review')[0]
                with open(prior.replace('$insert', f) + paper + '_paper.json') as p:
                    paper = json.load(p)
                p.close()
                decision = paper['decision']
                fina_dict = {}
                save_rev = []
                for r in rev['reviews']:
                    save_dict = {}
                    review_text = r['review']
                    token_text = sent_tokenize(review_text)
                    revv_list = []
                    for t in token_text:
                        asp_list = []
                        asp_text = annotator.annotate(t)
                        for sample in asp_text:
                            asp_list.append(sample[1])
                        asp = list(set(asp_list))
                        asp.append(t)
                        revv_list.append(asp)
                    save_dict['rev_with_aspects'] = revv_list
                    save_dict['confidence'] = r['confidence']
                    save_rev.append(save_dict)
                fina_dict['decision'] = decision
                fina_dict['rev'] = save_rev
                fina_list.append(fina_dict)
        if f == 'NIPS_2017' or f == 'NIPS_2018' or f == 'NIPS_2019':
            rev_list = os.listdir(prior_2.replace('$insert', f))
            for rev_f in rev_list:
                with open(prior_2.replace('$insert', f) + rev_f) as fp:
                    rev = json.load(fp)
                fp.close()
                paper = rev_f.split('_review')[0]
                with open(prior.replace('$insert', f) + paper + '_paper.json') as p:
                    paper = json.load(p)
                p.close()
                decision = paper['decision']
                fina_dict = {}
                save_rev = []
                for r in rev['reviews']:
                    save_dict = {}
                    review_text = r['review']
                    token_text = sent_tokenize(review_text)
                    revv_list = []
                    for t in token_text:
                        asp_list = []
                        asp_text = annotator.annotate(t)
                        for sample in asp_text:
                            asp_list.append(sample[1])
                        asp = list(set(asp_list))
                        asp.append(t)
                        revv_list.append(asp)
                    save_dict['rev_with_aspects'] = revv_list
                    save_rev.append(save_dict)
                fina_dict['decision'] = decision
                fina_dict['rev'] = save_rev
                fina_list.append(fina_dict)
    with open(f + '.json', 'w') as fw:
        json.dump(fina_list, fw)
# prior = 'F:\code\LLM_impact\processed_data\\'
# f_list = os.listdir('processed_data')
# for file in f_list:
#     fina_list = []
#     if os.path.exists(file):
#         print(file)
#         continue
#     with open(prior + file) as f:
#         review = json.load(f)
#     for rev in tqdm(review):
#         review_text = rev['review']
#         decision = rev['decision']
#         fina_dict = {}
#         save_rev = []
#         save_dict = {}
#         token_text = sent_tokenize(review_text)
#         revv_list = []
#         for t in token_text:
#             asp_list = []
#             asp_text = annotator.annotate(t)
#             for sample in asp_text:
#                 asp_list.append(sample[1])
#             asp = list(set(asp_list))
#             asp.append(t)
#             revv_list.append(asp)
#         save_dict['rev_with_aspects'] = revv_list
#         save_dict['rating'] = rev['rating']
#         save_dict['confidence'] = rev['confidence']
#         save_rev.append(save_dict)
#         fina_dict['decision'] = decision
#         fina_dict['rev'] = save_rev
#         fina_list.append(fina_dict)
#     with open(file, 'w') as fw:
#         json.dump(fina_list, fw)

# ir_str = 'F:\code\\novelty_dataset\$insert'
# for ir in ir_list:
#     if ir == 'ICLR_2021' or ir == 'ICLR_2022' or ir == 'NIPS_2021':
#         conf = 'confidence_score'
#         rate = 'rating_score'
#     elif ir == 'ICLR_2023':
#         conf = 'Confidence'
#         rate = 'Recommendation'
#     else:
#         conf = 'confidence'
#         rate = 'rating'
#     final_list = []
#     list_dir = os.listdir(ir_str.replace('$insert', ir))
#     for l in tqdm(list_dir):
#         prior = ir_str.replace('$insert', ir) + '\\' + l + '\\'
#
#         final_dict = {}
#         if not os.path.exists(prior + l + '.json'):
#             continue
#         with open(prior + l + '.json') as f:
#             reviews = json.load(f)
#         f.close()
#         decision = reviews['Decision:']
#         save_rev = []
#         for rev in reviews['reviews']:
#             save_dict = {}
#             review_text = rev['review_text']
#             token_text = sent_tokenize(review_text)
#             rev_list = []
#             for t in token_text:
#                 asp_list = []
#                 asp_text = annotator.annotate(t)
#                 for sample in asp_text:
#                     asp_list.append(sample[1])
#                 asp = list(set(asp_list))
#                 asp.append(t)
#                 rev_list.append(asp)
#             save_dict['rev_with_aspects'] = rev_list
#             save_dict['rating'] = rev[rate]
#             save_dict['confidence'] = rev[conf]
#             save_rev.append(save_dict)
#         final_dict['decision'] = decision
#         final_dict['rev'] = save_rev
#         final_list.append(final_dict)
#
#     with open(ir + '.json', 'w') as f:
#         json.dump(final_list, f)
