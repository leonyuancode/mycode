#张量的转置，tensorflow的transpose 方法
import  tensorflow as tf
tf.compat.v1.disable_eager_execution()
# 1、二维张量的转置
x=tf.constant([
    [1,2,3],
    [4,5,6]],tf.float32)

sess=tf.compat.v1.Session()
r=tf.transpose(x,perm=[1,0])
# r=tf.transpose(x,perm=[0,1])#perm=[0,1]时，表示不作任何转置操作
print(sess.run(r))
# 2、三维张量的转置（三维坐标默认坐标轴，0-行，1-列，2-深度）
x_2=tf.constant([
        [[2,5],[3,4],[8,2]],
        [[6,1],[1,2],[5,4]]
                ],tf.float32)

r_2=tf.transpose(x_2,perm=[1,0,2])#perm=[0,1,2]时，表示不作任何转置操作
r_3=tf.transpose(x_2,perm=[0,2,1])#perm=[0,1,2]时，表示不作任何转置操作
r_4=tf.transpose(x_2,perm=[2,1,0])#perm=[0,1,2]时，表示不作任何转置操作
print(sess.run(r_2))
print(sess.run(r_3))
print(sess.run(r_4))

print("--------------------------------------------------------------")
# 3、改变形状，通过reshape改变张量的形状，改变张量的维数，和不改变张量的维数
# 1、不改变张量的维数
t3d=tf.constant([
                [[1,2],[4,5],[6,7]],
                [[8,9],[10,11],[12,13]]
               ],tf.float32)
t1=tf.reshape(t3d,[4,1,-1])
print(sess.run(t1))
print(type(t1))
print(t1.shape)

print("==================================")
t4d=tf.constant([
                [
                [[2,5],[3,3],[8,2]],
                [[6,1],[1,2],[5,4]]
                ],
                [
                [[1,2],[3,6],[1,2]],
                [[3,1],[1,2],[2,1]]
                ]
                 ],tf.float32)

t2=tf.reshape(t4d,[2,-1])
print(sess.run(t2))