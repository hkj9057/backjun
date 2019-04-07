"""
#백준(모음 개수)
q = input()
e = ['a','e','i','o','u']
r = 0

for i in range(len(q)):

    for j in range(len(e)):

        if(q[i] == e[j]):
            r = r + 1

print(r)
"""

q = input()

w = ['C','A','M','B','R','I','D','G','E']
e = []
r = True

for i in range(len(q)):

    r = True

    for j in range(len(w)):

        if(q[i] == w[j]):
            r = False


    if(r == True):
        e.append(q[i])

e = ''.join(e)

print(e)
