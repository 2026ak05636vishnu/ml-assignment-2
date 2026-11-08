# ML Classification Models - Interactive Dashboard

## Problem Statement

This project implements a comprehensive machine learning classification system that demonstrates multiple classification algorithms on a real-world dataset. The objective is to build, train, evaluate, and compare 5 different classification models using standardized evaluation metrics, then deploy an interactive Streamlit web application for real-time model evaluation and prediction.

## Dataset Description

**Dataset**: Synthetic Classification Dataset with 15 Features

- **Total Samples**: 600
- **Number of Features**: 15 (exceeds minimum requirement of 12)
- **Feature Type**: Numerical features (standardized)
- **Target Variable**: Multi-class classification (3 classes: 0, 1, 2)
- **Data Split**: 80% training (480 samples), 20% testing (120 samples)
- **Preprocessing**: Features are standardized using StandardScaler for optimal model performance

### Features
- All features are numerical and normalized
- No missing values
- Features are generated to have meaningful patterns for classification

## Models Implemented

### 1. Logistic Regression
- **Type**: Linear classifier
- **Hyperparameters**: max_iter=1000, random_state=42
- **Use Case**: Quick baseline, interpretable probabilities
- **Observation**: Provides good baseline performance with fast training

### 2. Decision Tree Classifier
- **Type**: Tree-based classifier
- **Hyperparameters**: max_depth=10, random_state=42
- **Use Case**: Non-linear relationships, feature importance
- **Observation**: Can capture complex patterns but may overfit

### 3. K-Nearest Neighbors (KNN)
- **Type**: Instance-based learner
- **Hyperparameters**: n_neighbors=5
- **Use Case**: Non-parametric, local decision boundaries
- **Observation**: Performance depends on feature scaling and k value

### 4. Naive Bayes (Gaussian)
- **Type**: Probabilistic classifier
- **Hyperparameters**: Default Gaussian distribution
- **Use Case**: Fast training, good for baseline
- **Observation**: Assumes feature independence; works well for text/categorical

### 5. Support Vector Machine (SVM)
- **Type**: Margin-based classifier
- **Hyperparameters**: kernel='rbf', probability=True, random_state=42
- **Use Case**: High-dimensional data, powerful non-linear classification
- **Observation**: Best for complex decision boundaries; slower training

## Evaluation Metrics

For each model, the following metrics are calculated:

| Metric | Definition | Range | Interpretation |
|--------|-----------|-------|-----------------|
| **Accuracy** | (TP+TN)/(Total) | 0-1 | Overall correctness |
| **AUC Score** | Area Under ROC Curve | 0-1 | Model's ability to distinguish classes |
| **Precision** | TP/(TP+FP) | 0-1 | Correctness of positive predictions |
| **Recall** | TP/(TP+FN) | 0-1 | Coverage of positive instances |
| **F1 Score** | 2*(Precision*Recall)/(Precision+Recall) | 0-1 | Harmonic mean of precision & recall |
| **MCC** | Matthews Correlation Coefficient | -1 to 1 | Correlation coefficient for binary/multiclass |

## Model Performance Comparison

| ML Model Name | Accuracy | AUC | Precision | Recall | F1 | MCC |
|---------------|----------|-----|-----------|--------|----|----|
| Logistic Regression | 0.7833 | 0.8214 | 0.7844 | 0.7833 | 0.7829 | 0.6720 |
| Decision Tree | 0.8417 | 0.8751 | 0.8450 | 0.8417 | 0.8421 | 0.7602 |
| KNN | 0.8167 | 0.8506 | 0.8197 | 0.8167 | 0.8169 | 0.7227 |
| Naive Bayes | 0.7833 | 0.8179 | 0.7878 | 0.7833 | 0.7841 | 0.6703 |
| Support Vector Machine | 0.8667 | 0.9027 | 0.8694 | 0.8667 | 0.8673 | 0.7995 |

## Observations on Model Performance

### Logistic Regression
- Provides a solid baseline with decent accuracy (78.33%)
- Fast training time and interpretable coefficients
- Good for understanding linear relationships
- Suitable for production deployments due to simplicity

