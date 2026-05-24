import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalising the values to make them range from 0 to 1
x_train, x_test = x_train/255.0, x_test/255.0


datagen = ImageDataGenerator(
    rotation_range=10,
    zoom_range=0.1,
    width_shift_range=0.1,
    height_shift_range=0.1
)

datagen.fit(x_train)



model = models.Sequential([
    layers.Flatten(input_shape = (28, 28)),
    layers.Dense(128, activation = tf.keras.layers.LeakyReLU(alpha = 0.1)),
    layers.Dense(64, activation = tf.keras.layers.LeakyReLU(alpha = 0.1)),
    layers.Dense(10, activation = "softmax")
])

model.compile(
    optimizer = 'rmsprop',
    loss = 'spare_categorical_crossentropy',
    metrics = ['accuracy']
)

model.fit(x_train, y_train, epochs=5)

test_loss, test_acc = model.evaluate(x_test, y_test)

# Making Predictions
predictions = model.predict(x_test)

# Image Display
i = 567
plt.imshow(x_test[i], cmap = plt.cm.binary)
plt.title(f"Predicted: {predictions[i].argmax()}")
plt.show()