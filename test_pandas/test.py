import pandas as pd
import numpy as np

dct_1={"a":1,"b":2,"c":3}
dct_2={"a":11,"b":12,"c":13}
dct_3={"a":21,"b":22,"c":23}
lst=[dct_1,dct_2,dct_3]
df=pd.DataFrame(lst)
print(df)