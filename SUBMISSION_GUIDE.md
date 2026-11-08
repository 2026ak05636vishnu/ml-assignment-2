# ML Assignment 2 - Complete Submission Guide

**Deadline**: 08 November 2026 23:59 PM  
**Marks**: 15 (10 marks for models + 4 marks for app + 1 mark for BITS Lab screenshot)

---

## Overview of What You Have

This package contains a complete ML classification project with:

✅ **5 Classification Models** (Logistic Regression, Decision Tree, KNN, Naive Bayes, SVM)  
✅ **Interactive Streamlit App** (CSV upload, model selection, metrics display)  
✅ **Complete Documentation** (README, requirements, instructions)  
✅ **Training Scripts** (Automatic model generation and evaluation)  
✅ **Test Data** (600 samples, 15 features)  

---

## Step-by-Step Submission Process

### Phase 1: Local Testing (15 minutes)

#### 1.1 Install Dependencies
```bash
pip install -r requirements.txt
```

#### 1.2 Generate Models and Data
```bash
python generate_data_and_models.py
```

**Expected Output:**
```
✓ Dataset shape: (600, 16)
✓ Features: 15 (requirement: ≥12)
✓ Samples: 600 (requirement: ≥500)
✓ Classes: [0 1 2]
✓ test_data.csv saved (50 samples)
✓ scaler.joblib saved
✓ Models trained and saved
```

**Created Files:**
- `test_data.csv` (50 test samples)
- `scaler.joblib` (feature scaler)
- `model_results.csv` (metrics table)
- `models/` folder with 5 model files

#### 1.3 Test Streamlit App
```bash
streamlit run app.py
```

**Test Functionality:**
1. App loads at `http://localhost:8501`
2. Upload `test_data.csv`
3. Select each model and click "Evaluate Model"
4. Verify metrics display (Accuracy, AUC, Precision, Recall, F1, MCC)
5. Check Confusion Matrix visualization
6. View Classification Report
7. Compare all models table

✅ **All tests should pass without errors**

---

### Phase 2: GitHub Repository Setup (10 minutes)

#### 2.1 Create GitHub Repository

**Option A: Using GitHub Web Interface**
1. Go to https://github.com/new
2. Fill in:
   - **Repository name**: `ml-assignment-2`
   - **Description**: "ML Classification Models with Streamlit Dashboard"
   - **Visibility**: Public
   - **Initialize with README**: NO (we have our own)
3. Click "Create repository"
4. Copy the repository URL

**Option B: Using GitHub CLI**
```bash
gh repo create ml-assignment-2 --public --source=. --remote=origin --push
```

#### 2.2 Initialize Git and Push Code

```bash
# Initialize git (if not already done)
git init

# Configure git (if first time)
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Add all files
git add .

# Create initial commit
git commit -m "ML Assignment 2: Multi-model classification with Streamlit app

- 5 classification models (Logistic Regression, Decision Tree, KNN, Naive Bayes, SVM)
- 6 evaluation metrics (Accuracy, AUC, Precision, Recall, F1, MCC)
- Interactive Streamlit web application
- Complete documentation and setup scripts
- Test data and pre-trained models"

# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/ml-assignment-2.git

# Push to GitHub
git branch -M main
git push -u origin main
```

#### 2.3 Verify Repository Structure

On GitHub, verify:
- ✅ `app.py` present
- ✅ `requirements.txt` present
- ✅ `README.md` present
- ✅ `test_data.csv` present
- ✅ `models/` folder with all 5 models
- ✅ `scaler.joblib` present
- ✅ `.gitignore` present

**GitHub Repository URL Example:**  
`https://github.com/YOUR_USERNAME/ml-assignment-2`

---

### Phase 3: Streamlit Cloud Deployment (20 minutes)

#### 3.1 Deploy Application

1. Go to https://streamlit.io/cloud
2. Click "Sign in with GitHub" (create account if needed)
3. Click "New app"
4. Select:
   - **Repository**: `YOUR_USERNAME/ml-assignment-2`
   - **Branch**: `main`
   - **Main file path**: `app.py`
5. Click "Deploy"

**Status**: App will show "Deploying..." then "Running"

#### 3.2 Wait for Deployment

- ⏱️ **Typical time**: 3-5 minutes
- ℹ️ You can check logs for any errors
- 🔗 App URL will be in format: `https://ml-assignment-2-xxxxxx.streamlit.app`

#### 3.3 Test Deployed App

1. Click the app URL
2. Upload `test_data.csv`
3. Select model and click "Evaluate Model"
4. Verify all features work:
   - ✅ CSV upload works
   - ✅ Model selection dropdown works
   - ✅ Metrics display correctly
   - ✅ Confusion matrix shows
   - ✅ Classification report displays
   - ✅ Model comparison table appears

**Live Streamlit App URL Example:**  
`https://ml-assignment-2-xxxxxx.streamlit.app`

---

### Phase 4: BITS Lab Execution (Optional but Recommended)

#### 4.1 Run on BITS Virtual Lab

1. Connect to BITS Virtual Lab
2. Upload project files or clone from GitHub
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python generate_data_and_models.py`
5. Run: `streamlit run app.py`
6. **Take a screenshot** showing:
   - Terminal with running Streamlit app
   - URL displayed: `http://localhost:8501`
   - App loaded in browser showing the dashboard

#### 4.2 Save Screenshot

- Save as: `BITS_Lab_Screenshot.png`
- Include it in your submission document

---

### Phase 5: Prepare Submission Document

Create a **PDF document** with the following content (in order):

#### Section 1: Links (Top of Document)
```
GitHub Repository Link:
[Provide clickable link or URL]

Live Streamlit App Link:
[Provide clickable link or URL]
```

