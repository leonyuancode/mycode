
# 使用 tf.data 加载 pandas dataframes
import pandas as pd
import tensorflow as tf

#下载数据
csv_file=tf.keras.utils.get_file('heart_data','https://storage.googleapis.com/applied-dl/heart.csv')
df=pd.read_csv(csv_file)

#将thal（object）列转化为离散数值
df['thal']=pd.Categorical(df['thal'])
df['thal']=df.thal.cat.codes

target=df.pop('target')#将标签提取出来
dataset=tf.data.Dataset.from_tensor_slices((df.values,target.values))

# for feat, targ in dataset.take(5):
#   print ('Features: {}, Target: {}'.format(feat, targ))

train_dataset = dataset.shuffle(len(df)).batch(1)


def create_model():
    model=tf.keras.Sequential([
        tf.keras.layers.Dense(10,activation='relu'),
        tf.keras.layers.Dense(10,activation='relu'),
        tf.keras.layers.Dense(1,activation='sigmoid')
    ])
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    return  model

model=create_model()
model.fit(train_dataset,epochs=15)
print("-----------------------------------------------------------------------")

"""
代替特征列
将字典作为输入传输给模型就像创建 tf.keras.layers.Input 层的匹配字典一样简单，
应用任何预处理并使用 functional api。 您可以使用它作为 feature columns 的替代方法。
"""
inputs={key:tf.keras.layers.Input(shape=(),name=key) for key in df.keys()}
# print(inputs)
# {'age': <tf.Tensor 'age:0' shape=(None,) dtype=float32>, 'sex': <tf.Tensor 'sex:0' shape=(None,) dtype=float32>,
# 'cp': <tf.Tensor 'cp:0' shape=(None,) dtype=float32>, 'trestbps': <tf.Tensor 'trestbps:0' shape=(None,) dtype=float32>,
# 'chol': <tf.Tensor 'chol:0' shape=(None,) dtype=float32>, 'fbs': <tf.Tensor 'fbs:0' shape=(None,) dtype=float32>,
# 'restecg': <tf.Tensor 'restecg:0' shape=(None,) dtype=float32>, 'thalach': <tf.Tensor 'thalach:0' shape=(None,) dtype=float32>,
# 'exang': <tf.Tensor 'exang:0' shape=(None,) dtype=float32>, 'oldpeak': <tf.Tensor 'oldpeak:0' shape=(None,) dtype=float32>,
# 'slope': <tf.Tensor 'slope:0' shape=(None,) dtype=float32>, 'ca': <tf.Tensor 'ca:0' shape=(None,) dtype=float32>,
# 'thal': <tf.Tensor 'thal:0' shape=(None,) dtype=float32>}
x=tf.stack(list(inputs.values()),axis=-1)
x = tf.keras.layers.Dense(10, activation='relu')(x)
output = tf.keras.layers.Dense(1, activation='sigmoid')(x)
model_func = tf.keras.Model(inputs=inputs, outputs=output)
model_func.compile(optimizer='adam',
                   loss='binary_crossentropy',
                   metrics=['accuracy'])

dict_slices = tf.data.Dataset.from_tensor_slices((df.to_dict('list'), target.values)).batch(16)

model_func.fit(dict_slices, epochs=15)
