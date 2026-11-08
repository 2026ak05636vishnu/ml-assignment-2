# ML Assignment 2 - Final Submission Checklist

**Deadline**: 08 November 2026, 23:59 PM  
**Status**: Ready to Submit

---

## ✅ Pre-Submission Checklist

### Phase 1: Local Setup & Testing (15 minutes)

- [ ] Navigate to project directory
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Run model generation: `python generate_data_and_models.py`
- [ ] Verify output files created:
  - [ ] test_data.csv exists
  - [ ] scaler.joblib exists
  - [ ] model_results.csv exists
  - [ ] models/ folder exists with 5 models
- [ ] Run Streamlit app: `streamlit run app.py`
- [ ] Open browser to http://localhost:8501
- [ ] Test app functionality:
  - [ ] App loads without errors
  - [ ] CSV upload works (upload test_data.csv)
  - [ ] Model dropdown shows all 5 models
  - [ ] "Evaluate Model" button works
  - [ ] Metrics display correctly (6 metrics)
  - [ ] Confusion matrix shows
  - [ ] Classification report displays
  - [ ] Model comparison table visible
- [ ] Stop Streamlit app (Ctrl+C)

### Phase 2: GitHub Repository Setup (15 minutes)

- [ ] Create GitHub account (if not already done)
- [ ] Create new public repository:
  - [ ] Repository name: `ml-assignment-2`
  - [ ] Visibility: Public
  - [ ] Initialize README: Optional (we have our own)
- [ ] Copy repository URL
- [ ] Initialize git in local project:
  ```bash
  git init
  git config user.name "Your Name"
  git config user.email "your.email@example.com"
  ```
- [ ] Add all files:
  ```bash
  git add .
  ```
- [ ] Create commit:
  ```bash
  git commit -m "ML Assignment 2: Classification models with Streamlit app"
  ```
- [ ] Add remote:
  ```bash
  git remote add origin <YOUR_REPO_URL>
  ```
- [ ] Push to GitHub:
  ```bash
  git branch -M main
  git push -u origin main
  ```
- [ ] Verify files on GitHub:
  - [ ] app.py visible
  - [ ] requirements.txt visible
  - [ ] README.md visible
  - [ ] test_data.csv visible
  - [ ] scaler.joblib visible
  - [ ] models/ folder with 5 models visible
  - [ ] .gitignore visible

### Phase 3: Streamlit Cloud Deployment (25 minutes)

- [ ] Go to https://streamlit.io/cloud
- [ ] Sign in with GitHub account
- [ ] Click "New app"
- [ ] Select repository: `ml-assignment-2`
- [ ] Select branch: `main`
- [ ] Set main file: `app.py`
- [ ] Click "Deploy"
- [ ] Wait for deployment (typically 3-5 minutes):
  - [ ] Status shows "Running"
  - [ ] No errors in logs
