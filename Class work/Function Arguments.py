#Function Arguments
#1.Positional Arguments
'''def greet(name,age):
    print(f"Hello {name}, you are {age} year old.")
greet("Alice", 25)'''

'''def greet(age,name):
    print(f"Hello {name}, you are {age} year old.")
greet("Alice", 25)'''

#2.Keyword Arguments
'''def greet(name, age):
     print(f"Hello {name}, you are {age} years old.")
greet(age=25, name="Alice")'''

'''def greet(age, name):
     print(f"Hello {name}, you are {age} years old.")
greet(age=25, name="Alice")'''

#3.Default Arguments
'''def greet(name, age=18):
    print(f"Hello {name}, you are {age} years old.") 
greet("Bob")'''


#4.Variable-Length Arguments
#*args (Arbitrary Positional Arguments)
'''def add(*numbers):
    return sum(numbers) 
print(add(1, 2, 3, 4, 5))'''

#kwargs(Arbitrary Keyword Arguments)
'''def user_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}") 
user_info(name="Alice", age=25, city="New York")'''
