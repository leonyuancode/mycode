import tensorflow as tf

#张量的定义
# 所谓张量，可以理解为n维的数组或者矩阵，
# constant(value,dtype=None,shape=None,name="Const",verfy_shape=False)
# 常量->向量—>矩阵—>高维数组
# 1、零维张量，标量或者常量
t_1=tf.constant(3,tf.float32,shape=())
print(t_1)
#2、一维张量（向量）
t_2=tf.constant([-1,-2,1,2],tf.float32,shape=(4,),name='t')
print(t_2)
# 3、二维张量（矩阵）
t_3=tf.constant([
       [-1,1,8,5],
       [2,3,1,9],
       [7,2,6,4]
                ],tf.float32,shape=(3,4))
print(t_3)
# 4、三维张量
t_4=tf.constant(
    [
       [[-1,-11],[1,11],[8,18],[5,15]] ,
        [[2,12] ,[3,13],[1,11],[9,19]],
        [[7,17] ,[2,12],[6,16],[4,14]],
    ],
    dtype=tf.float32,shape=(3, 4, 2)#3行，4列，深度为2
)
print(t_4)
#5、四维向量
t_5=tf.constant(
   [  [
       [[-1,-11],[1,11],[8,18],[5,15]] ,
        [[2,12] ,[3,13],[1,11],[9,19]],
        [[7,17] ,[2,12],[6,16],[4,14]],
      ],
      [
       [[-1,-11],[1,11],[8,18],[5,15]] ,
        [[2,12] ,[3,13],[1,11],[9,19]],
        [[7,17] ,[2,12],[6,16],[4,14]],
      ]
   ],
    dtype=tf.float32,shape=(3, 4, 2,2),name="ttt"
)