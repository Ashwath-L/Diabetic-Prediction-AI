import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

def run_regression_demonstration(df):
    """
    Demonstrates Linear Regression and Multiple Linear Regression.
    Uses the dataset to predict 'BloodPressure' based on other continuous health metrics.
    Clearly marks this as an Educational Regression Demonstration.
    """
    print("=" * 50)
    print("EDUCATIONAL REGRESSION DEMONSTRATION")
    print("=" * 50)
    print("Explanation:")
    print("The diabetes prediction task is a classification problem because the target (Outcome)")
    print("represents binary classes (Diabetic vs Non-Diabetic). Regression is demonstrated")
    print("separately here using 'BloodPressure' as a continuous target variable because")
    print("Linear Regression was a core part of the internship syllabus.")
    print("-" * 50)
    
    # Preprocess specifically for this demonstration
    # Replace zeros with NaN in BloodPressure, BMI, and Age
    demo_df = df[['BloodPressure', 'BMI', 'Age', 'Glucose']].copy()
    demo_df = demo_df.replace(0, np.nan)
    
    # Drop rows where target (BloodPressure) is missing
    demo_df = demo_df.dropna(subset=['BloodPressure'])
    
    # Impute other columns
    imputer = SimpleImputer(strategy='median')
    demo_imputed = pd.DataFrame(imputer.fit_transform(demo_df), columns=demo_df.columns)
    
    # Define Target and Features
    y = demo_imputed['BloodPressure']
    
    # --- 1. Simple Linear Regression (Feature: BMI) ---
    X_simple = demo_imputed[['BMI']]
    X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(X_simple, y, test_size=0.2, random_state=42)
    
    simple_model = LinearRegression()
    simple_model.fit(X_train_s, y_train_s)
    y_pred_s = simple_model.predict(X_test_s)
    
    # Evaluation
    mae_s = mean_absolute_error(y_test_s, y_pred_s)
    r2_s = r2_score(y_test_s, y_pred_s)
    
    print("\n--- 1. Simple Linear Regression ---")
    print(f"Predicting BloodPressure using BMI")
    print(f"Formula: BloodPressure = {simple_model.coef_[0]:.4f} * BMI + {simple_model.intercept_:.4f}")
    print(f"Mean Absolute Error (MAE): {mae_s:.2f} mmHg")
    print(f"Coefficient of Determination (R2): {r2_s:.4f}")
    
    # --- 2. Multiple Linear Regression (Features: BMI, Age, Glucose) ---
    X_multi = demo_imputed[['BMI', 'Age', 'Glucose']]
    X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(X_multi, y, test_size=0.2, random_state=42)
    
    multi_model = LinearRegression()
    multi_model.fit(X_train_m, y_train_m)
    y_pred_m = multi_model.predict(X_test_m)
    
    # Evaluation
    mae_m = mean_absolute_error(y_test_m, y_pred_m)
    r2_m = r2_score(y_test_m, y_pred_m)
    
    print("\n--- 2. Multiple Linear Regression ---")
    print(f"Predicting BloodPressure using BMI, Age, and Glucose")
    print("Coefficients:")
    for feat, coef in zip(X_multi.columns, multi_model.coef_):
        print(f" - {feat}: {coef:.4f}")
    print(f"Intercept: {multi_model.intercept_:.4f}")
    print(f"Mean Absolute Error (MAE): {mae_m:.2f} mmHg")
    print(f"Coefficient of Determination (R2): {r2_m:.4f}")
    print("=" * 50)
    
    return {
        'simple': {
            'features': ['BMI'],
            'coef': simple_model.coef_.tolist(),
            'intercept': simple_model.intercept_,
            'mae': mae_s,
            'r2': r2_s
        },
        'multiple': {
            'features': ['BMI', 'Age', 'Glucose'],
            'coef': multi_model.coef_.tolist(),
            'intercept': multi_model.intercept_,
            'mae': mae_m,
            'r2': r2_m
        }
    }

if __name__ == "__main__":
    from src.data_analysis import load_data
    df = load_data()
    if df is not None:
        run_regression_demonstration(df)
