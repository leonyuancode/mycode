import time

d = {i:2 for i in range(1,100000000)}

t3 = time.time()
for k, v in d.items():
    pass
print("t3: " + str(time.time()-t3))
t4 = time.time()
for v in d.values():
    pass
print("t4: " + str(time.time()-t4))