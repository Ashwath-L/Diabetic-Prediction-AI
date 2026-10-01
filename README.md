# Diabetes Prediction Using Artificial Intelligence
### Educational Capstone Project - AI/ML Internship

This repository contains the code and documentation for a complete AI/ML internship project developed to predict whether a patient belongs to the diabetic or non-diabetic class. The project is strictly bounded by the concepts, technologies, and algorithms taught in the 15-day Artificial Intelligence internship syllabus.

---

## 1. Problem Statement
Diabetes mellitus is a chronic metabolic disease characterized by high blood sugar levels. Early identification is crucial for prevention and management. This project applies AI and machine learning algorithms to binary classification patterns in physiological data to determine whether individuals are classified as diabetic or non-diabetic.

## 2. Objective
To build an educational, end-to-end AI classification system that loads clinical datasets, cleans missing metrics, engineering interactive features, visualizes features, runs regression demonstrations, trains multiple supervised classifiers, profiles patients with unsupervised clustering, applies deep learning neural networks, and deploys the trained models on a professional Flask web dashboard.

## 3. Dataset
We use the standard **Pima Indians Diabetes Dataset** containing 768 patient observations from female patients of Pima Indian heritage.
- **Features (8)**: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age.
- **Target Output (1)**: Outcome (0 = Non-Diabetic, 1 = Diabetic).

## 4. Technologies Used
- **Programming Language**: Python
- **Data Manipulation**: Pandas, NumPy
- **Visualizations**: Matplotlib
- **Machine Learning**: Scikit-Learn
- **Deep Learning**: TensorFlow, Keras
- **Web App / Deployment**: Flask (with Jinja2 templates, HTML, CSS, client JS)
- **Interactive Playground**: Jupyter Notebook

## 5. Methodology
The project represents the complete **AI Project Lifecycle**:
```
Problem Identification ──► Data Collection ──► Data Analysis ──► Data Preprocessing
                                                                      │
Documentation ◄── Testing ◄── Deployment ◄── Model Selection ◄── Feature Engineering
```

## 6. Data Preprocessing
- **Invalid Zeros Treatment**: Physical variables (Glucose, Blood Pressure, Skin Thickness, Insulin, and BMI) cannot have a value of 0. These values are treated as missing observations and replaced with `np.nan`.
- **Imputation**: Missing values are imputed with the median of each column to ensure robustness against outliers.
- **Scaling**: Standardized using `StandardScaler` to ensure zero mean and unit variance.

## 7. Feature Engineering
- **Interaction Term**: Created a simple interactive feature to capture joint risk: `Glucose_Age_Interaction = Glucose * Age`.
- **Feature Selection & Importance**: Checked feature correlations with the outcome label using Pandas correlation ranking.

## 8. Regression Demonstration
- **Simple Linear Regression**: Predicted continuous `BloodPressure` using `BMI`.
- **Multiple Linear Regression**: Predicted continuous `BloodPressure` using `BMI`, `Age`, and `Glucose`.
- *Note: Regression is included purely as an educational demonstration of the syllabus topic. Tabular diabetes classification uses binary classification.*

## 9. Classification Models
Trained three classifiers on the scaled training features:
1. **Logistic Regression**: Linear boundary classification utilizing the sigmoid function.
2. **K-Nearest Neighbors (KNN)**: Non-parametric distance-based instance voting (\(K=5\)).
3. **Decision Tree**: Rule-based structural splits on clinical metrics.

## 10. Clustering
- **K-Means Clustering**: Data-driven grouping of records based on Glucose and BMI using a fixed \(K=3\) clusters.
- **Hierarchical Clustering**: Bottom-up agglomerative grouping.
- *Note: Clusters represent groups of patients with similar physical characteristics, NOT clinical diagnoses.*

## 11. Artificial Neural Network (ANN)
Designed a feedforward Deep Neural Network using TensorFlow/Keras:
- **Input Layer**: 9 features (including the engineered interaction feature).
- **Hidden Layer 1**: 16 neurons with `ReLU` activation.
- **Hidden Layer 2**: 8 neurons with `ReLU` activation.
- **Output Layer**: 1 neuron with `Sigmoid` activation for binary outcome probability.
- **Compilation**: Optimizer `Adam` and Loss function `binary_crossentropy`.

## 12. Model Evaluation
Evaluated Logistic Regression, KNN, Decision Tree, and ANN on the test set. Measured:
- **Accuracy**, **Precision**, and **Recall**.
- Generated **Confusion Matrices** identifying True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives (FN).

## 13. Deployment
The Flask web server loads the fitted imputer, scaler, and model files. It exposes endpoints for:
- Home: Dashboard overview.
- Prediction: Form receiving patient inputs, cleaning zeros, imputing, scaling, and outputting individual predictions from all 4 models.
- Data Analysis, Model Comparison, Clustering, ANN, Ethics, Concepts, Internship Learning, and About pages.

## 14. AI Ethics
- **Bias**: Selection bias of using a single demographic cohort.
- **Fairness**: Equal performance across demographic subdivisions.
- **Transparency**: Decision Trees/Logistic Regression are white-box; ANNs are black-box.
- **Privacy**: Safe storage of clinical inputs.
- **Safeguard Disclaimer**:
  > **Educational Disclaimer:** This project is developed for Artificial Intelligence internship learning and demonstration purposes only. The predictions generated by these machine learning models are not medical diagnoses and should not be used for medical decision-making. Please consult a qualified healthcare professional for medical advice.

## 15. 15-Day Internship Learning Mapping
Mapped day-by-day to show where each concept is demonstrated:
- **Day 1**: AI Fundamentals and intelligent agent formulation.
- **Day 2**: Python classes, functions, and NumPy matrices.
- **Day 3**: Pandas CSV loading and Matplotlib visualizations.
- **Day 4**: Jupyter environment and ML types.
- **Day 5**: SimpleImputer and StandardScaler preprocessing.
- **Day 6**: Linear Regression and Supervised classifiers (LR, KNN, DT).
- **Day 7**: Accuracy/Precision/Recall evaluation and Clustering (K-Means/Hierarchical).
- **Day 8**: ANN building and training in Keras.
- **Day 9**: CNN & NLP concept reviews (filters, tokenization, sentiment).
- **Day 10**: TensorFlow library checks and Computer Vision (Face Recognition/Object Detection).
- **Day 11**: Recommendation systems and Ethics/Privacy practices.
- **Day 12**: Generative AI LLMs and Prompt Engineering structured templates.
- **Day 13**: Lifecycle modeling and model deployment on Flask.
- **Day 14**: Healthcare applications and mini-project codebase.
- **Day 15**: Model testing splits, verification, and presentations.

## 16. Results
- Output results (Accuracy, Precision, Recall) are populated dynamically upon training completion.

## 17. Limitations
- Single demographic cohort (Pima Indian women) limits generalization.
- Simple features without time-series, lifestyle, or dietary history.

## 18. Future Scope
- Integrating continuous glucose monitoring (CGM) IoT feeds.
- Extending dataset demographics.

---

## 19. How to Run

### Prerequisite: Install dependencies
Ensure Python is installed on your system. Run:
```bash
pip install -r requirements.txt
```

### Step 1: Train Models & Generate Visualizations
Run the pipeline training script. This downloads the dataset, cleans it, trains all models, and generates Matplotlib charts:
```bash
python train_all.py
```

### Step 2: Start the Web Dashboard
Launch the Flask local web server:
```bash
python app.py
```

### Step 3: Access the App
Open your browser and navigate to:
[http://127.0.0.1:5000](http://127.0.0.1:5000)
