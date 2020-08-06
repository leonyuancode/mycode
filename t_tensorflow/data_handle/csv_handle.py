import  functools
import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds

#获取数据
TRAIN_DATA_URL = "https://storage.googleapis.com/tf-datasets/titanic/train.csv"
TEST_DATA_URL = "https://storage.googleapis.com/tf-datasets/titanic/eval.csv"
train_file_path=tf.keras.utils.get_file("train.csv",TRAIN_DATA_URL)
test_file_path=tf.keras.utils.get_file("eval.csv",TEST_DATA_URL)
# print(train_file_path)
# print(test_file_path)
# C:\Users\Administrator\.keras\datasets\train.csv
# C:\Users\Administrator\.keras\datasets\eval.csv

#让numpy数据更容易读
np.set_printoptions(precision=3,suppress=True)

# CSV 文件的每列都会有一个列名。dataset 的构造函数会自动识别这些列名。
# 如果你使用的文件的第一行不包含列名，那么需要将列名通过字符串列表传给 make_csv_dataset 函数的 column_names 参数。
# CSV_COLUMNS = ['survived', 'sex', 'age', 'n_siblings_spouses', 'parch', 'fare', 'class', 'deck', 'embark_town', 'alone']
# dataset = tf.data.experimental.make_csv_dataset(
#     column_names=CSV_COLUMNS,
#     )

# 这个示例使用了所有的列。如果你需要忽略数据集中的某些列，创建一个包含你需要使用的列的列表，然后传给构造器的（可选）参数 select_columns
# dataset = tf.data.experimental.make_csv_dataset(
#   select_columns = columns_to_use,
#  )

#对于包含模型需要预测的值的列是你需要显式指定的。
LABEL_COLUMN = 'survived'
# LABELS = [0, 1]

def get_dataset(file_path):
    dataset=tf.data.experimental.make_csv_dataset(
        file_path,
        batch_size=12,
        label_name=LABEL_COLUMN,
        na_value="?",
        num_epochs=1,
        ignore_errors=True
    )
    return dataset

raw_train_data=get_dataset(train_file_path)
raw_test_data=get_dataset(test_file_path)
print(type(raw_train_data))#<class 'tensorflow.python.data.ops.dataset_ops.PrefetchDataset'>

"""
dataset 中的每个条目都是一个批次，用一个元组（多个样本，多个标签）表示。
样本中的数据组织形式是以列为主的张量（而不是以行为主的张量），
每条数据中包含的元素个数就是批次大小（这个示例中是 12）。
"""
# examples, labels = next(iter(raw_train_data)) # 第一个批次
# print("EXAMPLES: \n", examples, "\n")
# print("LABELS: \n", labels)
"""
分类数据
CSV 数据中的有些列是分类的列。也就是说，这些列只能在有限的集合中取值。
使用 tf.feature_column API 创建一个 tf.feature_column.indicator_column 集合，每个 tf.feature_column.indicator_column 对应一个分类的列。
"""
CATEGORIES = {
    'sex': ['male', 'female'],
    'class' : ['First', 'Second', 'Third'],
    'deck' : ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'embark_town' : ['Cherbourg', 'Southhampton', 'Queenstown'],
    'alone' : ['y', 'n']
}
categorical_columns=[]
for feature,vocab in CATEGORIES.items():
    cat_col=tf.feature_column.categorical_column_with_vocabulary_list(key=feature,vocabulary_list=vocab)
    categorical_columns.append(tf.feature_column.indicator_column(cat_col))

# print(categorical_columns)
# [IndicatorColumn(categorical_column=VocabularyListCategoricalColumn(key='sex', vocabulary_list=('male', 'female'), dtype=tf.string, default_value=-1, num_oov_buckets=0)),
#  IndicatorColumn(categorical_column=VocabularyListCategoricalColumn(key='class', vocabulary_list=('First', 'Second', 'Third'), dtype=tf.string, default_value=-1, num_oov_buckets=0)),
#  IndicatorColumn(categorical_column=VocabularyListCategoricalColumn(key='deck', vocabulary_list=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'), dtype=tf.string, default_value=-1, num_oov_buckets=0)),
#  IndicatorColumn(categorical_column=VocabularyListCategoricalColumn(key='embark_town', vocabulary_list=('Cherbourg', 'Southhampton', 'Queenstown'), dtype=tf.string, default_value=-1, num_oov_buckets=0)),
#  IndicatorColumn(categorical_column=VocabularyListCategoricalColumn(key='alone', vocabulary_list=('y', 'n'), dtype=tf.string, default_value=-1, num_oov_buckets=0))]

def process_continuous_data(mean,data):
    #标准化数据
    data=tf.cast(data,tf.float32)*1/(2*mean)
    return tf.reshape(data,[-1,1])

MEANS = {
    'age' : 29.631308,
    'n_siblings_spouses' : 0.545455,
    'parch' : 0.379585,
    'fare' : 34.385399
}

numerical_columns = []

for feature in MEANS.keys():
  num_col = tf.feature_column.numeric_column(feature, normalizer_fn=functools.partial(process_continuous_data, MEANS[feature]))
  numerical_columns.append(num_col)

#创建预处理层
preprocessing_layer=tf.keras.layers.DenseFeatures(categorical_columns+numerical_columns)

#构建模型
model = tf.keras.Sequential([
  preprocessing_layer,
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(1, activation='sigmoid'),
])

model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy'])

train_data=raw_train_data.shuffle(500)
test_data=raw_test_data
model.fit(train_data,epochs=20)
test_loss,test_accuracy=model.evaluate(test_data)
print('\n\nTest Loss {}, Test Accuracy {}'.format(test_loss, test_accuracy))

#使用 tf.keras.Model.predict 推断一个批次或多个批次的标签。
predictions=model.predict(test_data)

l1=list(test_data)
l2=l1[0]
l3=l2[1]
print(l2)
print("-----------------------------------------------------------")
print(l3)

for prediction,survived in zip(predictions[:10], l3[:10]):
    print("Predicted survival: {:.2%}".format(prediction[0]),
          " | Actual outcome: ",
          ("SURVIVED" if bool(survived) else "DIED"))













