import numpy as np
import random


def count_in_bin(values, lower, upper):
    '''
    @param value is a seq contains datas
    @return a seq that count by bins interval
    '''
    seq = [0,0,0]
    for i in values:
        if i <= lower:
            seq[0] += 1
        elif i > lower and i <= upper:
            seq[1] += 1
        else:
            seq[2] += 1
    return seq

count_in_bin([2.09, 0.5, 3.48, 1.44, 5.2, 2.86, 2.62, 6.31], 2, 4)

np.histogram([2.09, 0.5, 3.48, 1.44, 5.2, 2.86, 2.62, 6.31],2)


def histogram(values, dividers):
    '''
    

    Parameters
    ----------
    values : value is a seq contains datas
    dividers : a seq contains bins dividers

    Returns
    -------
    a seq that count by bins interval

    '''
    copy_value = []
    for i in values:
        copy_value.append(i)
    copy_dividers = []
    for i in dividers:
        copy_dividers.append(i)
    first = 0
    last = len(dividers)-1
    s = []
    for i in range(len(dividers)+1):
        s.append(0)
    while last-first>=0:
        values = list(copy_value)
        if last == first:
            for i in values:
                if i <= dividers[first]:
                    s[first]+=1
                    copy_value.remove(i)
                elif i > dividers[last]:
                    s[first+1]+=1
                    copy_value.remove(i)
            last-=1
            first+=1
        elif last - first == 1:
            for i in values:
                if i <= dividers[first]:
                    s[first]+=1
                    copy_value.remove(i)
                elif i > dividers[last]:
                    s[last+1]+=1
                    copy_value.remove(i)
                else:
                    s[last]+=1
                    copy_value.remove(i)
            last-=1
            first+=1
        else:
            for i in values:
                if i <= dividers[first]:
                    s[first]+=1
                    copy_value.remove(i)
                elif i > dividers[last]:
                    s[last+1]+=1
                    copy_value.remove(i)
            last-=1
            first+=1
    return s

values = [random.randint(0, 100) for i in range(50)]
interval = max(values) - min(values)
dividers = [min(values) + i * (interval / 10) for i in range(1, 10)]
print(values)
print(dividers)
print(histogram(values, dividers))
print(histogram([1,2,3,4,5,6,7,8,9,10],[2,5,7]))




