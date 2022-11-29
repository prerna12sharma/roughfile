# name1=input("enter 1:-")
# name2=input("enter 2:-")
# i=0
# while i<len(name1):
#     j=0
#     while j<len(name2):
#         j=j+1
#     i=i+1
# if i>j:
#     print(name1)
# elif i<j:
#     print(name2)
# else:
#     print(name1,name2)

# num=int(input("enter number:-"))
# x=0
# y=1
# z=0
# while z<=num:
#     print(z)
#     x=y
#     y=z
#     z=x+y
    

# num=int(input("enter:-"))
# rev=0
# while num>0:
#     i=num%10
#     rev=(rev*10)+i
#     num=num//10
# print(rev)

# num=int(input("ent"))
# i=1
# f=1
# while i<=num:
#     f=f*i
#     i=i+1
# print(f)

# arm=int(input())
# org=arm
# sum=0
# while arm>0:
#     sum=sum+(arm%10)*(arm%10)*(arm%10)
#     arm=arm//10
# if org==sum:
#     print("arm")
# else:
#     print("notarm")

# i=0
# while i<10:
#     i=i+1
#     if i==3:
#         pass
#     else:
#         print(i)

# num=int(input())
# i=0
# sum=0
# while num>0:
#     i=(i*10)+(num%10)
#     sum=sum+i
#     num=num//10
#     print(sum)


# li=[{"rani":1,"prerna":2}]
# i=0
# while i<len(li):
#     for j in li[0].values():
#         print(j)
#     i=i+1


# li=[1,2,2,3,4,5,6,4,4,8]
# i=0
# store=[]
# while i<len(li):
#     if li[i] not in store:
#         store.append(li[i])
#     i=i+1
# print(store)


# num=input("enter:-")
# i=0
# s=''
# while i<len(num):
#     c=int(num[i])**2
#     s=s+str(c)
#     i=i+1
# print(s)

# li=[1,2,3,4,5,7,8,7]
# i=0
# s=[]
# while i<len(li):
#     if li[i]==7:
#         pass
#     else:
#         s.append(li[i])
#     i=i+1
# print(s)



# li=[1,-2,3,-4,5,-7,-8,7]
# i=0
# pos=[]
# neg=[]
# while i<len(li):
#     if li[i]>0:
#         pos.append(li[i])
#     else:
#         neg.append(li[i])
#     i=i+1
# print("postive:",pos)
# print("negative:",neg)

# li=[["A","B"],["A","B","C"],["B","C"]]
# i=0
# while i<len(li):
#     j=0
#     c=0
#     while j<len(li[i]):
#         if "A" in li[i][j]:
#             c=c+1
#         j=j+1
#     i=i+1
# print(c)

# x=lambda a,b: a+b
# print(x(3,5)) 

# n=int(input("enter"))
# i=0
# s=[]
# while i<n:
#     num=int(input())
#     s.append(num)
#     i=i+1
# s.reverse()
# print(s)


# N=int(input())
# i=0
# sume=0
# sumod=0
# while i<=N:
#     if i%2==0:
#         sume=sume+i
#     else:
#         sumod=sumod+i
# print(sume)
# print(sumod)

# d=dict()
# for i in range(1,16):
#     d[i]=i**2
# print(d)
           

# dic={1:60,2:10,3:30,4:40,5:50}
# max=0
# min=dic[1]
# for i in dic:
#     if dic[i]>max:
#         max=dic[i]
#     elif dic[i]<min:
#         min=dic[i]
# print(max,min)

# d="w3resourse"
# dic={}
# for i in d:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# print(dic)


# d=[{"item":"item1","amt":400},{"item":"item2","amt":300},{"item":"item1","amt":900}]
# s={}
# for i in d:
#     if i["item"] in s:
#         s[i["item"]]+=i["amt"]
#     else:
#         s[i["item"]]=i["amt"]
# print((s))

# li=[1,2,3]
# lis=[1,2,3]
# i=0
# sum=0
# l=[]
# while i<len(li):
#     j=0
#     while j<len(lis):
#         if i==j:
#             sum=li[i]+lis[j]
#             l.append(sum)
#         j=j+1
#     i=i+1
# print(l)


# li=[[1,2,3],[1,2,3]]
# i=0
# sum=0
# lis=[]
# while i<len(li):
#     j=0
#     while j<len(li[i]):
#         sum=sum+li[i][j]
#         lis.append(sum)
#         j=j+1
#     i=i+1
# print(lis)

