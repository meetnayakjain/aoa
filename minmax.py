def min_max(arr,low,high):
    # if 1 element in arr
    if high == low:
        return arr[low],arr[low]
    
    else:
        mid = (low+high)//2
        min1,max1=min_max(arr,low,mid)
        min2,max2=min_max(arr,mid+1,high)

    return min(min1,min2),max(max1,max2)

arr = [1000, 11, 445, 1, 330, 300]
n = len(arr)
min_element, max_element = min_max(arr, 0, n - 1)
print("Minimum element:", min_element)
print("Maximum element:", max_element)