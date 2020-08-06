# 一、随机数
# 1、均匀分布随机数
import tensorflow as tf
import  matplotlib.pyplot as plt
import numpy as np
import  math
tf.compat.v1.disable_eager_execution()#tensorlow 2.0版本不支持1.0版本，添加此语句保证可以正常运行

x=tf.random.uniform([10,4,20,5],minval=0,maxval=10,dtype=tf.float32)
session=tf.compat.v1.Session()
array=session.run(x)
print(array.shape)
array1d=array.reshape([-1])
plt.hist(array1d)
plt.show()
# 1、正太分布随机数
sigma=1
mu=10
result=tf.random.normal([10,4,20,5],mean=mu,stddev=sigma,dtype=tf.float32)
array=session.run(result)
array1d=array.reshape([-1])
histogram,bins,patch=plt.hist(array1d,25,color='gray')
x=np.arange(5,15,0.01)
y=1.0/(math.sqrt(2*np.pi)*sigma)*np.exp(-np.power(x-mu,2.0)/(2*math.pow(sigma,2)))
plt.plot(x,y)
plt.show()

