def search(arr,x):
    low = 0
    high = len(arr)-1
    mid = 0

    while low<=high:
        mid = (high + low)//2

        if arr[mid]<x:
            low = mid+1

        elif arr[mid]>x:
            high = mid-1

        else:
            return mid
        
    return -1


arr = [ 2, 3, 4, 10, 40 ]
x = 10

result = search(arr,x)

if result == -1:
    print('Number not found')

else:
    print(f'Number at index {arr.index(x)}')