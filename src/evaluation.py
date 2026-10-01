import os
import pickle
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import tensorflow as tf

def evaluate_models(X_test, y_test):
    """
    Evaluates the trained models (Logistic Regression, KNN, Decision Tree, ANN)
    using Accuracy, Precision, Recall, and Confusion Matrices.
    Generates comparison tables and saves charts under static/plots/.
    """
    # 1. Load trained classification models
    with open("models/logistic_regression.pkl", "rb") as f:
        lr_model = pickle.load(f)
    with open("models/knn.pkl", "rb") as f:
        knn_model = pickle.load(f)
    with open("models/decision_tree.pkl", "rb") as f:
        dt_model = pickle.load(f)
        
    # Load ANN model
    ann_model = tf.keras.models.load_model("models/ann_model/diabetes_ann.keras")
    
    # 2. Get predictions
    models = {
        'Logistic Regression': lr_model,
        'K-Nearest Neighbors': knn_model,
        'Decision Tree': dt_model,
        'Artificial Neural Network': ann_model
    }
    
    metrics_summary = {}
    
    # Create static directory if it doesn't exist
    os.makedirs("static/plots", exist_ok=True)
    
    for name, model in models.items():
        if name == 'Artificial Neural Network':
            y_prob = model.predict(X_test).flatten()
            y_pred = (y_prob > 0.5).astype(int)
        else:
            y_pred = model.predict(X_test)
            
        # Calculate metrics
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, zero_division=0)
        rec = recall_score(y_test, y_pred, zero_division=0)
        cm = confusion_matrix(y_test, y_pred)
        
        # Split CM components
        tn, fp, fn, tp = cm.ravel()
        
        metrics_summary[name] = {
            'Accuracy': acc,
            'Precision': prec,
            'Recall': rec,
            'ConfusionMatrix': {
                'TN': int(tn), 'FP': int(fp),
                'FN': int(fn), 'TP': int(tp)
            }
        }
        
        # Plot Confusion Matrix
        plt.figure(figsize=(6, 5))
        plt.imshow([[tn, fp], [fn, tp]], interpolation='nearest', cmap=plt.cm.Blues)
        plt.title(f'Confusion Matrix: {name}', color='#E6F1FF', pad=15)
        
        # Draw values
        labels = [
            [f"True Neg (TN)\n{tn}", f"False Pos (FP)\n{fp}"],
            [f"False Neg (FN)\n{fn}", f"True Pos (TP)\n{tp}"]
        ]
        for i in range(2):
            for j in range(2):
                color = 'white' if (i == 0 and j == 0) or (i == 1 and j == 1) else 'black'
                # Make color high contrast depending on background intensity
                val = cm[i, j]
                # Scale color based on value
                text_color = 'white' if val > (len(y_test)/3) else 'black'
                plt.text(j, i, labels[i][j], ha="center", va="center", color=text_color, fontweight='bold')
                
        plt.colorbar()
        plt.xticks([0, 1], ['Predicted Non-Diabetic', 'Predicted Diabetic'], color='#E6F1FF')
        plt.yticks([0, 1], ['Actual Non-Diabetic', 'Actual Diabetic'], color='#E6F1FF', rotation=90, va="center")
        
        # Styling
        fig = plt.gcf()
        fig.patch.set_facecolor('#0A192F')
        ax = plt.gca()
        ax.set_facecolor('#0E2238')
        ax.tick_params(colors='#E6F1FF')
        
        # Save path formatting
        filename = f"cm_{name.lower().replace(' ', '_').replace('-', '_')}.png"
        plt.tight_layout()
        plt.savefig(f"static/plots/{filename}", facecolor=fig.get_facecolor(), edgecolor='none')
        plt.close()
        
    # 3. Create Model Comparison Bar Chart
    df_metrics = pd.DataFrame(metrics_summary).T.reset_index().rename(columns={'index': 'Model'})
    
    # Save the dataframe metrics as a pickle file
    with open("models/evaluation_metrics.pkl", "wb") as f:
        pickle.dump(metrics_summary, f)
        
    # Generate bar chart
    x = np.arange(len(df_metrics))
    width = 0.25
    
    plt.figure(figsize=(10, 6))
    plt.bar(x - width, df_metrics['Accuracy'], width, label='Accuracy', color='#00D1FF')
    plt.bar(x, df_metrics['Precision'], width, label='Precision', color='#7B61FF')
    plt.bar(x + width, df_metrics['Recall'], width, label='Recall', color='#FF6B6B')
    
    plt.title('Model Performance Comparison', color='#E6F1FF', fontsize=16, pad=15)
    plt.xlabel('Models', color='#E6F1FF', fontsize=12)
    plt.ylabel('Scores', color='#E6F1FF', fontsize=12)
    plt.xticks(x, df_metrics['Model'], color='#E6F1FF')
    plt.ylim(0, 1.1)
    plt.legend(facecolor='#0A192F', edgecolor='#00D1FF', labelcolor='#E6F1FF')
    
    # Styling
    fig = plt.gcf()
    fig.patch.set_facecolor('#0A192F')
    ax = plt.gca()
    ax.set_facecolor('#0E2238')
    ax.tick_params(colors='#E6F1FF')
    ax.spines['bottom'].set_color('#00D1FF')
    ax.spines['left'].set_color('#00D1FF')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.savefig('static/plots/model_comparison.png', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    
    # Print metrics table
    print("=" * 60)
    print("MODEL PERFORMANCE METRICS")
    print("=" * 60)
    print(f"{'Model':<30} | {'Accuracy':<10} | {'Precision':<10} | {'Recall':<10}")
    print("-" * 65)
    for model_name, score in metrics_summary.items():
        acc_str = f"{score['Accuracy']:.4f}"
        prec_str = f"{score['Precision']:.4f}"
        rec_str = f"{score['Recall']:.4f}"
        print(f"{model_name:<30} | {acc_str:<10} | {prec_str:<10} | {rec_str:<10}")
    print("=" * 60)
    
    return metrics_summary

if __name__ == "__main__":
    from src.data_analysis import load_data
    from src.feature_engineering import add_features
    from src.preprocessing import preprocess_pipeline
    
    df = load_data()
    if df is not None:
        df_eng = add_features(df)
        X_train, X_test, y_train, y_test, _, _ = preprocess_pipeline(df_eng)
        evaluate_models(X_test, y_test)
