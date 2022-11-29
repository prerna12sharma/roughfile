li=[1,3,3,5,8,9,11]
mean=0
median=0
mode=0
count=len(li)
i=0
sum=0
while i<len(li):
        sum=sum+li[i]
        mean=sum/count
        median=((count+1)//2)-1
        i=i+1
print(mean)
print(li[median])