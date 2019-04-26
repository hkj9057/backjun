q = int(input())

pos = -1

e = []
stack = []

for i in range(q):

    w = input()
    e.append(w)

def push(stack, pos, num):

    stack.append(num)
    pos += 1

    return stack,pos

def pop(stack, pos):

    if(pos == -1):
        return stack, pos, -1000

    num = stack[pos]
    del stack[pos]
    pos -= 1
    return stack, pos, num

for i in range(q):

    w = e[i]

    if(w[0] == 'p' and w[1] == 'u'):
        num = w.split(' ')[1]
        stack, pos = push(stack, pos, num)



    if (w[0] == 'p' and w[1] == 'o'):

        if (pos == -1):
            print(-1)

        else:
            stack, pos, num = pop(stack, pos)
            print(num)


    if(w[0] == 's'):
        print(len(stack))

    if(w[0] == 'e'):
        if(len(stack) == 0):
            print(1)
        else:
            print(0)

    if(w[0] == 't'):

        if(len(stack) == 0):
            print(-1)

        else:
            print(stack[pos])


