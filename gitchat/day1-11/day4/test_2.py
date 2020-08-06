
def max_len(*lists):
    return max(*lists,key=lambda v : len(v))

def head(lst):
    return lst[0] if len(lst)>0 else None
def tail(lst):
    return lst[-1] if len(lst)>0 else None
def mul_print():
    for i in range(1,10):
        for j in range(1,i+1):
            print(str(j)+"*"+str(i)+"="+str(j*i),end="  ")
        print()

def pair(t):
    return list(zip(t[:-1],t[1:]))

from random import randint,sample,shuffle
def sample_t():
    lst=[randint(0,50) for _ in range(100)]
    print(lst[:5])
    lst_sample=sample(lst,10)
    print(lst_sample)
    shuffle(lst_sample)
    print(lst_sample)

if __name__=='__main__':
    print(max_len([1,2,3],[4,5,6,7],[8]))
    # mul_print()
    print("-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
    print(pair([1,2,3,4]))
    print(pair(range(10)))
    sample_t()