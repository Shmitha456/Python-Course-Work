#Letter'E'
'''n=int(input("Enter the Size: "))

for row in range(n):
    for col in range(n):
        if col==0 or row==0 or (row==0 and col<n//2) or row==n//2 or  (row==n-1 and col>n//2) or row==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''


#Letter'A'
'''for row in range(6):
    for col in range(5):
        if((col==0 or col==4)and (row!=0) or ((row==0 or row==3) and (col>0 and col<4))):
            print("*",end='')
        else:
            print(end=' ')
    print()'''


#Letter'B'
'''for row in range(7):
    for col in range(4):
        if(col==0 or (col==3 and (row!=0 and row!=6)) or ((row==0 or row==3 or row==6)and (col>0 and col<3))): 
            print('*',end='')
        else:
            print(' ',end='')
    print()'''



#Letter'C'
'''for row in range(6):
    for col in range(4):
        if((col==0 and (row!=0 and row!=5))) or ((row==0 or row==5)and (col!=0)): 
            print('*',end='')
        else:
            print(' ',end='')
    print()'''

#letter'S'
'''for row in range(7):
    for col in range(4):
        if ((row == 0 or row == 3 or row == 6) and 0 < col < 3) or (col == 0 and 0 < row < 3) or (col == 3 and 3 < row < 6):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''



#Letter'K'
'''for row in range(7):
    for col in range(4):
        if col==0 or row+col==3 or row-col==3:
            print("*",end='')
        else:
            print(' ',end='')
    print()'''



#Letter'H'
'''n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if col==0 or row==n//2 or col==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''


#Letter'M'
#
'''for row in range(7):
    for col in range(4):
        if col==0 or col==4-1 or row+col==3 or col-row==0:
             print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''                         


#Letter'I'
'''n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or col==n//2 or row//4:
             print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#Letter'T'
'''n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or col==n//2:
             print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


#Letter'R'
'''n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if col==0 or ((row==0 or (col!=0 and col!=n//2))) or row==n//2:
             print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
