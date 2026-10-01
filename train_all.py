import os
import sys

# Ensure current directory is in Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.data_analysis import load_data, inspect_dataset, display_analysis_summary, generate_eda_plots
from src.feature_engineering import add_features, analyze_feature_importance
from src.preprocessing import preprocess_pipeline
from src.regression import run_regression_demonstration
from src.classification import train_classifiers
from src.clustering import run_clustering
from src.neural_network import train_ann
from src.evaluation import evaluate_models

def main():
    print("=" * 60)
    print("STARTING DIABETES PREDICTION AI PIPELINE TRAINING")
    print("=" * 60)
    
    # 1. Load Data
    print("\n[Step 1] Loading raw dataset...")
    df = load_data("data/diabetes.csv")
    if df is None:
        print("Failed to load dataset. Exiting pipeline.")
        return
    print(f"Dataset loaded successfully with shape: {df.shape}")
    
    # 2. Exploratory Data Analysis & Save Plots
    print("\n[Step 2] Performing Pandas Inspection & generating EDA plots...")
    results = inspect_dataset(df)
    display_analysis_summary(results)
    generate_eda_plots(df)
    print("EDA plots saved in 'static/plots/'.")
    
    # 3. Feature Engineering Analysis
    print("\n[Step 3] Running Feature Engineering Analysis...")
    df_eng = add_features(df)
    importance_df = analyze_feature_importance(df_eng)
    print("Feature correlation analysis:")
    print(importance_df.to_string(index=False))
    
    # 4. Data Preprocessing & Scaling
    print("\n[Step 4] Preprocessing dataset (imputation, train-test split, Scaling)...")
    # Note: We pass the raw df. Preprocessing handles imputation on 8 features, 
    # then applies feature engineering, and finally scales the 9 resulting features.
    X_train, X_test, y_train, y_test, imputer, scaler = preprocess_pipeline(df)
    print("Dataset scaling completed and scaler/imputer saved in 'models/'.")
    
    # 5. Regression Demonstration
    print("\n[Step 5] Running separate Educational Regression Demonstration...")
    run_regression_demonstration(df)
    
    # 6. Train Classification Models
    print("\n[Step 6] Training classification models (LR, KNN, Decision Tree)...")
    lr, knn, dt = train_classifiers(X_train, y_train)
    print("Classification models trained and saved in 'models/'.")
    
    # 7. Unsupervised Clustering
    print("\n[Step 7] Running Unsupervised Clustering (K-Means & Hierarchical)...")
    kmeans_labels, hier_labels = run_clustering(df)
    print("Clustering completed and visualizations saved in 'static/plots/'.")
    
    # 8. Train Deep Learning ANN
    print("\n[Step 8] Training Keras Artificial Neural Network (ANN)...")
    ann, history = train_ann(X_train, y_train, X_test, y_test, epochs=35, batch_size=32)
    print("ANN model trained and saved in 'models/ann_model/'.")
    
    # 9. Evaluate Models
    print("\n[Step 9] Evaluating all models on the test set and generating confusion matrices...")
    metrics = evaluate_models(X_test, y_test)
    print("\n" + "=" * 60)
    print("PIPELINE TRAINING AND EVALUATION COMPLETED SUCCESSFULLY")
    print("=" * 60)

if __name__ == "__main__":
    main()
