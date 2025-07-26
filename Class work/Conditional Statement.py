#Conditional Statement (1.1)
'''data={
'shmitha@gmail.com':'123@',
'koreboina@gamil.com':'789!',
'sree@gmail.com':'456',
}

email,pwd=input('Enter the email and pwd: ').split()
if data.get(email)==pwd:
    print ('login successful')
else:
    print ('invalid login')'''


#Conditional Statement(1.2)
'''items=['coffee','icecream','samosa','idly']
stocks=[20,50,40,0]
data=input("Enter the item:")

if data in items:
    ind=items.index(data)
    if stocks[ind]>0:
        print("Ava")
    else:
        print("out of stock.please try again")
else:
    print('item not ava')'''

#Conditional Statement
'''items=['coffee','icecream','samosa','idly']
stocks=[20,50,40,0]
distance=[13,4,9,12]
rating=[3.2,4,4.3,1]
cost=[150,60,20,40]
veg=[True,True,False,True]
time=[40,10,25,15]

data=input("Enter the item: ")
int=items.index(data)
if distance[ind]<5 and rating[ind]>4 and cost[ind]<500 and veg[ind] and time[ind]<30'''

#Conditional Statement
num=int(input('Enter the number: '))
