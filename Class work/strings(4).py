#string
#4. String Testing Methods (Boolean Results) 
#startswith
l=['PFS20', 'PFS30', 'PFS22', 'JFS22', 'DS20']
for i in l:
    if i.startswith('PFS'):
        print(i)

#endswith
l=['demo.png','resume.pdf','index.webp','add.py','mul.py','sub.py']
for i in l:
    if i.endswith('png'):
        print(i)

l=['demo.png','resume.pdf','index.webp','add.py','mul.py','sub.py']
for i in l:
    if i.endswith('py'):
        print(i)
