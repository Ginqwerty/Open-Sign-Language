# SLRTP2025 Sign Language Production Challenge: Methodology, Results and Future Work

## Introduction
The 2025 Sign Language Production Challenge, the first Sign Language Production Challenge, was launched to establish a standardized benchmark for converting spoken-language sentences into continuous sign-language skeleton sequences (Text-to-Pose) and to enable fair, reproducible comparisons across different deep learning–based SLP systems. Held as part of the third SLRTP Workshop at CVPR 2025, it evaluated Text-to-Pose architectures on the publicly available RWTH-PHOENIX-Weather-2014T dataset and a custom hidden test set drawn from similar weather-broadcast data. By defining a suite of quantitative metrics (including BLEU, DTW-MJE and a novel “total distance” expressiveness score) and releasing a high-quality skeleton extraction and evaluation pipeline, the challenge addresses the field’s prior lack of unified evaluation protocols and provides a consistent baseline for future research in sign language generation.

Here are the key statistics for the first Sign Language Production Challenge:
- A total of 33 participants took part in the competition.
- Across the development and final phases, they submitted 231 solutions.
- The challenge ran for 49 days, from January 13 to March 3, 2025.


## Analysis of the Top 3 Teams

### Team 1 (USTC-MoE, 1st Place)
A retrieval-based framework built around gloss annotations. Their pipeline comprises four modules:
1. **Text2Gloss:**  
   Fine-tune a multilingual XLM-R model to convert input sentences into gloss sequences.
2. **Sign2Gloss:**  
   Train a Continuous Sign Language Recognition (CSLR) model to label each frame of 3D pose data with glosses.
3. **Gloss-Pose Dictionary Construction:**  
   Use the CSLR model to segment all training poses into sub-pose clips, each keyed by its gloss.
4. **Text2Sign Retrieval:**  
   At inference, translate text to gloss, retrieve the corresponding pose clips from the dictionary, and concatenate them to form the final sign sequence.  
   This approach uses ~355.9 M parameters, requires no additional data augmentation, and guarantees high-fidelity, natural transitions by grounding each gloss in real human motion.

### Team 2 (hfut-lmc, 2nd Place)
A fully generative, diffusion-based Text-Driven Conditional Diffusion Model (TCDM) that maps text directly to pose sequences without gloss supervision:
- **Forward/Reverse Diffusion:** Add Gaussian noise to ground-truth poses over 1,000 steps, then learn a denoiser _D(pₜ, g)_ conditioned on text features _g_ to recover clean poses.  
- **Denoiser Architecture:** Sequential sub-stages of linear embedding, sinusoidal positional encoding, multi-head self-attention, and cross-attention with the text condition.  
- **Losses:** Joint position L1 loss plus a bone-orientation loss (λ = 0.1) to ensure accurate joint placement and realistic limb articulation.  
- **Text Encoder:** Expanded to 4 layers, 8 heads, and 1,024-dim embeddings; trained with Adam at 1e-3.  
This end-to-end model synthesizes coherent sign motion directly from text, mitigating regression-to-mean artifacts via its combined loss design.

### Team 3 (Hacettepe, 3rd Place)
A gloss-free, transformer-based method that learns a compact latent pose space via an autoencoder, then maps text into that space:
1. **Latent Pose Autoencoder:**  
   Disentangles 534-dim input (face, body, hands) into four regions, encoding into an 80-dim latent vector with region-specific L1 reconstruction and encoder-weight regularization.
2. **Non-Autoregressive Transformer:**  
   Uses a 3-layer encoder + 6-layer decoder to predict all latent pose codes in parallel, taking 768-dim BERT sentence vectors (reduced to 512 dims) as input.
3. **Training:**  
   First optimize L1 reconstruction loss between predicted and true latents; then apply channel-wise KL divergence for articulator-aware regularization—entirely without gloss annotations.

This approach synthesizes novel pose sequences in a learned latent space, striking a balance between accuracy and efficiency.

