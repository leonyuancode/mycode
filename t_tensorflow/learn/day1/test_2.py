# 二、Tensor与Numpy的ndarry转换
# 1、Tensor转换为ndarry

import  tensorflow as tf
import  numpy as np
tf.compat.v1.disable_eager_execution()#tensorlow 2.0版本不支持1.0版本，添加此语句保证可以正常运行
t=tf.constant([1,2,3],tf.float32)
sess = tf.compat.v1.Session()
array=sess.run(t)
print(type(array))
print(array)
array=t.eval(session=sess)#利用Tensor的成员函数eval转化为ndarry
print(array)

with tf.compat.v1.Session() as sess_2:
    array=t.eval()
    print(array)

# 二、ndarry转化为tensor ，通过conver_to_tensor 实现将ndarry转化为Tensor的功能
array=np.array([1,2,3],np.float32)
t=tf.convert_to_tensor(array,tf.float32,name='t')
print(t)
print("-------------------------------------------------")
# 三、张量的尺寸
# 1、利用shape得到张量的尺寸
t=tf.constant(
    [
        [1,2,3],
        [4,3,5]
    ],tf.float32
)
s=tf.shape(t)
print(s)
print(sess.run(s))
# 2、利用get_shape()或成员变量shape得到张量的尺寸
s=t.shape
# s=t.get_shape()
print("=========")
print(s)
print(type(s))
print(s[0])
print(type(s[0]))
print(s[-1])#3
print(len(s))#2
# 四、图像转化为张量