#### Section 2: BITS Lab Screenshot
```
[Include screenshot of app running on BITS Virtual Lab]
```

#### Section 3: Project Documentation

Copy-paste the following from your `README.md`:

1. **Problem Statement**
2. **Dataset Description**
3. **Models Used** (with comparison table)
4. **Performance Observations**
5. **Overall Winner**
6. **Repository Structure**
7. **Installation & Setup**

#### Section 4: Model Performance Table

```
| ML Model Name | Accuracy | AUC | Precision | Recall | F1 | MCC |
|---|---|---|---|---|---|---|
| Logistic Regression | 0.7833 | 0.8214 | 0.7844 | 0.7833 | 0.7829 | 0.6720 |
| Decision Tree | 0.8417 | 0.8751 | 0.8450 | 0.8417 | 0.8421 | 0.7602 |
| KNN | 0.8167 | 0.8506 | 0.8197 | 0.8167 | 0.8169 | 0.7227 |
| Naive Bayes | 0.7833 | 0.8179 | 0.7878 | 0.7833 | 0.7841 | 0.6703 |
| Support Vector Machine | 0.8667 | 0.9027 | 0.8694 | 0.8667 | 0.8673 | 0.7995 |
```

---

## Final Submission Checklist

Before submitting, verify ALL items:

### Code & Repository
- [ ] GitHub repository created and public
- [ ] All files committed and pushed to GitHub
- [ ] `app.py` present in repository
- [ ] `requirements.txt` present
- [ ] `README.md` complete and detailed
- [ ] `test_data.csv` in repository
- [ ] `models/` folder with all 5 models
- [ ] `scaler.joblib` in repository
- [ ] `.gitignore` configured

### Streamlit App
- [ ] App deployed on Streamlit Community Cloud
- [ ] App opens without errors
- [ ] CSV upload feature works
- [ ] Model selection dropdown works
- [ ] Evaluation metrics display correctly
- [ ] Confusion matrix visualizes
- [ ] Classification report shows
- [ ] Model comparison table displays
- [ ] All 5 models working

### Documentation
- [ ] README.md has problem statement
- [ ] README.md has dataset description
- [ ] README.md has models used section
- [ ] README.md has performance table
- [ ] README.md has observations on each model
- [ ] README.md identifies winner (SVM - 86.67%)

### Submission Document
- [ ] PDF file created
- [ ] GitHub repository link included (clickable)
- [ ] Streamlit app link included (clickable)
- [ ] BITS Lab screenshot included
- [ ] README content included
- [ ] Model performance table included
- [ ] File name: `ML_Assignment_2_YourName.pdf`

### Technical Requirements Met
- [ ] ≥5 classification models implemented (✓ 5 models)
- [ ] ≥6 evaluation metrics calculated (✓ 6 metrics)
- [ ] ≥12 features in dataset (✓ 15 features)
- [ ] ≥500 samples in dataset (✓ 600 samples)
- [ ] Streamlit app with 4+ features (✓ CSV upload, model selection, metrics, confusion matrix)
- [ ] Models saved and loaded correctly
- [ ] README with required structure
- [ ] test_data.csv included

---

## Important Links & Information

### Key URLs
- **GitHub**: https://github.com
- **Streamlit Cloud**: https://streamlit.io/cloud
- **BITS Support**: csislabsupport@wilp.bits-pilani.ac.in

### Model Performance Summary

**🏆 Best Model: Support Vector Machine (SVM)**
- Accuracy: **86.67%**
- AUC Score: **0.9027**
- F1 Score: **0.8673**

### Marks Breakdown (15 marks)
- Model Implementation: **10 marks** (1 mark per model metrics)
- Streamlit App Development: **4 marks** (CSV upload, model selection, metrics, confusion matrix)
- BITS Lab Screenshot: **1 mark**

---

## Troubleshooting

### Issue: App shows "Models not found"
**Solution**: 
```bash
python generate_data_and_models.py
git add models/
git commit -m "Add trained models"
git push
```

### Issue: Import errors after deployment
**Solution**: Check requirements.txt has all packages:
```bash
pip freeze > requirements.txt
```

### Issue: Streamlit app slow or timing out
**Solution**: Reduce test data size or optimize model loading (use `@st.cache_resource`)

### Issue: Can't connect to GitHub from terminal
**Solution**: Use personal access token instead of password:
```bash
git remote set-url origin https://YOUR_TOKEN@github.com/YOUR_USERNAME/ml-assignment-2.git
```

---

## Timeline

| Phase | Task | Time | Deadline |
|-------|------|------|----------|
| 1 | Local testing & verification | 15 min | - |
| 2 | GitHub repository setup | 10 min | - |
| 3 | Streamlit Cloud deployment | 20 min | - |
| 4 | BITS Lab execution (optional) | 15 min | - |
| 5 | Prepare submission PDF | 10 min | - |
| **Total** | **Complete Submission** | **~70 minutes** | **8 Nov, 23:59** |

---

## Success Criteria

Your submission is complete when:

✅ GitHub repository is public and contains all required files  
✅ Streamlit app is deployed and fully functional  
✅ Live app link opens interactive dashboard  
✅ All 5 models load and evaluate successfully  
✅ PDF document contains all required information  
✅ Links are clickable and verified working  
✅ Submitted before deadline (8 Nov 23:59 PM)  

---

**Good luck with your submission! 🚀**

For any issues, contact:
- **BITS Lab Issues**: csislabsupport@wilp.bits-pilani.ac.in
- **General Support**: raj.rohan@wilp.bits-pilani.ac.in

Subject: "NSP1 ML Assignment 2: [Your Issue]"
