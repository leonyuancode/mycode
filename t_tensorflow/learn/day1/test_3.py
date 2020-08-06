import tensorflow as tf
import matplotlib.pyplot as plt
tf.compat.v1.disable_eager_execution()#tensorlow 2.0版本不支持1.0版本，添加此语句保证可以正常运行

image=tf.io.read_file("./test.png",'r')#读取数据
image_tensor=tf.image.decode_png(image)#解码为张量
session=tf.compat.v1.Session()#创建会话

print(image_tensor)
shape=tf.shape(image_tensor)
print("-----",session.run(shape))
image_ndarray=image_tensor.eval(session=session)#利用Tensor的成员函数eval转化为ndarry
plt.imshow(image_ndarray)
plt.show()
print(image_tensor.get_shape())#(None, None, None)