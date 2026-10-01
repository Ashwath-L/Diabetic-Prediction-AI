import pandas as pd
import numpy as np

def add_features(df):
    """
    Applies simple feature engineering consistent with the syllabus.
    Creates an interaction feature: Glucose_Age_Interaction = Glucose * Age
    """
    df_engineered = df.copy()
    
    # Simple interaction term (Data Transformation / Feature Extraction)
    df_engineered['Glucose_Age_Interaction'] = df_engineered['Glucose'] * df_engineered['Age']
    
    return df_engineered

def analyze_feature_importance(df):
    """
    Analyzes the importance of features using correlation with the output label (Outcome).
    This demonstrates feature selection concepts.
    """
    # Calculate correlations
    correlations = df.corr()['Outcome'].sort_values(ascending=False)
    
    # Exclude Outcome itself
    correlations = correlations.drop('Outcome', errors='ignore')
    
    importance_list = []
    for feat, corr in correlations.items():
        importance_list.append({
            'Feature': feat,
            'Correlation': round(corr, 4),
            'Strength': 'Strong' if abs(corr) > 0.4 else ('Moderate' if abs(corr) > 0.2 else 'Weak')
        })
        
    return pd.DataFrame(importance_list)

if __name__ == "__main__":
    from src.data_analysis import load_data
    df = load_data()
    if df is not None:
        df_eng = add_features(df)
        importance_df = analyze_feature_importance(df_eng)
        print("=" * 50)
        print("FEATURE ENGINEERING COMPLETE")
        print("=" * 50)
        print(f"New column added. Engineered DataFrame shape: {df_eng.shape}")
        print("\nFeature Importance (Correlation with Outcome):")
        print(importance_df.to_string(index=False))
        print("=" * 50)
