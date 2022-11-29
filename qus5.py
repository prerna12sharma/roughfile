li=[1,3,4,5,2]
li1=[6,7,9,8,12]
lis=li+li1
i=0
a=0
while i<len(lis):
        j=0
        while j<len(lis):
                if lis[i]<lis[j]:
                        a=lis[j]
                        lis[j]=lis[i]
                        lis[i]=a
                j=j+1
        i=i+1
print(lis)
