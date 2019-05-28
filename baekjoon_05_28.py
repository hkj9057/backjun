a = int(input())

arr = [[0 for i in range(2)] for j in range(a+1)]

arr[1][0] = 0
arr[1][1] = 1

for i in range(2,a+1):
    arr[i][0] = arr[i-1][0] + arr[i-1][1]
    arr[i][1] = arr[i-1][0]

print(arr[a][0] + arr[a][1])