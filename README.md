# Medical Hallucination
The emergence of Foundation Models (e.g., Large Language Models [LLM] and Large Vision Models [LVM]) capable of processing and generating multi-modal data has transformed AI’s role in medicine. However, these models have limitations, particularly hallucination, where inaccurate or fabricated information is generated. We define **medical hallucination** as instances where models, particularly LLMs, produce misleading medical information that can adversely affect clinical decision-making.

By examining their unique characteristics, underlying causes, and critical implications, we categorize and exemplify medical hallucinations, highlighting their potentially life-threatening outcomes. Our contributions
include a taxonomy for understanding and addressing medical hallucinations, experiments using medical hallucination benchmarks and physician-annotated medical records, and insights from a multi-national clinician survey on their experiences with medical hallucinations. 

Our experiments reveal that inference techniques such as Chain-of-Thought (CoT), Retrieval-Augmented Generation (RAG), and Internet Search impact hallucination rates, emphasizing the need for tailored mitigation strategies. These findings underscore the ethical and practical imperative for robust detection and mitigation strategies, establishing a foundation for regulatory policies that prioritize patient safety and uphold clinical integrity as AI integrates further into healthcare. 


##  📣 News
[2025-02-16] 🎉🎉🎉 Our preprint paper has been submitted to arxiv: 

