"""
Quick script to generate test data and trained models for the ML assignment
Run this locally first: python generate_data_and_models.py
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, roc_auc_score, precision_score, recall_score, f1_score, matthews_corrcoef
import joblib
import os

print("="*80)
print("ML ASSIGNMENT - MODEL TRAINING & DATA GENERATION")
print("="*80)

# Create models directory
os.makedirs('models', exist_ok=True)

# Generate dataset
print("\n1. Generating synthetic dataset...")
np.random.seed(42)
n_samples = 600
n_features = 15

X = np.random.randn(n_samples, n_features)
target = ((X[:, 0] + X[:, 1] > 0) & (X[:, 2] < 0.5)).astype(int)
target = np.where(X[:, 3] > 0, 1 - target, target)
target = np.where(X[:, 4] > 1, 2, target)

feature_names = [f'feature_{i}' for i in range(n_features)]
df = pd.DataFrame(X, columns=feature_names)
df['target'] = target

print(f"   ✓ Dataset shape: {df.shape}")
print(f"   ✓ Features: {n_features} (requirement: ≥12)")
print(f"   ✓ Samples: {n_samples} (requirement: ≥500)")
print(f"   ✓ Classes: {sorted(np.unique(target))}")

# Save test data
print("\n2. Saving test data...")
test_data = df.head(50).copy()
test_data.to_csv('test_data.csv', index=False)
print(f"   ✓ test_data.csv saved (50 samples)")

# Prepare training data
X = df.drop('target', axis=1).values
y = df['target'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save scaler
joblib.dump(scaler, 'scaler.joblib')
print("\n3. Feature scaling...")
print(f"   ✓ scaler.joblib saved")

# Define and train models
models_dict = {
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(random_state=42, max_depth=10),
    'KNN': KNeighborsClassifier(n_neighbors=5),
    'Naive Bayes': GaussianNB(),
    'Support Vector Machine': SVC(kernel='rbf', probability=True, random_state=42)
}

results = []

print("\n4. Training models...")
for model_name, model in models_dict.items():
    model.fit(X_train_scaled, y_train)

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

    results.append({
        'Model': model_name,
        'Accuracy': f'{accuracy:.4f}',
        'AUC': f'{auc:.4f}',
        'Precision': f'{precision:.4f}',
        'Recall': f'{recall:.4f}',
        'F1': f'{f1:.4f}',
        'MCC': f'{mcc:.4f}'
    })

    model_file = model_name.replace(' ', '_').lower() + '.joblib'
    model_path = os.path.join('models', model_file)
    joblib.dump(model, model_path)
    print(f"   ✓ {model_name:25} | Acc: {accuracy:.4f} | F1: {f1:.4f}")

# Save results
results_df = pd.DataFrame(results)
results_df.to_csv('model_results.csv', index=False)

print("\n" + "="*80)
print("MODEL COMPARISON TABLE")
print("="*80)
print(results_df.to_string(index=False))

print("\n" + "="*80)
print("✓ SETUP COMPLETE!")
print("="*80)
print("\nGenerated files:")
print("  ✓ test_data.csv (50 samples for testing)")
print("  ✓ scaler.joblib (StandardScaler)")
print("  ✓ model_results.csv (metrics comparison)")
print("  ✓ models/logistic_regression.joblib")
print("  ✓ models/decision_tree.joblib")
print("  ✓ models/knn.joblib")
print("  ✓ models/naive_bayes.joblib")
print("  ✓ models/support_vector_machine.joblib")

print("\nNext steps:")
print("  1. Commit all files to GitHub")
print("  2. Go to https://streamlit.io/cloud")
print("  3. Deploy using this repository")
print("  4. Share the Streamlit app link")
print("\n" + "="*80)
