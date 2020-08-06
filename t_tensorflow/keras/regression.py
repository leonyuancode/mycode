import  numpy as np
import  pandas as pd
z = np.array([1, 2, 3, 4,5, 6, 7, 8,9, 10, 11, 12,13, 14, 15,16])
z=z[:10]
print(z.reshape(-1,5))

list_1=[1,2,3]
ser=pd.Series(list_1)
print(ser)