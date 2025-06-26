import json
from LLMdec.src.estimation import estimate_text_distribution
from LLMdec.src.MLE import MLE
from tokenize_tool import sen_tokenize
from tqdm import tqdm
words = [
    "meticulously", "reportedly", "lucidly", "innovatively", "aptly",
    "methodically", "excellently", "compellingly", "impressively", "undoubtedly",
    "scholarly", "strategically", "intriguingly", "competently", "intelligently",
    "hitherto", "thoughtfully", "profoundly", "undeniably", "admirably",
    "creatively", "logically", "markedly", "thereby", "contextually",
    "distinctly", "judiciously", "cleverly", "invariably", "successfully",
    "chiefly", "refreshingly", "constructively", "inadvertently", "effectively",
    "intellectually", "rightly", "convincingly", "comprehensively", "seamlessly",
    "predominantly", "coherently", "evidently", "notably", "professionally",
    "subtly", "synergistically", "productively", "purportedly", "remarkably",
    "traditionally", "starkly", "promptly", "richly", "nonetheless",
    "elegantly", "smartly", "solidly", "inadequately", "effortlessly",
    "forth", "firmly", "autonomously", "duly", "critically",
    "immensely", "beautifully", "maliciously", "finely", "succinctly",
    "further", "robustly", "decidedly", "conclusively", "diversely",
    "exceptionally", "concurrently", "appreciably", "methodologically", "universally",
    "thoroughly", "soundly", "particularly", "elaborately", "uniquely",
    "neatly", "definitively", "substantively", "usefully", "adversely",
    "primarily", "principally", "discriminatively", "efficiently", "scientifically",
    "alike", "herein", "additionally", "subsequently", "potentially",
    "commendable", "innovative", "meticulous", "intricate", "notable",
    "versatile", "noteworthy", "invaluable", "pivotal", "potent",
    "fresh", "ingenious", "cogent", "ongoing", "tangible",
    "profound", "methodical", "laudable", "lucid", "appreciable",
    "fascinating", "adaptable", "admirable", "refreshing", "proficient",
    "intriguing", "thoughtful", "credible", "exceptional", "digestible",
    "prevalent", "interpretative", "remarkable", "seamless", "economical",
    "proactive", "interdisciplinary", "sustainable", "optimizable", "comprehensive",
    "vital", "pragmatic", "comprehensible", "unique", "fuller",
    "authentic", "foundational", "distinctive", "pertinent", "valuable",
    "invasive", "speedy", "inherent", "considerable", "holistic",
    "insightful", "operational", "substantial", "compelling", "technological",
    "beneficial", "excellent", "keen", "cultural", "unauthorized",
    "strategic", "expansive", "prospective", "vivid", "consequential",
    "manageable", "unprecedented", "inclusive", "asymmetrical", "cohesive",
    "replicable", "quicker", "defensive", "wider", "imaginative",
    "traditional", "competent", "contentious", "widespread", "environmental",
    "instrumental", "substantive", "creative", "academic", "sizeable",
    "extant", "demonstrable", "prudent", "practicable", "signatory",
    "continental", "unnoticed", "automotive", "minimalistic", "intelligent",
    "underscores", "necessitating", "delves", "adaptability",
    "delved", "delve", "elucidated", "underscore",
    "credibility", "advancements", "elucidation", "underpinnings",
    "equitable", "perplexing", "excels", "intricacies",
    "persuasiveness", "delineation", "elucidate", "provision",
    "bolster", "discourse", "meticulous", "endeavors",
    "tangible", "commendable", "showcasing", "imperative",
    "encompassing", "offering"
]
estimate_text_distribution(f"LLMdec/data/training_data/CS/human_data.parquet", f"LLMdec/data/training_data/CS/ai_data.parquet", f"LLMdec/distribution/CS.parquet")
model = MLE(f"LLMdec/distribution/CS.parquet")
words = list(set(words))
count_dict = {'summary': 0, 'motivation': 0, 'substance': 0, 'replicability': 0, 'originality': 0, 'soundness': 0, 'clarity': 0, 'meaningful_comparison': 0}


def check_sentence(sentence):
    # Convert sentence to lowercase and split it into words
    sentence_words = sentence.lower().split()

    # Check if any word from the list is in the sentence
    for word in words:
        if word in sentence_words:
            return True, word

    # If no words from the list are found
    return False, None


save_list = []
ai = 0
ai_sen_length = 0
ai_word_length = 0
no_ai = 0
no_ai_sen_length = 0
no_ai_word_length = 0
with open('ICLR_2024.json') as f:
    data = json.load(f)
    for x in tqdm(data):
        for rev in x['rev']:
            rev_length = 0
            rev_sen_length = 0
            save_dic = {}
            count_dict1 = {'summary': 0, 'motivation': 0, 'substance': 0, 'replicability': 0, 'originality': 0,
                          'soundness': 0, 'clarity': 0, 'meaningful_comparison': 0}

            rev_sentence = rev['rev_with_aspects']
            rev_sen_length += len(rev_sentence)
            usage = False
            for sen_list in rev_sentence:
                if 'O' in sen_list and len(sen_list) == 2:
                    continue
                eva_sentence = sen_list[-1]
                if len(eva_sentence) < 10:
                    continue
                res, word = check_sentence(eva_sentence)
                test_token = sen_tokenize(eva_sentence)[0]
                rev_length += len(test_token)
                if len(test_token) <= 3:
                    continue
                estimated, ci = model.inference_change(test_token)
                #print(estimated, ci)
                if estimated == -10:
                    continue
                if not res and estimated == 1.0:
                    usage = True
                for item in sen_list:
                    for key in count_dict.keys():
                        if key in item:
                            count_dict[key] += 1
                for item in sen_list:
                    for key in count_dict1.keys():
                        if key in item:
                            count_dict1[key] += 1
            if usage:
                # save_dic['decision'] = x['decision']
                # save_dic['score'] = rev['rating']
                # save_dic['confidence'] = rev['confidence']
                # values = list(count_dict1.values())
                # save_dic['aspect'] = values
                # save_list.append(save_dic)
                ai+=1
                ai_sen_length +=rev_sen_length
                ai_word_length += rev_length
            else:
                no_ai+=1
                no_ai_sen_length+=rev_sen_length
                no_ai_word_length += rev_length

print(ai_sen_length/ai)
print(ai_word_length/ai)
print(no_ai_sen_length/no_ai)
print(no_ai_word_length/no_ai)
# ICLR
# ai_sen_length 22.118472250665576
# ai_word_length 193.92883473274625
# no_ai_sen_length 20.695248016668003
# no_ai_word_length 156.34233512300665
#
# NIPS
# ai_sen_length 22.383072739632905
# ai_word_length 209.30625424881032
# no_ai_sen_length 20.321201679767416
# no_ai_word_length 164.873479056746


# with open('noAI_ICLR_2023.json', 'w') as f:
#     json.dump(save_list, f)
# f.close()
# with open('noaicount_dict_ICLR23.txt', 'w') as fp:
#     for k, v in count_dict.items():
#         fp.write(k + ':' + str(v))
#         fp.write('\n')
# fp.close()
# ICLR
# 9775
# 22.13145780051151
# 194.23867007672635
# 12470
# 20.684041700080193
# 156.73528468323977
# NIPS
# 5884
# 22.383072739632905
# 209.30625424881032
# 9287
# 20.321201679767416
# 164.873479056746
