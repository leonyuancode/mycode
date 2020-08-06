import  numpy as np
x=np.array([[2,1],[1,2]])
print(x)
xt=x.transpose()
print(xt)
xt[0,0]=1.0
print(xt)
x2=xt.dot(x)#矩阵的乘积
print(x2)
import numpy.linalg as lg
print(lg.inv(x2))#逆矩阵