## Contents
- [What makes Medical Hallucination Special?](#difference)
- [Hallucinations in Medical LLMs](#llms)
- [Medical Hallucination Benchmarks](#benchmarks)
- [Detection Methods for Medical Hallucination](#detection)
- [Mitigation Methods for Medical Hallucination](#mitigation)

## What makes Medical Hallucination Special? <a name="difference"></a>

## Hallucinations in Medical LLMs <a name="llms"></a>
Please refer to table 1 of our paper for examples of medical hallucination in clinical tasks, and table 2 for an organized taxonomy of medical hallucination. 
| Title | Institute | Date | Code
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------: | :-----------: | :-------------: |
| [MedHalu: Hallucinations in Responses to Healthcare Queries by Large Language Models](https://arxiv.org/abs/2409.19492) | University of Surrey<br>Georgia Institute of Technology | 2024-09 | N/A
| [Creating trustworthy llms: Dealing with hallucinations in healthcare ai](https://arxiv.org/abs/2311.01463) |  University of Washington Bothell <br>Kaiser Permanente | 2023-09 | N/A
| [Knowledge Overshadowing Causes Amalgamated Hallucination in Large Language Models](https://arxiv.org/pdf/2407.08039) |  University of Illinois Urbana-Champaign<br>The Hong Kong Polytechnic University<br>Stanford University | 2024-07 | N/A
| [Mechanistic Understanding and Mitigation of Language Model Non-Factual Hallucinations](https://arxiv.org/pdf/2403.18167v2) |  University of Toronto<br>McGill University<br>Mila– Québec AI Institute<br>University of California, Riverside | 2024-06 | N/A
| [Language models are susceptible to incorrect patient self diagnosis in medical applications](https://arxiv.org/pdf/2309.09362) | University of Maryland, College Park<br>Johns Hopkins University | 2023-09 | N/A
| [The Dawn After the Dark: An Empirical Study on Factuality Hallucination in Large Language Models](https://arxiv.org/pdf/2401.03205) | Renmin University of China<br>Université de Montréal | 2024-01 | https://github.com/RUCAIBox/HaluEval-2.0



## Medical Hallucination Benchmarks <a name="benchmarks"></a>
Please refer to table 3 of our paper for details on medical hallucination benchmarks. 
| Title | Institute | Date | Code/Dataset
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------: | :-----------: | :-------------: |
| [Med-HALT: Medical Domain Hallucination Test for Large Language Models](https://arxiv.org/abs/2307.15343) | Saama AI Research | 2023-10 | [https://medhalt.github.io/](https://medhalt.github.io/)
| [Hallucination benchmark in medical visual question answering](https://arxiv.org/abs/2401.05827v2) | University College London | 2024-04 | https://github.com/knowlab/halt-medvqa
| [Detection, Diagnosis, and Explanation: A Benchmark for Chinese Medial Hallucination Evaluation](https://aclanthology.org/2024.lrec-main.428/) | Peking University <br> Ministry of Education <br> Beijing Jiaotong University| 2024-05 | [link to drive](https://drive.google.com/drive/folders/1DrdovKwZIh6AX_JjL8BVpUmI9djiIwn_)
| [MedVH: Towards Systematic Evaluation of Hallucination for Large Vision Language Models in the Medical Context](https://arxiv.org/abs/2407.02730) | The Ohio State University <br> University of Oxford| 2024-07 | https://github.com/dongzizhu/MedVH
| [Detecting and Evaluating Medical Hallucinations in Large Vision Language Models](https://arxiv.org/abs/2406.10185) | Fudan University <br> Tencent Youtu Lab <br> Cognition and Intelligent Technology Laboratory <br>  Ministry of Education <br> AI and Unmanned Systems Engineering Research Center of Jilin Province| 2024-06 | https://github.com/ydk122024/Med-HallMark
| [K-QA: AReal-World Medical Q&A Benchmark](https://arxiv.org/pdf/2401.14493) | K Health Inc <br> The Hebrew University of Jerusalem | 2024-01 | https://github.com/Itaymanes/K-QA
| [Grounding LLMs to In-prompt Instructions: Reducing Hallucinations Caused by Static Pre-training Knowledge](https://aclanthology.org/2024.safety4convai-1.1/) | Heriot-Watt University | 2024-05 | https://github.com/AddleseeHQ/in-prompt-grounding
| [Medical Expert Annotations of Unsupported Facts in Doctor-Written and LLM-Generated Patient Summaries](https://physionet.org/content/ann-pt-summ/1.0.0/) | University of Münster <br> MIT <br> Duke University | 2024-04 | https://github.com/stefanhgm/patient_summaries_with_llms
| [MedHallBench: A New Benchmark for Assessing Hallucination in Medical Large Language Models](https://arxiv.org/abs/2412.18947) | University of Warwick <br> Cranfield University <br> University of Oxford | 2025-01 | N/A

## Dection Methods for Medical Hallucination <a name="detection"></a>
### Type 1: Factual Verification <a name="detection"></a>
| Title | Institute | Date | Code
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------: | :-----------: | :-------------: |
| [Complex Claim Verification with Evidence Retrieved in the Wild](https://aclanthology.org/2024.naacl-long.196.pdf) | The University of Texas at Austin | 2025-01 | https://github.com/jifan-chen/Fact-checking-via-Raw-Evidence
 | [FACTSCORE: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://aclanthology.org/2023.emnlp-main.741.pdf) | University of Washington <br> University of Massachusetts Amherst <br> Allen Institute for AI <br> Meta AI | 2023-12 | https://github.com/shmsw25/FActScore

 ### Type 2: Summary Consistency Verification <a name="detection"></a>
| Title | Institute | Date | Code
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------: | :-----------: | :-------------: |
| [Answers Unite! Unsupervised Metrics for Reinforced Summarization Models](https://aclanthology.org/D19-1320.pdf) | CNRS <br> Sorbonne Université<br> LIP6 <br> reciTAL | 2019-11 | https://github.com/ThomasScialom/summa-qa
| [Asking and Answering Questions to Evaluate the Factual Consistency of Summaries](https://aclanthology.org/2020.acl-main.450.pdf) | New York University <br> Facebook AI <br>  CIFAR Associate Fellow | 2020-07 | https://github.com/W4ngatang/qags
 | [QuestEval: Summarization Asks for Fact-based Evaluation](https://aclanthology.org/2021.emnlp-main.529.pdf) | CNRS <br> Sorbonne Université<br> LIP6 <br> reciTAL <br> New York University | 2021-11 | https://github.com/ThomasScialom/QuestEval 
 | [Ranking Generated Summaries by Correctness: An Interesting but Challenging Application for Natural Language Inference](https://aclanthology.org/P19-1213.pdf) | Amazon <br> Technische Universitat <br> Bar-Ilan University, Ramat-Gan | 2019-08 | https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/2002

 ### Type 3: Uncertainty-Based Hallucination Detection <a name="detection"></a>
| Title | Institute | Date | Code
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------: | :-----------: | :-------------: |
| [Looking for a Needle in a Haystack: A Comprehensive Study of Hallucinations in Neural Machine Translation](https://aclanthology.org/2023.eacl-main.75.pdf) |Instituto de Telecomunicações <br> Instituto Superior Técnico & LUMLIS <br> Unbabel <br> University of Edinburgh | 2023-05 | https://github.com/deep-spin/hallucinations-in-nmt
| [Enhancing Uncertainty-Based Hallucination Detection with Stronger Focus](https://arxiv.org/pdf/2311.13230) | Shanghai Jiaotong University <br> Amazon AWS AI <br> Westlake University <br> IGSNRR, Chinese Academy of Sciences| 2023-11 | https://github.com/zthang/focus
| [Detecting hallucinations in large language models using semantic entropy](https://www.nature.com/articles/s41586-024-07421-0) | University of Oxford | 2024-06 | https://github.com/jlko/semantic_uncertainty <br> https://github.com/jlko/long_hallucinations
| [Decomposing Uncertainty for Large Language Models through Input Clarification Ensembling](https://arxiv.org/pdf/2311.08718) | UC Santa Barbara <br> MIT-IBM Watson AI Lab, IBM Research <br> MIT CSAIL| 2024-06 | https://github.com/UCSB-NLP-Chang/llm_uncertainty

## Mitigation Methods for Medical Hallucination <a name="mitigation"></a>
| Title | Institute | Date | Code
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------: | :-----------: | :-------------: |
| [MedHallBench: A New Benchmark for Assessing Hallucination in Medical Large Language Models](https://arxiv.org/abs/2412.18947) | University of Warwick <br> Cranfield University <br> University of Oxford | 2025-01 | N/A

## 📑 Citation

Please consider citing 📑 our paper if our repository is helpful to your work, thanks sincerely!

```
@article{kim2024medical,
  title   = "Medical Hallucination in Foundation Models and Their Impact on Healthcare",
  author = "Kim, Yubin and Jeong, Hyewon andChen, Shan and Li, Shuyue Stella and Lu, Mingyu and Alhamoud, Kumail and Mun, Jimin and Grau, Cristina and Jung, Minseok and Gameiro, Rodrigo and Fan, Lizhou and Park, Eugene and Lin, Tristan and Yoon, Joonsik and Yoon, Wonjin and Sap, Maarten and Tsvetkov, Yulia and Liang, Paul and Xu, Xuhai and Liu, Xin and McDuff, Daniel and Lee, Hyeonhoon and Park, Hae Won and Tulebaev, Samir and Breazeal, Cynthia",
  journal = "arXiv preprint arXiv.XXXXXXX",
  year    = "2025",
  url     = "https://arxiv.org/abs/XXXX.XXXX" 
}
```
