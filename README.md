# Impact of large language models on peer review opinions from a fine-grained perspective: Evidence from top conference proceedings in AI
## Overview

**Dataset and source code for paper "Impact of large language models on peer review opinions from a fine-grained perspective: Evidence from top conference proceedings in AI".**

This study examined the changes in peer review reports for academic articles following the emergence of LLMs, emphasizing variations at fine-grained level. The primary contributions of this paper include:

- This paper conducts a fine-grained statistical analysis of the review report texts from two artificial intelligence conferences. We find that the popularity of artificial intelligence has had the most significant impact on ICLR review reports, resulting in the lowest historical average length. Additionally, the average length of reviews from reviewers with a confidence score of 1 has shown an upward trend in recent years.
- Analyzed the proportion of evaluation aspects in the review reports of AI-assisted and non-AI-assisted reviewers. We found that compared to non-AI-assisted reviewers, AI-assisted reviewers significantly increased the proportion of summaries, while the proportion of evaluations focusing on originality decreased..
- Explored the relationship between the evaluation aspects mentioned in the review reports of AI-assisted reviewers and the scores they assigned. The results indicate that the impact of various evaluation aspects on scoring is relatively weak, and the correlation with reviewers' confidence scores is generally low.
## Directory structure

<pre>
LLM_impact                                        Root directory
├── LLM_dec                                       LLM detection model
├── Aspect_Identification.py                      Identify sentence aspects in the review
├── Correlation_Calculation.py                    Correlation analysis calculation
├── Draw_Pie_Chart.py                             Draw charts
├── Figure_draw.py                                Draw Figures
├── LLM_detection.py                              LLM assisted detection
├── Review_Length_Count.py                        Review length statistics
├── taales_ssc.py                                 Sentence complexity calculation
├── tokenize_tool.py                              Tokenize tool for LLMdec
│
└── README.md
</pre>
