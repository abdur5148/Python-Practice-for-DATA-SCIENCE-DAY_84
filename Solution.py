dic = {}
var1 = input("Enter : ")
for var1 in var1:
    dic[var1] = dic.get(var1, 0)+1
print('\n'.join(['%s,%s' % (i, j) for i, j in dic.items()]))
