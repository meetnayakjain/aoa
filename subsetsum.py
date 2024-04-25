flag = False

def subsetSum(i,n,set,sum,subset):
    global flag

    if sum == 0:
        flag = True
        print("The subset is : ",subset,end="\t")
        print()
        return
    
    if i == n:
        return "Sum not Found"
    
    if set[i] <= sum:
        subset.append(set[i])

        subsetSum(i+1,n,set,sum-set[i],subset)

        subset.pop()

    subsetSum(i+1,n,set,sum,subset)


if __name__=="__main__":
	set = [3, 34, 4, 12, 5, 2]
	sum = 7
	n = len(set)
	subset = []
	subsetSum(0, n, set, sum, subset)
    
if not flag:
    print("There is no such subset")
