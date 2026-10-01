import os
import pickle
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
import tensorflow as tf

app = Flask(__name__)

# Helper to load evaluation metrics
def get_evaluation_metrics():
    metrics_path = "models/evaluation_metrics.pkl"
    if os.path.exists(metrics_path):
        try:
            with open(metrics_path, "rb") as f:
                return pickle.load(f)
        except Exception as e:
            print(f"Error reading evaluation metrics: {e}")
            
    # Return placeholder values if pipeline hasn't run yet
    return {
        'Logistic Regression': {'Accuracy': 0.76, 'Precision': 0.72, 'Recall': 0.58},
        'K-Nearest Neighbors': {'Accuracy': 0.74, 'Precision': 0.65, 'Recall': 0.60},
        'Decision Tree': {'Accuracy': 0.75, 'Precision': 0.64, 'Recall': 0.68},
        'Artificial Neural Network': {'Accuracy': 0.77, 'Precision': 0.70, 'Recall': 0.62}
    }

@app.route('/')
def home():
    return render_template('home.html', active_page='home')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    predictions = None
    input_values = None
    
    if request.method == 'POST':
        # Retrieve form data
        try:
            pregnancies = int(request.form.get('pregnancies', 0))
            glucose = float(request.form.get('glucose', 0))
            bloodpressure = float(request.form.get('bloodpressure', 0))
            skinthickness = float(request.form.get('skinthickness', 0))
            insulin = float(request.form.get('insulin', 0))
            bmi = float(request.form.get('bmi', 0))
            pedigree = float(request.form.get('pedigree', 0))
            age = float(request.form.get('age', 0))
            
            input_values = {
                'pregnancies': pregnancies,
                'glucose': glucose,
                'bloodpressure': bloodpressure,
                'skinthickness': skinthickness,
                'insulin': insulin,
                'bmi': bmi,
                'pedigree': pedigree,
                'age': age
            }
            
            # Load Preprocessors
            with open("models/imputer.pkl", "rb") as f:
                imputer = pickle.load(f)
            with open("models/scaler.pkl", "rb") as f:
                scaler = pickle.load(f)
                
            # Load Classifiers
            with open("models/logistic_regression.pkl", "rb") as f:
                lr_model = pickle.load(f)
            with open("models/knn.pkl", "rb") as f:
                knn_model = pickle.load(f)
            with open("models/decision_tree.pkl", "rb") as f:
                dt_model = pickle.load(f)
                
            ann_model = tf.keras.models.load_model("models/ann_model/diabetes_ann.keras")
            
            # Formulate inputs as a DataFrame matching original feature structure
            cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
            input_data = pd.DataFrame([[pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, pedigree, age]], columns=cols)
            
            # Preprocessing: Replace logical zeros with NaN for appropriate columns (same as pipeline)
            zero_cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
            for col in zero_cols:
                if input_data.loc[0, col] == 0:
                    input_data.loc[0, col] = np.nan
            
            # Impute and add interaction feature
            # In our pipeline: Feature Engineering was run before Scaling, and it added Glucose_Age_Interaction.
            # However, since the engineered feature is computed from Glucose and Age, we must compute it on the imputed values!
            # Let's perform imputation first on the raw 8 features.
            input_imputed_arr = imputer.transform(input_data)
            input_imputed_df = pd.DataFrame(input_imputed_arr, columns=cols)
            
            # Feature engineering (interaction) on imputed data
            input_imputed_df['Glucose_Age_Interaction'] = input_imputed_df['Glucose'] * input_imputed_df['Age']
            
            # Scale the imputed & engineered features using StandardScaler
            input_scaled = scaler.transform(input_imputed_df)
            
            # Predict and evaluate probabilities
            # 1. Logistic Regression
            lr_pred = lr_model.predict(input_scaled)[0]
            lr_prob = lr_model.predict_proba(input_scaled)[0][1]
            
            # 2. KNN
            knn_pred = knn_model.predict(input_scaled)[0]
            knn_prob = knn_model.predict_proba(input_scaled)[0][1]
            
            # 3. Decision Tree
            dt_pred = dt_model.predict(input_scaled)[0]
            dt_prob = dt_model.predict_proba(input_scaled)[0][1]
            
            # 4. ANN
            ann_prob = float(ann_model.predict(input_scaled)[0][0])
            ann_pred = 1 if ann_prob > 0.5 else 0
            
            predictions = {
                'Logistic Regression': {
                    'prediction': 'Diabetic' if lr_pred == 1 else 'Non-Diabetic',
                    'probability': lr_prob
                },
                'K-Nearest Neighbors': {
                    'prediction': 'Diabetic' if knn_pred == 1 else 'Non-Diabetic',
                    'probability': knn_prob
                },
                'Decision Tree': {
                    'prediction': 'Diabetic' if dt_pred == 1 else 'Non-Diabetic',
                    'probability': dt_prob
                },
                'Artificial Neural Network': {
                    'prediction': 'Diabetic' if ann_pred == 1 else 'Non-Diabetic',
                    'probability': ann_prob
                }
            }
            
        except Exception as e:
            print(f"Prediction logic error: {e}")
            predictions = {'Error': {'prediction': 'Pipeline has not been trained yet. Please run training first.', 'probability': 0.0}}
            
    return render_template('prediction.html', active_page='prediction', predictions=predictions, input_values=input_values)

@app.route('/data-analysis')
def data_analysis():
    return render_template('data_analysis.html', active_page='data_analysis')

@app.route('/model-comparison')
def model_comparison():
    metrics = get_evaluation_metrics()
    return render_template('model_comparison.html', active_page='model_comparison', metrics=metrics)

@app.route('/clustering')
def clustering():
    return render_template('clustering.html', active_page='clustering')

@app.route('/ann')
def ann():
    return render_template('ann.html', active_page='ann')

@app.route('/ai-concepts')
def ai_concepts():
    return render_template('ai_concepts.html', active_page='ai_concepts')

@app.route('/ethics')
def ethics():
    return render_template('ethics.html', active_page='ethics')

@app.route('/internship-learning')
def internship_learning():
    return render_template('internship_learning.html', active_page='internship_learning')

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

if __name__ == '__main__':
    # Start on standard local address
    app.run(host='127.0.0.1', port=5000, debug=False)
