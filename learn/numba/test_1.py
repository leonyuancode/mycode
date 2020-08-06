import numpy as np
import  pandas as pd
import numba
from numba import jit
from numba import jit
print(numba.__version__)

x = {'a': [1, 2, 3], 'b': [20, 30, 40]}

@jit(nopython=True)
def use_pandas(a): # Function will not benefit from Numba jit
    df = pd.DataFrame.from_dict(a) # Numba doesn't know about pd.DataFrame
    df += 1                        # Numba doesn't understand what this is
    return df.cov()                # or this!

print(use_pandas(x))