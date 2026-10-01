import os
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for server generation
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

def run_clustering(df, n_clusters=3):
    """
    Runs K-Means and Hierarchical (Agglomerative) Clustering.
    Uses 'Glucose' and 'BMI' features for clustering.
    Saves visual plots to static/plots/.
    """
    print("=" * 50)
    print("CLUSTERING ANALYSIS (UNSUPERVISED LEARNING)")
    print("=" * 50)
    print("Explanation:")
    print(f"Clustering is performed using a fixed number of clusters (K={n_clusters}).")
    print("These clusters represent groups of records with similar characteristics.")
    print("They are NOT medical diagnoses and do NOT represent diabetic/non-diabetic outcome classes.")
    print("-" * 50)
    
    # 1. Prepare data (clean and impute)
    subset = df[['Glucose', 'BMI']].copy()
    subset = subset.replace(0, np.nan)
    
    # Impute missing values
    imputer = SimpleImputer(strategy='median')
    X_imputed = imputer.fit_transform(subset)
    
    # Scale for clustering
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_imputed)
    
    # Create output directories
    os.makedirs("static/plots", exist_ok=True)
    
    # 2. K-Means Clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans_labels = kmeans.fit_predict(X_scaled)
    
    # Plot K-Means
    plt.figure(figsize=(8, 6))
    colors = ['#00D1FF', '#7B61FF', '#FF6B6B']
    for i in range(n_clusters):
        cluster_data = X_imputed[kmeans_labels == i]
        plt.scatter(cluster_data[:, 0], cluster_data[:, 1], c=colors[i], label=f'Group {i+1}', alpha=0.7, edgecolors='none')
    
    # Plot centroids
    centroids_unscaled = scaler.inverse_transform(kmeans.cluster_centers_)
    plt.scatter(centroids_unscaled[:, 0], centroids_unscaled[:, 1], c='#E6F1FF', s=150, marker='*', label='Centroids', edgecolors='black', linewidths=1.5)
    
    plt.title('K-Means Clustering (Groups of Similar Records)', color='#E6F1FF', fontsize=14, pad=15)
    plt.xlabel('Glucose', color='#E6F1FF', fontsize=12)
    plt.ylabel('BMI', color='#E6F1FF', fontsize=12)
    plt.legend(facecolor='#0A192F', edgecolor='#00D1FF', labelcolor='#E6F1FF')
    
    # Theme adjustments
    fig = plt.gcf()
    fig.patch.set_facecolor('#0A192F')
    ax = plt.gca()
    ax.set_facecolor('#0E2238')
    ax.tick_params(colors='#E6F1FF')
    ax.spines['bottom'].set_color('#00D1FF')
    ax.spines['left'].set_color('#00D1FF')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig('static/plots/clustering_kmeans.png', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    
    # 3. Hierarchical Clustering (Agglomerative)
    hierarchical = AgglomerativeClustering(n_clusters=n_clusters)
    hier_labels = hierarchical.fit_predict(X_scaled)
    
    # Plot Hierarchical Clustering
    plt.figure(figsize=(8, 6))
    for i in range(n_clusters):
        cluster_data = X_imputed[hier_labels == i]
        plt.scatter(cluster_data[:, 0], cluster_data[:, 1], c=colors[i], label=f'Group {i+1}', alpha=0.7, edgecolors='none')
        
    plt.title('Hierarchical Clustering (Groups of Similar Records)', color='#E6F1FF', fontsize=14, pad=15)
    plt.xlabel('Glucose', color='#E6F1FF', fontsize=12)
    plt.ylabel('BMI', color='#E6F1FF', fontsize=12)
    plt.legend(facecolor='#0A192F', edgecolor='#00D1FF', labelcolor='#E6F1FF')
    
    # Theme adjustments
    fig = plt.gcf()
    fig.patch.set_facecolor('#0A192F')
    ax = plt.gca()
    ax.set_facecolor('#0E2238')
    ax.tick_params(colors='#E6F1FF')
    ax.spines['bottom'].set_color('#00D1FF')
    ax.spines['left'].set_color('#00D1FF')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig('static/plots/clustering_hierarchical.png', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    
    # Compute cluster statistics for reporting
    df_temp = pd.DataFrame(X_imputed, columns=['Glucose', 'BMI'])
    df_temp['KMeans_Cluster'] = kmeans_labels
    df_temp['Hier_Cluster'] = hier_labels
    
    print("K-Means Cluster Breakdown (Mean Values):")
    for i in range(n_clusters):
        c_mean = df_temp[df_temp['KMeans_Cluster'] == i].mean()
        print(f" Group {i+1}: Glucose = {c_mean['Glucose']:.2f}, BMI = {c_mean['BMI']:.2f}, Size = {len(df_temp[df_temp['KMeans_Cluster'] == i])}")
        
    print("\nPlots successfully saved in 'static/plots/' directory.")
    print("=" * 50)
    
    return kmeans_labels, hier_labels

if __name__ == "__main__":
    from src.data_analysis import load_data
    df = load_data()
    if df is not None:
        run_clustering(df)
