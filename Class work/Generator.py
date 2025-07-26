'''def feed(l):
    return l

l=['1..100','101..200','201..300','302...400']
print(feed(l))'''


'''def feed(l):
    yield l

l=['1..100','101..200','201..300','302...400']
load=feed(l)
print(next(load))'''



'''def feed(l):
    for i in l:
        yield i

l=['1..100','101..200','201..300','302...400']
load=feed(l)
print(next(load))
print(next(load))
print(next(load))
print(next(load))'''




'''def feed(l):
    for i in l:
        yield i

def feed1(l):
    for i in l:
        return i

l=['1..100','101..200','201..300','302...400']
print(feed1(l))
print(feed1(l))
print(feed1(l))
print(feed1(l))

load=feed(l)
print(next(load))
print(next(load))
print(next(load))
print(next(load))'''



'''def feed(l):
    for i in l:
        yield i

l=['file1','file2','file3','file4']
load=feed(l)
print(next(load))
print(next(load))
print(next(load))
print(next(load))'''



def simple_generator():
    print("Start")
    yield 1
    yield 2
    yield 3
    print("End") 

gen = simple_generator() 
print(next(gen))  
print(next(gen))  
print(next(gen))  
print(next(gen))
print(next(gen))
