import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds
#设置数据的路径以及加载数据
DATA_URL='https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz'
path=tf.keras.utils.get_file('mnist.npz',DATA_URL)
with np.load(path) as data:
    train_examples=data['x_train']
    train_lables=data['y_train']
    test_examples=data['x_test']
    test_lables=data['y_test']

train_dataset=tf.data.Dataset.from_tensor_slices((train_examples,train_lables))
test_dataset=tf.data.Dataset.from_tensor_slices((test_examples,test_lables))

#打乱和批次化数据集
BATCH_SIZE=64
SHUFFLE_BUFFER_SIZE=100
train_dataset=train_dataset.shuffle(SHUFFLE_BUFFER_SIZE).batch(BATCH_SIZE)
test_dataset=test_dataset.batch(BATCH_SIZE)

def create_model():
    model=tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dense(10,activation='softmax')
    ])
    model.compile(
        optimizer=tf.keras.optimizers.RMSprop(),
        loss=tf.keras.losses.SparseCategoricalCrossentropy(),
        metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])
    return model

model=create_model()
model.fit(train_dataset,epochs=10)

model.evaluate(test_dataset)

model.summary()
