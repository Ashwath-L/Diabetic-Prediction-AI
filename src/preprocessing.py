import numpy as np
import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from src.data_analysis import load_data
from src.feature_engineering import add_features

def preprocess_pipeline(df, test_size=0.2, random_state=42):
    """
    Executes a clean data cleaning, imputation, feature engineering, and scaling pipeline.
    """
    # 1. Handle invalid zeros (except for Pregnancies and Outcome, zeros are invalid)
    zero_cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    df_clean = df.copy()
    for col in zero_cols:
        df_clean[col] = df_clean[col].replace(0, np.nan)
        
    # Split into features (X: 8 features) and target (y)
    X = df_clean.drop(columns=['Outcome'])
    y = df_clean['Outcome']
    
    # 2. Train-test split before imputation and scaling to avoid data leakage
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    # 3. Impute missing values on the 8 original features
    imputer = SimpleImputer(strategy='median')
    X_train_imputed_arr = imputer.fit_transform(X_train)
    X_test_imputed_arr = imputer.transform(X_test)
    
    # Convert back to DataFrames to retain column names for feature engineering
    feature_cols = X.columns
    X_train_imputed = pd.DataFrame(X_train_imputed_arr, columns=feature_cols)
    X_test_imputed = pd.DataFrame(X_test_imputed_arr, columns=feature_cols)
    
    # 4. Feature engineering (interaction feature) on the imputed data
    X_train_eng = add_features(X_train_imputed)
    X_test_eng = add_features(X_test_imputed)
    
    # 5. Feature scaling using StandardScaler on all 9 engineered features
    scaler = StandardScaler()
    X_train_scaled_arr = scaler.fit_transform(X_train_eng)
    X_test_scaled_arr = scaler.transform(X_test_eng)
    
    # Convert scaled outputs back to DataFrames
    engineered_cols = X_train_eng.columns
    X_train_scaled = pd.DataFrame(X_train_scaled_arr, columns=engineered_cols)
    X_test_scaled = pd.DataFrame(X_test_scaled_arr, columns=engineered_cols)
    
    # Save the imputer and scaler for deployment
    os.makedirs("models", exist_ok=True)
    with open("models/imputer.pkl", "wb") as f:
        pickle.dump(imputer, f)
    with open("models/scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)
        
    return X_train_scaled, X_test_scaled, y_train, y_test, imputer, scaler

if __name__ == "__main__":
    df = load_data()
    if df is not None:
        X_train_s, X_test_s, y_train, y_test, imp, scl = preprocess_pipeline(df)
        print("=" * 50)
        print("PREPROCESSING COMPLETE")
        print("=" * 50)
        print(f"X_train shape: {X_train_s.shape}")
        print(f"X_test shape: {X_test_s.shape}")
        print("Imputer and Scaler fitted and saved in 'models/' directory.")
        print("=" * 50)
