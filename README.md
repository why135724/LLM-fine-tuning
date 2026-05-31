本框架使用官方PEFT库，完成对于qwen1.5-qwen2.5的LoRA微调。针对于明确知道漏洞类型的内存泄露，会有更好的效果，即LLM的微调适合来产生“专才”。同时测试针对于humaneval数据集的SFT，发现微调之后性能反而下降，还是要从基模型训练入手。

安装环境：
1.conda create -n llm python=3.10

2.conda install pytorch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 pytorch-cuda=12.1 -c pytorch -c nvidia

3.pip install -r requirements.txt

运行
1.create_data.py 生成漏洞检测训练数据集

2.create_data_root.py 生成根因定位训练集&测试集数据集

3.create_data_test.py 生成漏洞检测测试数据集

4.train_linjiu.py 训练漏洞检测模型

5.train_linjiu_root.py 训练根因定位模型

6.predict_linjiu.py 测试漏洞检测模型

7.predict_linjiu_root.py 测试根因定位模型


前端最后呈现测试时间应该是  调前端框架时间+运行create_data_test.py时间+运行predict_linjiu.py时间

# 🛠️ LoRA Fine-Tuning Framework for Qwen (1.5 / 2.5)

**Focus:** Specialized vulnerability-aware fine-tuning with PEFT (LoRA)  
**Target Models:** Qwen-1.5, Qwen-2.5  
**Application Scenarios:** Memory leak detection & root cause localization  

---

## 🧠 Motivation

Large Language Models excel as generalists—but struggle with highly specialized tasks.  
This framework demonstrates that **LoRA fine-tuning** makes LLMs effective **specialists**, especially when the task is well-defined and narrowly scoped.

### ✅ Key Insight
Fine-tuning Qwen models via LoRA significantly improves performance on **explicit memory leak vulnerability detection**.

### ❌ Conversely
Naive SFT on HumanEval-style code generation led to performance degradation, reinforcing that:

> **"Fine-tuning amplifies specialization—not generalization."**

For broad reasoning and code synthesis, base model pretraining remains superior.

---

## 🧩 What This Framework Does

- Uses official **PEFT** library for efficient LoRA adaptation  
- Supports **Qwen-1.5** and **Qwen-2.5**  
- Provides end-to-end pipelines for:
  - 🔍 Vulnerability detection (memory leaks)
  - 🧭 Root cause localization  
- Includes **dataset construction**, **training**, **inference**, and **evaluation**

---

## 🏗️ Project Structure

llm-lora-finetune/
├── create_data.py # Build vulnerability detection training set
├── create_data_root.py # Build root cause localization train/test sets
├── create_data_test.py # Build vulnerability detection test set
├── train_linjiu.py # Train vulnerability detection model
├── train_linjiu_root.py # Train root cause localization model
├── predict_linjiu.py # Inference for vulnerability detection
├── predict_linjiu_root.py # Inference for root cause localization
├── requirements.txt
└── README.md
---

## ⚙️ Environment Setup
bash
1. Create conda environment
conda create -n llm python=3.10
conda activate llm
2. Install PyTorch with CUDA support
conda install pytorch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 pytorch-cuda=12.1 \
-c pytorch -c nvidia
3. Install Python dependencies
pip install -r requirements.txt
---

## 🚀 Quick Start

### 1️⃣ Prepare Training Data
bash
python create_data.py # Vulnerability detection training data
python create_data_root.py # Root cause localization data
### 2️⃣ Train Models
bash
python train_linjiu.py # Train vulnerability detection model
python train_linjiu_root.py # Train root cause localization model
### 3️⃣ Run Inference
bash
python predict_linjiu.py # Test vulnerability detection
python predict_linjiu_root.py # Test root cause localization
---

## ⏱️ Frontend Timing Notes

To accurately reflect end-to-end latency in the UI, the frontend should compute:
Total Time =
Frontend Framework Latency
create_data_test.py Execution Time
predict_linjiu.py Execution Time

This ensures realistic performance reporting for vulnerability detection workflows.

---

## 📊 Experimental Findings

| Task                        | Base Model | LoRA Fine-Tuned |
|-----------------------------|------------|-----------------|
| Memory Leak Detection        | ❌ Poor    | ✅ Strong        |
| Root Cause Localization      | ⚠️ Limited | ✅ Improved      |
| HumanEval Code Generation    | ✅ Good    | ❌ Worse         |

---

## 🧠 Conclusion

> **LoRA fine-tuning is highly effective for narrow, well-defined domains** (e.g., known vulnerability types),  
> but **not recommended** for general-purpose code reasoning without retraining from base weights.

---

## 📌 Future Work

- Extend to other vulnerability classes (buffer overflows, use-after-free)
- Compare **QLoRA vs. full LoRA**
- Explore **multi-task specialization**
- Investigate **catastrophic forgetting mitigation**

---

## 📬 Contact

For questions, suggestions, or collaborations, feel free to reach out.

<p align="center">
⭐ If this helps your research or engineering work, consider starring the repo! ⭐
</p>
