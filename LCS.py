def lcs(X,Y):
    m=len(X)
    n=len(Y)

    L = [[None]*(n+1) for i in range(m+1)]

    for i in range (m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j]=0
            elif X[i-1]==Y[j-1]:
                L[i][j]=1+L[i-1][j-1]
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1])

    return L[m][n]

if __name__ == '__main__': 
    S1 = "AGGTABGXTXAYB"
    S2 = "GXTXAYB"
    print("Length of LCS is", lcs(S1, S2))