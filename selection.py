def selection(a):
    n=len(a)
    for i in range(n - 1):
        mini = i
        for j in range(i + 1,n):
            if A[mini] > A[j]:
                mini = j
                A[i], A[mini] = A[mini], A[i]
A = [64, 25, 12, 22, 11]
selection(A)
print("Sorted array",A)
