import tensorflow as tf
from tensorflow import keras
import IPython
import kerastuner as kt

(img_train, label_train), (img_test, label_test) = keras.datasets.fashion_mnist.load_data()
img_train = img_train.astype('float32') / 255.0
img_test = img_test.astype('float32') / 255.0

hh=kt.HyperParameters()

# define the model
def model_builder(hp):
    model = keras.Sequential()
    model.add(keras.layers.Flatten(input_shape=(28, 28)))

    # Tune the number of units in the first Dense layer
    # Choose an optimal value between 32-512
    hp_units = hp.Int('units', min_value=32, max_value=512, step=32)  # 从32至512的范围内搜索第一层神经元个数
    model.add(keras.layers.Dense(units=hp_units, activation='relu'))
    model.add(keras.layers.Dense(10))
    # Tune the learning rate for the optimizer
    # Choose an optimal value from 0.01, 0.001, or 0.0001
    hp_learning_rate = hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])  # 从0.01，0.001和0.0001中搜索最佳的学习率
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=hp_learning_rate),
                  loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    return model


#实例化Hyperband，需要指定超模型、优化的目标（函数）、最大迭代次数等
tuner = kt.Hyperband(model_builder,
                     objective='val_accuracy',
                     max_epochs=10,
                     factor=3,
                     directory='my_dir',
                     project_name='intro_to_kt',
                     overwrite=True)# overwrite参数删除之前保存的checkpoint和log，从头开始搜索

class ClearTrainingOutput(tf.keras.callbacks.Callback):
    def on_train_end(*args, **kwargs):
        IPython.display.clear_output(wait=True)
        pass


tuner.search(img_train, label_train, epochs=10,
             validation_data=(img_test, label_test), callbacks=[ClearTrainingOutput()])

# Get the optimal hyperparameters
best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]

print(f"""
The hyperparameter search is complete. The optimal number of units in the first densely-connected
layer is {best_hps.get('units')} and the optimal learning rate for the optimizer
is {best_hps.get('learning_rate')}.
""")

# Build the model with the optimal hyperparameters and train it on the data
model = tuner.hypermodel.build(best_hps)
model.fit(img_train, label_train, epochs=10, validation_data=(img_test, label_test))

"""
训练步骤：
    1、建立了超模(模型的额层数，)
    2、实例化Hyperband(RandomSearch, Hyperband, BayesianOptimization, and Sklearn)
    3、tuner.search
    4、tuner.get_best_hyperparameters
    5、tuner.hypermodel.build(best_hps)

"""