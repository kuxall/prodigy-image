import json
import tensorflow as tf
import numpy as np

# Load the annotated data from the JSONL file exported from Prodigy
def load_data(file_path):
    data = []
    with open(file_path, "r") as f:
        for line in f:
            example = json.loads(line)
            # breakpoint()
            image = example["image"]
            # label = example["task_label"][0] # Access the label from the "task_label" key

            # label = example["annotation"]["label"] # Access the label from the "annotation" key

            label = example["label"][0]
            data.append((image, label))
    return data

# Preprocess the data
def preprocess_data(data):
    X = []
    y = []
    for image, label in data:
        X.append(image)
        y.append(label)
    X = np.array(X)
    y = np.array(y)
    return X, y

# Train a simple convolutional neural network
def train_model(X_train, y_train, X_test, y_test):
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, 3, activation="relu", input_shape=(28, 28, 1)),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(10, activation="softmax")
    ])
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))
    return model

# Load the data
data = load_data("/home/darshan/Documents/anyproimage/images_dataset.jsonl")

# Split the data into train and test sets
train_data = data[:int(0.8 * len(data))]
test_data = data[int(0.8 * len(data)):]

# Preprocess the data
X_train, y_train = preprocess_data(train_data)
X_test, y_test = preprocess_data(test_data)

# Train the model
model = train_model(X_train, y_train, X_test, y_test)

# Save the model for future use
model.save("model.h5")
