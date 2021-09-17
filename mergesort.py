def merge(seq,p,r):
    q = (p+r)//2
    n1 = q-p
    n2 = r-q
    L = [0]*n1
    R = [0]*n2
    for i in range(n1):
        L[i] = seq[p:q][i]
    for i in range(n2):
        R[i] = seq[q:r][i]
    i = 0
    j = 0
    for x in range(p,r):
        if i==n1:
            seq[x] = R[j]
            j+=1
        elif j==n2:
            seq[x] = L[i]
            i+=1
        elif L[i]<=R[j]:
            seq[x] = L[i]
            i+=1
        else:
            seq[x] = R[j]
            j+=1


def Mergesort(seq,q,r):
    if r-q>=2:
        Mergesort(seq,q,(r+q)//2)
        Mergesort(seq,(r+q)//2,r)
        merge(seq,q,r)

