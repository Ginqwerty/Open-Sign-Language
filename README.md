# Open-Sign-Language
This repository is all you need for Sign Language Study!

📌 This project is licensed under the Apache License 2.0 – see the LICENSE file for details.

## :memo: Table of Contents
- [Datasets](#datasets) 
- [Papers](#papers)
  - [Survey Papers](#survey-papers)
  - [SLR Papers](#slr-papers)
  - [SLT Papers](#slt-papers)
  - [SLP Papers](#slp-papers)
- [Leaderboard](#leaderboard)
  - [SLR Leaderboard](#slr-leaderboard)
  - [SLT Leaderboard](#slt-leaderboard)
  - [SLP Leaderboard](#slp-leaderboard)

## 🔍 Datasets
- Please refer to [this page](helper/datasets.md) for more information.

### Commonly Used Fingerspelling Datasets
| Dataset                                                                                                                   | Year | Language    | #Samples                         | #Signers | Domain                    |
|---------------------------------------------------------------------------------------------------------------------------|-------|-------------|----------------------------------|----------|---------------------------|
| [ChicagoFSWild](https://home.ttic.edu/~klivescu/ChicagoFSWild.htm)                                                       | 2018  | American    | 7304 sequences                   | 168      | Letters + Char            |
| [ChicagoFSWild+](https://home.ttic.edu/~klivescu/ChicagoFSWild.htm)                                                      | 2019  | American    | 55,232 sequences                 | 260      | Letters + Char            |
| [ArASL](https://data.mendeley.com/datasets/y7pckrw6z2/1)                                                                  | 2019  | Arabic      | 54,049 images                    | 40       | Letters                   |
| [RWTH-FingerSpelling](https://www-i6.informatik.rwth-aachen.de/aslr/fingerspelling.php)                                  | 2006  | German      | 1,400 image sequences            | 20       | Letters + Umlauts + Number |

### Commonly Used Isolated Datasets
| Dataset                                                                                                                 | Year | Language       | #Samples                        | #Signers | Domain                                   |
|-------------------------------------------------------------------------------------------------------------------------|-------|----------------|---------------------------------|----------|------------------------------------------|
| [Purdue RVL-SLLL](https://engineering.purdue.edu/RVL/Database/ASL/asl-database-front.htm)                               | 2002  | American       | 2,576 video clips               | 14       | Motion primitives + Handshapes + General |
| [Boston ASLLVD](https://www.bu.edu/asllrp/av/dai-asllvd.html#vid)                                                       | 2008  | American       | 9,800 tokens                    | 6        | General                                  |
| [MS-ASL](https://www.microsoft.com/en-us/research/project/ms-asl/)                                                      | 2018  | American       | 25,513 videos                   | 222      | General                                  |
| [WLASL](https://dxli94.github.io/WLASL/)                                                                                | 2019  | American       | 21,083 videos                   | 119      | General                                  |
| [ASL-100-RGBD](https://longlong-jing.github.io/ASL-100-RGBD/)                                                           | 2020  | American       | ~4,150 tokens                   | 22       | General                                  |
| [ASL Citizen](https://www.microsoft.com/en-us/research/project/asl-citizen/)                                            | 2023  | American       | 83,399 videos                   | 52       | General                                  |
| [LSA-64](https://facundoq.github.io/datasets/lsa64/)                                                                    | 2016  | Argentina      | 3,200 video sequences           | 10       | Dictionary                               |

### Commonly Used Continuous Datasets
| Dataset                                                                                                              | Year | Language          | #Samples               | #Signers | Domain     |
|----------------------------------------------------------------------------------------------------------------------|-------|-------------------|------------------------|----------|------------|
| [RWTH-Boston-104](https://www-i6.informatik.rwth-aachen.de/aslr/database-rwth-boston-104.php)                       | 2007  | American          | 201 sentences          | 3        | General    |
| [How2Sign](https://how2sign.github.io/)                                                                             | 2020  | American          | >35k sentences         | 11       | General    |
| [OpenASL](https://github.com/chevalierNoir/OpenASL)                                                                 | 2022  | American          | -                      | ~220     | General    |
| [YouTube-ASL](https://github.com/google-research/google-research/tree/master/youtube_asl)                           | 2023  | American          | -                      | >2500    | General    |
| [DailyMoth-70h](https://github.com/facebookresearch/ssvp_slt)                                                       | 2024  | American          | 48,386 clips           | 1        | News       |
| [BOBSL](https://www.robots.ox.ac.uk/~vgg/data/bobsl/)                                                               | 2021  | British           | 1.2M sequences         | 39       | General    |
| [CSL-Daily](https://ustc-slr.github.io/datasets/2021_csl_daily/)                                                    | 2021  | Chinese           | 20,645 videos          | 10       | General    |
| [RWTH-PHOENIX 2012](https://www-i6.informatik.rwth-aachen.de/web/Software/Databases/Signlanguage/details/rwth-phoenix/index.php) | 2012  | Germany           | 1,980 sentences        | 7        | Weather    |
| [RWTH-PHOENIX 2014](https://www-i6.informatik.rwth-aachen.de/~koller/RWTH-PHOENIX/)                                 | 2014  | Germany           | 6,861 sentences        | 9        | Weather    |
| [RWTH-PHOENIX14T](https://www-i6.informatik.rwth-aachen.de/~koller/RWTH-PHOENIX-2014-T/)                            | 2020  | Germany           | 8,257 sentences        | 9        | Weather    |

## :scroll: Papers
### Survey Papers
**********************************************************************************************************************
### Datasets Survey Papers
#### 2022
##### Journal
- **[LREC 2022]** Challenges with sign language datasets for sign language recognition and translation. [Paper](https://repositori.upf.edu/items/7e5fd976-eb4f-4cc5-878b-a1d9eef5a370)

**********************************************************************************************************************
### SLR Survey Papers
#### 2024
##### Journal
- **[Information Processing & Management]** Reviewing 25 years of continuous sign language recognition research: Advances, challenges, and prospects. [Paper](https://www.sciencedirect.com/science/article/abs/pii/S0306457324001341)
- **[IEEE Access]** Sign Language Recognition: A Comprehensive Review of Traditional and Deep Learning Approaches, Datasets, and Challenges. [Paper](https://ieeexplore.ieee.org/abstract/document/10526274) 
- **[Advanced Robotics]** A Review of Deep Learning-Based Approaches to Sign Language Processing. [Paper](https://www.tandfonline.com/doi/full/10.1080/01691864.2024.2442721)


#### 2023
##### Conference
- **[ICCV]** Unraveling a Decade: A Comprehensive Survey on Isolated Sign Language Recognition. [Paper](https://openaccess.thecvf.com/content/ICCV2023W/AMFG/html/Sarhan_Unraveling_a_Decade_A_Comprehensive_Survey_on_Isolated_Sign_Language_ICCVW_2023_paper.html)
- **[ICCMC]** A Extensive Survey on Sign Language Recognition Methods. [Paper](https://ieeexplore.ieee.org/abstract/document/10084111?casa_token=8ZZtp84cwlcAAAAA:xXU_dxbMEJCGnQKtg7Qmxz7UyrLxjvLYwDo_z3MULrvwVIhVriEjXHgCPlKQ3fVkg0z1IcHpfw)

##### Journal
- **[ACM TALLIP]** State of the Art of Automation in Sign Language: A Systematic Review. [Paper](https://dl.acm.org/doi/abs/10.1145/3564769?casa_token=wAEiDbMCTJQAAAAA:qOFU940hFNb5ARyCx2GaZ-jtvvUdXgNe1QSYMwXzZM9-ly2okGpTWi2Ayrqyg5zf6f_WohX6auKSkw)

#### 2022
##### Arxiv
- **[Arxiv]** A Comprehensive Review of Sign Language Recognition: Different Types, Modalities, and Datasets. [Paper](https://arxiv.org/abs/2204.03328)

##### Journal
- **[Meas. Sens.]** Survey on sign language recognition in context of vision-based and deep learning. [Paper](https://www.sciencedirect.com/science/article/pii/S2665917422000198)
- **[Open Comput. Sci.]** Sign language identification and recognition: A comparative study. [Paper](https://www.degruyter.com/document/doi/10.1515/comp-2022-0240/html)
- **[IEEE Access]** Technological Solutions for Sign Language Recognition: A Scoping Review of Research Trends, Challenges, and Opportunities. [Paper](https://ieeexplore.ieee.org/abstract/document/9739689)

#### 2021
##### Conference
- **[ICITIIT]** ML Based Sign Language Recognition System. [Paper](https://ieeexplore.ieee.org/abstract/document/9399594?casa_token=hJN9G8JDMVwAAAAA:yOPOQyDOPQCdFOLkeiYq142UAw85bYNQFJkEqdK8ixutu8wyEMJyb9af5nMCWZE7KPtYydnYew)

##### Journal
- **[ScienceDirect]** Sign Language Recognition: A Deep Survey. [Paper](https://www.sciencedirect.com/science/article/pii/S095741742030614X?casa_token=P9dIGfGoMh0AAAAA:RPA7HImaRjZfsOJrJZ8INi-a9V0fJXp4hvKRRHLZMm_LySJee-lQ86zL9VcVdp2cQbkyK6zfsqM)
- **[Sensors]** Artificial Intelligence Technologies for Sign Language. [Paper](https://www.mdpi.com/1424-8220/21/17/5843)
- **[IEEE Access]** Deep Learning for Sign Language Recognition: Current Techniques, Benchmarks, and Open Issues. [Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9530569)
- **[ISA]** Machine Learning Methods for Sign Language Recognition: A Critical Review and Analysis. [Paper](https://www.sciencedirect.com/science/article/pii/S2667305321000454)
  
#### 2020
##### Conference
- **[INOCON]** Sign Language Recognition Techniques- A Review. [Paper](https://ieeexplore.ieee.org/abstract/document/9298376?casa_token=MrQiOVakC8QAAAAA:GG44e9mc7qGyzRwV07HaS_42kmNVqSN96Bu_2tI188wkiLI_KNfNwaEV7t_B81IKwh-YJlNNNw)

##### Journal
- **[Arab. J. Sci. Eng.]** A Survey on Artificial Intelligence in Chinese Sign Language
Recognition. [Paper](https://link.springer.com/article/10.1007/s13369-020-04758-2)
- **[J. Eng. Appl. Sci.]** Advances, challenges and opportunities in continuous sign language recognition. [Paper](https://fci.stafpu.bu.edu.eg/Computer%20Science/1273/publications/nada%20bahaa%20ibrahim%20ahmed_1205-1227.pdf)
- **[MTA]** Understanding Vision-Based Continuous Sign Language Recognition. [Paper](https://link.springer.com/article/10.1007/s11042-020-08961-z)
- **[EAAI]** A Comprehensive Survey and Taxonomy of Sign Language Research. [Paper](https://www.sciencedirect.com/science/article/abs/pii/S0952197622002925)
- 

##### Arxiv
- **[Arxiv]** Quantitative Survey of the State of the Art in Sign Language Recognition. [Paper](https://arxiv.org/abs/2008.09918)

#### 2019
##### Journal
- **[IEEE]** Technical approaches to Chinese sign language processing: A review. [Paper](https://ieeexplore.ieee.org/abstract/document/8764391)
- **[Arch. Comput. Methods Eng.]** Sign Language Recognition Systems: A Decade Systematic Literature
Review. [Paper](https://www.researchgate.net/profile/Parteek-Bhatia-2/publication/353571514_Sign_Language_Recognition_Systems_A_Decade_Systematic_Literature_Review/links/61039ff40c2bfa282a0d8a80/Sign-Language-Recognition-Systems-A-Decade-Systematic-Literature-Review.pdf)
- **[Int. J. Mach. Learn. & Cyber.]** A review of hand gesture and sign language recognition techniques. [Paper](https://link.springer.com/article/10.1007/s13042-017-0705-5)

<details>
  <summary><b>Earlier</b></summary>

  ##### Journal
  - **[IEEE]** Automatic sign language recognition: A survey. [Paper](https://ieeexplore.ieee.org/abstract/document/8075561?casa_token=CdoSrTyglMIAAAAA:e3KBEi9j3LO3-DUeTlb56NQlA4Hve1GWLuFKKOJce312gckmJFNrOyTatHifdIFa0XxWbkBjig)
  - **[ARPN]** SIGN LANGUAGE RECOGNITION: STATE OF THE ART. [Paper](https://www.researchgate.net/profile/Ashok-Sahoo-5/publication/262187093_Sign_language_recognition_State_of_the_art/links/02e7e53b246791ce2a000000/Sign-language-recognition-State-of-the-art.pdf)

</details>

******************************************************************************************************************

### SLT Survey Papers
#### 2024
##### Journal
- **[Advanced Robotics]** A Review of Deep Learning-Based Approaches to Sign Language Processing. [Paper](https://www.tandfonline.com/doi/full/10.1080/01691864.2024.2442721)

#### 2023
##### ArXiv
- **[ArXiv]** From Rule-Based Models to Deep Learning Transformers Architectures for Natural Language Processing and Sign Language Translation Systems: Survey, Taxonomy and Performance Evaluation. [Paper](https://arxiv.org/abs/2408.14825)

##### Journal
- **[Research in Computing Science]** A Comprehensive Review of Sign Language Translation Technologies Using Linguistic Approaches. [Paper](https://rcs.cic.ipn.mx/2023_152_11/A%20Comprehensive%20Review%20of%20Sign%20Language%20Translation%20Technologies%20Using%20Linguistic%20Approaches.pdf)
- **[Electronics]** Sign Language Translation: A Survey of Approaches and Techniques. [Paper](https://www.mdpi.com/2079-9292/12/12/2678)
- **[Expert Syst. Appl.]** A survey on Sign Language machine translation. [Paper](https://www.sciencedirect.com/science/article/pii/S0957417422020115)
- **[ACM TALLIP]** State of the Art of Automation in Sign Language: A Systematic Review. [Paper](https://dl.acm.org/doi/abs/10.1145/3564769?casa_token=wAEiDbMCTJQAAAAA:qOFU940hFNb5ARyCx2GaZ-jtvvUdXgNe1QSYMwXzZM9-ly2okGpTWi2Ayrqyg5zf6f_WohX6auKSkw)
- **[Univ. Access Inf. Soc.]** Machine translation from text to sign language: a systematic review. [Paper](https://link.springer.com/article/10.1007/s10209-021-00823-1)

#### 2021
##### Journal
- **[Sensors]** Artificial Intelligence Technologies for Sign Language. [Paper](https://www.mdpi.com/1424-8220/21/17/5843)

***********************************************************************************************************************
#### SLP Survey Papers

#### 2024
##### Journal
- **[ACM TALLIP]** A Comprehensive Review of Sign Language Production. [Paper](https://riunet.upv.es/handle/10251/212285)
- **[Expert Syst. Appl.]** A survey on recent advances in Sign Language Production. [Paper](https://www.sciencedirect.com/science/article/pii/S0957417423033481?casa_token=UmInOwI3diwAAAAA:bA4cZopQA1MtTfGYKQZR9QkKEUHp0rnHKLx7fepo9BFP2cSI80Xl4sEtr7p3yb4yvvmghKy8FzU)
- **[Advanced Robotics]** A Review of Deep Learning-Based Approaches to Sign Language Processing. [Paper](https://www.tandfonline.com/doi/full/10.1080/01691864.2024.2442721)

#### 2023
##### Journal
- **[ACM TALLIP]** State of the Art of Automation in Sign Language: A Systematic Review. [Paper](https://dl.acm.org/doi/abs/10.1145/3564769?casa_token=wAEiDbMCTJQAAAAA:qOFU940hFNb5ARyCx2GaZ-jtvvUdXgNe1QSYMwXzZM9-ly2okGpTWi2Ayrqyg5zf6f_WohX6auKSkw)
- **[Univ. Access Inf. Soc.]** Machine translation from text to sign language: a systematic review. [Paper](https://link.springer.com/article/10.1007/s10209-021-00823-1)

#### 2022
##### ArXiv
- **[ArXiv]** All You Need In Sign Language Production. [Paper](https://arxiv.org/abs/2201.01609)

#### 2021
##### Conference
- **[CVPR]** Sign Language Production: A Review. [Paper](https://openaccess.thecvf.com/content/CVPR2021W/ChaLearn/html/Rastgoo_Sign_Language_Production_A_Review_CVPRW_2021_paper.html)

##### Journal
- **[Sensors]** Artificial Intelligence Technologies for Sign Language. [Paper](https://www.mdpi.com/1424-8220/21/17/5843)

***********************************************************************************************************************
### SLR Papers
#### 2025
##### Conference
- **[WACV]** Sign Language Recognition: A Large-Scale Multi-View Dataset and Comprehensive Evaluation. [Paper](https://openaccess.thecvf.com/content/WACV2025/html/Dinh_Sign_Language_Recognition_A_Large-Scale_Multi-View_Dataset_and_Comprehensive_Evaluation_WACV_2025_paper.html)
- **[ICLR]** UNI-SIGN: TOWARD UNIFIED SIGN LANGUAGE UNDERSTANDING AT SCALE. [Paper](https://iclr.cc/virtual/2025/poster/31250)
- **[IEEE]** Continuous Sign Language Recognition With Multi-Scale Spatial-Temporal Feature Enhancement. [Paper](https://ieeexplore.ieee.org/abstract/document/10829616)

##### Journal
- **[MVA]** `MAM-FSD` Continuous Sign Language Recognition Based on Motor Attention Mechanism and Frame-Level Self-Distillation. [Paper](https://arxiv.org/pdf/2402.19118)
- **[FO]** Mamba vision models: Automated American sign language recognition. [Paper](https://www.sciencedirect.com/science/article/pii/S2773186325000143)
- **[SN]** Empowering deaf communication: a novel LSTM model for recognizing Indonesian sign language. [Paper](https://link.springer.com/article/10.1007/s10209-024-01095-1)
- **[ICPR]** EMPATH: MediaPipe-Aided Ensemble Learning with Attention-Based Transformers for Accurate Recognition of Bangla Word-Level Sign Language. [Paper](https://link.springer.com/chapter/10.1007/978-3-031-78305-0_23)
- **[Neurocomputing]** `Swin-MSTP` Swin-MSTP: Swin transformer with multi-scale temporal perception for continuous sign language recognition. [Paper](https://www.sciencedirect.com/science/article/abs/pii/S0925231224017867)
- **[Scientific Reports]** Improved feature reduction framework for sign language recognition using autoencoders and adaptive Grey Wolf Optimization. [Paper](https://www.nature.com/articles/s41598-024-82785-x)
- **[MDPI]** Real-Time Norwegian Sign Language Recognition Using MediaPipe and LSTM. [Paper](https://www.mdpi.com/2414-4088/9/3/23)

##### ArXiv
- **[ArXiv]** `SSLR` SSLR: A Semi-Supervised Learning Method for Isolated Sign Language Recognition. [Paper](https://arxiv.org/abs/2504.16640)

#### 2024
##### Conference
- **[CVPR]** `SignGraph` SignGraph: A Sign Sequence is Worth Graphs of Nodes. [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Gan_SignGraph_A_Sign_Sequence_is_Worth_Graphs_of_Nodes_CVPR_2024_paper.html) | [Code](https://github.com/gswycf/SignGraph)
- **[ICEECT]** `SLRMPCMC` SLRMPCMC: Sign Language Recognition using Mediapipe and Cross-Model Comparison. [Paper](https://ieeexplore.ieee.org/abstract/document/10738932)
- **[ICME]** `XMC` Cross-Modality Consistency Mining for Continuous Sign Language Recognition with Text-Domain Equivalents. [Paper](https://ieeexplore.ieee.org/abstract/document/10687620)

##### Journal
- **[PR]** Scalable Frame Resolution for Efficient Continuous Sign Language Recognition. [Paper](https://dl.acm.org/doi/abs/10.1016/j.patcog.2023.109903)
- **[ACM TOMM]**  `SRM` Improving Continuous Sign Language Recognition with Consistency Constraints and Signer Removal. [Paper](https://dl.acm.org/doi/pdf/10.1145/3640815) | [Code](https://github.com/2000ZRL/LCSA_C2SLR_SRM)
- **[TALLIP]** Isolated Arabic Sign Language Recognition Using a Transformer-based Model and Landmark Keypoints. [Paper](https://dl.acm.org/doi/full/10.1145/3584984)
- **[IFS]** `SLR-YOLO` SLR-YOLO: An Improved YOLOv8 Network for Real-Time Sign Language Recognition. [Paper](https://content.iospress.com/articles/journal-of-intelligent-and-fuzzy-systems/ifs235132)
- **[AJSE]**  `CRKD` Continuous Sign Language Recognition Based on Cross-Resolution Knowledge Distillation. [Paper](https://arxiv.org/pdf/2303.06820)

##### ArXiv
- **[ArXiv]** `SignVTCL` SignVTCL: Multi-Modal Continuous Sign Language Recognition Enhanced by Visual-Textual Contrastive Learning. [Paper](https://arxiv.org/abs/2401.11847)

#### 2023
##### Conference
- **[AAAI]** `SEN` Self-Emphasizing Network for Continuous Sign Language Recognition. [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/25164)
- **[ACM MM]** `AdaBrowse` AdaBrowse: Adaptive Video Browser for Efficient Continuous Sign Language Recognition. [Paper](https://dl.acm.org/doi/abs/10.1145/3581783.3611745)
- **[ICASSP]** `DFConv` Self-Sufficient Framework for Continuous Sign Language Recognition. [Paper](https://ieeexplore.ieee.org/abstract/document/10095732)
- **[CVPR]** `CorrNet` Continuous Sign Language Recognition with Correlation Network. [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Hu_Continuous_Sign_Language_Recognition_With_Correlation_Network_CVPR_2023_paper.html) | [Code](https://github.com/hulianyuyy/CorrNet)
- **[CVPR]** `CTCA` Distilling Cross-Temporal Contexts for Continuous Sign Language Recognition. [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Guo_Distilling_Cross-Temporal_Contexts_for_Continuous_Sign_Language_Recognition_CVPR_2023_paper.html)
- **[CVPR]** `CVT-SLR` CVT-SLR: Contrastive Visual-Textual Transformation for Sign Language Recognition with Variational Alignment. [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Zheng_CVT-SLR_Contrastive_Visual-Textual_Transformation_for_Sign_Language_Recognition_With_Variational_CVPR_2023_paper.html) | [Code](https://github.com/binbinjiang/CVT-SLR)
- **[CVPR]** `NLA-SLR` Natural Language-Assisted Sign Language Recognition. [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Zuo_Natural_Language-Assisted_Sign_Language_Recognition_CVPR_2023_paper.html) | [Code](https://github.com/FangyunWei/SLRT)
- **[ICCV]** `CoSign` CoSign: Exploring Co-Occurrence Signals in Skeleton-Based Continuous Sign Language Recognition. [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Jiao_CoSign_Exploring_Co-occurrence_Signals_in_Skeleton-based_Continuous_Sign_Language_Recognition_ICCV_2023_paper.html)
- **[ICCV]** `C²ST` C<sup>2</sup>2ST: Cross-Modal Contextualized Sequence Transduction for Continuous Sign Language Recognition. [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_C2ST_Cross-Modal_Contextualized_Sequence_Transduction_for_Continuous_Sign_Language_Recognition_ICCV_2023_paper.html)
- **[ICCV]** `Cross-Ling` Improving Continuous Sign Language Recognition with Cross-Lingual Signs. [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Wei_Improving_Continuous_Sign_Language_Recognition_with_Cross-Lingual_Signs_ICCV_2023_paper.html) 
- **[NeurIPS]** `TwoStream-SLT` Two-Stream Network for Sign Language Recognition and Translation. [Paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6cd3ac24cdb789beeaa9f7145670fcae-Abstract-Conference.html)

##### Journal
- **[AJSE]** `TSRNet` Continuous Sign Language Recognition via Temporal Super-Resolution Network. [Paper](https://arxiv.org/pdf/2207.00928)
- **[PR]** `mLTSF-Net` Multi-Scale Local-Temporal Similarity Fusion for Continuous Sign Language Recognition. [Paper](https://arxiv.org/pdf/2107.12762)
- **[IEEE TM]** `Multilingual-CSLR` Collaborative Multilingual Continuous Sign Language Recognition: A Unified Framework. [Paper](https://ieeexplore.ieee.org/abstract/document/9954921)
- **[IEEE TM]** `PA-CMA` Prior-Aware Cross Modality Augmentation Learning for Continuous Sign Language Recognition. [Paper](https://ieeexplore.ieee.org/abstract/document/10105511)
- **[CIS]** `STTN` Spatial–Temporal Transformer for End-to-End Sign Language Recognition. [Paper](https://link.springer.com/content/pdf/10.1007/s40747-023-00977-w.pdf)
- **[IEEE Access]** `BAE-Attention` Boundary-Adaptive Encoder with Attention Method for Chinese Sign Language Recognition. [Paper](https://ieeexplore.ieee.org/abstract/document/9426906)
- **[AIHC]**  Continuous Sign Language Recognition Using Isolated Signs Data and Deep Transfer Learning. [Paper](https://link.springer.com/article/10.1007/s12652-021-03418-z)
- **[TPAMI]** `SignBERT+` SignBERT+: Hand-Model-Aware Self-Supervised Pre-Training for Sign Language Understanding. [Paper](https://ieeexplore.ieee.org/abstract/document/10109128?casa_token=4tAMXuomxmYAAAAA:b__eqgfzL1o-6nOkZjKl8LKb4D4PCghwglhvyAPrtISy584_JQsCH76IB0_D0uSgW5cr76YC1w)

#### 2022
##### Conference
- **[ISCA]** `LCSA` Local Context-aware Self-attention for Continuous Sign Language Recognition. [Paper](https://drive.google.com/file/d/1lMWfTHN_iE2uzimMy3dLO-W-jm9YRm9f/view)
- **[ECCV]** `TLP` Temporal Lift Pooling for Continuous Sign Language Recognition. [Paper](https://arxiv.org/pdf/2207.08734) | [Code](https://github.com/hulianyuyy/Temporal-Lift-Pooling)
- **[ECCV]** `RadialCTC` Deep Radial Embedding for Visual Sequence Learning. [Paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136660234.pdf)
- **[CVPR]** `C²SLR` C<sup>2</sup>SLR: Consistency-Enhanced Continuous Sign Language Recognition. [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Zuo_C2SLR_Consistency-Enhanced_Continuous_Sign_Language_Recognition_CVPR_2022_paper.html)

##### Journal
- **[Sensors]** `STAMF` Novel Spatio-Temporal Continuous Sign Language Recognition Using an Attentive Multi-Feature Network. [Paper](https://www.mdpi.com/1424-8220/22/17/6452)
- **[IEEE SPL]** `CA-SignBERT` A Cross-Attention BERT-Based Framework for Continuous Sign Language Recognition. [Paper](https://ieeexplore.ieee.org/abstract/document/9860060) 
  
##### ArXiv
- **[ArXiv]** `MSTN` Multi-View Spatial-Temporal Network for Continuous Sign Language Recognition. [Paper](https://arxiv.org/abs/2204.08747)
- **[ArXiv]** `MSTNet` Multi-Scale Temporal Network for Continuous Sign Language Recognition. [Paper](https://ui.adsabs.harvard.edu/abs/2024JEI....33b3059Z/abstract)


#### 2021
##### Conference
- **[ICCV]** `VAC` Visual Alignment Constraint for Continuous Sign Language Recognition. [Paper](https://openaccess.thecvf.com/content/ICCV2021/html/Min_Visual_Alignment_Constraint_for_Continuous_Sign_Language_Recognition_ICCV_2021_paper.html?ref=https://githubhelp.com)
- **[ICCV]** `SMKD` Self-Mutual Distillation Learning for Continuous Sign Language Recognition. [Paper](https://openaccess.thecvf.com/content/ICCV2021/html/Hao_Self-Mutual_Distillation_Learning_for_Continuous_Sign_Language_Recognition_ICCV_2021_paper.html)
- **[IJCNN]** `ST-GCN` Continuous Sign Language Recognition based on Multi-Part Skeleton Data. [Paper](https://ieeexplore.ieee.org/abstract/document/9534003?casa_token=thEBwazoFYIAAAAA:fUv87iU1KeXdvPKAlIDFwtqU3Ke3qa5VgySmVPiwAPcXCco_0T1DwRi2WaYyp6y2UAdUT46Pjw)
- **[CVPR]** Fingerspelling Detection in American Sign Language. [Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Shi_Fingerspelling_Detection_in_American_Sign_Language_CVPR_2021_paper.html)

##### Journal
- **[TCSVT]** `SBD-RL` Semantic Boundary Detection With Reinforcement Learning for Continuous Sign Language Recognition. [Paper](https://ieeexplore.ieee.org/document/9106402)
- **[Sensors]** `SLRGAN` Continuous Sign Language Recognition through a Context-Aware Generative Adversarial Network. [Paper](https://www.mdpi.com/1424-8220/21/7/2437)
- **[IEEE TM]** `PiSLTRc` PiSLTRc: Position-Informed Sign Language Transformer with Content-Aware Convolution. [Paper](https://ieeexplore.ieee.org/abstract/document/9528010?casa_token=BGggtyj1xRwAAAAA:J9CxdVukp4J_Pqj_6A0Y_F0YYm9OgmHkHleLFaQ5TG9BI6gHVrHI_DdUkqvZC3LXPTqzAaVYDQ)
- **[ESA]** `H-GAN` An optimized Generative Adversarial Network based continuous sign language classification. [Paper](https://www.sciencedirect.com/science/article/pii/S0957417421007077?casa_token=s44ja4hAVuIAAAAA:eM-qEtKbXx13wXSGe1uvnBaaeHpq2nE2qHalvgiPMnnid9ZsBJD6Fmv1Juou0cmoDT4VQxSIEG4)
- **[IEEE TM]** `STMC-SLRT` Spatial-Temporal Multi-Cue Network for Sign Language Recognition and Translation. [Paper](https://ieeexplore.ieee.org/abstract/document/9354538?casa_token=6GwJXPuM4KoAAAAA:voN-SsfLLaRZes_Z_ZoHow552I41YujlhVuoDxNLnl-ObGZfEPhHbUm7iOb5F-5J9GsYNEbo7g)
- **[IEEE Access]** `SignBERT` SignBERT: A BERT-Based Deep Learning Framework for Continuous Sign Language Recognition. [Paper](https://ieeexplore.ieee.org/abstract/document/9635818)
- **[IEEE TM]** `EnStimCTC ` A Comprehensive Study on Deep Learning-Based Methods for Sign Language Recognition. [Paper](https://ieeexplore.ieee.org/abstract/document/9393618?casa_token=BNvKjD_WV1EAAAAA:4OTJLsUOvBoFJP0AVshweZCFYZqRApBqY_78tkbAJGRLkJemt1wOQsXW9dXjbUWBThY_fUT0Gg) 


#### 2020
##### Conference
- **[ICPR]** `ISFT` Continuous Sign Language Recognition with Iterative Spatiotemporal Fine-Tuning. [Paper](https://ieeexplore.ieee.org/abstract/document/9412364?casa_token=aPxqQhLKsmAAAAAA:lZzpfURV_LnCzObhw5IOGXJwQDhCl-zuFJNF13_YO1nVZFIfbDcmnQccBGaE_LBCnJVhm3BclA)
- **[ECAI]** `SAFI` Self-Attention-Based Fully-Inception Networks for Continuous Sign Language Recognition. [Paper](https://ebooks.iospress.nl/doi/10.3233/FAIA200425)
- **[ICPR]** `SAN` Context Matters: Self-Attention for Sign Language Recognition. [Paper](https://ieeexplore.ieee.org/document/9412916)
- **[ECCV]** `SMS` Stochastic Fine-Grained Labeling of Multi-State Sign Glosses for Continuous Sign Language Recognition. [Paper](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123610171.pdf)
- **[ECCV]** `FCN` Fully Convolutional Networks for Continuous Sign Language Recognition. [Paper](https://arxiv.org/pdf/2007.12402)
- **[ACM MM]** `CMAug` Boosting Continuous Sign Language Recognition via Cross Modality Augmentation. [Paper](https://dl.acm.org/doi/abs/10.1145/3394171.3413931?casa_token=xSfegIdlgFMAAAAA:L5yZ-ien9d5yA8W9IT_Uxt_b_qUyySG_mvaM49cgDNKAGnzTH7i6gH1E1oTmtm5DlWpYjGRZxMUufQ)
- **[CVPR]** `SL-Transf` Sign Language Transformers: Joint End-to-end Sign Language Recognition and Translation.  
    [Paper](https://openaccess.thecvf.com/content_CVPR_2020/papers/Camgoz_Sign_Language_Transformers_Joint_End-to-End_Sign_Language_Recognition_and_Translation_CVPR_2020_paper.pdf) | [Code](https://github.com/neccam/nslt)
- **[AAAI]** `STMC` Spatial-Temporal Multi-Cue Network for Continuous Sign Language Recognition. [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/7001) 

##### Journal
- **[JCR]** Skeleton-Based Chinese Sign Language Recognition and Generation for Bidirectional Communication Between Deaf and Hearing People. [Paper](https://www.sciencedirect.com/science/article/abs/pii/S089360802030040X?casa_token=ja72CdvWb00AAAAA:ffcRBH9Whu94gknblx4W1SeLSGOW14SBo7U0OIBKokL-xkekUmbBoY5o62zVxFfpSojBno150hk)
- **[TPAMI]** `Multi-Stream CLH` Weakly Supervised Learning with Multi-Stream CNN-LSTM-HMMs to Discover Sequential Parallelism in Sign Language Videos. [Paper](https://ieeexplore.ieee.org/abstract/document/8691602?casa_token=lP-Fkwedp_EAAAAA:dvSygKGlDR60MWhvjK7e3vClHtNB3mrLVCRp_Yov2z5ElEIpBRz-b_b9ge23QRLRFxi7DGku1Q)
- **[IEEE Access]** `CMA-TE` Continuous Sign Language Recognition through Cross-Modal Alignment of Video and Text Embeddings in a Joint-Latent Space. [Paper](https://ieeexplore.ieee.org/abstract/document/9090828)
- **[Sensors]** Recognition of Non-Manual Content in Continuous Japanese Sign Language. [Paper](https://www.mdpi.com/1424-8220/20/19/5621)


#### 2019
##### Conference
- **[MAHCI]** `CSLR-PL` Continuous Sign Language Recognition Based on Pseudo-Supervised Learning. [Paper](https://dl.acm.org/doi/abs/10.1145/3347319.3356837?casa_token=WD5tRGP4LhgAAAAA:3eMfuqCSDBd1DveZEyWaWyKiWHK-AMaWXh3JOc5N3a8fy1a28mcU7YCxThBLymSORu2BaLmH_WUrhg)
- **[ICIP]** `CSLR-RL` Continuous Sign Language Recognition via Reinforcement Learning. [Paper](https://ieeexplore.ieee.org/abstract/document/8802972?casa_token=AqKmDYqrWu0AAAAA:SIAqXsquMqEz3cqHHGiRdwghEW5pYApCEVFA5Fi-smg6yqBiI0DpuXN5EMbPinmI_w_15v7Ljg)
- **[CVPR]** `Align-iOpt` Iterative Alignment Network for Continuous Sign Language Recognition. [Paper](https://ieeexplore.ieee.org/document/8954236)
-  **[ICME]** `DPLD` Dynamic Pseudo Label Decoding for Continuous Sign Language Recognition. [Paper](https://ieeexplore.ieee.org/abstract/document/8784863?casa_token=PB1_yvyZouwAAAAA:lnaTKwd2UfJDjWkk2vkd08RMgtnDfbuWoE3eMNwjTHYGsYgK74XPlDS2osPhVvQaC2QdvKJHmA)
-  **[BigMM]** `WIC-NGC` Deep Grammatical Multi-classifier for Continuous Sign Language Recognition. [Paper](https://ieeexplore.ieee.org/document/8919458)
-  **[APSIPA ASC]** Exploring RNN-Transducer for Chinese Speech Recognition. [Paper](https://ieeexplore.ieee.org/document/9023133)
-  **[IJCAI]** `DenseTCN` Dense Temporal Convolution Network for Sign Language Translation. [Paper](https://www.ijcai.org/proceedings/2019/0105.pdf)

##### Journal
- **[IEEE TM]** `IterativeTrain` A Deep Neural Framework for Continuous Sign Language Recognition by Iterative Training. [Paper](https://ieeexplore.ieee.org/document/8598757)

##### ArXiv
- **[ArXiv]** `Sf-net` Sf-net: Structured feature network for continuous sign language recognition. [Paper](https://arxiv.org/abs/1908.01341) 


#### 2018
##### Conference
- **[IJCAI]** `DCN-IterativeOpt` Dilated Convolutional Network with Iterative Optimization for Continuous Sign Language Recognition. [Paper](https://pujunfu.github.io/publications/IJCAI2018Dilated/paper.pdf)
- **[AAAI]** `LS-HAN` Video-based Sign Language Recognition Without Temporal Segmentation. [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/11903)
- **[AAAI]** `HLSTM` Hierarchical LSTM for Sign Language Translation. [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/12235)
- **[CVPRW]** `3DRCNN` Recognizing American Sign Language Gestures from Within Continuous Videos. [Paper](https://openaccess.thecvf.com/content_cvpr_2018_workshops/w41/html/Ye_Recognizing_American_Sign_CVPR_2018_paper.html)

#### 2017
##### Conference
- **[CVPR]** `ReSign` Re-Sign: Re-Aligned End-to-End Sequence Modelling with Deep Recurrent CNN-HMMs. [Paper](https://openaccess.thecvf.com/content_cvpr_2017/html/Koller_Re-Sign_Re-Aligned_End-To-End_CVPR_2017_paper.html)
- **[ICCV]** `SubUNets` SubUNets: End-to-End Hand Shape and Continuous Sign Language Recognition. [Paper](https://openaccess.thecvf.com/content_iccv_2017/html/Camgoz_SubUNets_End-To-End_Hand_ICCV_2017_paper.html) | [Code](https://github.com/neccam/SubUNets)
- **[CVPR]** `StagedOpt` Recurrent Convolutional Neural Networks for Continuous Sign Language Recognition by Staged Optimization. [Paper](https://openaccess.thecvf.com/content_cvpr_2017/html/Cui_Recurrent_Convolutional_Neural_CVPR_2017_paper.html)
- **[SenSys]** `DeepASL` DeepASL: Enabling Ubiquitous and Non-Intrusive Word and Sentence-Level Sign. [Paper](https://dl.acm.org/doi/abs/10.1145/3131672.3131693)

##### Journal
- **[CMRA]** `Openpose-LSTM` Towards Continuous Sign Language Recognition with Deep Learning. [Paper](https://homepages.inf.ed.ac.uk/hhastie2/pubs/humanoids.pdf)


#### 2016
##### Conference
- **[LREC]** `HamNoSys CSLR` Automatic Alignment of HamNoSys Subunits for Continuous Sign Language Recognition. [Paper](https://www.researchgate.net/profile/Oscar-Koller/publication/299634721_Automatic_Alignment_of_HamNoSys_Subunits_for_Continuous_Sign_Language_Recognition/links/57038dd108ae646a9da99e79/Automatic-Alignment-of-HamNoSys-Subunits-for-Continuous-Sign-Language-Recognition.pdf)
- **[BMVC]** `Deep Sign` Deep Sign: Hybrid CNN-HMM for Continuous Sign Language Recognition. [Paper](https://s3.eu-central-1.amazonaws.com/eu-st01.ext.exlibrisgroup.com/44SUR_INST/storage/alma/11/B1/D7/EE/FE/33/9E/97/1B/8D/FF/9F/13/80/87/67/Koller_BMVC2016.pdf?response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250104T222933Z&X-Amz-SignedHeaders=host&X-Amz-Expires=119&X-Amz-Credential=AKIAJN6NPMNGJALPPWAQ%2F20250104%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Signature=d93fb750a40df90faad98c2a45f3ce2ffeebf0f93247af6f03ed51b2a7ac6a9f)


***********************************************************************************************************************
### SLT Papers

### Gloss-based SLT
#### 2025
##### Conference
- **[COLING]** `TextCTC-SLT` Improvement in Sign Language Translation Using Text CTC Alignment. [Paper](https://arxiv.org/abs/2412.09014) | [Code](https://github.com/Claire874/TextCTC-SLT)
- **[CVPR]** Lost in Translation, Found in Context: Sign Language Translation with Contextual Cues. [Paper](https://arxiv.org/abs/2501.09754)

#### 2024
##### Conference
- **[ECCV]** `EVSign` EVSign: Sign Language Recognition and Translation with Streaming Events. [Paper](https://arxiv.org/pdf/2407.12593)
- **[NAACL]** `SDDA` Signer Diversity-driven Data Augmentation for Signer-Independent Sign Language Translation. [Paper](https://aclanthology.org/2024.findings-naacl.140/)
- **[ECAI]** Improving Non-autoregressive Sign Language Translation with Random Ordering Progressive Prediction Pre-training.

#### 2023
##### Conference
- **[ICLR]** `SLTUNET` SLTUNET: A Simple Unified Model for Sign Language Translation. [Paper](https://arxiv.org/abs/2305.01778)|[Code](https://github.com/bzhangGo/sltunet)

#### 2022
##### Conference
- **[WACV]** `HST-GNN` Sign Language Translation with Hierarchical Spatio-Temporal Graph Neural Network. [Paper](https://openaccess.thecvf.com/content/WACV2022/html/Kan_Sign_Language_Translation_With_Hierarchical_Spatio-Temporal_Graph_Neural_Network_WACV_2022_paper.html)
- **[NeurIPS]** `TwoStream-SLT` Two-Stream Network for Sign Language Recognition and Translation. [Paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6cd3ac24cdb789beeaa9f7145670fcae-Abstract-Conference.html)
- **[CVPR]** `MMTLB` A Simple Multi-Modality Transfer Learning Baseline for Sign Language Translation. [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Chen_A_Simple_Multi-Modality_Transfer_Learning_Baseline_for_Sign_Language_Translation_CVPR_2022_paper.html)

##### Journal
- **[Applied Intelligence]** Sign language recognition and translation network based on multi-view data. [Paper](https://link.springer.com/article/10.1007/s10489-022-03407-5)

##### ArXiv
- **[ArXiv]** Leveraging Graph-based Cross-modal Information Fusion for Neural Sign Language Translation. [Paper](https://arxiv.org/abs/2211.00526)


#### 2021
##### Conference
- **[CVPR]** `BN-TIN-Transf` Improving Sign Language Translation with Monolingual Data by Sign Back-Translation. [Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Zhou_Improving_Sign_Language_Translation_With_Monolingual_Data_by_Sign_Back-Translation_CVPR_2021_paper.html)
- **[MT Summit]** `BERT2RND` Frozen Pretrained Transformers for Neural Sign Language Translation. [Paper](https://biblio.ugent.be/publication/8719287) | [Code](https://github.com/m-decoster/fpt4slt)

##### Journal
- **[Neurocomputing]** `Facial-SLT` Enhancing neural sign language translation by highlighting the facial expression information. [Paper](https://www.sciencedirect.com/science/article/abs/pii/S0925231221012698)
- **[IET]** How Important Is Motion in Sign Language Translation? [Paper](https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/cvi2.12037)
- **[IEEE TMM]** `STMC-T` Spatial-Temporal Multi-Cue Network for Sign Language Recognition and Translation. [Paper](https://ieeexplore.ieee.org/abstract/document/9354538?casa_token=i6bC3STkl88AAAAA:5cpJmkjzhXbXWrenMLHctPadd4xaj6-uA2jlqq-zwM6NHXp0n6VrTt3wkXUHg886-T7So9FYVg) 

#### 2020
##### Conference
- **[ACCV]** Understanding Motion in Sign Language: A New Structured Translation Dataset. [Paper](https://openaccess.thecvf.com/content/ACCV2020/html/Rodriguez_Understanding_Motion_in_Sign_Language_A_New_Structured_Translation_Dataset_ACCV_2020_paper.html)

##### ArXiv
- **[ArXiv]** `STMC-Transf` Better Sign Language Translation with STMC-Transformer. [Paper](https://arxiv.org/abs/2004.00588)|[Code](https://github.com/kayoyin/transformer-slt)

#### 2019
##### Journal
- **[MDPI]** Neural Sign Language Translation Based on Human Keypoint Estimation. [Paper](https://www.mdpi.com/2076-3417/9/13/2683)


#### 2018
##### Conference
- **[CVPR]** `NSLT` Neural Sign Language Translation. [Paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Camgoz_Neural_Sign_Language_CVPR_2018_paper.html)|[Code](https://github.com/neccam/nslt)
- **[ACM MM]** `CTF` Connectionist Temporal Fusion for Sign Language Translation. [Paper](https://dl.acm.org/doi/abs/10.1145/3240508.3240671?casa_token=V4-a-LYLGbIAAAAA:2xoc5DhlkaP8cnsupWmoajZxBdQdwVUJXdCs_vZxmfIDIVEavWC1SWCCwBMxdSbVHSPBrneFyRzGCw)

### Gloss-free SLT

#### 2025
##### Conference
- **[WACV]** `UniGloR` A Spatio-Temporal Representation Learning as an Alternative to Traditional Glosses in Sign Language Translation and Production. [Paper](https://arxiv.org/abs/2407.02854) | [Code](https://github.com/eddie-euijun-hwang/UniGloR)
- **[ICLR]** UNI-SIGN: TOWARD UNIFIED SIGN LANGUAGE UNDERSTANDING AT SCALE. [Paper](https://iclr.cc/virtual/2025/poster/31250)
- **[ACL]** Improving Multilingual Sign Language Translation with Automatically Clustered Language Family Information. [Paper](https://aclanthology.org/2025.coling-main.241/)

##### ArXiv
- **[ArXiv]** Spatio-temporal transformer to support automatic sign language translation. [Paper](https://arxiv.org/abs/2502.02587)
- **[ArXiv]** `ADAT` ADAT: Time-Series-Aware Adaptive Transformer Architecture for Sign Language Translation. [Paper](https://arxiv.org/abs/2504.11942)
- **[ArXiv]** Sign Language Translation using Frame and Event Stream: Benchmark Dataset and Algorithms. [Paper](https://arxiv.org/abs/2503.06484)
- **[ArXiv]** GLoT: A Novel Gated-Logarithmic Transformer for Efficient Sign Language Translation. [Paper](https://arxiv.org/abs/2502.12223)

  
#### 2024
##### Conference
- **[NeurIPS]** Scaling Sign Language Translation. [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/ced76a666704e381c3039871ffe558ee-Abstract-Conference.html)
- **[NeurIPS]** `SignCL` Improving Gloss-free Sign Language Translation by Reducing Representation Density. [Paper](https://arxiv.org/abs/2405.14312) | [Code](https://github.com/JinhuiYE/SignCL)
- **[ACL]** `SLT-SEM` Sign Language Translation with Sentence Embedding Supervision. [Paper](https://aclanthology.org/2024.acl-short.40/) | [Code](https://github.com/yhamidullah/sem-slt)
- **[ECCV]** `VAP` Visual Alignment Pre-training for Sign Language Translation. [Paper](https://fq.pkwyx.com/default/https/www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05894.pdf)
- **[CVPR]** `LLM-SLT` LLMs Are Good Sign Language Translators. [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Gong_LLMs_are_Good_Sign_Language_Translators_CVPR_2024_paper.html)
- **[LREC-COLING]** `SimulSLT-CLT` Adaptive Simultaneous Sign Language Translation with Confident Translation Length Estimation. [Paper](https://aclanthology.org/2024.lrec-main.34/) | [Code](https://github.com/tongsun99/CTL)
- **[LREC-COLING]** `FLa-LLM` Factorized Learning Assisted with Large Language Model for Gloss-free Sign Language Translation. [Paper](https://arxiv.org/abs/2403.12556)
- **[AAAI]** `CV-SLT` Conditional Variational Autoencoder for Sign Language Translation with Cross-Modal Alignment. [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/29937)|[Code](https://github.com/rzhao-zhsq/CV-SLT)
- **[ICASSP]** `EMF-SLT` An Explicit Multi-Modal Fusion Method for Sign Language Translation. [Paper](https://ieeexplore.ieee.org/abstract/document/10446966?casa_token=n9nZhBsV_rQAAAAA:udlmgkU8simclxDuSQQ4tbVgLOHa_ha8fkp128G7YtzvbZnhDHbuZJTeJGD1op_RFerAgPlFAg)
- **[ICLR]** `Sign2GPT` Sign2GPT: Leveraging Large Language Models for Gloss-Free Sign Language Translation. [Paper](https://arxiv.org/abs/2405.04164)

  
##### ArXiv
- **[ArXiv]** `LLaVA-SLT` Visual Language Tuning for Sign Language Translation. [Paper](https://arxiv.org/abs/2412.16524) 
- **[ArXiv]** Towards Privacy-Aware Sign Language Translation at Scale. [Paper](https://arxiv.org/abs/2402.09611) | [Code](https://github.com/facebookresearch/ssvp_slt)
- **[ArXiv]** Unsupervised Sign Language Translation and Generation. [Paper](https://arxiv.org/abs/2402.07726)
- **[ArXiv]** American Sign Language Video to Text Translation. [Paper](https://arxiv.org/abs/2402.07255) | [Code](https://github.com/jiSilverH/idlf23-aslt)
- **[ArXiv]** `Online-CSLRT` Towards Online Sign Language Recognition and Translation. [Paper](https://arxiv.org/abs/2401.05336) | [Code](https://github.com/FangyunWei/SLRT)
- **[ArXiv]** Improving Gloss-free Sign Language Translation by Reducing Representation Density. [Paper](https://arxiv.org/abs/2405.14312)
- **[ArXiv]** `MSKA-SLT` Multi-Stream Keypoint Attention Network for Sign Language Recognition and Translation. [Paper](https://arxiv.org/abs/2405.05672) | [Code](https://github.com/sutwangyan/MSKA)
- **[ArXiv]** `Signformer` Signformer is all you need: Towards Edge AI for Sign Language. [Paper](https://arxiv.org/abs/2411.12901)
- **[ArXiv]** `C²RL` C<sup>2</sup>RL: Content and Context Representation Learning for Gloss-free Sign Language Translation and Retrieval. [Paper](https://arxiv.org/abs/2408.09949)


#### 2023
##### Conference
- **[CVPR]** `GASLT` Gloss Attention for Gloss-Free Sign Language Translation. [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Yin_Gloss_Attention_for_Gloss-Free_Sign_Language_Translation_CVPR_2023_paper.html)|[Code](https://github.com/YinAoXiong/GASLT)
- **[ICCV]** `GFSLT-VLP` Gloss-free Sign Language Translation: Improving from Visual-Language Pretraining. [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Zhou_Gloss-Free_Sign_Language_Translation_Improving_from_Visual-Language_Pretraining_ICCV_2023_paper.html)|[Code](https://github.com/zhoubenjia/GFSLT-VLP)
- **[ICCV]** `IP-SLT` Sign Language Translation with Iterative Prototype. [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Yao_Sign_Language_Translation_with_Iterative_Prototype_ICCV_2023_paper.html)
- **[ICLR]** `SLTUNET` SLTUNET: A Simple Unified Model for Sign Language Translation. [Paper](https://arxiv.org/abs/2305.01778)|[Code](https://github.com/bzhangGo/sltunet)
- **[IJCAI]** `SLT-CND` Efficient Sign Language Translation with a Curriculum-Based Non-Autoregressive Decoder. [Paper](https://www.ijcai.org/proceedings/2023/0584.pdf)|[Code](https://github.com/yp20000921/CND)
- **[ICASSP]** `ConSLT` A Token-Level Contrastive Framework for Sign Language Translation. [Paper](https://ieeexplore.ieee.org/document/10095466)|[Code](https://github.com/biaofuxmu/ConSLT)
- **[CVPRW]** `SLT-IV` Sign Language Translation from Instructional Videos. [Paper](https://openaccess.thecvf.com/content/CVPR2023W/WiCV/html/Tarres_Sign_Language_Translation_from_Instructional_Videos_CVPRW_2023_paper.html) | [Code](https://imatge-upc.github.io/slt_how2sign_wicv2023/)
- **[NeurIPS]** `YouTube-ASL` YouTube-ASL: A Large-Scale, Open-Domain American Sign Language-English Parallel Corpus. [Paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/5c61452daca5f0c260e683b317d13a3f-Abstract-Datasets_and_Benchmarks.html)

##### ArXiv
- **[ArXiv]** `XmDA` Cross-modality Data Augmentation for End-to-End Sign Language Translation. [Paper](https://arxiv.org/abs/2305.11096) ｜ [Code](https://github.com/Atrewin/SignXmDA)
- **[ArXiv]** `GloFE` Gloss-Free End-to-End Sign Language Translation. [Paper](https://arxiv.org/abs/2305.12876) | [Code](https://github.com/HenryLittle/GloFE)
  
#### 2022
##### Conference
- **[WMT]** Spatio-Temporal Sign Language Representation and Translation. [Paper](https://aclanthology.org/2022.wmt-1.94/)
- **[WMT]** Experimental Machine Translation of the Swiss German Sign Language via 3D augmentation of body keypoints. [Paper](https://aclanthology.org/2022.wmt-1.95/)|[Code](https://github.com/DFKI-SignLanguage/slt)
- **[ACL]** `PET` Prior knowledge and memory enriched transformer for sign language translation. [Paper](https://aclanthology.org/2022.findings-acl.297/)
- **[ACM MM]** `MC-SLT` MC-SLT: Towards Low-Resource Signer-Adaptive Sign Language Translation. [Paper](https://dl.acm.org/doi/abs/10.1145/3503161.3548069?casa_token=L598dOYlqkoAAAAA:xQFoL2cNaUDHi8ZJBUrvwH0wwADx0tcYYP5AsYjAaRyMGOWA0I9fjIwgSelOuHgmPQTvKPPx-z3Faw)
- **[CVPR]** `MLSLT` MLSLT: Towards Multilingual Sign Language Translation. [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Yin_MLSLT_Towards_Multilingual_Sign_Language_Translation_CVPR_2022_paper.html)
- **[CVPR]** `MMTLB` A Simple Multi-Modality Transfer Learning Baseline for Sign Language Translation. [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Chen_A_Simple_Multi-Modality_Transfer_Learning_Baseline_for_Sign_Language_Translation_CVPR_2022_paper.html)
- **[NAACL]** `TIN-SLT` Explore More Guidance: A Task-aware Instruction Network for Sign Language Translation Enhanced with Data Augmentation. [Paper](https://arxiv.org/abs/2204.05953)|[Code](https://github.com/yongcaoplus/TIN-SLT)
- **[EMNLP]** `OpenASL` Open-Domain Sign Language Translation Learned from Online Video. [Paper](https://arxiv.org/abs/2205.12870)|[Code](https://github.com/chevalierNoir/OpenASL)

##### Journal
- **[IEEE]** `CSGCR` Conditional Sentence Generation and Cross-Modal Reranking for Sign Language Translation. [Paper](https://ieeexplore.ieee.org/document/9447976)
- **[TPAMI]** SignNet II: A Transformer-Based Two-Way Sign Language Translation Model. [Paper](https://ieeexplore.ieee.org/abstract/document/9999492?casa_token=xMAJ5BjvkxcAAAAA:5vE39AHI9I_VQhm_63DHaGq5QDWnsqkakWZk_wZHknNkJ5U0OHzspyjJlTh66R6A9MIa_nMN9g)

##### ArXiv
- **[ArXiv]** Tackling low-resourced sign language translation: Upc at wmt-slt 22. [Paper](https://arxiv.org/abs/2212.01140)

##### Others
- `TF-H2S` Sign Language Translation based on Transformers for the How2Sign Dataset. [Paper](https://imatge.upc.edu/web/sites/default/files/pub/xCabot22.pdf) 

#### 2021
##### Conference
- **[FG]** Content4All Open Research Sign Language Translation Datasets. [Paper](https://ieeexplore.ieee.org/abstract/document/9667087?casa_token=nk-N5KAO-LoAAAAA:NuKoACOOZQuikSF5P49ckq3EgrpGET7RWEcTx8GnoxT58sCNaQRTuj7iCWAFl1OBEkhor_XYZg)
- **[ACM MM]** `SimulSLT` SimulSLT: End-to-End Simultaneous Sign Language Translation. [Paper](https://dl.acm.org/doi/abs/10.1145/3474085.3475544?casa_token=a9gNRsIfavQAAAAA:-AyOjcYz8C2Q9rrOrQkYqTX2JY9nnPfdxFx9lzdM7vs53LyQr96Z4AbQYhzsSJUErgWqbyqZbhBYqw)
- **[ACM MM]** Skeleton-Aware Neural Sign Language Translation. [Paper](https://dl.acm.org/doi/abs/10.1145/3474085.3475577?casa_token=OBMg4J0TsuIAAAAA:Gt-RQM15Q-0W7Y0NbepwamUTGH-JSKl0xQ_jbXZL1esAdslKB-66mlPH6V6A6uBiy2-UWVHY72SKvg)
- **[ICCV]** Stochastic Transformer Networks with Linear Competing Units: Application to end-to-end SL Translation. [Paper](https://openaccess.thecvf.com/content/ICCV2021/html/Voskou_Stochastic_Transformer_Networks_With_Linear_Competing_Units_Application_To_End-to-End_ICCV_2021_paper.html)

##### Journal
- **[ACM TACCESS]** Deep Learning Methods for Sign Language Translation. [Paper](https://dl.acm.org/doi/abs/10.1145/3477498)

#### 2020
##### Conference
- **[CVPR]** `SL-Transf` Sign Language Transformers: Joint End-to-end Sign Language Recognition and Translation.  
    [Paper](https://openaccess.thecvf.com/content_CVPR_2020/papers/Camgoz_Sign_Language_Transformers_Joint_End-to-End_Sign_Language_Recognition_and_Translation_CVPR_2020_paper.pdf) | [Code](https://github.com/neccam/nslt)
- **[ECCV]** `MCT-SLT` Multi-channel Transformers for Multi-articulatory Sign Language Translation. [Paper](https://link.springer.com/chapter/10.1007/978-3-030-66823-5_18)
- **[FG]** `Tokenization-SLT` Neural Sign Language Translation by Learning Tokenization. [Paper](https://ieeexplore.ieee.org/abstract/document/9320278?casa_token=gH_yVfmcWG0AAAAA:bRns7IujaRUnpfFkh5MznP2mTlcH315MmBMBBk5-uE_4XZhd2jVNLvi8H4vlzbkFNJtHKvdpdQ)
- **[NeurIPS]** `Tspnet` Tspnet: Hierarchical feature learning via temporal semantic pyramid for sign language translation. [Paper](https://proceedings.neurips.cc/paper/2020/hash/8c00dee24c9878fea090ed070b44f1ab-Abstract.html)|[CODE](https://github.com/verashira/TSPNet)
- **[ICTC]** Robust Keypoint Normalization Method for Korean Sign Language Translation Using Transformer. [Paper](https://ieeexplore.ieee.org/document/9289551)

##### Journal
- **[CIN]** An Improved Sign Language Translation Model with Explainable Adaptations for Processing Long Sign Sentences. [Paper](https://onlinelibrary.wiley.com/doi/full/10.1155/2020/8816125)

#### 2019
##### Journal
- **[MDPI AS]** Neural Sign Language Translation based on Human Keypoint Estimation. [Paper](https://www.mdpi.com/2076-3417/9/13/2683)

#### 2018
##### Conference
- **[CVPR]** `NSLT` Neural Sign Language Translation. [Paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Camgoz_Neural_Sign_Language_CVPR_2018_paper.html)|[Code](https://github.com/neccam/nslt)
- **[AAAI]** Hierarchical LSTM for Sign Language Translation. [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/12235)


***********************************************************************************************************************
### SLP Papers
#### 2025
##### Conference
- **[ECCV]** `Signavatars` Signavatars: A Large-Scale 3D Sign Language Holistic Motion Dataset and Benchmark. [Paper](https://arxiv.org/pdf/2310.20436)
- **[CVPR]** Discrete to Continuous: Generating Smooth Transition Poses from Sign Language Observation. [Paper](https://arxiv.org/abs/2411.16810)

##### ArXiv
- **[ArXiv]** `CNSign` Beyond Words: AuralLLM and SignMST-C for Precise Sign Language Production and Bidirectional Accessibility. [Paper](https://arxiv.org/abs/2501.00765)
- **[ArXiv]** A Transformer-Based Framework for Greek Sign Language Production using Extended Skeletal Motion Representations. [Paper](https://arxiv.org/abs/2503.02421)
- **[ArXiv]** Towards AI-driven Sign Language Generation with Non-manual Markers. [Paper](https://arxiv.org/abs/2502.05661)
- **[ArXiv]** Text-Driven Diffusion Model for Sign Language Production. [Paper](https://arxiv.org/abs/2503.15914)
- **[ArXiv]** Disentangle and Regularize: Sign Language Production with Articulator-Based Disentanglement and Channel-Aware Regularization. [Paper](https://arxiv.org/abs/2504.06610)

#### 2024
##### Conference
- **[CVPR]** `Neural Sign Actors` Neural Sign Actors: A Diffusion Model for 3D Sign Language Production from Text. [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Baltatzis_Neural_Sign_Actors_A_Diffusion_Model_for_3D_Sign_Language_CVPR_2024_paper.html)
- **[WACV]** Sign Language Production with Latent Motion Transformer. [Paper](https://openaccess.thecvf.com/content/WACV2024/html/Xie_Sign_Language_Production_With_Latent_Motion_Transformer_WACV_2024_paper.html)
- **[ECCV]** `Spoken2Sign` A Simple Baseline for Spoken Language to Sign Language Translation with 3D Avatars. [Paper](https://arxiv.org/pdf/2401.04730)
- **[ECCV]** `SignGen` SignGen: End-to-End Sign Language Video Generation with Latent Diffusion. [Paper](https://eccv.ecva.net/virtual/2024/poster/2581)
- **[AAAI]** `G2P-DDM` G2P-DDM: Generating Sign Pose Sequence from Gloss Sequence with Discrete Diffusion Model. [Paper](https://arxiv.org/abs/2208.09141) | [Project Page](https://slpdiffusier.github.io/g2p-ddm/)
- **[IEEE FG]** A Gloss-free Sign Language Production with Discrete Representation. [Paper](https://ieeexplore.ieee.org/abstract/document/10581980?casa_token=k1MKhNXwmBAAAAAA:Zxygq6G2ane541p99NTFBF8bC_QdHDYhkNB5yNs1eUYXtDu780u19flLsGigA8j7e2iQVqlupA)
- **[IEEE FG]** `Data-Driven` A Data-Driven Representation for Sign Language Production. [Paper](https://ieeexplore.ieee.org/document/10581995)

##### Journal
- **[TOMM]** `GCDM` Gloss-driven Conditional Diffusion Models for Sign Language Production. [Paper](https://dl.acm.org/doi/abs/10.1145/3663572)

##### ArXiv
- **[ArXiv]** `T2S-GPT` T2S-GPT: Dynamic Vector Quantization for Autoregressive Sign Language Production from Text. [Paper](https://arxiv.org/abs/2406.07119) | [Project Page](https://t2sgpt-demo.yinaoxiong.cn/)
- **[ArXiv]** iSign: A Benchmark for Indian Sign Language Processing. [Paper](https://arxiv.org/abs/2407.05404)
- **[ArXiv]** `UniGloR` A Spatio-Temporal Representation Learning as an Alternative to Traditional Glosses in Sign Language Translation and Production. [Paper](https://arxiv.org/abs/2407.02854) | [Code](https://github.com/eddie-euijun-hwang/UniGloR)
- **[ArXiv]** `LVMCN` Linguistics-Vision Monotonic Consistent Network for Sign Language Production. [Paper](https://arxiv.org/abs/2412.16944)
- **[ArXiv]** `Sign-IDD` Sign-IDD: Iconicity Disentangled Diffusion for Sign Language Production. [Paper](https://arxiv.org/abs/2412.13609) | [Code](https://github.com/NaVi-start/Sign-IDD)
- **[ArXiv]** `MS2SL` MS2SL: Multimodal Spoken Data-Driven Continuous Sign Language Production. [Paper](https://arxiv.org/abs/2407.12842)
- **[ArXiv]** `SignLLM` SignLLM: Sign Language Production Large Language Models. [Paper](https://arxiv.org/abs/2405.10718)
- **[ArXiv]** `Stitching T2P` Sign Stitching: A Novel Approach to Sign Language Production. [Paper](https://arxiv.org/abs/2405.07663)
  
##### Workshop
- **[NuerIPS]** Generative Interpolation of Sign Language Poses using RVQ-VAE. [Paper](https://openreview.net/pdf?id=leI9WFbHT2)

#### 2023
##### Conference
- **[SEM]** `IFECE` Including Facial Expressions in Contextual Embeddings for Sign Language Generation. [Paper](https://arxiv.org/pdf/2202.05383)
- **[FG]** `SignVQNet` Autoregressive Sign Language Production: A Gloss-Free Approach with Discrete Representations. [Paper](https://arxiv.org/abs/2309.12179) | [Code](https://github.com/eddie-euijun-hwang/SignVQNet)


##### ArXiv
- **[ArXiv]** `SignDiff` SignDiff: Learning Diffusion Models for American Sign Language Production. [Paper](https://www.researchgate.net/publication/373518983_SignDiff_Learning_Diffusion_Models_for_American_Sign_Language_Production) | [Project Page](https://signdiff.github.io/)


#### 2022
##### Conference
- **[CVPR]** `FS-NET` Signing at scale: Learning to co-articulate signs for large-scale photo-realistic sign language production. [Paper](https://openaccess.thecvf.com/content/CVPR2022/papers/Saunders_Signing_at_Scale_Learning_to_Co-Articulate_Signs_for_Large-Scale_Photo-Realistic_CVPR_2022_paper.pdf)
- **[ACM]** `GEN-OBT` Gloss Semantic-Enhanced Network with Online Back-Translation for Sign Language Production. [Paper](https://dl.acm.org/doi/pdf/10.1145/3503161.3547830?casa_token=EFCvF9EDF80AAAAA:EWgC9MBv5iQhBxXAnHncwsIiGibHeEhhZ1dxLAWPe5T73njwNOXj-RgECQZ6hCcAaqJVeRs03F71KQ)
- **[3DV]** There and Back Again: 3D Sign Language Generation from Text Using Back-Translation. [Paper](https://ieeexplore.ieee.org/abstract/document/10044459)

##### Journal
- **[IEEE]** Spatial–Temporal Graph Transformer With Sign Mesh Regression for Skinned-Based Sign Language Production. [Paper](https://ieeexplore.ieee.org/abstract/document/9970737)

##### ArXiv
- **[ArXiv]** Non-Autoregressive Sign Language Production via Knowledge Distillation. [Paper](https://arxiv.org/abs/2208.06183)

#### 2021
##### Conference
- **[ACM MM]** `NAT-EA` Towards Fast and High-Quality Sign Language Production. [Paper](https://dl.acm.org/doi/abs/10.1145/3474085.3475463?casa_token=anYLezVhxNYAAAAA:XaOvgclXT1VHV0vE6IbfECNS3YpPp5JbgXHb42s5KvJnG5WUD11Yh3xsXRVZDRBngQNFYExPmBvO6g)
- **[ICCV]** `Mixed SIGNals` Mixed SIGNals: Sign Language Production via a Mixture of Motion Primitives. [Paper](https://openaccess.thecvf.com/content/ICCV2021/html/Saunders_Mixed_SIGNals_Sign_Language_Production_via_a_Mixture_of_Motion_ICCV_2021_paper.html)
- **[BMVC]** `NSLP-G` Non-Autoregressive Sign Language Production with Gaussian Space. [Paper](https://www.bmvc2021-virtualconference.com/assets/papers/1102.pdf)

##### Journal
- **[IJCV]** Continuous 3D Multi-Channel Sign Language Production via Progressive Transformers and Mixture Density Networks. [Paper](https://link.springer.com/article/10.1007/s11263-021-01457-9)

#### 2020
##### Conference
- **[ECCV]** `Progressive Transf` Progressive transformers for end-to-end sign language production. [Paper](https://arxiv.org/abs/2004.14874) | [Code](https://github.com/BenSaunders27/ProgressiveTransformersSLP)
- **[IJCV]** Text2Sign: Towards Sign Language Production Using Neural Machine Translation and Generative Adversarial Networks. [Paper](https://link.springer.com/article/10.1007/s11263-019-01281-2)
- **[WACV]** Neural Sign Language Synthesis: Words Are Our Glosses. [Paper](https://ieeexplore.ieee.org/document/9093516)
- **[BMCV]** `Adversarial Training` Adversarial Training for Multi-Channel Sign Language Production. [Paper](https://arxiv.org/abs/2008.12405)

##### Journal
- **[INNS]** Skeleton-based Chinese sign language recognition and generation for bidirectional communication between deaf and hearing people. [Paper](https://www.sciencedirect.com/science/article/pii/S089360802030040X?casa_token=YZ0ClcVeheIAAAAA:K9iH5d-jWl6TJQdCw7ixw-GcvT5Z29XoqwmrH2LTwjoEyuYsRKcjPmmv4vOqWujxLywbcsVzgEA)
  
<details>
  <summary><b>Earlier</b></summary>

  ##### Conference
  - **[BMVC 2018]** Sign Language Production using Neural Machine Translation and Generative Adversarial Networks. [Paper](https://d1wqtxts1xzle7.cloudfront.net/82179482/0906-libre.pdf?1647335598=&response-content-disposition=inline%3B+filename%3DSign_Language_Production_Using_Neural_Ma.pdf&Expires=1735083159&Signature=PqXBi-RC7J7Wx3towVVQfjte12~5pYISgQEePLlAMSNpdQk3mRogSC3YPPpZrHSDCUWF6JfGnGgMo-Oql050Mwz2ObfqkO6KEY6vTe3b25zUIP3HCnwWLMrxnr72LIhyO-17QE6Kt~etKxg48LzCnh9wCSN6uM5IbBkjetxtdeJ-Kw7OuXL5gcKZ-Zduxw99D7SVinzBHZ4~Z5y48SR5feBXMN7fIdqpyuzGF9MeAoauSXEfXN2xOr4m2~aI-0EP9bCvtD2M5J1SmojmbpXYL~7vT1CMqLOEKkBdULONElsrqBkImamhIsmy0paiayJblEmgjRBYlsHOG7-GJiC05w__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)

</details>

## 🏆 Leaderboard

### SLR Leaderboard
### Results on SIGNUM dataset
| Model Name      | Year | Architecture    |WER      | Model Input   | Conference/Journal	     | Code        |
|-----------------|------|-----------------|---------|---------------|-------------------------|-------------|
|[IterativeTrain](https://ieeexplore.ieee.org/document/8598757)          |2019  |CNN + BLSTM    |2.8      |RGB-Frames     |IEEE TM                  |-            |
|[Re-Sign](https://openaccess.thecvf.com/content_cvpr_2017/html/Koller_Re-Sign_Re-Aligned_End-To-End_CVPR_2017_paper.html)          |2017  |CNN + BLSTM + HMM    |4.8      |RGB-Frames     |CVPR                     |-            |
|[Deep Sign](https://s3.eu-central-1.amazonaws.com/eu-st01.ext.exlibrisgroup.com/44SUR_INST/storage/alma/11/B1/D7/EE/FE/33/9E/97/1B/8D/FF/9F/13/80/87/67/Koller_BMVC2016.pdf?response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250104T222933Z&X-Amz-SignedHeaders=host&X-Amz-Expires=119&X-Amz-Credential=AKIAJN6NPMNGJALPPWAQ%2F20250104%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Signature=d93fb750a40df90faad98c2a45f3ce2ffeebf0f93247af6f03ed51b2a7ac6a9f)          |2016  |CNN + HMM    |7.4     |RGB-Frames     |BMVC                     |-            |



### Results on PHOENIX-2014 dataset
| Model Name      | Year | Architecture    |WER      | Model Input   | Conference/Journal	     | Code        |
|-----------------|------|-----------------|---------|---------------|-------------------------|-------------|
|[Cross-Ling](https://openaccess.thecvf.com/content/ICCV2023/html/Wei_Improving_Continuous_Sign_Language_Recognition_with_Cross-Lingual_Signs_ICCV_2023_paper.html)       |2023  | -  |16.7     |RGB-Frames     |ICCV            |-            |
|[SignVTCL](https://arxiv.org/abs/2401.11847)       |2024  | S3D + CTC + mBART + Adapters |17.6     |RGB-Frames, Skeleton-Keypoints, Optical Flow    | ArXiv        |-            |
|[C²ST](https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_C2ST_Cross-Modal_Contextualized_Sequence_Transduction_for_Continuous_Sign_Language_Recognition_ICCV_2023_paper.html)       |2023  | -  |17.7     |RGB-Frames     |ICCV            |-            |
|[CA-SignBERT](https://ieeexplore.ieee.org/abstract/document/9860060)          |2022  |  (3+2+1)D ResNet + BERT + BLSTM + CTC  |18.6     |RGB-Frames     |IEEE SPL             |-            |
|[MAM-FSD](https://arxiv.org/pdf/2402.19118)       |2025  | CNN + 1DCNN + BSLTM | 18.8     | RGB-Frames   | MVA        |-            |
|[TwoStream-SLT](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6cd3ac24cdb789beeaa9f7145670fcae-Abstract-Conference.html)          |2023  | S3D + CTC  |18.8     |RGB-Frames, Skeleton-Keypoints     |  NeurIPS     |-            |
|[MultiSignGraph](https://openaccess.thecvf.com/content/CVPR2024/html/Gan_SignGraph_A_Sign_Sequence_is_Worth_Graphs_of_Nodes_CVPR_2024_paper.html)        |2024  | GCN + KNN   |19.1     |RGB-Frames     |CVPR      |[Available](https://github.com/gswycf/SignGraph)         |
|[CorrNet](https://openaccess.thecvf.com/content/CVPR2023/html/Hu_Continuous_Sign_Language_Recognition_With_Correlation_Network_CVPR_2023_paper.html)          |2023  | CNN + BLSTM   | 19.4     |RGB-Frames     |CVPR             | [Available](https://github.com/hulianyuyy/CorrNet)            |
|[XMC-n](https://ieeexplore.ieee.org/abstract/document/10687620)          |2024  | -   | 19.82     |RGB-Frames     |ICME             |-            |
|[STTN](https://link.springer.com/content/pdf/10.1007/s40747-023-00977-w.pdf)          |2023  | Transformer   | 19.98     |RGB-Frames     |CIS             |-            |
|[SignBERT+](https://ieeexplore.ieee.org/abstract/document/10109128?casa_token=4tAMXuomxmYAAAAA:b__eqgfzL1o-6nOkZjKl8LKb4D4PCghwglhvyAPrtISy584_JQsCH76IB0_D0uSgW5cr76YC1w)          |2023  | - | 20.0        |Skeleton-Keypoints      | TPAMI          |-        |
|[PA-CMA](https://ieeexplore.ieee.org/abstract/document/10105511)          |2023  | CNN-TCN + BLSTM + CTC   | 20.0     |RGB-Frames     |IEEE TM       |-            |
|[SignGraph](https://openaccess.thecvf.com/content/CVPR2024/html/Gan_SignGraph_A_Sign_Sequence_is_Worth_Graphs_of_Nodes_CVPR_2024_paper.html)        |2024  | GCN + KNN   |20.1     |RGB-Frames     |CVPR      |[Available](https://github.com/gswycf/SignGraph)         |
|[CoSign-2s](https://openaccess.thecvf.com/content/ICCV2023/html/Jiao_CoSign_Exploring_Co-occurrence_Signals_in_Skeleton-based_Continuous_Sign_Language_Recognition_ICCV_2023_paper.html)          |2023  | GCN + CNN + BLSTM   |20.1     |RGB-Frames, Skeleton-Keypoints     |ICCV             |-            |
|[CVT-SLR](https://openaccess.thecvf.com/content/CVPR2023/html/Zheng_CVT-SLR_Contrastive_Visual-Textual_Transformation_for_Sign_Language_Recognition_With_Variational_CVPR_2023_paper.html)          |2023  | CNN + MLP + Self-Attention + CTC  |20.1     |RGB-Frames   |CVPR      |  [Available](https://github.com/binbinjiang/CVT-SLR)          |
|[RadialCTC](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136660234.pdf)          |2022  | -  |20.2      |RGB-Frames     |ECCV             |-            |
|[MultiModal SignBERT](https://ieeexplore.ieee.org/abstract/document/9635818)          |2021  | (3+2+1)DCNN + BERT + LSTM   |20.2      |RGB-Frames     |IEEE Access                  |-            |
|[CTCA](https://openaccess.thecvf.com/content/CVPR2023/html/Guo_Distilling_Cross-Temporal_Contexts_for_Continuous_Sign_Language_Recognition_CVPR_2023_paper.html)          |2023  | CNN + 1D-TCN + BLSTM + CTC  | 20.3      |RGB-Frames     |CVPR         |-            |
|[C²SLR](https://openaccess.thecvf.com/content/CVPR2022/html/Zuo_C2SLR_Consistency-Enhanced_Continuous_Sign_Language_Recognition_CVPR_2022_paper.html)          |2022  | -   |20.4      |RGB-Frames     |CVPR                |-            |
|[STMC-SLRT](https://ieeexplore.ieee.org/abstract/document/9354538?casa_token=6GwJXPuM4KoAAAAA:voN-SsfLLaRZes_Z_ZoHow552I41YujlhVuoDxNLnl-ObGZfEPhHbUm7iOb5F-5J9GsYNEbo7g)          |2021  |2D-CNN + TempConv + BLSTM + CTC    |20.7      |RGB-Frames     |IEEE TM                  |-            |
|[AdaBrowse](https://dl.acm.org/doi/abs/10.1145/3581783.3611745)          |2023  |CNN + BLSTM    |20.7      |RGB-Frames     |ACM MM             |-            |
|[DFConv](https://ieeexplore.ieee.org/abstract/document/10095732)          |2023  | CNN + ME + BLSTM |20.8      |RGB-Frames     |ICASSP                 |-            |
|[TLP](https://arxiv.org/pdf/2207.08734)          |2022  | CNN + BLSTM + CTC    |20.8      |RGB-Frames     |ECCV                 |[Available](https://github.com/hulianyuyy/Temporal-Lift-Pooling)            |
|[CRKD](https://arxiv.org/pdf/2303.06820)         |2024  | ResNet50 + 2D-CNN + TSCM-2D CNN + CTC + MSE   |20.9      |RGB-Frames     | AJSE            |-            |
|[Multilingual-CSLR](https://ieeexplore.ieee.org/abstract/document/9954921)          |2023  | CNN + BLSTM + CTC |20.9      |RGB-Frames     |IEEE TM      |-            |
|[SEN](https://ojs.aaai.org/index.php/AAAI/article/view/25164)         |2023  |CNN + BLSTM  |21.0      |RGB-Frames     |AAAI                |-            |
|[SMKD](https://openaccess.thecvf.com/content/ICCV2021/html/Min_Visual_Alignment_Constraint_for_Continuous_Sign_Language_Recognition_ICCV_2021_paper.html?ref=https://githubhelp.com)          |2021  |CNN + BLSTM + CTC    |21.0      |RGB-Frames     |ICCV                |-            |
|[SignBERT](https://ieeexplore.ieee.org/abstract/document/9635818)          |2021  | (3+2+1)DCNN + BERT + LSTM   |21.4      |RGB-Frames     |IEEE Access                  |-            |
|[MSTNet](https://ui.adsabs.harvard.edu/abs/2024JEI....33b3059Z/abstract)          |2022  | CNN + Transformer   |21.4      |RGB-Frames     |ArXiv           |-            |
|[STAMF](https://www.mdpi.com/1424-8220/22/17/6452)          |2022  |CNN + MHA + BLSTM + CTC| 21.5      |RGB-Frames, Skeleton-Keypoints     |Sensors                  |-            |
|[LCSA](https://drive.google.com/file/d/1lMWfTHN_iE2uzimMy3dLO-W-jm9YRm9f/view)          |2022  |VGGNet + Transformer   |21.9      |RGB-Frames     |ISCA                 |-            |
|[CMAug](https://dl.acm.org/doi/abs/10.1145/3394171.3413931?casa_token=xSfegIdlgFMAAAAA:L5yZ-ien9d5yA8W9IT_Uxt_b_qUyySG_mvaM49cgDNKAGnzTH7i6gH1E1oTmtm5DlWpYjGRZxMUufQ)          |2020  |CNN-TCN + LSTM    |21.9      |RGB-Frames     |ACM MM                  |-            |
|[VAC](https://openaccess.thecvf.com/content/ICCV2021/html/Min_Visual_Alignment_Constraint_for_Continuous_Sign_Language_Recognition_ICCV_2021_paper.html?ref=https://githubhelp.com)          |2021  |CNN + BLSTM + CTC    |22.3      |RGB-Frames     |ICCV                  |-            |
|[MSTN](https://arxiv.org/abs/2204.08747)          |2022  |Vit + GCN + Transformer + CTC    |22.8      |RGB-Frames, Skelenton-Keypoints     |ICCV                  |-            |
|[mLTSF-Net + GFE](https://arxiv.org/pdf/2107.12762)          |2023  |FCN    |23.0      |RGB-Frames     |PR |-            |
|[PiSLTRc](https://ieeexplore.ieee.org/abstract/document/9528010?casa_token=BGggtyj1xRwAAAAA:J9CxdVukp4J_Pqj_6A0Y_F0YYm9OgmHkHleLFaQ5TG9BI6gHVrHI_DdUkqvZC3LXPTqzAaVYDQ)          |2021  |CNN + Transformer    |23.2      |RGB-Frames     |IEEE TM          |-            |
|[SLRGAN](https://www.mdpi.com/1424-8220/21/7/2437)          |2021  |GAN    |23.4      |RGB-Frames     |Sensors |-            |
|[mLTSF-Net](https://arxiv.org/pdf/2107.12762)          |2023  |FCN    |23.5      |RGB-Frames     |PR |-            |
|[IterativeTrain + SBD-RL](https://ieeexplore.ieee.org/document/9106402)          |2021  | - | 23.5    |RGB-Frames     |TCSVT         |-            |
|[FCN](https://arxiv.org/pdf/2007.12402)          |2020  |FCN + GFE   |23.9      |RGB-Frames     |ECCV             |-            |
|[CMA-TE](https://ieeexplore.ieee.org/abstract/document/9090828)          |2020  |CNN + BLSTM    |24.00      |RGB-Frames     |IEEE Access             |-            |
|[IterativeTrain](https://ieeexplore.ieee.org/document/8598757)          |2019  |CNN + BLSTM    |24.4      |RGB-Frames     |IEEE TM                  |-            |
|[TSRNet](https://arxiv.org/pdf/2207.00928)          |2023  | -  |24.7      |RGB-Frames     |AJSE       |-            |
|[SMS](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123610171.pdf)          |2020  |2DCNN + Transformer    |25.3      |RGB-Frames     |ECCV                  |-            |
|[Multi-Stream CLH](https://ieeexplore.ieee.org/abstract/document/8691602?casa_token=lP-Fkwedp_EAAAAA:dvSygKGlDR60MWhvjK7e3vClHtNB3mrLVCRp_Yov2z5ElEIpBRz-b_b9ge23QRLRFxi7DGku1Q)          |2020  | Multi-Stream CNN-LSTM-HMM    |26.0    |RGB-Frames     |TPAMI         |-            |
|[Re-Sign](https://openaccess.thecvf.com/content_cvpr_2017/html/Koller_Re-Sign_Re-Aligned_End-To-End_CVPR_2017_paper.html)          |2017  |CNN + BLSTM + HMM    |26.8     |RGB-Frames     |CVPR                     |-            |
|[SBD-RL](https://ieeexplore.ieee.org/document/9106402)          |2021  | CNN + BLSTM + CTC + RL |28.6    |RGB-Frames     |TCSVT         |-            |
|[SAN](https://ieeexplore.ieee.org/document/9412916)          |2020  |2D-CNN + Transformer    |29.7     |RGB-Frames     |ICPR         |-            |
|[SAFI](https://ebooks.iospress.nl/doi/10.3233/FAIA200425)          |2020  | (2+1)D-CNN + Self-Attention   |31.3     |RGB-Frames     | ECAI                    |-            |
[ISFT](https://ieeexplore.ieee.org/abstract/document/9412364?casa_token=aPxqQhLKsmAAAAAA:lZzpfURV_LnCzObhw5IOGXJwQDhCl-zuFJNF13_YO1nVZFIfbDcmnQccBGaE_LBCnJVhm3BclA)          |2020  | (2+1)D-CNN + BLSTM   |34.4    |RGB-Frames     |ICPR                     |-            |
|[DPLD + TEM](https://ieeexplore.ieee.org/abstract/document/8784863?casa_token=PB1_yvyZouwAAAAA:lnaTKwd2UfJDjWkk2vkd08RMgtnDfbuWoE3eMNwjTHYGsYgK74XPlDS2osPhVvQaC2QdvKJHmA)          |2019  | I3D-BGRU-CTC    |34.5     |RGB-Frames     |ICME                     |-            |
|[SF-Net(ResNet-18)](https://arxiv.org/abs/1908.01341)          |2019  | 2D3DCNN + LSTM + BLSTM   |34.9     |RGB-Frames     |ArXiv                     |-            |
|[Align-iOpt](https://ieeexplore.ieee.org/document/8954236)          |2019  | 3D-ResNet + BLSTM + Attention-LSTM + CTC|36.7     |RGB-Frames     |CVPR                     |-            |
|[DCN-IterativeOpt](https://pujunfu.github.io/publications/IJCAI2018Dilated/paper.pdf)          |2019  |3DCNN + CTC    |37.3     |RGB-Frames     |IJCAI                     |-            |
|[CSLR-RL](https://ieeexplore.ieee.org/abstract/document/8802972?casa_token=AqKmDYqrWu0AAAAA:SIAqXsquMqEz3cqHHGiRdwghEW5pYApCEVFA5Fi-smg6yqBiI0DpuXN5EMbPinmI_w_15v7Ljg)          |2019  | 3D-ResNet + Transformer   |38.3     |RGB-Frames     |ICIP                    |-           |
|[LS-HAN](https://ojs.aaai.org/index.php/AAAI/article/view/11903)          |2018  | CNN + LS + HAN  |38.3     |RGB-Frames     |AAAI                    |-           |
|[StagedOpt](https://openaccess.thecvf.com/content_cvpr_2017/html/Cui_Recurrent_Convolutional_Neural_CVPR_2017_paper.html)          |2017  |CNN + BLSTM    |38.7     |RGB-Frames     |CVPR                    |-           |
|[Deep Sign](https://s3.eu-central-1.amazonaws.com/eu-st01.ext.exlibrisgroup.com/44SUR_INST/storage/alma/11/B1/D7/EE/FE/33/9E/97/1B/8D/FF/9F/13/80/87/67/Koller_BMVC2016.pdf?response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250104T222933Z&X-Amz-SignedHeaders=host&X-Amz-Expires=119&X-Amz-Credential=AKIAJN6NPMNGJALPPWAQ%2F20250104%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Signature=d93fb750a40df90faad98c2a45f3ce2ffeebf0f93247af6f03ed51b2a7ac6a9f)          |2016  |CNN + HMM    |38.8     |RGB-Frames     |BMVC                     |-            |
|[CSLR-PL](https://dl.acm.org/doi/abs/10.1145/3347319.3356837?casa_token=WD5tRGP4LhgAAAAA:3eMfuqCSDBd1DveZEyWaWyKiWHK-AMaWXh3JOc5N3a8fy1a28mcU7YCxThBLymSORu2BaLmH_WUrhg)          |2019  |3DCNN + BGRU + CTC    |40.6     |RGB-Frames     |MAHCI                    |-            |
|[SubUNets](https://openaccess.thecvf.com/content_iccv_2017/html/Camgoz_SubUNets_End-To-End_Hand_ICCV_2017_paper.html)          |2017  |CNN + BLSTM    |40.7     |RGB-Frames     |ICCV                    |[Avaliable](https://github.com/neccam/SubUNets)            |
|[HamNoSys CSLR](https://www.researchgate.net/profile/Oscar-Koller/publication/299634721_Automatic_Alignment_of_HamNoSys_Subunits_for_Continuous_Sign_Language_Recognition/links/57038dd108ae646a9da99e79/Automatic-Alignment-of-HamNoSys-Subunits-for-Continuous-Sign-Language-Recognition.pdf)          |2016  |CNN + HMM    |45.1     |RGB-Frames     |LREC                     |-            |



### Results on PHOENIX-2014T dataset
| Model Name      | Year | Architecture    |WER      | Model Input   | Conference/Journal	     | Code        |
|-----------------|------|-----------------|---------|---------------|-------------------------|-------------|
|[SignVTCL](https://arxiv.org/abs/2401.11847)       |2024  | S3D + CTC + mBART + Adapters |17.9     |RGB-Frames, Skeleton-Keypoints, Optical Flow    | ArXiv        |-            |
|[Cross-Ling](https://openaccess.thecvf.com/content/ICCV2023/html/Wei_Improving_Continuous_Sign_Language_Recognition_with_Cross-Lingual_Signs_ICCV_2023_paper.html)       |2023  | -  |18.5     |RGB-Frames     |ICCV            |-            |
|[C²ST](https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_C2ST_Cross-Modal_Contextualized_Sequence_Transduction_for_Continuous_Sign_Language_Recognition_ICCV_2023_paper.html)       |2023  | -  |18.9     |RGB-Frames     |ICCV            |-            |
|[MultiSignGraph](https://openaccess.thecvf.com/content/CVPR2024/html/Gan_SignGraph_A_Sign_Sequence_is_Worth_Graphs_of_Nodes_CVPR_2024_paper.html)        |2024  | GCN + KNN   |19.1     |RGB-Frames     |CVPR      |[Available](https://github.com/gswycf/SignGraph)         |
|[TwoStream-SLT](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6cd3ac24cdb789beeaa9f7145670fcae-Abstract-Conference.html)          |2023  | S3D + CTC  |19.3     |RGB-Frames, Skeleton-Keypoints     |  NeurIPS     |-            |
|[MAM-FSD](https://arxiv.org/pdf/2402.19118)       |2025  | CNN + 1DCNN + BSLTM | 19.4     | RGB-Frames   | MVA        |-            |
|[SignBERT+](https://ieeexplore.ieee.org/abstract/document/10109128?casa_token=4tAMXuomxmYAAAAA:b__eqgfzL1o-6nOkZjKl8LKb4D4PCghwglhvyAPrtISy584_JQsCH76IB0_D0uSgW5cr76YC1w)          |2023  | - |19.9        |Skeleton-Keypoints      | TPAMI          |-        |
|[SignGraph](https://openaccess.thecvf.com/content/CVPR2024/html/Gan_SignGraph_A_Sign_Sequence_is_Worth_Graphs_of_Nodes_CVPR_2024_paper.html)        |2024  | GCN + KNN   |20.0     |RGB-Frames     |CVPR      |[Available](https://github.com/gswycf/SignGraph)         |
|[PA-CMA](https://ieeexplore.ieee.org/abstract/document/10105511)          |2023  | CNN-TCN + BLSTM + CTC   | 20.0     |RGB-Frames     |IEEE TM       |-            |
|[CoSign-2s](https://openaccess.thecvf.com/content/ICCV2023/html/Jiao_CoSign_Exploring_Co-occurrence_Signals_in_Skeleton-based_Continuous_Sign_Language_Recognition_ICCV_2023_paper.html)          |2023  | GCN + CNN + BLSTM   |20.1     |RGB-Frames, Skeleton-Keypoints     |ICCV             |-            |
|[C²SLR](https://openaccess.thecvf.com/content/CVPR2022/html/Zuo_C2SLR_Consistency-Enhanced_Continuous_Sign_Language_Recognition_CVPR_2022_paper.html)          |2022  | -   |20.4      |RGB-Frames     |CVPR                |-            |
|[CorrNet](https://openaccess.thecvf.com/content/CVPR2023/html/Hu_Continuous_Sign_Language_Recognition_With_Correlation_Network_CVPR_2023_paper.html)          |2023  | CNN + BLSTM   | 20.5     |RGB-Frames     |CVPR             | [Available](https://github.com/hulianyuyy/CorrNet)            |
|[SEN](https://ojs.aaai.org/index.php/AAAI/article/view/25164)         |2023  |CNN + BLSTM  |20.7      |RGB-Frames     |AAAI                |-            |
|[TLP](https://arxiv.org/pdf/2207.08734)          |2022  | CNN + BLSTM + CTC    |21.2      |RGB-Frames     |ECCV                 |[Available](https://github.com/hulianyuyy/Temporal-Lift-Pooling)            |
|[SMKD](https://openaccess.thecvf.com/content/ICCV2021/html/Min_Visual_Alignment_Constraint_for_Continuous_Sign_Language_Recognition_ICCV_2021_paper.html?ref=https://githubhelp.com)          |2021  |CNN + BLSTM + CTC    |22.4      |RGB-Frames     |ICCV                |-            |
|[PiSLTRc](https://ieeexplore.ieee.org/abstract/document/9528010?casa_token=BGggtyj1xRwAAAAA:J9CxdVukp4J_Pqj_6A0Y_F0YYm9OgmHkHleLFaQ5TG9BI6gHVrHI_DdUkqvZC3LXPTqzAaVYDQ)          |2021  |CNN + Transformer    |22.9     |RGB-Frames     |IEEE TM          |-            |
|[Multi-Stream CLH](https://ieeexplore.ieee.org/abstract/document/8691602?casa_token=lP-Fkwedp_EAAAAA:dvSygKGlDR60MWhvjK7e3vClHtNB3mrLVCRp_Yov2z5ElEIpBRz-b_b9ge23QRLRFxi7DGku1Q)          |2020  | Multi-Stream CNN-LSTM-HMM    |24.1    |RGB-Frames     |TPAMI         |-            |
|[CMA-TE](https://ieeexplore.ieee.org/abstract/document/9090828)          |2020  |CNN + BLSTM    |24.3      |RGB-Frames     |IEEE Access             |-            |
|[SL-Transf](https://openaccess.thecvf.com/content_CVPR_2020/papers/Camgoz_Sign_Language_Transformers_Joint_End-to-End_Sign_Language_Recognition_and_Translation_CVPR_2020_paper.pdf)         |2020  | Transformer  |  24.49    |RGB-Frames     | CVPR           |[Avaliable](https://github.com/neccam/nslt)        |
|[FCN](https://arxiv.org/pdf/2007.12402)          |2020  |FCN + GFE   |25.1     |RGB-Frames     |ECCV             |-            |



### Results on CSL-Daily dataset
| Model Name      | Year | Architecture    |WER      | Model Input   | Conference/Journal	     | Code        |
|-----------------|------|-----------------|---------|---------------|-------------------------|-------------|
|[SignVTCL](https://arxiv.org/abs/2401.11847)       |2024  | S3D + CTC + mBART + Adapters |24.1     |RGB-Frames, Skeleton-Keypoints, Optical Flow    | ArXiv        |-            |
|[MAM-FSD](https://arxiv.org/pdf/2402.19118)       |2025  | CNN + 1DCNN + BSLTM | 24.5     | RGB-Frames   | MVA        |-            |
|[TwoStream-SLT](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6cd3ac24cdb789beeaa9f7145670fcae-Abstract-Conference.html)          |2023  | S3D + CTC  |25.3     |RGB-Frames, Skeleton-Keypoints     |  NeurIPS     |-            |
|[C²ST](https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_C2ST_Cross-Modal_Contextualized_Sequence_Transduction_for_Continuous_Sign_Language_Recognition_ICCV_2023_paper.html)       |2023  | -  | 25.8     |RGB-Frames     |ICCV            |-            |
|[MultiSignGraph](https://openaccess.thecvf.com/content/CVPR2024/html/Gan_SignGraph_A_Sign_Sequence_is_Worth_Graphs_of_Nodes_CVPR_2024_paper.html)        |2024  | GCN + KNN   |26.4     |RGB-Frames     |CVPR      |[Available](https://github.com/gswycf/SignGraph)         |
|[XMC-d](https://ieeexplore.ieee.org/abstract/document/10687620)          |2024  | -   | 26.4     |RGB-Frames     |ICME             |-            |
|[XMC-n](https://ieeexplore.ieee.org/abstract/document/10687620)          |2024  | -   | 26.8     |RGB-Frames     |ICME             |-            |
|[CoSign-2s](https://openaccess.thecvf.com/content/ICCV2023/html/Jiao_CoSign_Exploring_Co-occurrence_Signals_in_Skeleton-based_Continuous_Sign_Language_Recognition_ICCV_2023_paper.html)        |2023  | GCN + CNN + BLSTM   |27.2     |RGB-Frames, Skeleton-Keypoints     |ICCV       |-         |
|[SignGraph](https://openaccess.thecvf.com/content/CVPR2024/html/Gan_SignGraph_A_Sign_Sequence_is_Worth_Graphs_of_Nodes_CVPR_2024_paper.html)        |2024  | GCN + KNN   |27.4     |RGB-Frames     |CVPR      |[Available](https://github.com/gswycf/SignGraph)         |
|[PA-CMA](https://ieeexplore.ieee.org/abstract/document/10105511)          |2023  | CNN-TCN + BLSTM + CTC   | 28.7     |RGB-Frames     |IEEE TM       |-            |
|[CorrNet](https://openaccess.thecvf.com/content/CVPR2023/html/Hu_Continuous_Sign_Language_Recognition_With_Correlation_Network_CVPR_2023_paper.html)          |2023  | CNN + BLSTM   | 30.1     |RGB-Frames     |CVPR             | [Available](https://github.com/hulianyuyy/CorrNet)            |
|[SEN](https://ojs.aaai.org/index.php/AAAI/article/view/25164)         |2023  |CNN + BLSTM  |30.7     |RGB-Frames     |AAAI                |-            |
|[IterativeTrain](https://ieeexplore.ieee.org/document/8598757)    &#10018;        |2019  |CNN + BLSTM    |32.4      |RGB-Frames     |IEEE TM     |-            |
|[FCN](https://arxiv.org/pdf/2007.12402)    &#10018;      |2020  |FCN + GFE   |32.5      |RGB-Frames     |ECCV             |-            |
|[LS-HAN](https://ojs.aaai.org/index.php/AAAI/article/view/11903)    &#10018;      |2018  | CNN + LS + HAN  |39.4     |RGB-Frames     |AAAI                    |-           |
|[SubUNets](https://openaccess.thecvf.com/content_iccv_2017/html/Camgoz_SubUNets_End-To-End_Hand_ICCV_2017_paper.html)          |2017  |CNN + BLSTM    |41.0     |RGB-Frames     |ICCV                    |[Avaliable](https://github.com/neccam/SubUNets)            |

##### CSL-Daily SLR Table Notation:
&#10018; denotes the results were implemented by [BN-TIN-Transf](https://openaccess.thecvf.com/content/CVPR2021/html/Zhou_Improving_Sign_Language_Translation_With_Monolingual_Data_by_Sign_Back-Translation_CVPR_2021_paper.html)


### Results on CSL-Split I dataset
| Model Name      | Year | Architecture    |WER      | Model Input   | Conference/Journal	     | Code        |
|-----------------|------|-----------------|---------|---------------|-------------------------|-------------|
|[C²SLR + SRM](https://dl.acm.org/doi/pdf/10.1145/3640815)          |2024  | -   |0.68     |RGB-Frames     |ACM TOMM                |[Available](https://github.com/2000ZRL/LCSA_C2SLR_SRM)           |
|[STAMF](https://www.mdpi.com/1424-8220/22/17/6452)          |2022  |CNN + MHA + BLSTM + CTC| 0.7     |RGB-Frames, Skeleton-Keypoints     |Sensors                  |-            |
|[MSTNet](https://ui.adsabs.harvard.edu/abs/2024JEI....33b3059Z/abstract)          |2022  | CNN + Transformer   |0.7      |RGB-Frames     |ArXiv           |-            |
|[CorrNet](https://openaccess.thecvf.com/content/CVPR2023/html/Hu_Continuous_Sign_Language_Recognition_With_Correlation_Network_CVPR_2023_paper.html)          |2023  | CNN + BLSTM   | 0.8    |RGB-Frames     |CVPR             | [Available](https://github.com/hulianyuyy/CorrNet)            |
|[SEN](https://ojs.aaai.org/index.php/AAAI/article/view/25164)         |2023  |CNN + BLSTM  |0.8  |RGB-Frames     |AAAI                |-            |
|[C²SLR](https://openaccess.thecvf.com/content/CVPR2022/html/Zuo_C2SLR_Consistency-Enhanced_Continuous_Sign_Language_Recognition_CVPR_2022_paper.html)          |2022  | -   |0.9     |RGB-Frames     |CVPR                |-            |
|[CA-SignBERT](https://ieeexplore.ieee.org/abstract/document/9860060)          |2022  |  (3+2+1)D ResNet + BERT + BLSTM + CTC  |1.14     |RGB-Frames     |IEEE SPL             |-            |
|[STTN](https://link.springer.com/content/pdf/10.1007/s40747-023-00977-w.pdf)          |2023  | Transformer   | 1.2   |RGB-Frames     |CIS             |-            |
|[ST-GCN](https://ieeexplore.ieee.org/abstract/document/9534003?casa_token=thEBwazoFYIAAAAA:fUv87iU1KeXdvPKAlIDFwtqU3Ke3qa5VgySmVPiwAPcXCco_0T1DwRi2WaYyp6y2UAdUT46Pjw)         |2021  |GCN + BLSTM + LSTM  |1.3  |RGB-Frames     |IJCNN                |-            |
|[LCSA](https://drive.google.com/file/d/1lMWfTHN_iE2uzimMy3dLO-W-jm9YRm9f/view)          |2022  |VGGNet + Transformer   |1.4      |RGB-Frames     |ISCA                 |-            |
|[MultiModal SignBERT](https://ieeexplore.ieee.org/abstract/document/9635818)          |2021  | (3+2+1)DCNN + BERT + LSTM   |1.52      |RGB-Frames     |IEEE Access                  |-            |
|[VAC](https://openaccess.thecvf.com/content/ICCV2021/html/Min_Visual_Alignment_Constraint_for_Continuous_Sign_Language_Recognition_ICCV_2021_paper.html?ref=https://githubhelp.com)          |2021  |CNN + BLSTM + CTC    |1.6      |RGB-Frames     |ICCV                  |-            |
|[MSTN](https://arxiv.org/abs/2204.08747)          |2022  |Vit + GCN + Transformer + CTC    |1.9     |RGB-Frames, Skelenton-Keypoints     |ICCV                  |-            |
|[STMC](https://ojs.aaai.org/index.php/AAAI/article/view/7001)          |2020  |CNN + BLSTM + CTC    |2.1      |RGB-Frames     |AAAI                  |-            |
|[SignBERT](https://ieeexplore.ieee.org/abstract/document/9635818)          |2021  | (3+2+1)DCNN + BERT + LSTM   |2.26      |RGB-Frames     |IEEE Access                  |-            |
|[CMA-TE](https://ieeexplore.ieee.org/abstract/document/9090828)          |2020  |CNN + BLSTM    |2.4      |RGB-Frames     |IEEE Access             |-            |
|[EnStimCTC](https://ieeexplore.ieee.org/abstract/document/9393618?casa_token=BNvKjD_WV1EAAAAA:4OTJLsUOvBoFJP0AVshweZCFYZqRApBqY_78tkbAJGRLkJemt1wOQsXW9dXjbUWBThY_fUT0Gg)          |2021  | -  |2.41      |RGB-Frames     |IEEE TM            |-            |
|[mLTSF-Net](https://arxiv.org/pdf/2107.12762)          |2023  |FCN    |2.5      |RGB-Frames     |PR |-            |
|[CRKD](https://arxiv.org/pdf/2303.06820)         |2024  | ResNet50 + 2D-CNN + TSCM-2D CNN + CTC + MSE   |2.6      |RGB-Frames     | AJSE            |-            |
|[PiSLTRc](https://ieeexplore.ieee.org/abstract/document/9528010?casa_token=BGggtyj1xRwAAAAA:J9CxdVukp4J_Pqj_6A0Y_F0YYm9OgmHkHleLFaQ5TG9BI6gHVrHI_DdUkqvZC3LXPTqzAaVYDQ)          |2021  |CNN + Transformer    |2.8      |RGB-Frames     |IEEE TM          |-            |
|[FCN](https://arxiv.org/pdf/2007.12402)          |2020  |FCN + GFE   |3.0     |RGB-Frames     |ECCV             |-            |
|[SF-Net(ResNet-18)](https://arxiv.org/abs/1908.01341)          |2019  | 2D3DCNN + LSTM + BLSTM   |3.8    |RGB-Frames     |ArXiv                     |-            |
|[DPLD + TEM](https://ieeexplore.ieee.org/abstract/document/8784863?casa_token=PB1_yvyZouwAAAAA:lnaTKwd2UfJDjWkk2vkd08RMgtnDfbuWoE3eMNwjTHYGsYgK74XPlDS2osPhVvQaC2QdvKJHmA)          |2019  | I3D-BGRU-CTC    |4.7    |RGB-Frames     |ICME                     |-            |
|[DPLD](https://ieeexplore.ieee.org/abstract/document/8784863?casa_token=PB1_yvyZouwAAAAA:lnaTKwd2UfJDjWkk2vkd08RMgtnDfbuWoE3eMNwjTHYGsYgK74XPlDS2osPhVvQaC2QdvKJHmA)          |2019  | I3D-BGRU-CTC    |5.6     |RGB-Frames     |ICME                     |-            |
|[HLSTM-atten](https://ojs.aaai.org/index.php/AAAI/article/view/12235)          |2018  | 3D-CNN + LSTM    |10.2     |RGB-Frames     |AAAI                     |-            |
|[HLSTM](https://ojs.aaai.org/index.php/AAAI/article/view/12235)          |2018  | 3D-CNN + LSTM   |10.7     |RGB-Frames     |AAAI                     |-            |
|[CTF](https://dl.acm.org/doi/abs/10.1145/3240508.3240671?casa_token=V4-a-LYLGbIAAAAA:2xoc5DhlkaP8cnsupWmoajZxBdQdwVUJXdCs_vZxmfIDIVEavWC1SWCCwBMxdSbVHSPBrneFyRzGCw)          |2018  | C3D-ResNet + TConv + BGRU + CTC  |11.2     |RGB-Frames     |ACM MM                     |-            |


### Results on CSL-Split II dataset
| Model Name      | Year | Architecture    |WER      | Model Input   | Conference/Journal	     | Code        |
|-----------------|------|-----------------|---------|---------------|-------------------------|-------------|
|[CA-SignBERT](https://ieeexplore.ieee.org/abstract/document/9860060)          |2022  |  (3+2+1)D ResNet + BERT + BLSTM + CTC  |19.80     |RGB-Frames     |IEEE SPL             |-            |
|[SignBERT](https://ieeexplore.ieee.org/abstract/document/9635818)          |2021  | (3+2+1)DCNN + BERT + LSTM   |24.90      |RGB-Frames     |IEEE Access                  |-            |
|[STMC](https://ojs.aaai.org/index.php/AAAI/article/view/7001)          |2020  |CNN + BLSTM + CTC    |28.6      |RGB-Frames     |AAAI                  |-            |
|[Align-iOpt](https://ieeexplore.ieee.org/document/8954236)          |2019  | 3D-ResNet + BLSTM + Attention-LSTM + CTC|32.7     |RGB-Frames     |CVPR                     |-            |
|[WIC-NGC](https://ieeexplore.ieee.org/document/8919458)          |2019  | 3D-ResNet + BLSTM   | 50.9     |RGB-Frames     |BigMM       |-            |


**********************************************************************************************************************
### SLT Leaderboard

### Results on Phoenix-2014T dataset
#### Gloss-based
| Model Name      | Year | BLEU-4      | Model Input   | Conference/Journal     | Code    |
|-----------------|------|-------------|---------------|------------------------|---------|
|[TextCTC-SLT](https://arxiv.org/pdf/2412.09014) | 2025| 28.42 | RGB-Frames | COLING | [Available](https://github.com/Claire874/TextCTC-SLT)|
|[TwoStream-SLT](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6cd3ac24cdb789beeaa9f7145670fcae-Abstract-Conference.html)          |2022  |26.71       |RGB-Frames, Skeleton-Keypoints     | NeurIPS          |-        |
|[SLTUNET](https://arxiv.org/abs/2305.01778)         |2023  |26.00        |RGB-Frames     | ICLR                   |[Avaliable](https://github.com/bzhangGo/sltunet)         |
|[ConSLT](https://ieeexplore.ieee.org/document/10095466)         |2023  |25.48        |RGB-Frames     | ICASSP                  |[Avaliable](https://github.com/biaofuxmu/ConSLT)       |
|[MMTLB](https://openaccess.thecvf.com/content/CVPR2022/html/Chen_A_Simple_Multi-Modality_Transfer_Learning_Baseline_for_Sign_Language_Translation_CVPR_2022_paper.html)          |2022  |24.60        |RGB-Frames     | CVPR          |-        |
|[STMC-Transf](https://arxiv.org/abs/2004.00588)         |2020  |24.00        |RGB-Frames     | ArXiv                   |[Avaliable](https://github.com/kayoyin/transformer-slt)         |
|[STMC-T](https://ieeexplore.ieee.org/abstract/document/9354538?casa_token=i6bC3STkl88AAAAA:5cpJmkjzhXbXWrenMLHctPadd4xaj6-uA2jlqq-zwM6NHXp0n6VrTt3wkXUHg886-T7So9FYVg)          |2021  |23.65        |RGB-Frames     | IEEE TMM          |-        |
|[BN-TIN-Transf + BT](https://openaccess.thecvf.com/content/CVPR2021/html/Zhou_Improving_Sign_Language_Translation_With_Monolingual_Data_by_Sign_Back-Translation_CVPR_2021_paper.html)          |2021  |23.51        |RGB-Frames     | CVPR          |-        |
|[SimulSLT](https://dl.acm.org/doi/abs/10.1145/3474085.3475544?casa_token=a9gNRsIfavQAAAAA:-AyOjcYz8C2Q9rrOrQkYqTX2JY9nnPfdxFx9lzdM7vs53LyQr96Z4AbQYhzsSJUErgWqbyqZbhBYqw)        |2021  |23.14        |RGB-Frames     | ACM MM            |-       |
|[BN-TIN-Transf](https://openaccess.thecvf.com/content/CVPR2021/html/Zhou_Improving_Sign_Language_Translation_With_Monolingual_Data_by_Sign_Back-Translation_CVPR_2021_paper.html)          |2021  |22.54        |RGB-Frames     | CVPR          |-        |
|[BERT2RND](https://biblio.ugent.be/publication/8719287)         |2021  |22.47        |RGB-Frames     | MT Summit                   |[Avaliable](https://github.com/m-decoster/fpt4slt)        |
|[SL-Transf](https://openaccess.thecvf.com/content_CVPR_2020/papers/Camgoz_Sign_Language_Transformers_Joint_End-to-End_Sign_Language_Recognition_and_Translation_CVPR_2020_paper.pdf)         |2020  |22.45        |RGB-Frames     | CVPR           |[Avaliable](https://github.com/neccam/nslt)        |
[HST-GNN](https://openaccess.thecvf.com/content/WACV2022/html/Kan_Sign_Language_Translation_With_Hierarchical_Spatio-Temporal_Graph_Neural_Network_WACV_2022_paper.html)         |2022  |22.3       |RGB-Frames     | WACV                   |-        |
[NSLT](https://openaccess.thecvf.com/content_cvpr_2018/html/Camgoz_Neural_Sign_Language_CVPR_2018_paper.html)         |2018  |18.13       |RGB-Frames     | CVPR                   |[Avaliable](https://github.com/neccam/nslt)        |
[Facial-SLT](https://www.sciencedirect.com/science/article/abs/pii/S0925231221012698)         |2021  |10.89       |RGB-Frames     | Neurocomputing                |-        |


#### Gloss-free
| Model Name      | Year | BLEU-4      | Model Input   | Conference/Journal    | Code     |
|-----------------|------|-------------|---------------|-----------------------|----------|
|[CV-SLT](https://ojs.aaai.org/index.php/AAAI/article/view/29937)          |2022  |29.27       |RGB-Frames    | AAAI          |[Avaliable](https://github.com/rzhao-zhsq/CV-SLT)        |
|[MSKA-SLT](https://arxiv.org/abs/2405.05672)          |2024  |29.03       |Skeleton-Keypoints    | ArXiv          |[Avaliable](https://github.com/sutwangyan/MSKA)        |
|[TwoStream-SLT](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6cd3ac24cdb789beeaa9f7145670fcae-Abstract-Conference.html)          |2022  |28.95       |RGB-Frames, Skeleton-Keypoints     | NeurIPS          |-        |
|[SLTUNET](https://arxiv.org/abs/2305.01778)          |2023  |28.47        |RGB-Frames     | ICLR           |[Avaliable](https://github.com/bzhangGo/sltunet)         |
|[MMTLB](https://openaccess.thecvf.com/content/CVPR2022/html/Chen_A_Simple_Multi-Modality_Transfer_Learning_Baseline_for_Sign_Language_Translation_CVPR_2022_paper.html)          |2022  |28.39        |RGB-Frames     | CVPR          |-        |
|[IP-SLT](https://openaccess.thecvf.com/content/ICCV2023/html/Yao_Sign_Language_Translation_with_Iterative_Prototype_ICCV_2023_paper.html)          |2023  |27.97        |RGB-Frames     | ICCV          |-        |
|[C²RL](https://arxiv.org/abs/2408.09949)          |2024  |26.75        |RGB-Frames      | ArXiv          |-        |
|[VAP](https://fq.pkwyx.com/default/https/www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05894.pdf)          |2024  |26.16        |RGB-Frames     | ECCV          |-        |
|[EMF-SLT](https://ieeexplore.ieee.org/abstract/document/10446966?casa_token=n9nZhBsV_rQAAAAA:udlmgkU8simclxDuSQQ4tbVgLOHa_ha8fkp128G7YtzvbZnhDHbuZJTeJGD1op_RFerAgPlFAg)          |2024  |26.01        |RGB-Frames     | ICASSP          |-        |
|[SignBERT+](https://ieeexplore.ieee.org/abstract/document/10109128?casa_token=4tAMXuomxmYAAAAA:b__eqgfzL1o-6nOkZjKl8LKb4D4PCghwglhvyAPrtISy584_JQsCH76IB0_D0uSgW5cr76YC1w)          |2023  |25.70        |Skeleton-Keypoints      | TPAMI          |-        |
|[XmDA](https://arxiv.org/abs/2305.11096)          |2023  |25.36        |RGB-Frames     | ArXiv          |[Avaliable](https://github.com/Atrewin/SignXmDA)        |
|[SLT-CND](https://www.ijcai.org/proceedings/2023/0584.pdf)          |2023  |24.71        |RGB-Frames     | IJCAI          |[Avaliable](https://github.com/yp20000921/CND)        |
|[BN-TIN-Transf + BT](https://openaccess.thecvf.com/content/CVPR2021/html/Zhou_Improving_Sign_Language_Translation_With_Monolingual_Data_by_Sign_Back-Translation_CVPR_2021_paper.html)          |2021  |24.32        |RGB-Frames     | CVPR          |-        |
|[SimulSLT-CTL](https://aclanthology.org/2024.lrec-main.34/)          |2024  |24.20        |RGB-Frames     | LREC-COLING           |[Avaliable](https://github.com/tongsun99/CTL)         |
|[SLT-SEM](https://aclanthology.org/2024.acl-short.40/)          |2024  |24.12        |RGB-Frames     | ACL           |-         |
|[PET](https://aclanthology.org/2022.findings-acl.297/)          |2022  |24.02        |RGB-Frames     | ICLR           |-         |
|[SimulSLT-CTL++](https://aclanthology.org/2024.lrec-main.34/)          |2024  |23.75        |RGB-Frames     | LREC-COLING           |[Avaliable](https://github.com/tongsun99/CTL)         |
|[Online-CSLRT](https://arxiv.org/abs/2401.05336)          |2024  |23.69        |RGB-Frames     | ArXiv           |[Avaliable](https://github.com/FangyunWei/SLRT)         |
|[Signformer](https://arxiv.org/abs/2411.12901)          |2024  |23.43        |RGB-Frames     | ArXiv           |-        |
|[LLaVA-SLT](https://arxiv.org/abs/2412.16524)  |2024  |23.43  |RGB-Frames  | ArXiv  |-  |
|[LLM-SLT](https://openaccess.thecvf.com/content/CVPR2024/html/Gong_LLMs_are_Good_Sign_Language_Translators_CVPR_2024_paper.html)          |2024  |23.40        |RGB-Frames     | CVPR                   |-        |
|[FLa-LLM](https://arxiv.org/abs/2403.12556)          |2024  |23.09        |RGB-Frames     | LREC-COLING           |-        |
|[SignCL](https://arxiv.org/pdf/2405.14312) | 2024 | 22.74 | RGB-Frames | NeurIPS | [Available](https://github.com/JinhuiYE/SignCL) | 
|[Sign2GPT](https://arxiv.org/abs/2405.04164)          |2024  |22.52        |RGB-Frames     | ArXiv                |-        |
|[BN-TIN-Transf](https://openaccess.thecvf.com/content/CVPR2021/html/Zhou_Improving_Sign_Language_Translation_With_Monolingual_Data_by_Sign_Back-Translation_CVPR_2021_paper.html)          |2021  |21.68        |RGB-Frames     | CVPR          |-        |
|[ConSLT](https://ieeexplore.ieee.org/document/10095466)         |2023  |21.59        |RGB-Frames     | ICASSP                  |[Avaliable](https://github.com/biaofuxmu/ConSLT)       |
|[GFSLT-VLP](https://openaccess.thecvf.com/content/ICCV2023/html/Zhou_Gloss-Free_Sign_Language_Translation_Improving_from_Visual-Language_Pretraining_ICCV_2023_paper.html)         |2023  |21.44        |RGB-Frames     | ICCV                   |[Avaliable](https://github.com/zhoubenjia/GFSLT-VLP)        |
|[SL-Transf](https://openaccess.thecvf.com/content_CVPR_2020/papers/Camgoz_Sign_Language_Transformers_Joint_End-to-End_Sign_Language_Recognition_and_Translation_CVPR_2020_paper.pdf)         |2020  |21.32        |RGB-Frames     | CVPR                   |[Avaliable](https://github.com/neccam/nslt)        |
|[MCT-SLT](https://link.springer.com/chapter/10.1007/978-3-030-66823-5_18)         |2020  |18.30        |RGB-Frames     | ECCV                 |-      |
|[GASLT](https://openaccess.thecvf.com/content/CVPR2023/html/Yin_Gloss_Attention_for_Gloss-Free_Sign_Language_Translation_CVPR_2023_paper.html)         |2023  |15.74        |RGB-Frames     | CVPR            |[Avaliable](https://github.com/YinAoXiong/GASLT)       |
|[CSGCR](https://ieeexplore.ieee.org/document/9447976)        |2022  |15.18        |RGB-Frames     | IEEE            |-       |
|[Tspnet](https://proceedings.neurips.cc/paper/2020/hash/8c00dee24c9878fea090ed070b44f1ab-Abstract.html)         |2020  |13.41        |RGB-Frames     | NeurIPS               |[Avaliable](https://github.com/verashira/TSPNet)        |
|[Tokenization-SLT](https://ieeexplore.ieee.org/abstract/document/9320278?casa_token=gH_yVfmcWG0AAAAA:bRns7IujaRUnpfFkh5MznP2mTlcH315MmBMBBk5-uE_4XZhd2jVNLvi8H4vlzbkFNJtHKvdpdQ)        |2020  |13.25        |RGB-Frames     | FG            |-       |
|[UniGloR](https://arxiv.org/abs/2407.02854)       |2024  |12.86        |RGB-Frames     | ArXiv            |-       |
|[SimulSLT](https://dl.acm.org/doi/abs/10.1145/3474085.3475544?casa_token=a9gNRsIfavQAAAAA:-AyOjcYz8C2Q9rrOrQkYqTX2JY9nnPfdxFx9lzdM7vs53LyQr96Z4AbQYhzsSJUErgWqbyqZbhBYqw)       |2021  |12.27        |RGB-Frames     | ACM MM            |-       |
|[NSLT](https://openaccess.thecvf.com/content_cvpr_2018/html/Camgoz_Neural_Sign_Language_CVPR_2018_paper.html)         |2018  |9.58        |RGB-Frames     | CVPR                   |[Avaliable](https://github.com/neccam/nslt)        |


**********************************************************************************************************************
### Results on CSL-Daily dataset
#### Gloss-based
| Model Name      | Year | BLEU-4      | Model Input   | Conference/Journal      | Code                                    |
|-----------------|------|-------------|---------------|-------------------------|-----------------------------------------|
|[TwoStream-SLT](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6cd3ac24cdb789beeaa9f7145670fcae-Abstract-Conference.html)          |2022  |25.79       |RGB-Frames, Skeleton-Keypoints     | NeurIPS          |-        |
|[SLTUNET](https://arxiv.org/abs/2305.01778)         |2023  |23.76       |RGB-Frames     | ICLR                   |[Avaliable](https://github.com/bzhangGo/sltunet)  |
|[TextCTC-SLT](https://arxiv.org/pdf/2412.09014) | 2025| 22.47 | RGB-Frames | COLING | [Available](https://github.com/Claire874/TextCTC-SLT)|
|[MMTLB](https://openaccess.thecvf.com/content/CVPR2022/html/Chen_A_Simple_Multi-Modality_Transfer_Learning_Baseline_for_Sign_Language_Translation_CVPR_2022_paper.html)          |2022  |21.46        |RGB-Frames     | CVPR          |-        |
|[BN-TIN-Transf + BT](https://openaccess.thecvf.com/content/CVPR2021/html/Zhou_Improving_Sign_Language_Translation_With_Monolingual_Data_by_Sign_Back-Translation_CVPR_2021_paper.html)          |2021  |19.67       |RGB-Frames     | CVPR          |-        |
[HST-GNN](https://openaccess.thecvf.com/content/WACV2022/html/Kan_Sign_Language_Translation_With_Hierarchical_Spatio-Temporal_Graph_Neural_Network_WACV_2022_paper.html)         |2022  |17.8       |RGB-Frames     | WACV                   |-        |
|[BN-TIN-Transf](https://openaccess.thecvf.com/content/CVPR2021/html/Zhou_Improving_Sign_Language_Translation_With_Monolingual_Data_by_Sign_Back-Translation_CVPR_2021_paper.html)          |2021  |16.25        |RGB-Frames     | CVPR          |-        |
|[NSLT + Luong](https://openaccess.thecvf.com/content_cvpr_2018/html/Camgoz_Neural_Sign_Language_CVPR_2018_paper.html) 	&#x2726;        |2018  |11.03        |RGB-Frames     | CVPR                   |[Avaliable](https://github.com/neccam/nslt)        |


#### Gloss-free
| Model Name      | Year | BLEU-4      | Model Input   | Conference/Journal     | Code                                    |
|-----------------|------|-------------|---------------|------------------------|-----------------------------------------|
|[MSKA-SLT](https://arxiv.org/abs/2405.05672)          |2024  |25.52       |Skeleton-Keypoints    | ArXiv          |[Avaliable](https://github.com/sutwangyan/MSKA)        |
|[TwoStream-SLT](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6cd3ac24cdb789beeaa9f7145670fcae-Abstract-Conference.html)          |2022  |25.42       |RGB-Frames, Skeleton-Keypoints     | NeurIPS          |-        |
|[SLTUNET](https://arxiv.org/abs/2305.01778)         |2023  |25.01        |RGB-Frames     | ICLR                   |[Avaliable](https://github.com/bzhangGo/sltunet) |
|[MMTLB](https://openaccess.thecvf.com/content/CVPR2022/html/Chen_A_Simple_Multi-Modality_Transfer_Learning_Baseline_for_Sign_Language_Translation_CVPR_2022_paper.html)          |2022  |23.92        |RGB-Frames     | CVPR          |-        |
|[C²RL](https://arxiv.org/abs/2408.09949)          |2024  |21.61        |RGB-Frames      | ArXiv          |-        |
|[XmDA](https://arxiv.org/abs/2305.11096)          |2023  |21.58        |RGB-Frames     | ArXiv          |[Avaliable](https://github.com/Atrewin/SignXmDA)        |
|[BN-TIN-Transf + BT](https://openaccess.thecvf.com/content/CVPR2021/html/Zhou_Improving_Sign_Language_Translation_With_Monolingual_Data_by_Sign_Back-Translation_CVPR_2021_paper.html)          |2021  |21. 34       |RGB-Frames     | CVPR          |-        |
|[VAP](https://fq.pkwyx.com/default/https/www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05894.pdf)          |2024  |20.85        |RGB-Frames     | ECCV          |-        |
|[LLaVA-SLT](https://arxiv.org/abs/2412.16524)  |2024  |20.42  |RGB-Frames  | ArXiv  |-  |
|[IP-SLT](https://openaccess.thecvf.com/content/ICCV2023/html/Yao_Sign_Language_Translation_with_Iterative_Prototype_ICCV_2023_paper.html)          |2023  |16.72      |RGB-Frames     | ICCV          |-        |
|[SLT-CND](https://www.ijcai.org/proceedings/2023/0584.pdf)          |2023  |16.61        |RGB-Frames     | IJCAI          |[Avaliable](https://github.com/yp20000921/CND)        |
|[SignCL](https://arxiv.org/pdf/2405.14312) | 2024 | 16.16 | RGB-Frames | NeurIPS | [Available](https://github.com/JinhuiYE/SignCL) | 
|[LLM-SLT](https://openaccess.thecvf.com/content/CVPR2024/html/Gong_LLMs_are_Good_Sign_Language_Translators_CVPR_2024_paper.html)          |2024  |15.75       |RGB-Frames     | CVPR                   |-        |
|[Sign2GPT](https://arxiv.org/abs/2405.04164)          |2024  |15.40        |RGB-Frames     | ArXiv                |-        |
|[ConSLT](https://ieeexplore.ieee.org/document/10095466)         |2023  |14.53        |RGB-Frames     | ICASSP                  |[Avaliable](https://github.com/biaofuxmu/ConSLT)       |
|[FLa-LLM](https://arxiv.org/abs/2403.12556)          |2024  |14.20        |RGB-Frames     | LREC-COLING           |-        |
|[BN-TIN-Transf](https://openaccess.thecvf.com/content/CVPR2021/html/Zhou_Improving_Sign_Language_Translation_With_Monolingual_Data_by_Sign_Back-Translation_CVPR_2021_paper.html)          |2021  |13.19        |RGB-Frames     | CVPR          |-        |
|[GFSLT-VLP](https://openaccess.thecvf.com/content/ICCV2023/html/Zhou_Gloss-Free_Sign_Language_Translation_Improving_from_Visual-Language_Pretraining_ICCV_2023_paper.html)         |2023  |11.00        |RGB-Frames     | ICCV                   |[Avaliable](https://github.com/zhoubenjia/GFSLT-VLP)        |
|[NSLT + Luong](https://openaccess.thecvf.com/content_cvpr_2018/html/Camgoz_Neural_Sign_Language_CVPR_2018_paper.html) 	&#x2726;        |2018  |7.56        |RGB-Frames     | CVPR                   |[Avaliable](https://github.com/neccam/nslt)        |
|[GASLT](https://openaccess.thecvf.com/content/CVPR2023/html/Yin_Gloss_Attention_for_Gloss-Free_Sign_Language_Translation_CVPR_2023_paper.html)         |2023  |4.07        |RGB-Frames     | CVPR            |[Avaliable](https://github.com/YinAoXiong/GASLT)       |
|[SL-Transf](https://openaccess.thecvf.com/content_CVPR_2020/papers/Camgoz_Sign_Language_Transformers_Joint_End-to-End_Sign_Language_Recognition_and_Translation_CVPR_2020_paper.pdf)  &#x2749;       |2020  |3.03       |RGB-Frames     | CVPR                   |[Avaliable](https://github.com/neccam/nslt)        |
|[Tspnet](https://proceedings.neurips.cc/paper/2020/hash/8c00dee24c9878fea090ed070b44f1ab-Abstract.html) &#x2605;        |2020  |2.97        |RGB-Frames     | NeurIPS               |[Avaliable](https://github.com/verashira/TSPNet)        |

##### CSL-Daily Gloss-Free Table Notation:

&#x2726; denotes results reproduced by [`BN-TIN-Transf`](https://openaccess.thecvf.com/content/CVPR2021/html/Zhou_Improving_Sign_Language_Translation_With_Monolingual_Data_by_Sign_Back-Translation_CVPR_2021_paper.html)

&#x2749; denotes results reproduced by [`GFSLT-VLP`](https://openaccess.thecvf.com/content/ICCV2023/html/Zhou_Gloss-Free_Sign_Language_Translation_Improving_from_Visual-Language_Pretraining_ICCV_2023_paper.html)

&#x2605; denotes results reproduced by [`GASLT`](https://openaccess.thecvf.com/content/CVPR2023/html/Yin_Gloss_Attention_for_Gloss-Free_Sign_Language_Translation_CVPR_2023_paper.html)


**********************************************************************************************************************
### Results on How2Sign dataset
#### Gloss-free
| Model Name      | Year | BLEU-4      | Model Input   | Conference/Journal     | Code                                    |
|-----------------|------|-------------|---------------|------------------------|-----------------------------------------|
|[VAP](https://fq.pkwyx.com/default/https/www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05894.pdf)          |2024  |12.87        |RGB-Frames     | ECCV          |-        |
|[YouTube-ASL](https://proceedings.neurips.cc/paper_files/paper/2023/hash/5c61452daca5f0c260e683b317d13a3f-Abstract-Datasets_and_Benchmarks.html)          |2024  |12.39        |RGB-Frames     | NeurIPS          |-        |
|[SLT-SEM](https://aclanthology.org/2024.acl-short.40/)        |2024  |11.7        |RGB-Frames     | ACL              |[Avaliable](https://github.com/yhamidullah/sem-slt)        |
|[FLa-LLM](https://arxiv.org/abs/2403.12556)          |2024  |9.66        |RGB-Frames     | LREC-COLING           |-        |
|[SLT-IV](https://openaccess.thecvf.com/content/CVPR2023W/WiCV/html/Tarres_Sign_Language_Translation_from_Instructional_Videos_CVPRW_2023_paper.html)        |2023  |8.03        |RGB-Frames     | CVPRW              |[Avaliable](https://imatge-upc.github.io/slt_how2sign_wicv2023/)        |
|[GloFE-VN](https://arxiv.org/abs/2305.12876)        |2023  |2.24        |RGB-Frames     | ArXiv              |[Avaliable](https://github.com/HenryLittle/GloFE)        |
|[UniGloR](https://arxiv.org/abs/2407.02854)       |2024  |2.22        |RGB-Frames     | ArXiv            |-       |
|[TF-H2S](https://imatge.upc.edu/web/sites/default/files/pub/xCabot22.pdf)          |2022  |2.21        |RGB-Frames     | -           | -        |


**********************************************************************************************************************
### Results on OpenASL dataset
#### Gloss-free
| Model Name      | Year | BLEU-4      | Model Input   | Conference/Journal     | Code                                    |
|-----------------|------|-------------|---------------|------------------------|-----------------------------------------|
|[C²RL](https://arxiv.org/abs/2408.09949)          |2024  |13.21        |RGB-Frames      | ArXiv          |-        |
|[GloFE-VN](https://arxiv.org/abs/2305.12876)        |2023  |7.06        |RGB-Frames     | ArXiv              |[Avaliable](https://github.com/HenryLittle/GloFE)        |
|[OpenASL](https://arxiv.org/abs/2205.12870)        |2022  |6.72        |RGB-Frames     | EMNLP              |[Avaliable](https://github.com/chevalierNoir/OpenASL)        |
|[I3D-Transformer](https://arxiv.org/abs/2205.12870)        |2022  |5.66        |RGB-Frames     |-              |-        |
|[NSLT](https://openaccess.thecvf.com/content_cvpr_2018/html/Camgoz_Neural_Sign_Language_CVPR_2018_paper.html) &#10066;        |2018  |4.58        |RGB-Frames     | CVPR                   |[Avaliable](https://github.com/neccam/nslt)        |

##### OpenASL Gloss-Free Table Notation:

&#10066; denotes results reproduced by [`OpenASL`](https://arxiv.org/abs/2205.12870)

**********************************************************************************************************************
### SLP Leaderboard

### Results on Phoenix-2014T dataset

#### Gloss to Pose
| Model Name      | Year | BLEU-4      | WER       | DTW-P       | Conference/Journal     | Code         |
|-----------------|------|-------------|-----------|-------------|------------------------|--------------|
| [FS-NET](https://openaccess.thecvf.com/content/CVPR2022/papers/Saunders_Signing_at_Scale_Learning_to_Co-Articulate_Signs_for_Large-Scale_Photo-Realistic_CVPR_2022_paper.pdf) | 2022 | 18.78  | - | -  | CVPR |  -   |
| [Adversarial Training](https://arxiv.org/abs/2008.12405) | 2020 | 11.7  | - | - | BMVC |  -   |
| [Progressive Transf](https://arxiv.org/abs/2004.14874) | 2020 | 10.43  | - | -  | ECCV |  [Avaliable](https://github.com/BenSaunders27/ProgressiveTransformersSLP)   |
| [NSLP-G](https://www.bmvc2021-virtualconference.com/assets/papers/1102.pdf) | 2021 | 9.39  | - | - | BMVC |  -   |
| [LVMCN](https://arxiv.org/abs/2412.16944) | 2024 | 9.36  | - | 10.14  | ArXiv |  -   |
| [Data-Driven](https://ieeexplore.ieee.org/document/10581995) | 2024 | 9.17  | - | - | SEM |  -   |
| [Sign-IDD](https://arxiv.org/abs/2412.13609) | 2024 | 9.08  | - | - | ArXiv |  -   |
| [GEN-OBT](https://dl.acm.org/doi/abs/10.1145/3503161.3547830?casa_token=_MlXpMYEzNoAAAAA:2L5Ktxo-G1ygXpL4LQnPcYmTPKrUiJU5wKUIYATaillFPDL90iyz5Q7egp_9_aX6WcnsCXdGIZ8gWA) | 2022 | 8.01  | 81.78 | 10.07  | ACM |  -   |
| [GCDM](https://dl.acm.org/doi/abs/10.1145/3663572) | 2024 | 7.91  | 81.94 | 11.10  | ACM |  -   |
| [G2P-DDM](https://arxiv.org/abs/2208.09141) | 2024 | 7.50 | - | -  | AAAI |  -   |
| [NAT-EA](https://dl.acm.org/doi/abs/10.1145/3474085.3475463?casa_token=anYLezVhxNYAAAAA:XaOvgclXT1VHV0vE6IbfECNS3YpPp5JbgXHb42s5KvJnG5WUD11Yh3xsXRVZDRBngQNFYExPmBvO6g) | 2021 | 6.66  | 82.01 | -  | ACM MM |  -   |
| [NAT-AT](https://dl.acm.org/doi/abs/10.1145/3474085.3475463?casa_token=anYLezVhxNYAAAAA:XaOvgclXT1VHV0vE6IbfECNS3YpPp5JbgXHb42s5KvJnG5WUD11Yh3xsXRVZDRBngQNFYExPmBvO6g) | 2021 | 5.53  | 88.15 | -  | ACM |  -   |



#### Text to Pose
| Model Name      | Year | BLEU-4      | DTW-P     | with Gloss   | Conference/Journal     | Code         |
|-----------------|------|-------------|-----------|--------------|------------------------|--------------|
| [Spoken2Sign](https://arxiv.org/pdf/2401.04730) | 2024 | 25.46  | - | ✅ | ECCV |  -   |
| [SignDiff](https://arxiv.org/pdf/2308.16082) | 2023 | 22.15  | - | ❌ | ArXiv |  -   |
| [FS-NET](https://openaccess.thecvf.com/content/CVPR2022/papers/Saunders_Signing_at_Scale_Learning_to_Co-Articulate_Signs_for_Large-Scale_Photo-Realistic_CVPR_2022_paper.pdf) | 2022 | 21.10  | - |  ❌ | CVPR |  -   |
| [SignGen](https://eccv.ecva.net/virtual/2024/poster/2581) | 2024 | 19.71  | - | ❌ | ECCV |  -   |
| [T2S-GPT](https://arxiv.org/abs/2406.07119) | 2024 | 11.87 | - |  ❌ | ArXiv |  -   |
| [NSLP-G (+ Finetuning)](https://www.bmvc2021-virtualconference.com/assets/papers/1102.pdf) | 2021 | 11.07 | - |  ❌ | BMVC |  -   |
| [NSLP-G](https://www.bmvc2021-virtualconference.com/assets/papers/1102.pdf) | 2021 | 10.95 | - |  ❌ | BMVC |  -   |
| [Adversarial Training](https://arxiv.org/abs/2008.12405) | 2020 | 10.81 | - |  ❌ | BMVC |  -   |
| [Progressive Transf](https://arxiv.org/abs/2004.14874) | 2020 | 10.51  | - |  ❌ | ECCV |  [Avaliable](https://github.com/BenSaunders27/ProgressiveTransformersSLP)   |
| [Progressive Transf](https://arxiv.org/abs/2004.14874) | 2020 | 9.68  | - |  ✅ | ECCV |  [Avaliable](https://github.com/BenSaunders27/ProgressiveTransformersSLP)   |
| [Data-Driven](https://ieeexplore.ieee.org/document/10581995) | 2024 | 9.20  | - | ❌ | SEM |  -   |
| [IFECE (MFs)](https://openaccess.thecvf.com/content/CVPR2022/papers/Saunders_Signing_at_Scale_Learning_to_Co-Articulate_Signs_for_Large-Scale_Photo-Realistic_CVPR_2022_paper.pdf) | 2023 | 8.19  | - | ✅ | SEM |  -   |
| [SignVQNet](https://arxiv.org/abs/2309.12179) | 2024 | 6.85  | - | ❌ | FG |  -   |
| [IFECE (MFs + FI + AUs)](https://openaccess.thecvf.com/content/CVPR2022/papers/Saunders_Signing_at_Scale_Learning_to_Co-Articulate_Signs_for_Large-Scale_Photo-Realistic_CVPR_2022_paper.pdf) | 2023 | 5.76  | - | ✅ | SEM |  -   |
| [MS2SL](https://arxiv.org/abs/2407.12842) | 2024 | 4.26  | - | ❌ | ArXiv |  -   |
  


### Results on CSL-Daily dataset

#### Text to Pose
| Model Name      | Year | BLEU-4      | DTW-P     | with Gloss   | Conference/Journal     | Code         |
|-----------------|------|-------------|-----------|--------------|------------------------|--------------|
| [Spoken2Sign](https://arxiv.org/pdf/2401.04730) | 2024 | 21.44  | - | -  | ✅ | ECCV |  -   |
