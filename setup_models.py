#!/usr/bin/env python3
"""Setup script to train all ML models and save them."""

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

# Create models directory
os.makedirs('models', exist_ok=True)

# Generate synthetic dataset with 12+ features and 500+ samples
np.random.seed(42)
n_samples = 600
n_features = 15

# Create features
X = np.random.randn(n_samples, n_features)

# Create target with some pattern
target = ((X[:, 0] + X[:, 1] > 0) & (X[:, 2] < 0.5)).astype(int)
target = np.where(X[:, 3] > 0, 1 - target, target)
target = np.where(X[:, 4] > 1, 2, target)

# Create DataFrame
feature_names = [f'feature_{i}' for i in range(n_features)]
df = pd.DataFrame(X, columns=feature_names)
df['target'] = target

print(f"Dataset shape: {df.shape}")
print(f"Feature count: {n_features}")
print(f"Sample count: {n_samples}")
print(f"Classes: {np.unique(target)}")

# Save test data (first 50 samples)
test_data = df.head(50).copy()
test_data.to_csv('test_data.csv', index=False)
print(f"\n✓ Test data saved (shape: {test_data.shape})")

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

# Define models
models_dict = {
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(random_state=42, max_depth=10),
    'KNN': KNeighborsClassifier(n_neighbors=5),
    'Naive Bayes': GaussianNB(),
    'Support Vector Machine': SVC(kernel='rbf', probability=True, random_state=42)
}

results = []

print("\n" + "="*80)
print("Training Models...")
print("="*80)

for model_name, model in models_dict.items():
    print(f"\nTraining {model_name}...")

    # Train model
    model.fit(X_train_scaled, y_train)

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

    print(f"  Accuracy: {accuracy:.4f} | AUC: {auc:.4f} | F1: {f1:.4f} | MCC: {mcc:.4f}")

    results.append({
        'Model': model_name,
        'Accuracy': accuracy,
        'AUC': auc,
        'Precision': precision,
        'Recall': recall,
        'F1': f1,
        'MCC': mcc
    })

    # Save model
    model_file = model_name.replace(' ', '_').lower() + '.joblib'
    model_path = os.path.join('models', model_file)
    joblib.dump(model, model_path)
    print(f"  ✓ Saved to models/{model_file}")

# Save results
results_df = pd.DataFrame(results).set_index('Model')
results_df.to_csv('model_results.csv')

print("\n" + "="*80)
print("MODEL COMPARISON RESULTS")
print("="*80)
print(results_df.round(4).to_string())
print("\n✓ All models trained and saved!")
print("✓ Ready for Streamlit deployment!")
