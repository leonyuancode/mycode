
import  tensorflow as tf
from tensorflow.keras import  layers
from tensorflow.keras import regularizers
# print(tf.__version__)

import tensorflow_docs as tfdocs
import tensorflow_docs.modeling
import tensorflow_docs.plots

from  IPython import display
from matplotlib import pyplot as plt

import numpy as np

import pathlib
import shutil
import tempfile

#日志的地址
logdir = pathlib.Path(tempfile.mkdtemp())/"tensorboard_logs"
shutil.rmtree(logdir, ignore_errors=True)
print("log================",logdir)


#加载数据（28个属性，1个二进制类标签）
gz = tf.keras.utils.get_file('HIGGS.csv.gz', 'http://mlphysics.ics.uci.edu/data/higgs/HIGGS.csv.gz')

FEATURES=28
#直接从压缩包中读取数据，不用中间减压一步
ds=tf.data.experimental.CsvDataset(gz,[float(),]*(FEATURES+1),compression_type="GZIP")

#拆分数据，把属性和标签拆分开
def pack_row(*row):
    label=row[0]
    features=tf.stack(row[1:],1)
    return features,label
packed_ds=ds.batch(10000).map(pack_row).unbatch()
# #用图表展示第一个数据的属性
# for features,label in packed_ds.batch(1000).take(1):
#     print(features[0])
#     plt.hist(features.numpy().flatten(),bins=101)
# plt.show()


N_VALIDATION = int(1e3)#验证集1000个
N_TRAIN = int(1e4)#训练集10000个
BUFFER_SIZE = int(1e4)#缓存的大小10000
BATCH_SIZE = 500#批大小500
STEPS_PER_EPOCH = N_TRAIN//BATCH_SIZE#每一代的步骤数（20）
# print(N_TRAIN)
# print(STEPS_PER_EPOCH)

#获取验证集和训练集的数据
validate_ds=packed_ds.take(N_VALIDATION).cache()#1000个验证集
train_ds=packed_ds.skip(N_VALIDATION).take(N_TRAIN).cache()#10000个训练集

# 验证集和训练集划分成批
validate_ds=validate_ds.batch(BATCH_SIZE)
train_ds=train_ds.shuffle(BUFFER_SIZE).repeat().batch(BATCH_SIZE)

"""python
    def decayed_learning_rate(step):
      return initial_learning_rate / (1 + decay_rate * step / decay_step)
"""
#优化器，学习率初始是0.001，每1000个epoch为单位
lr_schedule=tf.keras.optimizers.schedules.InverseTimeDecay(
    0.001,decay_steps=STEPS_PER_EPOCH*1000,
    decay_rate=1,staircase=False)
# print("-------------------------------------lllllllllllllllllll---------------------------------")
# print(lr_schedule)

def get_optimizer():
    return tf.keras.optimizers.Adam(lr_schedule)

# step=np.linspace(0,100000)
# lr=lr_schedule(step)
# plt.figure(figsize=(8,6))
# plt.plot(step/STEPS_PER_EPOCH,lr)
# plt.ylim([0,max(plt.ylim())])
# plt.xlabel('Epoch')
# _ =plt.ylabel('learning Rate')
# plt.show()

def get_callbacks(name):
  return [
    tfdocs.modeling.EpochDots(),
    tf.keras.callbacks.EarlyStopping(monitor='val_binary_crossentropy', patience=200),
    tf.keras.callbacks.TensorBoard(logdir/name),
  ]

def compile_and_fit(model, name, optimizer=None, max_epochs=10000):
  if optimizer is None:
    optimizer = get_optimizer()
  model.compile(optimizer=optimizer,
                loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                metrics=[
                  tf.keras.losses.BinaryCrossentropy(
                      from_logits=True, name='binary_crossentropy'),
                  'accuracy'])

  model.summary()

  history = model.fit(
    train_ds,
    steps_per_epoch = STEPS_PER_EPOCH,
    epochs=max_epochs,
    validation_data=validate_ds,
    callbacks=get_callbacks(name),
    verbose=0)
  return history


#微模型（一隐层）
tiny_model = tf.keras.Sequential([
    layers.Dense(16, activation='elu', input_shape=(FEATURES,)),
    layers.Dense(1)
])

size_histories = {}
size_histories['Tiny'] = compile_and_fit(tiny_model, 'sizes/Tiny')

plotter = tfdocs.plots.HistoryPlotter(metric = 'binary_crossentropy', smoothing_std=10)
plotter.plot(size_histories)
plt.ylim([0.5, 0.7])
plt.show()

