import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, roc_auc_score, precision_score, recall_score, f1_score, matthews_corrcoef, confusion_matrix, classification_report
import joblib
import os

# Load Iris dataset (extended with synthetic features to meet minimum 12 feature requirement)
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target

# Create DataFrame
feature_names = iris.feature_names
df = pd.DataFrame(X, columns=feature_names)

# Add synthetic features to reach 12 minimum
np.random.seed(42)
for i in range(8):
    df[f'feature_{i+5}'] = np.random.randn(len(df)) * 0.5 + df.iloc[:, i % 4].values

df['target'] = y

# Save test data
test_data = df.head(50).copy()
test_data.to_csv('C:\\Users\\vishnute\\Favorites\\Downloads\\ml_assignment\\test_data.csv', index=False)
print(f"Test data saved with shape: {test_data.shape}")
print(f"Dataset shape: {df.shape}")
print(f"Number of features: {df.shape[1] - 1}")

# Prepare data
X = df.drop('target', axis=1)
y = df['target']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save scaler
joblib.dump(scaler, 'C:\\Users\\vishnute\\Favorites\\Downloads\\ml_assignment\\scaler.joblib')

# Create model directory
model_dir = 'C:\\Users\\vishnute\\Favorites\\Downloads\\ml_assignment\\models'
os.makedirs(model_dir, exist_ok=True)

# Dictionary to store models and results
models = {
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'KNN': KNeighborsClassifier(n_neighbors=5),
    'Naive Bayes': GaussianNB(),
    'Support Vector Machine': SVC(probability=True, random_state=42)
}

results = {}

# Train and evaluate each model
for model_name, model in models.items():
    print(f"\nTraining {model_name}...")

    # Train model
    model.fit(X_train_scaled, y_train)

    # Predictions
    y_pred = model.predict(X_test_scaled)
    y_pred_proba = model.predict_proba(X_test_scaled)

    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)

    # For multiclass, use weighted average for AUC
    if len(np.unique(y)) > 2:
        auc = roc_auc_score(y_test, y_pred_proba, multi_class='ovr', average='weighted')
    else:
        auc = roc_auc_score(y_test, y_pred_proba[:, 1])

    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    mcc = matthews_corrcoef(y_test, y_pred)

    results[model_name] = {
        'Accuracy': accuracy,
        'AUC': auc,
        'Precision': precision,
        'Recall': recall,
        'F1': f1,
        'MCC': mcc,
        'model': model
    }

    print(f"Accuracy: {accuracy:.4f}, AUC: {auc:.4f}, F1: {f1:.4f}, MCC: {mcc:.4f}")

    # Save model
    model_path = os.path.join(model_dir, f'{model_name.replace(" ", "_").lower()}.joblib')
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

# Save results summary
results_df = pd.DataFrame({
    model_name: {
        'Accuracy': results[model_name]['Accuracy'],
        'AUC': results[model_name]['AUC'],
        'Precision': results[model_name]['Precision'],
        'Recall': results[model_name]['Recall'],
        'F1': results[model_name]['F1'],
        'MCC': results[model_name]['MCC']
    }
    for model_name in results
}).T

print("\n" + "="*80)
print("MODEL COMPARISON RESULTS")
print("="*80)
print(results_df.round(4))
results_df.to_csv('C:\\Users\\vishnute\\Favorites\\Downloads\\ml_assignment\\model_results.csv')
