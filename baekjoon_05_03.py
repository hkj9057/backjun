import random
import time
import multiprocessing

start_time = time.time()


def bubble(w,flag):
    for i in range(len(w)):
        for j in range(len(w) - 1):
            if(flag ==1):
                if (w[j] < w[j + 1]):
                    w[j], w[j + 1] = w[j + 1], w[j]
            else:
                if (w[j] > w[j + 1]):
                    w[j], w[j + 1] = w[j + 1], w[j]
    return w

def matching(w,e,r):
    for i in range(len(w)):
        for j in range(len(w)):
            if(w[i] == e[j]):
                r.append(j+1)
    return r

def first_input(w,e):
    for i in range(8):
        q = random.randrange(20,100)
        #q = int(input())
        w.append(q)
        e.append(q)
    return w,e

def cal_total(w, t, r):
    sum = 0
    for i in range(5):
        sum += w[i]
        t.append(r[i])
    return t, sum

def count(num):
    for k in range(25):
        w = []
        e = []
        r = []
        t = []
        sum = 0
        w,e = first_input(w,e)
        w = bubble(w,1)
        r = matching(w,e,r)
        t,sum = cal_total(w,t,r)
        t = bubble(t,0)


num_list = ['a1','a2','a3','a4']

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=6)
    pool.map(count, num_list)
    pool.close()
    pool.join()



print("--- %s seconds ---"%(time.time() - start_time))
#print(sum)
#print("%d %d %d %d %d"%(t[0],t[1],t[2],t[3],t[4]))