#小模型（两隐层）
small_model = tf.keras.Sequential([
    # `input_shape` is only required here so that `.summary` works.
    layers.Dense(16, activation='elu', input_shape=(FEATURES,)),
    layers.Dense(16, activation='elu'),
    layers.Dense(1)
])

size_histories['Small'] = compile_and_fit(small_model, 'sizes/Small')

#中等模型（三隐层）64 units
medium_model = tf.keras.Sequential([
    layers.Dense(64, activation='elu', input_shape=(FEATURES,)),
    layers.Dense(64, activation='elu'),
    layers.Dense(64, activation='elu'),
    layers.Dense(1)
])
size_histories['Medium']  = compile_and_fit(medium_model, "sizes/Medium")

#大模型（四隐层）512units
large_model = tf.keras.Sequential([
    layers.Dense(512, activation='elu', input_shape=(FEATURES,)),
    layers.Dense(512, activation='elu'),
    layers.Dense(512, activation='elu'),
    layers.Dense(512, activation='elu'),
    layers.Dense(1)
])
size_histories['large'] = compile_and_fit(large_model, "sizes/large")


plotter.plot(size_histories)
a = plt.xscale('log')
plt.xlim([5, max(plt.xlim())])
plt.ylim([0.5, 0.7])
plt.xlabel("Epochs [Log Scale]")
plt.show()

display.IFrame(
    src="https://tensorboard.dev/experiment/vW7jmmF9TmKmy3rbheMQpw/#scalars&_smoothingWeight=0.97",
    width="100%", height="800px")


#Strategies to prevent overfitting

shutil.rmtree(logdir/'regularizers/Tiny', ignore_errors=True)
shutil.copytree(logdir/'sizes/Tiny', logdir/'regularizers/Tiny')
regularizer_histories = {}
regularizer_histories['Tiny'] = size_histories['Tiny']
# L1正则化,增加的代价与权重系数的绝对值成比例
# L2正则化,增加的代价与权重系数的平方成正比

print("Strategies to prevent overfitting=============================================================================================")
l2_model = tf.keras.Sequential([
    layers.Dense(512, activation='elu',
                 kernel_regularizer=regularizers.l2(0.001),
                 input_shape=(FEATURES,)),
    layers.Dense(512, activation='elu',
                 kernel_regularizer=regularizers.l2(0.001)),
    layers.Dense(512, activation='elu',
                 kernel_regularizer=regularizers.l2(0.001)),
    layers.Dense(512, activation='elu',
                 kernel_regularizer=regularizers.l2(0.001)),
    layers.Dense(1)
])

regularizer_histories['l2'] = compile_and_fit(l2_model, "regularizers/l2")
plotter.plot(regularizer_histories)
plt.ylim([0.5, 0.7])
plt.show()


# result = l2_model(FEATURES)
# regularization_loss=tf.add_n(l2_model.losses)

# dropout：一种防止神经网络过拟合的手段。
# 随机的拿掉网络中的部分神经元，从而减小对W权重的依赖，以达到减小过拟合的效果。
# 注意：dropout只能用在训练中，测试的时候不能dropout，要用完整的网络测试哦

dropout_model = tf.keras.Sequential([
    layers.Dense(512, activation='elu', input_shape=(FEATURES,)),
    layers.Dropout(0.5),
    layers.Dense(512, activation='elu'),
    layers.Dropout(0.5),
    layers.Dense(512, activation='elu'),
    layers.Dropout(0.5),
    layers.Dense(512, activation='elu'),
    layers.Dropout(0.5),
    layers.Dense(1)
])

regularizer_histories['dropout'] = compile_and_fit(dropout_model, "regularizers/dropout")

# Combined L2 + dropout
combined_model = tf.keras.Sequential([
    layers.Dense(512, kernel_regularizer=regularizers.l2(0.0001),
                 activation='elu', input_shape=(FEATURES,)),
    layers.Dropout(0.5),
    layers.Dense(512, kernel_regularizer=regularizers.l2(0.0001),
                 activation='elu'),
    layers.Dropout(0.5),
    layers.Dense(512, kernel_regularizer=regularizers.l2(0.0001),
                 activation='elu'),
    layers.Dropout(0.5),
    layers.Dense(512, kernel_regularizer=regularizers.l2(0.0001),
                 activation='elu'),
    layers.Dropout(0.5),
    layers.Dense(1)
])

regularizer_histories['combined'] = compile_and_fit(combined_model, "regularizers/combined")
# View in TensorBoard
# %tensorboard --logdir {logdir}/regularizers

display.IFrame(
    src="https://tensorboard.dev/experiment/fGInKDo8TXes1z7HQku9mw/#scalars&_smoothingWeight=0.97",
    width = "100%",
    height="800px")

