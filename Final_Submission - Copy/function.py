def iterations(a):
    if len(a) == 1:
        return [a]

    comination_list = []
    character = a[0]
    rest_list = iterations(a[1:])

    for i in rest_list:
        for m in range(len(rest_list)+1):
            comination_list.append(i[:m]+character+i[m:])
        
    return comination_list





























def iterations_2(a):
    if len(a)==1:
        return [a]

    char_ = a[0] #c
    rest_ = iterations_2(a[1:]) #['ab','ba']
    combination_list = []

    #a
    #b

    #bc

    #abc
    #bac
    #bca
    for i in rest_:
        for m in range(len(rest_)+1):#0,1,2
            combination_list.append(i[:m]+char_ + i[m:])
            #                       i[:0] + a + i[0:]

    return combination_list

def fib(a):
    if a<=1:
        return a
    
    return fib(a-1)+fib(a-2)

# print(iterations_2("abc"))
list_ = ['b','c']
print(list_[:0])
print(list_[0:])
print("----------")

print(list_[:1])
print(list_[1:])
print("----------")
print(iterations_2("abc"))