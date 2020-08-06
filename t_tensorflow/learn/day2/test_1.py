import  tensorflow as tf
tf.compat.v1.disable_eager_execution()
# 1、改变张量的数据类型（通过cast()函数实现）
t=tf.constant([
         [0,2,0],
         [0,0,1]
],tf.float32)
session=tf.compat.v1.Session()
r=tf.cast(t,tf.bool)
print(session.run(r))
t_2=tf.constant([
    [False ,True, False],
    [False ,False , True]
],tf.bool)
r_2=tf.cast(r,tf.float32)
print(session.run(r_2))
