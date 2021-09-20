#用分治法求最大增加值
lis_dec = [1,2]
def find_cross_max(Array, low, mid, high):
    lt_sum = Array[mid]
    if mid ==0:
        lt_sum = 0
    rt_sum = Array[mid]
    for i in range(mid,low-1,-1):
        left_sum = sum(Array[i:mid])
        if lt_sum < left_sum:
            lt_sum = left_sum
    for i in range(mid,high+1):
        right_sum = sum(Array[mid:i+1])
        if rt_sum < right_sum:
            rt_sum = right_sum
    return lt_sum+rt_sum
def find_max(Array, low, high):
    if high == low:
        return Array[low]
    else:
        mid = (low + high)//2
        left_sum = find_max(Array,low,mid)
        right_sum = find_max(Array,mid+1,high)
        cross_sum = find_cross_max(Array,low,mid,high)
        if left_sum>=right_sum and left_sum>=cross_sum:
            return left_sum
        elif right_sum>=left_sum and right_sum>=cross_sum:
            return right_sum
        else:
            return cross_sum
print(find_max(lis_dec, 0, len(lis_dec)-1))