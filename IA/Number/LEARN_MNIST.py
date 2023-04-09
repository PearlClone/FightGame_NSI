import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

new_model = tf.keras.models.load_model("nn.h5")

new_model.fit(x_train, y_train, epochs=500)
print()
print('=================================================================')
print()
new_model.evaluate(x_test, y_test)

new_model.summary()

new_model.save("./nn.h5")
new_model.save("./neural_net")
new_model.save("./nn_weights.h5")
