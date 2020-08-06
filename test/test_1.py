import numpy as np
import pandas as pd
from time import *
from numba import jit,njit
df = pd.DataFrame({'a': np.random.randn(100000),
                   'b': np.random.randn(100000),
                   'N': np.random.randint(100, 1000, (100000)),
                  'x': 'x'})
@njit
def f(x):
    return x * (x - 1)
@njit
def integrate_f(a, b, N):
    s = 0
    dx = (b - a) / N
    for i in range(N):
           s += f(a + i * dx)
    return s * dx
begin=time()
data=df.apply(lambda x: integrate_f(x['a'], x['b'], x['N']), axis=1)
print('1--',time()-begin)
begin=time()
lst=[]
for i,x in df.iterrows():
    lst.append(integrate_f(x['a'], x['b'], x['N']))
ser=pd.Series(lst)
print('2--',time()-begin)

begin=time()
lst=[]
for x in df.itertuples():
    lst.append(integrate_f(x[1], x[2], x[3]))
ser=pd.Series(lst)
print('3--',time()-begin)

begin=time()
lst=[]
d1=df['a'].to_numpy()
d2=df['b'].to_numpy()
d3=df['N'].to_numpy()
for i in range(len(d1)):
    lst.append(integrate_f(d1[i], d2[i], d3[i]))
ser=pd.Series(lst)
print('4--',time()-begin)

begin=time()
lst=[]
for x in df[['a', 'b', 'N']].values:
    lst.append(integrate_f(x[0], x[1], x[2]))
ser=pd.Series(lst)
print('5--',time()-begin)


"""
1-- 16.958218812942505 #apply
2-- 25.00351619720459  #iterrows
3-- 14.098752498626709 #itertuples
4-- 70.71325945854187  #to_numpy
5-- 14.989575862884521 #values
"""
"""
1-- 6.486000299453735
2-- 17.30899977684021
3-- 0.2890000343322754
4-- 0.36500024795532227
5-- 0.20199990272521973
"""