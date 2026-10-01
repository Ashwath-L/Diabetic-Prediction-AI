import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

os.makedirs("static/presentation_assets", exist_ok=True)

# Generate UI Preview 1: AI Prediction Dashboard
fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
fig.patch.set_facecolor('#0A192F')
ax.set_facecolor('#0A192F')
ax.axis('off')

# Header bar
rect_hdr = patches.Rectangle((0.02, 0.88), 0.96, 0.1, linewidth=1, edgecolor='#00D1FF', facecolor='#172A45', transform=ax.transAxes)
ax.add_patch(rect_hdr)
ax.text(0.05, 0.93, "DIABETES PREDICT.AI  |  AI Patient Clinical Assessment", color='#00D1FF', fontsize=12, fontweight='bold', transform=ax.transAxes, va='center')
ax.text(0.85, 0.93, "Status: Online (Port 5000)", color='#4ECCA3', fontsize=9, transform=ax.transAxes, va='center')

# Input parameters card
rect_input = patches.Rectangle((0.02, 0.12), 0.46, 0.73, linewidth=1, edgecolor='#233554', facecolor='#172A45', transform=ax.transAxes)
ax.add_patch(rect_input)
ax.text(0.05, 0.80, "PATIENT CLINICAL FEATURES", color='#00D1FF', fontsize=10, fontweight='bold', transform=ax.transAxes)

inputs = [
    ("Pregnancies:", "6"),
    ("Plasma Glucose:", "148 mg/dL"),
    ("Blood Pressure:", "72 mmHg"),
    ("Skin Thickness:", "35 mm"),
    ("2-Hour Insulin:", "165 mu U/ml"),
    ("Body Mass Index (BMI):", "33.6 kg/m²"),
    ("Diabetes Pedigree:", "0.627"),
    ("Patient Age:", "50 Years")
]
for i, (label, val) in enumerate(inputs):
    y_pos = 0.73 - (i * 0.07)
    ax.text(0.05, y_pos, label, color='#E6F1FF', fontsize=8.5, transform=ax.transAxes)
    ax.text(0.38, y_pos, val, color='#00D1FF', fontsize=8.5, fontweight='bold', transform=ax.transAxes, ha='right')

# Output cards (4 models)
rect_out = patches.Rectangle((0.50, 0.12), 0.48, 0.73, linewidth=1, edgecolor='#233554', facecolor='#172A45', transform=ax.transAxes)
ax.add_patch(rect_out)
ax.text(0.53, 0.80, "AI MULTI-MODEL PREDICTION RESULTS", color='#7B61FF', fontsize=10, fontweight='bold', transform=ax.transAxes)

models_res = [
    ("Logistic Regression", "Diabetic", "Confidence: 74.8%", "#FF6B6B"),
    ("K-Nearest Neighbors", "Diabetic", "Confidence: 80.0%", "#FF6B6B"),
    ("Decision Tree", "Diabetic", "Confidence: 85.2%", "#FF6B6B"),
    ("Artificial Neural Network", "Diabetic", "Confidence: 79.4%", "#FF6B6B")
]

for i, (name, pred, conf, col) in enumerate(models_res):
    y_card = 0.62 - (i * 0.15)
    r = patches.Rectangle((0.52, y_card), 0.44, 0.12, linewidth=1, edgecolor=col, facecolor='#0E2238', transform=ax.transAxes)
    ax.add_patch(r)
    ax.text(0.54, y_card + 0.08, name, color='#E6F1FF', fontsize=8.5, fontweight='bold', transform=ax.transAxes)
    ax.text(0.54, y_card + 0.03, f"Class: {pred}  |  {conf}", color=col, fontsize=8, transform=ax.transAxes)

# Disclaimer at bottom
ax.text(0.50, 0.05, "* Educational Disclaimer: AI prediction generated for demonstration purposes only. Not a clinical diagnosis.", color='#8892B0', fontsize=7, transform=ax.transAxes, ha='center')

plt.tight_layout()
plt.savefig("static/presentation_assets/ui_prediction_dashboard.png", facecolor='#0A192F', bbox_inches='tight', dpi=200)
plt.close()

