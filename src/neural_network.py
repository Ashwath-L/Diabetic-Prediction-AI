import os
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def build_ann(input_dim):
    """
    Constructs a basic feedforward Artificial Neural Network (ANN) using Keras.
    Contains:
    - Input Layer: dimension matches feature count
    - Hidden Layer 1: 16 neurons, ReLU activation
    - Hidden Layer 2: 8 neurons, ReLU activation
    - Output Layer: 1 neuron, Sigmoid activation (for binary outcome)
    """
    model = Sequential([
        Dense(16, activation='relu', input_shape=(input_dim,), name='hidden_layer_1'),
        Dense(8, activation='relu', name='hidden_layer_2'),
        Dense(1, activation='sigmoid', name='output_layer')
    ])
    
    # Compile the model
    model.compile(
        optimizer='adam', 
        loss='binary_crossentropy', 
        metrics=['accuracy']
    )
    return model

def train_ann(X_train, y_train, X_test, y_test, epochs=50, batch_size=32):
    """
    Trains the ANN on the preprocessed training dataset.
    Saves the training progress plot and the model weights.
    """
    input_dim = X_train.shape[1]
    model = build_ann(input_dim)
    
    print("\nANN ARCHITECTURE SUMMARY:")
    model.summary()
    
    # Train the model
    history = model.fit(
        X_train, y_train,
        validation_data=(X_test, y_test),
        epochs=epochs,
        batch_size=batch_size,
        verbose=1
    )
    
    # Save the model
    os.makedirs("models/ann_model", exist_ok=True)
    # Save in standard Keras format
    model.save("models/ann_model/diabetes_ann.keras")
    
    # Plot training history (Loss & Accuracy)
    plt.figure(figsize=(12, 5))
    
    # Accuracy Plot
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Train Accuracy', color='#00D1FF', linewidth=2)
    plt.plot(history.history['val_accuracy'], label='Val Accuracy', color='#7B61FF', linewidth=2)
    plt.title('ANN Accuracy Over Epochs', color='#E6F1FF')
    plt.xlabel('Epochs', color='#E6F1FF')
    plt.ylabel('Accuracy', color='#E6F1FF')
    plt.legend(facecolor='#0A192F', edgecolor='#00D1FF', labelcolor='#E6F1FF')
    plt.tick_params(colors='#E6F1FF')
    
    # Theme adjustments
    ax = plt.gca()
    ax.set_facecolor('#0E2238')
    ax.spines['bottom'].set_color('#00D1FF')
    ax.spines['left'].set_color('#00D1FF')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Loss Plot
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Train Loss', color='#00D1FF', linewidth=2)
    plt.plot(history.history['val_loss'], label='Val Loss', color='#7B61FF', linewidth=2)
    plt.title('ANN Loss Over Epochs', color='#E6F1FF')
    plt.xlabel('Epochs', color='#E6F1FF')
    plt.ylabel('Loss', color='#E6F1FF')
    plt.legend(facecolor='#0A192F', edgecolor='#00D1FF', labelcolor='#E6F1FF')
    plt.tick_params(colors='#E6F1FF')
    
    # Theme adjustments
    ax = plt.gca()
    ax.set_facecolor('#0E2238')
    ax.spines['bottom'].set_color('#00D1FF')
    ax.spines['left'].set_color('#00D1FF')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    fig = plt.gcf()
    fig.patch.set_facecolor('#0A192F')
    
    plt.tight_layout()
    plt.savefig('static/plots/ann_training.png', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    
    print("\nANN training complete. Model saved to 'models/ann_model/diabetes_ann.keras'.")
    print("Training plot saved to 'static/plots/ann_training.png'.")
    
    return model, history

if __name__ == "__main__":
    from src.data_analysis import load_data
    from src.feature_engineering import add_features
    from src.preprocessing import preprocess_pipeline
    
    df = load_data()
    if df is not None:
        df_eng = add_features(df)
        X_train, X_test, y_train, y_test, _, _ = preprocess_pipeline(df_eng)
        train_ann(X_train, y_train, X_test, y_test, epochs=30)