# li=[1,2,3]
# i=0
# while i<len(li):
#     print(i)
#     i=i+1

# i=100
# while i<115:
#     z=i-99
#     if i>=15:
#         print(z)
#     i=i+1
    
# i=0
# while i<=50:
#     if i>=15 and i<=20:
#         print(i)
#     else:
#         pass
#     i=i+1


# print(li[0])
# print(li[0]["rani"])

# li=[{"a":1,"b":2},{"c":3}]
# i=0
# while i<len(li):
#     j=0
#     print(i)
#     i=i+1

# a=[50,6,23,45,66,60]
# i=0
# max=0
# smax=0
# while i<len(a):
#     if a[i]>max:
#         smax=max
#         max=a[i]
#     if a[i]<smax and a[i]>smax:
#         smax=a[i]
#     i=i+1
# print(smax)

# li=[['g','f'],['i','s'],['b','e','s','t']]
# i=0
# s=""
# while i<len(li):
#     j=0
#     while j<len(li[i]):
#         s=s+(li[i][j])
#         j=j+1
#     i=i+1
# print(s)


# num=input("enter")
# i=0
# s=''
# while i<len(num):
#     x=int(num[i])**2
#     s=s+str(x)
#     i=i+1
# print(s)


# li=['a','j','u','p']
# i=-1
# s=[]
# while i>=(-len(li)):
#     s.append(li[i])
#     i=i-1
# print(s)

# li=['1','2','3','4']
# i=0
# s=[]
# sum=0
# while i<len(li):
#     sum=int(li[i])+1
#     s.append(str(sum))
#     i=i+1
# print(s)

# a=['p','u','j','a']
# s=[]
# i=0
# while i<len(a):
#     j=0
#     b=[]
#     while j<len(a):
#         if a[i]==a[j]:
#             b.append(a[i])
#         j=j+1
#     if b not in s:
#         s.append(b)
#     i=i+1
# print(j)


# d={"a":10,"b":20,"c":30}
# d1={"a":10,"b":20,"d":40}
# count={}
# for i in d.keys():
#     for j in d1.keys():
#         if i==j:
#             count[i]=d[i]+d1[j]
# else:
#     count[i]=d1[i]
#     count[j]=d1[j]
# print(count)

# a="shantanu"
# i=0
# while i<len(a):
#     if i==2:
#         print(a[i])
#     i=i+1

# T=int(input())
# i=0
# while i<=T:
#     X=int(input())
#     if X>=2000:
#         print("YES")
#     else:
#         print("NO")
#     i=i+1


# T=int(input())
# i=0
# while i<=(T):
#     N=int(input())
#     j=0
#     s=[]
#     while j<=N:
#         a=int(input())
#         s.append(a)
#         j=j+1
#     i=i+1
# print(s)
#     j=0
#     s=[]
#     while j<=(N):
#         N=int(input())
#         s.append(N)
#         j=j+1
#     i=i+1
# print(s)

# for i in range(T):
#     N=int(input())
#     S=[]
#     for j in range(N):
#         A=int(input())
#         S.append(A)
        # c=0
        # for k in S:
        #     if S[k]%N==0:
        #         c=c+1
# print(s))

# n=int(input("ent:"))
# sum=0
# i=0
# while i<=n:
#     sum=sum+i
#     i=i+1
# for i in range(n):
#     sum=sum+i
# print(sum)

# Array assingment*************

# a=[1,2,3,4,5]
# a.reverse()
# print(a)


# li=["a","n","r","e","r","p"]
# rev=li[ ::-1]
# print(rev)

# li=["a","n","r","e","r","p"]
# i=-1
# s=[]
# while i>=(-len(li)):
#     s.append(li[i])
#     i=i-1
# print(s)

# li=[1,2,3,4,5]
# i=-1
# s=[]
# while i>=(-len(li)):
#     s.append(li[i])
#     i=i-1
# print(s)



# qus 2_______

# li=[1,3,3,5,8,9,11]
# mean=0
# median=0
# mode=0
# count=len(li)
# i=0
# sum=0
# while i<len(li):
#         sum=sum+li[i]
#         mean=sum/count
#         median=((count+1)//2)-1
#         i=i+1
# print(mean)
# print(li[median])


# qus3:-_____________


# qus4:-___________

# a=[1,2,3,3,4,5,5,6,1]
# i=0
# s=[]
# for i in a:
#         if i not in s:
#                 s.append(i)
#         i=i+1
# print(s)


