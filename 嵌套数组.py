
def nest(seq):
    Node = False
    deep = []
    for i in seq:
        if type(i)==list:
            Node = True
            deep.append(nest(i))
    if Node:
        return max(deep)+1       
    else:
        return 0
print(nest([[8,[2,[3,[4]]]],1,[2,4],[98]]))

deepl = []
def nest2(seq,deep):
    global deepl
    for i in seq:
        if type(i)==list:
            nest2(i,deep+1)
    deepl.append(deep)
nest2([1, [2], [[3], [[4], 5]]],0)
print(max(deepl))
































# def nesting_depth(a_list):
#     flag=False
#     num = []
#     for i in a_list:
#         if isinstance(i,list):
#           flag=True
#           num.append(nesting_depth(i))
#     if flag:
#         return max(num)+1
#     else:
#         return 0
# print(nesting_depth(l))