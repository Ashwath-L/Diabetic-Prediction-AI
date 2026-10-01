import os
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

def train_classifiers(X_train, y_train):
    """
    Trains the three classification models from the syllabus:
    1. Logistic Regression
    2. K-Nearest Neighbors (KNN)
    3. Decision Tree
    """
    # 1. Logistic Regression
    lr_model = LogisticRegression(random_state=42, max_iter=1000)
    lr_model.fit(X_train, y_train)
    
    # 2. K-Nearest Neighbors
    knn_model = KNeighborsClassifier(n_neighbors=5)
    knn_model.fit(X_train, y_train)
    
    # 3. Decision Tree
    dt_model = DecisionTreeClassifier(random_state=42, max_depth=5)
    dt_model.fit(X_train, y_train)
    
    # Save the models
    os.makedirs("models", exist_ok=True)
    with open("models/logistic_regression.pkl", "wb") as f:
        pickle.dump(lr_model, f)
    with open("models/knn.pkl", "wb") as f:
        pickle.dump(knn_model, f)
    with open("models/decision_tree.pkl", "wb") as f:
        pickle.dump(dt_model, f)
        
    return lr_model, knn_model, dt_model

if __name__ == "__main__":
    from src.data_analysis import load_data
    from src.feature_engineering import add_features
    from src.preprocessing import preprocess_pipeline
    
    df = load_data()
    if df is not None:
        df_eng = add_features(df)
        X_train, X_test, y_train, y_test, _, _ = preprocess_pipeline(df_eng)
        lr, knn, dt = train_classifiers(X_train, y_train)
        print("=" * 50)
        print("CLASSIFICATION MODEL TRAINING COMPLETE")
        print("=" * 50)
        print("Successfully trained and saved classification models:")
        print(" - Logistic Regression -> models/logistic_regression.pkl")
        print(" - K-Nearest Neighbors -> models/knn.pkl")
        print(" - Decision Tree       -> models/decision_tree.pkl")
        print("=" * 50)
