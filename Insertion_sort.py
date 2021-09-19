ins = [5, 4, 6, 1, 8, 3, 12, 15]
for i in range(0,ins.__len__()-1):
    j = i + 1
    while ins[i]>ins[j]:
        ins[i],ins[j] = ins[j],ins[i]
        if i>=1:
            j -= 1
            i -= 1
print(ins)