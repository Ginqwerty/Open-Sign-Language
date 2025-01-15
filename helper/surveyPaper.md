# Abstract

# Introduction

# Related Work
- Existing survey works typically focus on SLR, SLT, and SLP.
- Provide a general overview of some survey papers.
- Previous survey papers have provided an overview of sign language research over the past decade and proposed challenges and future directions as they see fit. However, their discussions on sign language datasets are minimal, with some only offering sporadic introductions to commonly used sign language datasets.
- [de-sisto-etal-2022-challenges] is the most similar to our work, but it primarily focuses on discussing annotation formats.
- In contrast, our work aims on datasets.

# Commonly Used Dataset Introduction
Due to space constraints, we introduce only a few commonly used Isolated Sign Language Datasets and Continuous Sign Language Datasets here. For more comprehensive information about sign language datasets, please refer to our GitHub link.
- Isolated Sign Language Dtasets
- Continuous Sign Language Datasets
- Sign Language Statistic Table

# Challenges and Future Direction
## Challenges
- Download issue.
- The language distribution of commonly used sign language datasets is uneven, with a particular focus on GDS, CSL, and ASL.
    - The global distribution heat map of sign language datasets.
- Due to the time-consuming and labor-intensive nature of annotating sign language datasets, high-quality datasets are often relatively small. For instance, high-quality datasets such as Phoenix2014T contain only a limited amount of data. Such a scale is insufficient to meet the demands of deep learning and large language models (LLMs).
- Different datasets use various annotation formats and are stored in different file formats, so cross-dataset training requires additional data preprocessing.

# Annotation 
- Based on an analysis of several commonly used datasets, we have identified their strengths and outlined the data content that future sign language datasets are recommended to include to support diverse sign language research.
  - Sign Language Video/Frames
  - Video Name
  - Start Time
  - End Time
  - Gloss(Not Necessary)  
  - Translation Text
 
 ## 1. Signer Level
Attributes describing the signers, crucial for analyzing variation in signing styles and personalization:
- **Height/Weight**: Influences signing space and gesture size, relevant for pose estimation.
- **Hand Dominance (Left/Right)**: Impacts signing directionality and gesture patterns.
- **Gender**: May correlate with signing style or cultural variations.
- **Age**: Affects signing fluency and style (e.g., children vs. adults).
- **Language Background**: Indicates native fluency or learned signing; vital for multilingual research.
- **Deaf/Hard of Hearing/Non-Deaf**: Influences signing proficiency and usage.

 ## 2. Annotation Level
Details describing the temporal and semantic information of signing sequences:
- **Time Alignment**: Essential for mapping signs to spoken language or glosses.
- **Sentence-Level Annotations**: Supports continuous signing translation and contextual understanding.
- **Word/Gloss-Level Annotations**: Fine-grained labels for recognizing specific signs.
- **Hand Keypoints (Pose)**: Tracks hand movements, aiding gesture recognition.
- **Facial Skeleton Keypoints**: Captures expressions integral to sign language grammar.
- **Body Keypoints**: Full-body motion tracking for complex gestures and non-manual signs.
- **Sign Boundary Information**: Distinguishes isolated signs within continuous signing.
- **Emotion Tags**: Links emotional expressions to signing, relevant for sentiment analysis.
- **Sign Speed/Intensity**: Tracks fluency and expressiveness, useful for speech-rate studies.

 ## 3. Recording Environment
Attributes of the data collection environment for reproducibility and robustness:
- **Camera Type and Resolution**: Impacts data quality and model accuracy.
- **Lighting Conditions**: Crucial for robust computer vision models.
- **Recording Angles**: Multi-angle views aid 3D modeling and pose recovery.
- **Recording Device Setup**: Monoscopic, stereoscopic, or depth cameras (e.g., RGB-D).

 ## 4. Additional Features for Multimodal Research
Attributes for research involving other modalities:
- **Audio Alignment**: Supports research on speech-to-sign translation.
- **Depth Data**: Adds 3D spatial information for precise hand tracking.
- **Heatmaps**: Captures areas of focus or intensity during signing.
- **Eye Gaze Tracking**: Essential for understanding conversational turn-taking.
- **Environmental Sounds**: Includes ambient noises for real-world scenarios.


****
### Note from Ni
- 推荐处理数据的步骤：
  - Sentence-Level Alignment: 句子级的翻译或信息对齐
  - 移除长时间没有手语动作的帧数，或者按照结尾动作进行视频分割
  - 移除不清晰的视频：确保视频清晰且动作明确
  - 数据平衡：确保不同类别（如单词、句子）和语境（如日常对话、专业领域）的平衡分布，区域方言：考虑同一手语内的地域差异
- 必须需要包含的信息：
  - Sign Language Video/Frames
  - Video Name 
  - Translation Text
  - Multimodal Features: Skeleton-Key Point Data(整体的，脸部局部的，左右手局部的）
- 推荐包含的数据：
  - Gloss(可以提供部分，做self- supervise learnign)
  - Word-Level Alignment

# Conclusion

# Reference
