import  numpy as np
import  pandas as pd
s=pd.Series([1,3,5,np.nan,6,8])
print(s)
dates=pd.date_range("20130101",periods=6)
print(dates)
print(type(dates))
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print(df)

df2=pd.DataFrame({'A':1.,
                  'B':pd.Timestamp('20130102'),
                  'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                  'D':np.array([3]*4,dtype='int32'),
                  'E':pd.Categorical(["test", "train", "test", "train"]),
                  'F': 'foo'})
print(df2)
print(df2.dtypes)
print("===============================")
print(df)
print(df.head())
print(df.head(2))
print(df.tail(3))
print(df.index)
print(df.to_numpy())
print(df2.to_numpy())
print("-------------------------------")

print(df)
print(df.describe())
print(df.T)#转置

print("******************************")
print(df)
print(df.sort_index(axis=1,ascending=False))#axis : {0 or 'index', 1 or 'columns'}axis=0,表示对左列index排序，axis=1表示对行index排序
print(help(pd.DataFrame.sort_index))
print(df.sort_values(by='A'))
print(df.sort_values(by=['A','B']))
print(help(pd.DataFrame.sort_values))