import  tensorflow as tf
tf.compat.v1.disable_eager_execution()
sess=tf.compat.v1.Session()
#访问张量中某一区域的值，通过slice函数访问张量中任一区域的值
# 1、一维张量
t_1=tf.constant([1,2,3,4,5],tf.float32)
d1=tf.slice(t_1,[1],[3])#def slice(input_, begin, size, name=None):
print(sess.run(d1))
#2、二维张量
t_2=tf.constant([
    [1,2,3,4],
    [5,6,7,8]
],tf.float32)
d2=tf.slice(t_2,[0,1],[2,2])
print(sess.run(d2))
#3、三维张量
"""
2 3 8         5 3  2
6 1 5         1 2  4  
7 2 -1        9 -3 3
"""
t_3=tf.constant([
    [[2,5],[3,3],[8,2]],
    [[6,1],[1,2],[5,4]],
    [[7,9],[2,-3],[-1,3]]
],tf.float32)
d3=tf.slice(t_3,[1,0,1],[2,2,1]) #[1,0,1] 1行，0列，1深 [2,2,1] 长2，宽2，深1
print(sess.run(d3))