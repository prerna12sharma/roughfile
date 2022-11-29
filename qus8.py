num1=[1,2,3,4,5]
num2=[6,7,8,9,10]
lis=num1+num2
sum=0
c=0
for i in lis:
        sum=sum+i
        c=c+1
        if c%2==0:
                median=(((c//2)+(c//2+1))//2)-1
        else:
                median=((i+1)//2)-1       
print(lis[median])