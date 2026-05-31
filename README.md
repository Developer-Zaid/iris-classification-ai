# 🌸 Iris Flower Classification Using AI

## 📌 Overview

This project was developed as part of **Week 2 of the Artificial Intelligence Internship Program at DecodeLabs**.

The objective of this project is to build a machine learning classification model that can identify different species of Iris flowers based on their physical characteristics. The project demonstrates the complete supervised learning workflow, including data preprocessing, model training, prediction, and evaluation.

---

## 🎯 Project Objective

Build a basic classification model using a small dataset by:

- Loading and understanding a dataset
- Splitting data into training and testing sets
- Applying a classification algorithm
- Evaluating model performance

---

## 📊 Dataset Information

The project uses the **Iris Dataset**, one of the most popular datasets for machine learning beginners.

### Dataset Statistics

| Attribute     | Value |
| ------------- | ----- |
| Total Samples | 150   |
| Features      | 4     |
| Classes       | 3     |

### Flower Classes

- Setosa
- Versicolor
- Virginica

### Features Used

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

---

## ⚙️ Technologies Used

- Python 3
- Scikit-learn
- NumPy
- Pandas

---

## 🧠 Machine Learning Concepts Applied

### Supervised Learning

The model learns patterns from labeled training data and predicts the class of unseen samples.

### Train-Test Split

The dataset is divided into:

- Training Data (80%)
- Testing Data (20%)

This ensures unbiased model evaluation.

### Feature Scaling

StandardScaler is used to normalize the feature values before training the model.

### K-Nearest Neighbors (KNN)

The KNN classification algorithm is used to classify flower species based on the similarity of nearby data points.

---

## 🔄 Project Workflow

```text
Load Iris Dataset
        ↓
Train-Test Split
        ↓
Feature Scaling
        ↓
KNN Model Training
        ↓
Prediction
        ↓
Accuracy Evaluation
        ↓
Confusion Matrix
        ↓
Classification Report
```

---

## 🚀 How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python iris_classifier.py
```

---

## 📈 Model Performance

### Dataset Summary

- Dataset Size: 150 Samples
- Features: 4
- Classes: 3

### Results

```text
Accuracy Score: 100.00%
```

### Confusion Matrix

```text
[[10 0 0]
 [0 9 0]
 [0 0 11]]
```

### Classification Report

```text
              precision    recall  f1-score   support

      setosa       1.00      1.00      1.00        10
  versicolor       1.00      1.00      1.00         9
   virginica       1.00      1.00      1.00        11

    accuracy                           1.00        30
   macro avg       1.00      1.00      1.00        30
weighted avg       1.00      1.00      1.00        30
```

---

## 📂 Project Structure

```text
iris-classification-ai/
│
├── iris_classifier.py
├── README.md
├── requirements.txt
└── screenshots/
```

---

## 📚 Learning Outcomes

Through this project, I learned:

- Data preprocessing techniques
- Train-test splitting
- Feature scaling
- K-Nearest Neighbors (KNN)
- Model training and prediction
- Accuracy evaluation
- Confusion Matrix analysis
- Classification Report interpretation
- Machine Learning workflow fundamentals

---

## 🏆 Internship Project

**Artificial Intelligence Internship Program**

Week 2 Project: **Data Classification Using AI**

Developed as part of the DecodeLabs Industrial Training Program.

---

## 👨‍💻 Author

**Zaid Hussain dahar**

Artificial Intelligence Intern