# Generate UI Preview 2: Analytics & EDA Hub
fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
fig.patch.set_facecolor('#0A192F')
ax.set_facecolor('#0A192F')
ax.axis('off')

# Header bar
rect_hdr = patches.Rectangle((0.02, 0.88), 0.96, 0.1, linewidth=1, edgecolor='#7B61FF', facecolor='#172A45', transform=ax.transAxes)
ax.add_patch(rect_hdr)
ax.text(0.05, 0.93, "DIABETES PREDICT.AI  |  Data Analysis & Statistical Intelligence", color='#00D1FF', fontsize=12, fontweight='bold', transform=ax.transAxes, va='center')
ax.text(0.85, 0.93, "Records: 768 / Features: 8", color='#E6F1FF', fontsize=9, transform=ax.transAxes, va='center')

# 3 Summary metrics cards
metrics = [
    ("Dataset Samples", "768", "Pima Indian Cohort", '#00D1FF'),
    ("Target Balance", "65.1% / 34.9%", "500 Non-Diab / 268 Diab", '#7B61FF'),
    ("Top Predictor", "Glucose (r=0.47)", "High Correlation with Class", '#4ECCA3')
]

for i, (title, val, sub, col) in enumerate(metrics):
    x_pos = 0.02 + (i * 0.33)
    r = patches.Rectangle((x_pos, 0.58), 0.30, 0.26, linewidth=1, edgecolor=col, facecolor='#172A45', transform=ax.transAxes)
    ax.add_patch(r)
    ax.text(x_pos + 0.02, 0.78, title, color='#8892B0', fontsize=8.5, transform=ax.transAxes)
    ax.text(x_pos + 0.02, 0.69, val, color=col, fontsize=13, fontweight='bold', transform=ax.transAxes)
    ax.text(x_pos + 0.02, 0.62, sub, color='#E6F1FF', fontsize=7.5, transform=ax.transAxes)

# Lower panel: Pipeline & Model Performance Table
rect_tbl = patches.Rectangle((0.02, 0.12), 0.96, 0.42, linewidth=1, edgecolor='#233554', facecolor='#172A45', transform=ax.transAxes)
ax.add_patch(rect_tbl)
ax.text(0.05, 0.48, "MODEL BENCHMARKING & VALIDATION COMPARISON (TEST SPLIT = 154 SAMPLES)", color='#00D1FF', fontsize=9, fontweight='bold', transform=ax.transAxes)

headers = ["Model Architecture", "Accuracy", "Precision", "Recall", "Best Use Case"]
tbl_rows = [
    ["Logistic Regression", "74.68%", "65.38%", "61.82%", "Fast, Interpretable Baseline"],
    ["K-Nearest Neighbors (KNN)", "73.38%", "61.67%", "67.27%", "Instance-based Clustering"],
    ["Decision Tree Classifier", "74.03%", "61.54%", "72.73%", "Highest Recall (Clinical Safety)"],
    ["Artificial Neural Network (ANN)", "75.32%", "67.35%", "60.00%", "Highest Accuracy & Precision"]
]

y_t = 0.42
for j, h in enumerate(headers):
    x_col = 0.05 + (j * 0.19)
    ax.text(x_col, y_t, h, color='#7B61FF', fontsize=8, fontweight='bold', transform=ax.transAxes)

for i, row in enumerate(tbl_rows):
    y_r = 0.35 - (i * 0.06)
    for j, val in enumerate(row):
        x_col = 0.05 + (j * 0.19)
        color = '#00D1FF' if j == 0 else ('#4ECCA3' if j in [1, 2, 3] else '#E6F1FF')
        ax.text(x_col, y_r, val, color=color, fontsize=7.8, transform=ax.transAxes)

ax.text(0.50, 0.05, "Generated automatically from live Flask back-end evaluation scripts.", color='#8892B0', fontsize=7, transform=ax.transAxes, ha='center')

plt.tight_layout()
plt.savefig("static/presentation_assets/ui_analytics_dashboard.png", facecolor='#0A192F', bbox_inches='tight', dpi=200)
plt.close()
print("Generated presentation UI assets successfully.")
