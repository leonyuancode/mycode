import  os
import tensorflow as tf
from tensorflow import  keras
# print(tf.version.VERSION)
# print(tf.__version__)

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
# print(train_images.shape) #(60000, 28, 28)
# print(test_labels.shape) #(10000,)
train_labels = train_labels[:1000]#1000个数字
test_labels = test_labels[:1000]
# print(train_images[:1000].shape)#(1000, 28, 28)
train_images = train_images[:1000].reshape(-1, 28 * 28) / 255.0
test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0

def create_model():
    model=tf.keras.models.Sequential([
        keras.layers.Dense(512,activation='relu',input_shape=(784,)),#一个784维的向量
        keras.layers.Dropout(0.2),
        keras.layers.Dense(10)
    ])
    model.compile(optimizer='adam',
                  loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    return  model

model=create_model()
model.summary()
