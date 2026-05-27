import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 1. Load MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# 2. Normalize the data
x_train, x_test = x_train / 255.0, x_test / 255.0

# 3. Reshape for ImageDataGenerator (Height, Width, Channels)
# ImageDataGenerator requires a channel dimension, so we add a 1 for grayscale.
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# 4. Data Augmentation
datagen = ImageDataGenerator(
    rotation_range=10,
    zoom_range=0.1,
    width_shift_range=0.1,
    height_shift_range=0.1
)

# Fit the generator on the correctly shaped training data
datagen.fit(x_train)

# 5. Build the model
model = models.Sequential([
    # Input shape now expects the channel dimension (28, 28, 1)
    layers.Flatten(input_shape=(28, 28, 1)),
    layers.Dense(128, activation=layers.LeakyReLU(alpha=0.1)),
    layers.Dense(64, activation=layers.LeakyReLU(alpha=0.1)),
    layers.Dense(10, activation='softmax')
])

# 6. Compile the model
model.compile(optimizer='rmsprop',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 7. Train the model with augmented data
model.fit(datagen.flow(x_train, y_train, batch_size=32), epochs=10)

# 8. Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"\nTest accuracy: {test_acc}")

# 9. Make predictions
predictions = model.predict(x_test)

# 10. Display the first image and prediction
# Squeeze removes the single channel dimension so matplotlib can plot it as a 2D grid
plt.imshow(x_test[0].squeeze(), cmap=plt.cm.binary)
plt.title(f"Predicted: {predictions[0].argmax()}")
plt.show()