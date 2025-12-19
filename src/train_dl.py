import tensorflow as tf
from tensorflow import keras

def train_mlp(X_train, y_train, num_classes):
    model = keras.Sequential([
        keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(num_classes, activation='softmax')
    ])

    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    model.fit(X_train, y_train, epochs=50, batch_size=8, validation_split=0.2)
    model.save("models/model_mlp.h5")

    return model
