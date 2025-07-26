#5. Membership Operators

names=['sumanth','tarak','sanjay','charan','vyshnavi']
print('in result:','rahul' in names) #in result: False
print('not in result:','suhas' not in names) #not in result: True

#6. Identity Operators
l=[1,2,3,4]
b=[1,2,3,4]

a=b #Assign b to a
print("l is b:",l is b)#l is b: False
print("a is b:",a is b)#a is b: True
print("id(l)",id(l))#id(l) 2257923058368
print("id(b)",id(b))#id(b) 2257878301824
print("id(a)",id(a))#id(a) 2257878301824
print("a is not b:", a is not b)#a is not b: False
print("l is not b:", l is not b)#l is not b: True    


#7. Bitwise Operators
'''3-011
5-101
------
3&5=001=1'''
print("3&5: ",3&5) #3&5:  1

'''4-100
5-101
------
4|5=101=5'''
print("4|5: ",4|5)#4|5:  5

'''5-101
6-110
------
5^6=011=3'''
print("5^6: ",5^6) #5^6:  3

'''1-001
---------
~1=110'''
print("~1: ",~1) #~1:  -2

'''2<<1
2=010
4=100'''
print("2<<1: ",2<<1) #2<<1:  4

'''4>>1
4=100
2=010'''
print("4>>1: ",4>>1) #4>>1:  2

'shmitha'.upper()

