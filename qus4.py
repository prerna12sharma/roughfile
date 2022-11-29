a=[1,2,3,3,4,5,5,6,1]
i=0
s=[]
for i in a:
        if i not in s:
                s.append(i)
        i=i+1
print(s)