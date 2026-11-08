# ML Assignment 2 - Implementation Instructions

## Quick Start

### Step 1: Generate Models and Test Data (Local Machine)

```bash
# Navigate to project directory
cd C:\Users\vishnute\Favorites\Downloads\ml_assignment

# Install dependencies
pip install -r requirements.txt

# Generate test data and train models
python generate_data_and_models.py
```

**Output**: This creates:
- `test_data.csv` - Test dataset
- `scaler.joblib` - Feature scaler
- `model_results.csv` - Metrics comparison
- `models/` folder with all 5 trained models

### Step 2: Test Locally with Streamlit

```bash
# Run the app
streamlit run app.py

# Open browser to http://localhost:8501
```

**Test the app**:
1. Upload `test_data.csv`
2. Select each model and click "Evaluate Model"
3. View confusion matrix and classification report
4. Compare all models

### Step 3: Push to GitHub

```bash
# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Make initial commit
git commit -m "ML Assignment 2: Classification models with Streamlit app"

# Add remote repository
git remote add origin <YOUR_GITHUB_REPO_URL>

# Push to GitHub
git push -u origin main
```

### Step 4: Deploy on Streamlit Community Cloud

1. Go to https://streamlit.io/cloud
2. Click "New App"
3. Select your GitHub repository
4. Choose branch: `main`
5. Set main file: `app.py`
6. Click "Deploy"

**Wait for deployment** (~3-5 minutes)

### Step 5: Test Deployed App

1. Click the Streamlit link
2. Upload `test_data.csv`
3. Evaluate models and verify functionality

## File Structure

```
ml-assignment/
├── app.py                          # Streamlit application
├── generate_data_and_models.py     # Model training script
├── setup_models.py                 # Alternative setup
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── .gitignore                      # Git ignore file
├── test_data.csv                   # Test dataset (50 samples)
├── scaler.joblib                   # Trained StandardScaler
├── model_results.csv               # Model metrics
└── models/
    ├── logistic_regression.joblib
    ├── decision_tree.joblib
    ├── knn.joblib
    ├── naive_bayes.joblib
    └── support_vector_machine.joblib
```

## Submission Checklist

Before submitting, ensure:

- [ ] Run `python generate_data_and_models.py` to create all files
- [ ] Test `streamlit run app.py` locally
- [ ] Push to GitHub with all files (including models/)
- [ ] Deploy on Streamlit Community Cloud successfully
- [ ] Test the live app
- [ ] README.md is complete and in GitHub repo
- [ ] test_data.csv is in GitHub repo
- [ ] All model files are in models/ folder
- [ ] requirements.txt has all dependencies

## Creating GitHub Repository

### Option 1: Using GitHub Web Interface

1. Go to https://github.com/new
2. Create new repository (name: `ml-assignment-2`)
3. Choose: Public
4. Initialize with README (optional)
5. Click "Create repository"
6. Copy repository URL

### Option 2: Using Git Command Line

```bash
# After creating repo on GitHub

cd ml-assignment

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: ML Classification models"

# Add remote
git remote add origin https://github.com/YOUR_USERNAME/ml-assignment-2.git

# Push
git branch -M main
git push -u origin main
```

## Troubleshooting

### Issue: "Module not found" error when deploying

**Solution**: Ensure all dependencies are in `requirements.txt`

```bash
# Generate requirements
pip freeze > requirements.txt
```

### Issue: Model files not found after deployment

**Solution**: Ensure model files are committed to GitHub

```bash
# Check if models/ folder is in git
git status

# Add models folder if missing
git add models/
git commit -m "Add trained models"
git push
```

### Issue: Streamlit app shows "No models found"

**Solution**: 
1. Run `python generate_data_and_models.py` locally
2. Ensure `models/` folder is in GitHub
3. Redeploy the app

## Important Notes

- **Models Directory**: Must be committed to GitHub
- **Test Data**: Use the provided `test_data.csv`
- **Features**: 15 features minimum requirement ✓
- **Samples**: 600 samples minimum requirement ✓
- **Metrics**: All 6 metrics calculated and displayed
- **Live App**: Must be fully functional on Streamlit Cloud

## Support

For issues with:
- **Model Training**: Review `generate_data_and_models.py`
- **Streamlit App**: Check `app.py` for correct model loading paths
- **GitHub Deployment**: Ensure repository is public
- **Streamlit Cloud**: Check deployment logs in Streamlit dashboard

---

**Ready to submit once:**
1. ✓ GitHub repository with all files
2. ✓ Streamlit app deployed and working
3. ✓ README.md with complete information
4. ✓ Test data in CSV format
5. ✓ All models saved in models/ folder