### Decision Tree Classifier
- Excellent performance with 84.17% accuracy
- Captures non-linear relationships well
- Feature importance can be extracted
- Risk of overfitting on complex trees

### K-Nearest Neighbors (KNN)
- Good accuracy of 81.67%
- Instance-based learning captures local patterns
- Sensitive to feature scaling (addressed with StandardScaler)
- Slower prediction time on large datasets

### Naive Bayes
- Similar performance to Logistic Regression (78.33%)
- Very fast training and prediction
- Assumes feature independence (may not hold for all datasets)
- Good for baseline and quick prototyping

### Support Vector Machine
- **🏆 Best Performer with 86.67% Accuracy**
- Highest AUC score (0.9027) indicates excellent class separation
- Excellent F1 score (0.8673) shows balanced precision-recall
- RBF kernel captures complex non-linear patterns
- Slightly slower training than simpler models but worth the accuracy gain

## Overall Winner for This Dataset

**Support Vector Machine (SVM)** achieves the best performance with:
- **Highest Accuracy**: 86.67%
- **Highest AUC Score**: 0.9027
- **Best F1 Score**: 0.8673
- **Best MCC Score**: 0.7995

The SVM's superior performance suggests that the decision boundaries in this dataset are highly non-linear and require sophisticated kernel methods to capture effectively.

## Repository Structure

```
ml-assignment/
├── app.py                 # Streamlit application
├── setup_models.py        # Model training script
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── test_data.csv         # Test dataset for evaluation
├── model_results.csv     # Trained model metrics
├── scaler.joblib         # Fitted StandardScaler
└── models/
    ├── logistic_regression.joblib
    ├── decision_tree.joblib
    ├── knn.joblib
    ├── naive_bayes.joblib
    └── support_vector_machine.joblib
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip or conda

### Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ml-assignment
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train models (if needed)**
   ```bash
   python setup_models.py
   ```

5. **Run Streamlit app**
   ```bash
   streamlit run app.py
   ```

6. **Access the app**
   - Open browser to `http://localhost:8501`

## Deployment on Streamlit Community Cloud

### Steps to Deploy

1. Push code to GitHub repository
2. Go to https://streamlit.io/cloud
3. Click "New App"
4. Select your GitHub repository
5. Choose the `main` branch
6. Set main file to `app.py`
7. Click Deploy

### Live App Features

- **CSV Upload**: Upload test data to evaluate models
- **Model Selection**: Choose any of the 5 trained models
- **Real-time Evaluation**: Get instant predictions and metrics
- **Confusion Matrix**: Visual representation of model performance
- **Classification Report**: Detailed per-class metrics
- **Model Comparison**: Compare all 5 models on uploaded data

## Usage

1. **Upload Test Data**
   - Prepare CSV file with the same features as training data
   - Include a 'target' column with ground truth labels

2. **Select Model**
   - Choose from dropdown: Logistic Regression, Decision Tree, KNN, Naive Bayes, SVM

3. **View Results**
   - Accuracy, AUC, Precision, Recall, F1, MCC scores
   - Confusion Matrix visualization
   - Classification Report

4. **Compare Models**
   - View performance of all models side-by-side
   - Identify best model for your data

## Key Technologies

- **Framework**: Python 3.x
- **ML Library**: scikit-learn
- **Web Framework**: Streamlit
- **Data Processing**: pandas, NumPy
- **Visualization**: matplotlib, seaborn
- **Model Serialization**: joblib

## Requirements

See `requirements.txt` for complete list:
- streamlit
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn
- joblib

## Notes

- All models are trained on the same dataset for fair comparison
- Features are scaled using StandardScaler for consistent performance
- Multi-class classification (3 classes) uses weighted averages for metrics
- AUC scores computed using One-vs-Rest approach for multiclass
- MCC score provides overall correlation between predicted and actual labels

## Academic Integrity

This project is developed as part of M.Tech AIML Machine Learning Assignment 2 (BITS WILP).

---

**Last Updated**: November 2026
**Status**: Ready for Deployment
