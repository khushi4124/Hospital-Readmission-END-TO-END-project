from flask import Flask, render_template, request
import joblib
import pandas as pd
app = Flask(__name__)
model = joblib.load("Readmission_model.pkl")
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    input_data = {
        'age': request.form.get('age'),
        'gender': request.form.get('gender'),
        'race': request.form.get('race'),
        'admission_type': request.form.get('admission_type'),
        'admission_source': request.form.get('admission_source'),
        'medical_specialty': request.form.get('medical_specialty'),
        'diag_1': request.form.get('diag_1'),
        'diag_2': request.form.get('diag_2'),
        'diag_3': request.form.get('diag_3'),
        'discharge_result': request.form.get('discharge_result'),
        'diabetesMed': request.form.get('diabetesMed'),
        'change': request.form.get('change'),
        'max_glu_serum': request.form.get('max_glu_serum'),
        'A1Cresult': request.form.get('A1Cresult'),
        'time_in_hospital': float(request.form.get('time_in_hospital')),
        'previous_hospital_visits': float(request.form.get('previous_hospital_visits')),
        'total_procedures': float(request.form.get('total_procedures'))
    }
    all_meds = ['metformin', 'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride', 'glipizide', 'glyburide', 'tolbutamide', 'pioglitazone', 'rosiglitazone', 'acarbose', 'miglitol', 'tolazamide', 'insulin', 'glyburide-metformin']
    for med in all_meds:
        input_data[med] = request.form.get(med, 'No')
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]

    result = "High Risk of Readmission" if prediction == 1 else "Low Risk of Readmission"
    print(f"DEBUG: The result is {result}")
    return render_template('index.html', prediction_text=f'Patient Risk: {result}')

if __name__ == "__main__":
    app.run(debug=True)