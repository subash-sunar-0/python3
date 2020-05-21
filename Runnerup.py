n =int(input())
arr = map(int, input().strip())

z =max(arr)

i=0 
while i<n:
    if z == max(arr):
        arr.remove(max(arr))
    i+=1

    print(max(arr))
