
# 规约运算：求和、平均值，最大、最小值
import  tensorflow as tf
tf.compat.v1.disable_eager_execution()
session=tf.compat.v1.Session()
# 规约函数大多具备一个参数axis，表示沿着张量的那个维度进行运算
# 1、求和
# （1）一维
t1d=tf.constant([3,4,1,5],tf.float32)
sum1=tf.reduce_sum(t1d,axis=0)
print(session.run(sum1))
# （2）二维 axis=0 沿着行（列和），axis=1 沿着列 （行和）（0,1）表示张哥张量
t2d=tf.constant([[3,4,1,5],[3,9,5,7]],tf.float32)
sum2_1=tf.reduce_sum(t2d,axis=0)
sum2_2=tf.reduce_sum(t2d,axis=1)
sum2_3=tf.reduce_sum(t2d,axis=(0,1))
print(session.run(sum2_1))
print(session.run(sum2_2))
print(session.run(sum2_3))
# （3）三维axis=0 沿着行（列和），axis=1 沿着列 （行和），axis=2表示沿着深度方向（0,1,2）表示张哥张量
t3d=tf.constant(
    [
        [[2,5],[3,3],[8,2]],
        [[6,1],[1,2],[5,4]],
        [[7,9],[2,-3],[-1,3]]
    ],tf.float32
)
sum3_1=tf.reduce_sum(t3d,axis=0)
print(session.run(sum3_1))

max_num=tf.argmax(t3d,axis=0)
min_num=tf.argmax(t3d,axis=1)
print(session.run(max_num))
print(session.run(min_num))
