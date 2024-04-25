def search(pat,txt):
    m=len(pat)
    n=len(txt)

    for i in range (n-m+1):
        j=0
        while j<m and txt[i+j]==pat[j]:
            j+=1

        if j == m:
            print(f'Pattern at index {i}')

if __name__=="__main__":
    text = "AABAACAADAABAABA"
    pattern = "AABA"
    search(pattern, text)
