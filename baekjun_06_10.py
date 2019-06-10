a = 0
b = 0
w = [1]
total = 0
c = []

while(True):

    q = int(input())
    if(q == -1):
        break
    a = str(q) + " = " + str(w[0])
    b = str(q) + " is NOT perfect."

    for i in range(2, int(q/2) + 1):
        if(q % i == 0):
            w.append(i)
            a = a + " + "
            a = a + str(i)

    for i in range(len(w)):
        total += w[i]

    if(total == q):
        c.append(a)
    else:
        c.append(b)

    a = 0
    w = [1]
    total = 0

for i in range(len(c)):
    print(c[i])