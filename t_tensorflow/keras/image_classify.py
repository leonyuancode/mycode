# from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds

# print("Version: ", tf.__version__)
# print("Eager mode: ", tf.executing_eagerly())
# print("Hub version: ", hub.__version__)
# print("GPU is", "available" if tf.config.experimental.list_physical_devices("GPU") else "NOT AVAILABLE")

#加载IMDB数据集
# 将训练集按照 6:4 的比例进行切割，从而最终我们将得到 15,000
# 个训练样本, 10,000 个验证样本以及 25,000 个测试样本
# train_validation_split = tfds.Split.TRAIN.subsplit([6, 4])
#
# (train_data, validation_data), test_data = tfds.load(
#     name="imdb_reviews",
#     split=(train_validation_split, tfds.Split.TEST),
#     as_supervised=True)
(train_data, validation_data, test_data) = tfds.load(
    name="imdb_reviews",
    split=('train[:60%]', 'train[60%:]', 'test'),
    as_supervised=True)

print("=============",type(train_data))

train_examples_batch, train_labels_batch = next(iter(train_data.batch(10)))
# print(train_examples_batch)
# print(train_labels_batch)

#1、如何表示文本 ：将句子转换为嵌入向量，使用一个事先训练好的文本嵌入作为首层，
                  # 好处：1）不必担心文本预处理 2）从迁移学习中受益 3）嵌入具有固定长度，更易于处理
#2、模型里有多少层
#3、每个层里有多少隐层单元
#输入的数据由句子组成，预测标签为0或者1


#我们首先创建一个使用Tensorflow Hub 模型嵌入（embed）语句的Keras层，并在几个输入样本中进行尝试。
# 无论输入文本长度如何，嵌入（embedding）输出的形状都是（num_examples, embedding_dimension）
embedding = "https://hub.tensorflow.google.cn/google/tf2-preview/gnews-swivel-20dim/1"
hub_layer = hub.KerasLayer(embedding, input_shape=[],
                           dtype=tf.string, trainable=True)
print(hub_layer(train_examples_batch[:3]))

#构建完整的模型
model=tf.keras.Sequential()
model.add(hub_layer)
model.add(tf.keras.layers.Dense(16,activation='relu'))
model.add(tf.keras.layers.Dense(1,activation='sigmoid'))
model.summary()
#损失函数与优化器
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(train_data.shuffle(10000).batch(512),
                    epochs=20,
                    validation_data=validation_data.batch(512),
                    verbose=1)

results = model.evaluate(test_data.batch(512), verbose=2)
for name, value in zip(model.metrics_names, results):
  print("%s: %.3f" % (name, value))
