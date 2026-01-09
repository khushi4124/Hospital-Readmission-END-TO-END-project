**Problem Statement**


Hospital readmission within 30 days of discharge is a major challenge for healthcare systems, reflecting both patient health stability and the quality of care provided. 

For diabetic patients, identifying those at risk is complex due to various factors like medication changes, glucose levels, and previous history. 

This project addresses this by using a dataset of over 1,00,000 instances to build a predictive model that classifies whether a patient is at high or low risk of readmission.

**Dataset Used:** https://www.kaggle.com/datasets/brandao/diabetes?select=diabetic_data.csv

**End-to-End Project Overview**


This project is a complete machine learning solution, covering everything from raw data cleaning and feature engineering to a live web deployment. 

I developed the model using a Scikit-Learn pipeline and integrated it into a Flask web application, allowing users to input patient data and receive an instant risk assessment.

**Approach**

**1. Data Cleaning**


The raw data contained many missing values marked as "?". I performed the following to prepare the data:

Dropped columns with excessive missing values such as weight and payer_code.

Removed rows with missing diagnosis values to maintain data integrity.

Handled the medical_specialty column by grouping low-frequency specialties into an 'other' category.

Replaced missing race values with the mode and medical_specialty missing values with "Unknown".

**2. Feature Engineering**

I transformed the data to make it suitable for machine learning:

Diagnosis Categorization: Simplified ICD-9 codes in diag_1, diag_2, and diag_3 into clinical categories like Circulatory, Respiratory, Digestive, and Diabetes.

ID Conversion: Converted numeric IDs for admission and discharge into meaningful categories like "discharged home", "transferred", or "emergency".

New Features: Created previous_hospital_visits by summing inpatient, outpatient, and emergency visits, and total_procedures by combining lab and non-lab procedures.

**3. Model Building Pipeline**

To ensure the model can be deployed easily, I built a ColumnTransformer and a Pipeline:

Preprocessing: Applied StandardScaler to numeric data, OneHotEncoder to categorical features, and OrdinalEncoder to ordered data like age and medication changes.

Algorithm: Used a Random Forest Classifier with 700 estimators and a max_depth of 15.

**Classification Report Metrics**

The performance of the Random Forest Classifier is evaluated using the following metrics from the final classification report:

**Precision (Class 1: 0.51):** This indicates that when the model flags a patient as "High Risk," it is correct approximately 51% of the time. This helps hospital staff filter down a massive list of patients to a targeted group that truly requires attention.

**Recall (Class 1: 0.94):** The model achieved an exceptionally high Recall of 94% for readmission cases. This means the system successfully identifies almost all patients who are actually at risk of returning to the hospital within 30 days.

**F1-Score (Class 1: 0.66):** The F1-score confirms a robust balance between precision and recall, ensuring the model remains reliable for real-world clinical use.
