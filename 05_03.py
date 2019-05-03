import multiprocessing
import time

start_time = time.time()


def count(name):
    sum = 0
    for i in range(1, 5000001):
        sum += i


num_list = ['a1','a2','a3','a4']

for num in num_list:

    count(num)


print("--- %s seconds ---"%(time.time() - start_time))