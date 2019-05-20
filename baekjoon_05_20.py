"""
#
q = int(input())
w = []
for i in range(q):
    e = input()
    w.append(e)

w = list(set(w))

for i in range(len(w)):
    for j in range(len(w) - 1):

        if (w[j] > w[j + 1]):
            w[j], w[j + 1] = w[j + 1], w[j]

        if(len(w[j]) > len(w[j+1])):
            w[j], w[j+1] = w[j+1], w[j]

for i in range(len(w)):
    print(w[i])
"""

q = int(input())

total = 0
score = 0
a = []
for i in range(1,int(q/2 + 1)):
    score = 0
    for j in range(i,int(q/2 + 2)):
        score += j
        if(score == q):
            a.append(i)
            total += 1
            break
        elif(score > q):
            break

total += 1
print(total)