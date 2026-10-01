import os
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def load_data(filepath="data/diabetes.csv"):
    """
    Loads the diabetes dataset using Pandas.
    """
    try:
        df = pd.read_csv(filepath)
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def inspect_dataset(df):
    """
    Inspects the dataset and returns a dictionary of basic metrics.
    Demonstrates Pandas rows, columns, data types, and null value checks.
    """
    if df is None:
        return {}
    
    num_rows, num_cols = df.shape
    columns = list(df.columns)
    dtypes = df.dtypes.to_dict()
    missing_values = df.isnull().sum().to_dict()
    
    # Statistical summary
    summary_stats = df.describe().to_dict()
    
    # Target (Outcome) class distribution
    class_dist = df['Outcome'].value_counts().to_dict()
    
    analysis_results = {
        'num_rows': num_rows,
        'num_cols': num_cols,
        'columns': columns,
        'dtypes': {k: str(v) for k, v in dtypes.items()},
        'missing_values': missing_values,
        'summary_stats': summary_stats,
        'class_distribution': class_dist
    }
    return analysis_results

def generate_eda_plots(df):
    """
    Generates Matplotlib charts for interpreting the dataset:
    1. Class distribution (Outcome)
    2. Distribution of key features (Glucose, BMI, Age, BloodPressure)
    3. Correlation heatmap
    Saves them to static/plots/
    """
    os.makedirs("static/plots", exist_ok=True)
    
    # Theme configuration helper
    def apply_dark_theme(fig, ax):
        fig.patch.set_facecolor('#0A192F')
        ax.set_facecolor('#0E2238')
        ax.tick_params(colors='#E6F1FF', labelsize=10)
        ax.spines['bottom'].set_color('#00D1FF')
        ax.spines['left'].set_color('#00D1FF')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.title.set_color('#E6F1FF')
        ax.xaxis.label.set_color('#E6F1FF')
        ax.yaxis.label.set_color('#E6F1FF')

    # --- Plot 1: Class Distribution ---
    fig, ax = plt.subplots(figsize=(6, 5))
    counts = df['Outcome'].value_counts()
    bars = ax.bar(['Non-Diabetic (0)', 'Diabetic (1)'], counts.values, color=['#7B61FF', '#00D1FF'], width=0.6)
    
    # Add values on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', color='#E6F1FF', fontweight='bold')
                    
    ax.set_title('Diabetes Class Distribution', fontsize=14, pad=15)
    ax.set_ylabel('Number of Records', fontsize=11)
    apply_dark_theme(fig, ax)
    plt.tight_layout()
    plt.savefig('static/plots/class_dist.png', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()

    # --- Plot 2: Key Feature Histograms ---
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.patch.set_facecolor('#0A192F')
    
    features = [
        ('Glucose', '#00D1FF'),
        ('BMI', '#7B61FF'),
        ('Age', '#FF6B6B'),
        ('BloodPressure', '#FFD166')
    ]
    
    for idx, (col, color) in enumerate(features):
        ax = axes[idx // 2, idx % 2]
        # Drop 0 values for plotting distribution (since 0 is invalid for these features)
        valid_data = df[df[col] > 0][col]
        
        ax.hist(valid_data, bins=20, color=color, edgecolor='#0A192F', alpha=0.85)
        ax.set_title(f'{col} Distribution (Valid Records)', fontsize=12)
        ax.set_xlabel(col, fontsize=10)
        ax.set_ylabel('Frequency', fontsize=10)
        
        # Apply dark theme properties
        ax.set_facecolor('#0E2238')
        ax.tick_params(colors='#E6F1FF')
        ax.spines['bottom'].set_color('#00D1FF')
        ax.spines['left'].set_color('#00D1FF')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.title.set_color('#E6F1FF')
        ax.xaxis.label.set_color('#E6F1FF')
        ax.yaxis.label.set_color('#E6F1FF')
        
    plt.suptitle('Distribution of Continuous Clinical Features', color='#E6F1FF', fontsize=16, y=0.98)
    plt.tight_layout()
    plt.savefig('static/plots/feature_histograms.png', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()

    # --- Plot 3: Correlation Matrix Heatmap ---
    # Filter out columns that shouldn't be included or use all
    corr = df.corr()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.imshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
    
    # Set tick labels
    ax.set_xticks(np.arange(len(corr.columns)))
    ax.set_yticks(np.arange(len(corr.index)))
    ax.set_xticklabels(corr.columns, rotation=45, ha='right', color='#E6F1FF')
    ax.set_yticklabels(corr.index, color='#E6F1FF')
    
    # Loop over data dimensions and create text annotations
    for i in range(len(corr.index)):
        for j in range(len(corr.columns)):
            text = ax.text(j, i, f"{corr.iloc[i, j]:.2f}",
                           ha="center", va="center", color="white" if abs(corr.iloc[i, j]) > 0.4 else "black", fontsize=9, fontweight='bold')
                           
    ax.set_title('Feature Correlation Matrix', fontsize=14, pad=15)
    fig.patch.set_facecolor('#0A192F')
    ax.set_facecolor('#0E2238')
    plt.colorbar(im, ax=ax)
    
    plt.tight_layout()
    plt.savefig('static/plots/correlation_matrix.png', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()

def display_analysis_summary(results):
    """
    Prints the analysis results nicely in the console.
    """
    print("=" * 50)
    print("PANDAS DATA INSPECTION & ANALYSIS")
    print("=" * 50)
    print(f"Number of Rows: {results.get('num_rows')}")
    print(f"Number of Columns: {results.get('num_cols')}")
    print("\nColumns and Data Types:")
    for col, dtype in results.get('dtypes', {}).items():
        print(f" - {col}: {dtype}")
        
    print("\nMissing Values Per Column:")
    for col, val in results.get('missing_values', {}).items():
        print(f" - {col}: {val}")
        
    print("\nClass Distribution (Outcome):")
    for cls, count in results.get('class_distribution', {}).items():
        label = "Diabetic" if cls == 1 else "Non-Diabetic"
        print(f" - {label} ({cls}): {count} records")
    print("=" * 50)

if __name__ == "__main__":
    df = load_data()
    if df is not None:
        results = inspect_dataset(df)
        display_analysis_summary(results)
        generate_eda_plots(df)
        print("EDA plots successfully saved to 'static/plots/'")
