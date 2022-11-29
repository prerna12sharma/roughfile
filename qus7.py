a=[1,2,3,4,5]
b=[6,3,8,9,4]
union=[]
intrs=[]
for i in a:
        if i not in union:
                union.append(i)
        if i in b:
                intrs.append(i)
        for j in b:
                if j not in union:
                        union.append(j)
print(union)
print(intrs)