# qus5:-___________

# li=[1,3,4,5,2]
# li1=[6,7,9,8,12]
# lis=li+li1
# i=0
# a=0
# while i<len(lis):
#         j=0
#         while j<len(lis):
#                 if lis[i]<lis[j]:
#                         a=lis[j]
#                         lis[j]=lis[i]
#                         lis[i]=a
#                 j=j+1
#         i=i+1
# print(lis)

# qus6:-__________

# a=[2,3,4,6,1]
# s=[]
# sum=0
# num=int(input("enter"))
# for i in a:
#         if i not in s:
#                 sum=sum+i
#                 s.append(i)
#                 if sum==num:
#                         break
#         else:
#                 pass
#         i=i+1
# print(s)

# qus7:-_______

# a=[1,2,3,4,5]
# b=[6,3,8,9,4]
# union=[]
# intrs=[]
# for i in a:
#         if i not in union:
#                 union.append(i)
#         if i in b:
#                 intrs.append(i)
#         for j in b:
#                 if j not in union:
#                         union.append(j)
# print(union)
# print(intrs)

# qus8:-_______

# num1=[1,2,3,4,5]
# num2=[6,7,8,9,10]
# lis=num1+num2
# sum=0
# c=0
# for i in lis:
#         sum=sum+i
#         c=c+1
#         if c%2==0:
#                 median=(((c//2)+(c//2+1))//2)-1
#         else:
#                 median=((i+1)//2)-1       
# print(lis[median])

# T=int(input())
# for i in range(T):
#     a,b=map(int,input().split())
#     if a>b:
#         print("yes")
#     else:
#         print("no")



# A,B,C=map(int,input().split())
# if A>B and A>C:
#     if B>C:
#         print(B)
#     else:
#         print(C)
# elif B>A and B>C:
#     if A>C:
#         print(A)
#     else:
#         print(C)
# elif C>A and C>A:
#     if A>B:
#         print(A)
#     else:
#         print(B)
# else:
#     print("none")

# k=1
# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#     	print(' ',end="")
#         b=b+1
#         j=1
#     	while j<=k:
#     		print('*',end=" " )
#     		j=j+1
#     	k=k+1
#     	print()
#     	i=i+1


# k=1
# i=1
# while i<=5:
# 	b=1
# 	while b<=5-i:
# 		print(' ',end="")
# 		b=b+1
# 	j=1
# 	while j<=k:
# 		print('*',end=" " )
# 		j=j+1
# 	k=k+1
# 	print()
# 	i=i+1


# k=1
# i=1
# while i<=5:
# 	b=1
# 	while b<=5-i:
# 		print(' ',end="")
# 		b=b+1
# 	j=1
# 	while j<=k:
# 		print('*',end=" " )
# 		j=j+1
# 	k=k+1
# 	print()
# # 	i=i+1

# n=int(input())
# i=1
# while i<=n:
# 	b=1
# 	while b<=5-i:
# 		print(' ',end=" ")
# 		b=b+1
# 	j=1
# 	while j<=i:
# 		print("*",end=" ")
# 		j=j+1
# 	# print()
# 	i=i+1
# 
# n=int(input())
# i=1
# while i<=n:
# 	j=1
# 	while j<=5:
# 		print(i,end=" ")
# 		j=j+1
# 	print()
# 	i=i+1
# n=int(input())
# num=1
# i=1
# while i<=n:
# 	j=1
# 	while j<=5:
# 		print(num,end=" ")
# 		num=num+1
# 		j=j+1
# 	print()
# 	i=i+1


# li=["a",12,30.6,9,"c"]
# i=0
# c=[]
# for i in li:
# for i in li:
# 	if i%3==0:
# 		c.append(i)
# 	else:
# 		pass
# print(c)

# a=int(input("enter"))
# if a%2==0:

# cook your dish here
# T=int(input())
# for i in range(T):
#     N=int(input())
#     for j in range(2*(N)):
#         li=[]
#         A=int(input())
#         li.append(A) 
# print(li)



# li=[1,2,3,2,3,2,4,5]
# l=[]
# i=0
# while i<len(li):
#         if i not in l:
#                 l.append(li[i])
#         else:
#                 pass
#         i=i+1
# print(l)


# a=[1,2,3,3,4,5,5,6,1]
# i=0
# s=[]
# for i in a:
#         if i not in s:
#                 s.append(i)
#         i=i+1
# print(s)




                                
        