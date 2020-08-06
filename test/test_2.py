
import pandas as pd
import numba
import  numpy as np
from time import *


df_trades=pd.read_csv("./bs.csv")
df_bs = df_trades.copy()
df_bs['dt'] = pd.to_datetime(df_bs['dt'])


# Make array type.  Type-expression is not supported in jit functions.
float_array =numba.types.float64[:]

# @numba.njit
# def foo():
#     # Make dictionary
#     d = Dict.empty(
#         key_type=types.unicode_type,
#         value_type=float_array,
#     )
#     # Fill the dictionary
#     d["posx"] = np.arange(3).astype(np.float64)
#     d["posy"] = np.arange(3, 6).astype(np.float64)
#     return d
#
# # d = foo()
# # # Print the dictionary
# # print(d)  # Out: {posx: [0. 1. 2.], posy: [3. 4. 5.]}
#
list_type = numba.types.ListType(numba.types.string)
@numba.njit
def generate_bs_dict(col_dt,col_kdcode,col_bs,col_name):
    d = numba.typed.Dict.empty(
        key_type=numba.types.string,
        value_type=list_type
    )
    n =len(col_dt)
    for i in range(n):
        lst=[]
        kdcode=col_kdcode[i]
        print(kdcode)
        d[col_kdcode[i]] =numba.typed.List.empty_list(numba.types.string)
        d[col_kdcode[i]].append(col_dt[i])
        d[col_kdcode[i]].append(col_bs[i])
        d[col_kdcode[i]].append(col_name[i])
        pass
    return d


dict_bs=generate_bs_dict(df_bs['dt'].to_numpy(dtype=str),
                            df_bs['kdcode'].to_numpy(dtype=str),
                             df_bs['b/s'].to_numpy(dtype=str),
                             df_bs['stock_name'].to_numpy(dtype=str))

print(dict_bs)

# list_type = numba.types.ListType(numba.types.float64)
#
# @numba.njit()
# def func():
#     d = numba.typed.Dict.empty(
#         key_type=numba.types.unicode_type,
#         value_type=list_type
#     )
#
#     d["a"] = numba.typed.List.empty_list(numba.types.float64)
#     d["a"].append(1)
#     d["a"].append(1)
#
#     return d
#
# print(func())