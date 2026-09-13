# 🌿 LeafLens AI

### A CNN-Based Plant Disease & Health Detection System

LeafLens AI is a deep learning-based web application designed to detect plant diseases and identify healthy leaves from leaf images.

The project uses CNNs and Transfer Learning with the PlantVillage dataset containing 54,305 images across 38 classes.

## ✨ Features

- 🌿 Plant disease and healthy-leaf detection
- 📷 Leaf image upload and prediction
- 🧠 CNN-based deep learning
- 🔄 Transfer Learning
- 📊 Model evaluation and comparison
- 🔍 Confusion matrix and misclassification analysis

## 🔗 Project

- [Kaggle Notebook](https://www.kaggle.com/code/minahilyaqoob/plant-disease-detection-using-cnn)

## 🧠 Models

The following models were trained and compared:

- CNN From Scratch
- MobileNetV2
- EfficientNetB0
- ResNet50

### 🏆 Best Model

**ResNet50**

- Test Accuracy: **95.24%**
- Macro F1-Score: **94.74%**

## 🛠️ Tech Stack

**Machine Learning:** Python, TensorFlow, Keras, CNN, Transfer Learning

**Computer Vision & Data:** NumPy, Pandas, Scikit-learn, PIL, Matplotlib, Seaborn

**Frontend:** React, TypeScript, Vite, CSS

**Backend:** FastAPI, Uvicorn

**Tools:** Kaggle, VS Code, Git, GitHub

## 📁 Project Structure

```text
LeafLens-AI/
├── backend/
├── frontend/
├── config.json
├── model.weights.h5
└── README.md
