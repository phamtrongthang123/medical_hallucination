## Hallucinations in Medical LLMs <a name="llms"></a>
Please refer to table 1 of our paper for examples of medical hallucination in clinical tasks, and table 2 for an organized taxonomy of medical hallucination. 
| Title | Institute | Date | Code
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------: | :-----------: | :-------------: |
| [The Dawn After the Dark: An Empirical Study on Factuality Hallucination in Large Language Models](https://arxiv.org/pdf/2401.03205) | Renmin University of China<br>Université de Montréal | 2024-01 | https://github.com/RUCAIBox/HaluEval-2.0

<br>

## Survey on Medical Hallucination among Healthcare Professionals <a name="survey"></a>



## Medical Hallucination Benchmarks <a name="benchmarks"></a>
Please refer to table 3 of our paper for details on medical hallucination benchmarks. 
| Title | Institute | Date | Code 
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------: | :-----------: | :-------------: |
| [Med-HALT: Medical Domain Hallucination Test for Large Language Models](https://arxiv.org/abs/2307.15343) | Saama AI Research | 2023-10 | [https://medhalt.github.io/](https://medhalt.github.io/)
| [Hallucination benchmark in medical visual question answering](https://arxiv.org/abs/2401.05827v2) | University College London | 2024-04 | https://github.com/knowlab/halt-medvqa
| [Detection, Diagnosis, and Explanation: A Benchmark for Chinese Medial Hallucination Evaluation](https://aclanthology.org/2024.lrec-main.428/) | Peking University <br> Ministry of Education <br> Beijing Jiaotong University| 2024-05 | [link to drive](https://drive.google.com/drive/folders/1DrdovKwZIh6AX_JjL8BVpUmI9djiIwn_)
| [MedVH: Towards Systematic Evaluation of Hallucination for Large Vision Language Models in the Medical Context](https://arxiv.org/abs/2407.02730) | The Ohio State University <br> University of Oxford| 2024-07 | https://github.com/dongzizhu/MedVH
| [Detecting and Evaluating Medical Hallucinations in Large Vision Language Models](https://arxiv.org/abs/2406.10185) | Fudan University <br> Tencent Youtu Lab <br> Cognition and Intelligent Technology Laboratory <br>  Ministry of Education <br> AI and Unmanned Systems Engineering Research Center of Jilin Province| 2024-06 | https://github.com/ydk122024/Med-HallMark
| [K-QA: AReal-World Medical Q&A Benchmark](https://arxiv.org/pdf/2401.14493) | K Health Inc <br> The Hebrew University of Jerusalem | 2024-01 | https://github.com/Itaymanes/K-QA
| [Grounding LLMs to In-prompt Instructions: Reducing Hallucinations Caused by Static Pre-training Knowledge](https://aclanthology.org/2024.safety4convai-1.1/) | Heriot-Watt University | 2024-05 | https://github.com/AddleseeHQ/in-prompt-grounding
| [Medical Expert Annotations of Unsupported Facts in Doctor-Written and LLM-Generated Patient Summaries](https://physionet.org/content/ann-pt-summ/1.0.0/) | University of Münster <br> MIT <br> Duke University | 2024-04 | https://github.com/stefanhgm/patient_summaries_with_llms

<br>

## LLM Experiments on Medical Hallucination Benchmark <a name="llm-exp"></a>


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

<br>

## Mitigation Methods for Medical Hallucination <a name="mitigation"></a>
| Title | Institute | Date | Code
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------: | :-----------: | :-------------: |
| [Benchmarking Retrieval-Augmented Generation for Medicine](https://aclanthology.org/2024.findings-acl.372.pdf) | Univeristy of Virginia <br> National Library of Medicine <br> National Institutes of Health | 2024-08 | https://teddy-xionggz.github.io/benchmark-medical-rag/
| [CoMT: Chain-of-Medical-Thought Reduces Hallucination in Medical Report Generation](https://arxiv.org/pdf/2406.11451v4) | Fudan University <br> Tencent YouTu Lab <br> Xiamen University <br> Cognition and Intelligent Technology Laboratory <br> Institute of Meta-Medical <br> Ministry of Education <br> Jilin Provincial Key Laboratory of Intelligence Science and Engineering | 2025-02 | https://github.com/FRENKIE-CHIANG/CoMT
| [Towards Mitigating Hallucination in Large Language Models via Self-Reflection](https://arxiv.org/pdf/2310.06271) | Center for Artificial Intelligence Research (CAiRE) <br> Hong Kong University of Science and Technology| 2023-10 | https://github.com/ziweiji/Self_Reflection_Medical
| [Chain-of-Knowledge: Grounding Large Language Models via Dynamic Knowledge Adapting over Heterogeneous Sources](https://export.arxiv.org/pdf/2305.13269) | DAMOAcademy, Alibaba Group <br> Nanyang Technological University <br> Singapore University of Technology and Design <br> Salesforce Research <br> Hupan Lab | 2024-02 | https://github.com/DAMO-NLP-SG/chain-of-knowledge

<br>


}
```
