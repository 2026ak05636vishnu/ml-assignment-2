import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.metrics import accuracy_score, roc_auc_score, precision_score, recall_score, f1_score, matthews_corrcoef, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="ML Classification Models", layout="wide")

st.title("🤖 Multi-Model Classification Dashboard")
st.markdown("---")

# Sidebar
st.sidebar.header("Configuration")

# Model directory and scaler path
MODEL_DIR = "models"
SCALER_PATH = "scaler.joblib"

# Load scaler
@st.cache_resource
def load_scaler():
    if os.path.exists(SCALER_PATH):
        return joblib.load(SCALER_PATH)
    return None

# Load models
@st.cache_resource
def load_models():
    models = {}
    model_files = {
        'Logistic Regression': 'logistic_regression.joblib',
        'Decision Tree': 'decision_tree.joblib',
        'KNN': 'knn.joblib',
        'Naive Bayes': 'naive_bayes.joblib',
        'Support Vector Machine': 'support_vector_machine.joblib'
    }

    for model_name, file_name in model_files.items():
        path = os.path.join(MODEL_DIR, file_name)
        if os.path.exists(path):
            models[model_name] = joblib.load(path)

    return models

scaler = load_scaler()
models = load_models()

if not models:
    st.warning("⚠️ Models not found. Please train models first and upload model files.")
    st.stop()

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Model Performance Comparison")

    # Load or create results
    if os.path.exists("model_results.csv"):
        results_df = pd.read_csv("model_results.csv", index_col=0)
        st.dataframe(results_df.round(4), use_container_width=True)
    else:
        st.info("Results data not available yet.")

with col2:
    st.subheader("📈 Metrics")
    model_choice = st.selectbox("Select Model:", list(models.keys()))

# Dataset Upload Section
st.markdown("---")
st.subheader("📁 Upload Test Data")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load test data
    test_df = pd.read_csv(uploaded_file)

    st.success(f"✅ File uploaded successfully! Shape: {test_df.shape}")

    # Separate features and target
    if 'target' in test_df.columns:
        X_test = test_df.drop('target', axis=1)
        y_test = test_df['target']
    else:
        st.warning("⚠️ 'target' column not found in CSV. Using last column as target.")
        X_test = test_df.iloc[:, :-1]
        y_test = test_df.iloc[:, -1]

    st.write(f"Features: {X_test.shape[1]}, Samples: {X_test.shape[0]}")

    # Scale features if scaler available
    if scaler:
        X_test_scaled = scaler.transform(X_test)
    else:
        X_test_scaled = X_test.values

    # Model selection and prediction
    st.markdown("---")
    st.subheader("🎯 Model Selection & Prediction")

    selected_model = st.selectbox("Choose a model for evaluation:", list(models.keys()), key="eval_model")

    if st.button("🚀 Evaluate Model", type="primary"):
        model = models[selected_model]

        # Predictions
        y_pred = model.predict(X_test_scaled)
        y_pred_proba = model.predict_proba(X_test_scaled)

        # Calculate metrics
        accuracy = accuracy_score(y_test, y_pred)

        # Handle multiclass AUC
        try:
            if len(np.unique(y_test)) > 2:
                auc = roc_auc_score(y_test, y_pred_proba, multi_class='ovr', average='weighted')
            else:
                auc = roc_auc_score(y_test, y_pred_proba[:, 1])
        except:
            auc = 0.0

        precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
        recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
        f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
        mcc = matthews_corrcoef(y_test, y_pred)

        # Display metrics
        st.markdown(f"### Results for {selected_model}")

        col1, col2, col3, col4, col5, col6 = st.columns(6)

        with col1:
            st.metric("Accuracy", f"{accuracy:.4f}")
        with col2:
            st.metric("AUC Score", f"{auc:.4f}")
        with col3:
            st.metric("Precision", f"{precision:.4f}")
        with col4:
            st.metric("Recall", f"{recall:.4f}")
        with col5:
            st.metric("F1 Score", f"{f1:.4f}")
        with col6:
            st.metric("MCC Score", f"{mcc:.4f}")

        # Confusion Matrix
        st.subheader("📊 Confusion Matrix")
        cm = confusion_matrix(y_test, y_pred)

        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax, cbar=True)
        ax.set_xlabel('Predicted')
        ax.set_ylabel('Actual')
        ax.set_title(f'Confusion Matrix - {selected_model}')
        st.pyplot(fig)

        # Classification Report
        st.subheader("📋 Classification Report")
        report = classification_report(y_test, y_pred, output_dict=True, zero_division=0)
        report_df = pd.DataFrame(report).transpose()
        st.dataframe(report_df.round(4), use_container_width=True)

else:
    st.info("👆 Please upload a CSV file to evaluate models.")

# Model Comparison Tab
st.markdown("---")
st.subheader("📊 All Models Comparison (on uploaded data)")

if uploaded_file is not None:
    comparison_data = []

    for model_name in models.keys():
        model = models[model_name]
        y_pred = model.predict(X_test_scaled)
        y_pred_proba = model.predict_proba(X_test_scaled)

        accuracy = accuracy_score(y_test, y_pred)
        try:
            if len(np.unique(y_test)) > 2:
                auc = roc_auc_score(y_test, y_pred_proba, multi_class='ovr', average='weighted')
            else:
                auc = roc_auc_score(y_test, y_pred_proba[:, 1])
        except:
            auc = 0.0

        precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
        recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
        f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
        mcc = matthews_corrcoef(y_test, y_pred)

        comparison_data.append({
            'Model': model_name,
            'Accuracy': accuracy,
            'AUC': auc,
            'Precision': precision,
            'Recall': recall,
            'F1': f1,
            'MCC': mcc
        })

    comparison_df = pd.DataFrame(comparison_data)
    st.dataframe(comparison_df.round(4), use_container_width=True)

    # Best model
    best_model = comparison_df.loc[comparison_df['Accuracy'].idxmax(), 'Model']
    st.success(f"🏆 Best Model by Accuracy: {best_model} ({comparison_df['Accuracy'].max():.4f})")

st.markdown("---")
st.markdown("### 📌 About This App")
st.markdown("""
- **5 Classification Models**: Logistic Regression, Decision Tree, KNN, Naive Bayes, SVM
- **6 Evaluation Metrics**: Accuracy, AUC, Precision, Recall, F1, MCC
- **Test Data**: Upload your CSV file with features and target column
- **Live Predictions**: Get predictions and metrics in real-time
""")
