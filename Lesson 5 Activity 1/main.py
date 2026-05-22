import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train, x_test = x_train / 255.0, x_test / 255.0

model = models.Sequential([
    layers.Flatten(input_shape = (28, 28)),
    layers.Dense(128, activation="relu"),
    layers.Dense(10, activation="softmax")
])

model.compile(
    optimizer = "adam",
    loss = "sparse_categorical_crossentropy",
    metrics = ["accuracy"]
)

model.fit(x_train, y_train, epochs=5)

test_loss, test_acc = model.evaluate(x_test, y_test)

predictions = model.predict(x_test)

i = 567
plt.imshow(x_test[i], cmap = plt.cm.binary)
plt.title(f"Predicted: {predictions[i].argmax()}")
plt.show()

# 1. Convert raw probabilities to hard digit guesses (0 to 9)

predicted_labels = np.argmax(predictions, axis=1)

# 2. Handle True Labels

# If your y_test is one-hot encoded (e.g., [0,0,0,1,0...]), convert it back to integers.

# If your y_test is already integers (0-9), you can just use: true_labels = y_test

true_labels = np.argmax(y_test, axis=1) if len(y_test.shape) > 1 else y_test

# 3. Find indices where the prediction does NOT match the true label

misclassified_indices = np.where(predicted_labels != true_labels)[0]

# 4. Print out a quick summary

print(f"Total misclassified digits: {len(misclassified_indices)} out of {len(x_test)}")

# Let's look at the first 3 mistakes the model made

for idx in misclassified_indices[:3]:
    print(f"Image Index: {idx}")
    print(f" True Label: {true_labels[idx]}")
    print(f" Model's Guess: {predicted_labels[idx]}")


# Optional: Display the first misclassified image using Matplotlib
if len(misclassified_indices) > 0:
    i = misclassified_indices[0]
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plt.title(f"True: {true_labels[i]}, Predicted: {predicted_labels[i]}")
    plt.show()
