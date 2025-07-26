#div
'''def divl(a,b):
    return a/b

a=int(input())
b=int(input())

print(divl(a,b))

divl= lambda a,b:a/b
print(divl (a,b))'''



#Squares
'''def squares(l):
    for i in range(len(l)):
        l[i]=l[i]**2
    return l

l=[1,2,3,4,5]
print(squares(l))

squ=list(map(lambda i:i**2,l))
print(squ)'''



'''l=["shmitha","dharshitha","sushmitha","deepika"]
squ=list(map(lambda i:i.title(),l))
print(squ)'''


'''l='python'
vol='aeiou'
squ=list(map(lambda i:'*' if i in vol else i,l))
print(squ)'''


'''l=[1,2,3,4,5,6,7,8,9,10]
squ=list(filter(lambda i:i%2==0,l))
print(squ)'''


'''l=[1,0,0,0,3,4,0,0,5,6,0,0,9]
squ=list(filter(lambda i:i!=0,l))
print(squ)'''



#dict
'''data={'mouse':True,'laptop':False,'soap':True,'phone':False,'charger':True}
d=list(filter(lambda i:data[i],data))
print(d)'''


'''data={'shmitha':90,'dharshitha':80,'sushmitha':70,'deepika':88}
d=dict(sorted(data.items(),key=lambda i:i[1]))
print(d)'''


'''data={'shmitha':90,'dharshitha':80,'sushmitha':70,'deepika':88}
d=dict(sorted(data.items(),key=lambda i:i[1],reverse=True))
print(d)'''




#list comp
#1 method
'''l=[]
for i in range(1,11):
    l.append(i)
print(l)'''


#2 method
'''k=[i for i in range(1,11)]
print(k)'''





#1 method
'''l=[]
for i in range(1,11):
    if i%2==0:
        l.append(i)
print(l)'''


#2 method
'''k=[i for i in range(1,11) if i%2==0]
print(k)'''




#1 method
'''l=[]
for i in range(1,11):
    if i%2==0:
        l.append(i)
print(l)'''


#2 method
'''k={i:i**2 for i in range(1,11)}
print(k)


{1:1,2:4,3:9,4:16}'''


#1 method
'''l=[]
for i in range(1,11):
    if i%2==0:
        l.append(i)
print(l)'''


#2 method
'''k=tuple(i for i in range(1,11))
print(k)'''


#1 method
'''l=[]
for i in range(1,11):
    if i%2==0:
        l.append(i)
print(l)'''


#2 method
'''k=[i+j for i in range(5)for j in range(5) ]
print(k)'''




