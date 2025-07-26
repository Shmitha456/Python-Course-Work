'''a=int(input("Entr a: "))
b=int(input("Entr b: "))

if a>b :
    print(f"{a} is greater than {b}")
elif a==b:
    print(f"{a} is equal to {b}")
else:
    print(f"{b} is greater than {a}")'''



'''a=int(input("Enter a: "))

if a%2==0 and a%3==0:
    print(f"2 & 3")
elif a%2==0:
    print(f"only 2")
elif a%3==0:
    print(f"only 3")

else:
    print(f"not div by 2 & 3")'''


'''name='shmitha'
for ch in name:
    print(f"ch = {ch}")'''



'''name=['shmitha','deepika','sushmitha','dharshitha']
for ch in name:
    print(f"ch = {ch}")'''


'''name={'shmitha','deepika','sushmitha','dharshitha'}
for ch in name:
    print(f"ch = {ch}")'''


'''name={1:'shmitha',2:'deepika',3:'sushmitha',4:'dharshitha'}
for i in name.keys():
    print(f"{i}-{name[i]}")'''


'''name={1:'shmitha',2:'deepika',3:'sushmitha',4:'dharshitha'}
for i in name.keys():
    print(f"{i}={name[i].title()}")'''



'''d={1:1,2:4,3:9,4:16}
for i in d.keys():
    print(f"{i}={d[i]}")'''



'''for i in range(2,21,2):
    print(f"{i}")'''



'''for i in range(20,1,-2):
    print(f"{i}")'''




'''for i in range(1,21):
    print(f"2 * {i} = {2*i}")'''



'''for i in range(1,21):
    print(f"17 * {i} = {17*i}")'''



for i in range(1,21):
    print(f"50 * {i} = {50*i}")


'''a=1
while a<=10:
    print(a)
    a+=1'''


'''email,pwd='123@gmail.com','xyz@123'

max_attempt=5
cur_attempt=1

while cur_attempt <= max_attempt:
    e=input("Enter the email: ")
    p=input("Enter the pwd: ")
    if (e==email) and (p==pwd):
        print("Login Successful")
        break
    else:
        print("Invalid email or pwd, Try Again")
    cur_attempt+=1
else:
    print("max attempts are done, try again")'''

