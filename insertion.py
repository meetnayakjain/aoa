def insertion(arr1):
    n=len(arr1)    # Traverse through 1 to len(arr)
    for i in range(1,n):
        key = arr1[i]
        j = i-1
        while j >= 0 and key < arr1[j] :
                arr1[j + 1] = arr1[j]
                j -= 1
        arr1[j + 1] = key

array = []
     n = int(input("Enter number of elements : "))
     for i in range(0, n):
         ele = int(input('Enter element'))
         array.append(ele)
    N = len(array)
arr1 = [12, 11, 13, 5, 6]
insertion(arr1)
print(arr1)
