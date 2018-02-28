import time

start = time.time()
for x in range(1,10000000):
    x*256
print(time.time() - start)

start2 = time.time()
for x in range(1,10000000):
    x << 8
print(time.time() - start2)