- [ ] Note the Streamlit app URL (e.g., https://ml-assignment-2-xxxxx.streamlit.app)
- [ ] Click app URL to open
- [ ] Test deployed app:
  - [ ] App loads without errors
  - [ ] Upload test_data.csv
  - [ ] Select model
  - [ ] Click "Evaluate Model"
  - [ ] Verify metrics display
  - [ ] Check confusion matrix
  - [ ] View classification report
  - [ ] See model comparison

### Phase 4: BITS Lab Execution (Optional but Recommended - 20 minutes)

- [ ] Connect to BITS Virtual Lab
- [ ] Upload/clone project files
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Generate models: `python generate_data_and_models.py`
- [ ] Run app: `streamlit run app.py`
- [ ] Verify app runs (shows URL: http://localhost:8501)
- [ ] Open browser and access app
- [ ] Take screenshot showing:
  - [ ] Terminal with "Streamlit is running on..."
  - [ ] Browser window with app dashboard
  - [ ] Screenshot includes URL or clear app interface
- [ ] Save screenshot as: `BITS_Lab_Screenshot.png`

### Phase 5: Create Submission Document (15 minutes)

- [ ] Open Word/Google Docs/PDF editor
- [ ] Create new document
- [ ] Add title: "ML Assignment 2 - Classification Models"
- [ ] Add submission info:
  - [ ] Your name
  - [ ] Date
  - [ ] Assignment name

**Section 1: Links (First Page)**
- [ ] Add heading: "Submission Links"
- [ ] Add GitHub repository link (make clickable)
- [ ] Add Streamlit app link (make clickable)
- [ ] Verify both links are clickable in PDF

**Section 2: Screenshot**
- [ ] Add heading: "BITS Lab Execution Screenshot"
- [ ] Insert BITS_Lab_Screenshot.png
- [ ] Add caption explaining screenshot

**Section 3: Project Documentation**
- [ ] Copy content from README.md sections:
  - [ ] Problem Statement
  - [ ] Dataset Description
  - [ ] Models Used (Logistic Regression, Decision Tree, KNN, Naive Bayes, SVM)
  - [ ] Evaluation Metrics (Accuracy, AUC, Precision, Recall, F1, MCC)
  - [ ] Model Performance Comparison Table
  - [ ] Observations on Each Model:
    - [ ] Logistic Regression observation
    - [ ] Decision Tree observation
    - [ ] KNN observation
    - [ ] Naive Bayes observation
    - [ ] SVM observation
    - [ ] Overall Winner identification (SVM - 86.67%)

**Section 4: Model Performance Table**
- [ ] Add comparison table with all metrics:
  
  | Model | Accuracy | AUC | Precision | Recall | F1 | MCC |
  |---|---|---|---|---|---|---|
  | Logistic Regression | 0.7833 | 0.8214 | 0.7844 | 0.7833 | 0.7829 | 0.6720 |
  | Decision Tree | 0.8417 | 0.8751 | 0.8450 | 0.8417 | 0.8421 | 0.7602 |
  | KNN | 0.8167 | 0.8506 | 0.8197 | 0.8167 | 0.8169 | 0.7227 |
  | Naive Bayes | 0.7833 | 0.8179 | 0.7878 | 0.7833 | 0.7841 | 0.6703 |
  | Support Vector Machine | 0.8667 | 0.9027 | 0.8694 | 0.8667 | 0.8673 | 0.7995 |

- [ ] Save document as PDF: `ML_Assignment_2_YourName.pdf`
- [ ] Verify PDF opens correctly
- [ ] Verify all links are clickable in PDF
- [ ] Check file size (should be reasonable, < 5MB)

### Phase 6: Final Verification

**Repository Verification**
- [ ] GitHub link is publicly accessible
- [ ] All required files present:
  - [ ] app.py
  - [ ] generate_data_and_models.py
  - [ ] requirements.txt
  - [ ] README.md
  - [ ] test_data.csv
  - [ ] scaler.joblib
  - [ ] models/logistic_regression.joblib
  - [ ] models/decision_tree.joblib
  - [ ] models/knn.joblib
  - [ ] models/naive_bayes.joblib
  - [ ] models/support_vector_machine.joblib
  - [ ] .gitignore

**Streamlit App Verification**
- [ ] App link is accessible
- [ ] App opens interactive dashboard
- [ ] Can upload test data
- [ ] Can select models
- [ ] Can evaluate models
- [ ] Metrics display correctly
- [ ] Confusion matrix shows
- [ ] Classification report displays
- [ ] Model comparison works

**PDF Document Verification**
- [ ] GitHub link included and clickable
- [ ] Streamlit app link included and clickable
- [ ] BITS Lab screenshot included
- [ ] README content included
- [ ] Model performance table included
- [ ] All sections present
- [ ] PDF is properly formatted
- [ ] No broken links
- [ ] File is readable and complete

### Phase 7: Submission

- [ ] Save PDF with name: `ML_Assignment_2_YourName.pdf`
- [ ] Note submission deadline: 08 November 2026, 23:59 PM
- [ ] Submit PDF through assignment portal:
  - [ ] Follow your university's submission process
  - [ ] Include GitHub repository link in submission
  - [ ] Include Streamlit app link in submission
  - [ ] Upload PDF document
- [ ] Verify submission was successful:
  - [ ] Confirmation message received
  - [ ] Submission timestamp recorded
  - [ ] Can access submitted files

---

## 📋 Files Submitted (PDF should contain)

- [ ] GitHub Repository Link: `https://github.com/[USERNAME]/ml-assignment-2`
- [ ] Streamlit App Link: `https://[name]-xxxxx.streamlit.app`
- [ ] BITS Lab Screenshot showing app running
- [ ] Problem Statement
- [ ] Dataset Description
- [ ] Models Used (5 models)
- [ ] Evaluation Metrics (6 metrics)
- [ ] Model Performance Comparison Table
- [ ] Observations on Each Model
- [ ] Overall Winner: Support Vector Machine (86.67%)

---

## ✅ Quality Checks

Before submitting, verify:

### Code Quality
- [ ] No syntax errors in Python files
- [ ] App runs without errors
- [ ] All imports work
- [ ] No hardcoded paths

### Documentation Quality
- [ ] README is comprehensive
- [ ] All sections present
- [ ] Clear writing and structure
- [ ] Model performances accurately reported
- [ ] Observations are meaningful

### App Functionality
- [ ] CSV upload works
- [ ] All 5 models load correctly
- [ ] All 6 metrics calculate
- [ ] Visualizations display properly
- [ ] No errors or warnings

### Submission Quality
- [ ] PDF is properly formatted
- [ ] All links are clickable
- [ ] Screenshot is clear
- [ ] Content is well-organized
- [ ] File size is reasonable

---

## ⚠️ Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| "Models not found" error | Run `python generate_data_and_models.py` |
| Import errors | Run `pip install -r requirements.txt` |
| Port 8501 already in use | Use `streamlit run app.py --server.port 8502` |
| Can't push to GitHub | Check git configuration and remote URL |
| Deployment fails | Check requirements.txt has all packages |
| App loads but no data | Ensure test_data.csv is in directory |
| Metrics won't calculate | Verify target column in CSV is labeled 'target' |
| PDF links not clickable | Make sure to save as PDF (not Print to PDF) |

---

## 🎯 Success Indicators

Your submission is successful when:

✅ GitHub repository is public and accessible  
✅ Streamlit app is deployed and working  
✅ All 5 models load and evaluate  
✅ PDF includes both clickable links  
✅ PDF includes BITS Lab screenshot  
✅ PDF includes complete documentation  
✅ Submitted before deadline  
✅ No plagiarism concerns  
✅ All requirements met  
✅ Ready for evaluation  

---

## 📅 Timeline

| Task | Due Date | Status |
|------|----------|--------|
| Setup & Testing | Any day | ✅ Pending |
| GitHub Push | Any day | ✅ Pending |
| Streamlit Deployment | Any day | ✅ Pending |
| BITS Lab Run | Any day | ✅ Pending |
| Create PDF | Before 8 Nov | ✅ Pending |
| **Final Submission** | **8 Nov 23:59 PM** | ⏰ Deadline |

---

## 🎓 Assignment Summary

**Objective**: Implement and deploy ML classification system  
**Models**: 5 (LR, DT, KNN, NB, SVM)  
**Metrics**: 6 (Accuracy, AUC, Precision, Recall, F1, MCC)  
**App**: Interactive Streamlit dashboard  
**Deployment**: Streamlit Community Cloud  
**Submission**: PDF with links and documentation  

---

## ✨ You're All Set!

Everything is ready. Follow the checklist above to ensure successful submission.

**Good luck! 🚀**

---

**Print this checklist and check off items as you complete them!**
