#assert keyword
'''n=int(input("Enter the amount: "))
assert n>0,"n needs to be positive"
print(n)'''


'''data={"BuyNow":True,"Bank":True,"Login":True}
assert data["BuyNow"]
print("proceed order")'''


'''data={"BuyNow":False,"Bank":True,"Login":True}
assert data["BuyNow"]
print("proceed order")'''



#ATM
data={
    1234:{"pin":123,"current_balance":4000,"history":[]},
    5678:{"pin":123,"current_balance":5000,"history":[]},
    9012:{"pin":123,"current_balance":7000,"history":[]}
    }

print("Welcome to the ATM")
acc=int(input("Enter the account number: "))
pin=int(input("Enter the pin: "))

if acc in data and data[acc]["pin"]==pin:
    print("Login Successful")

    while True:
        print('''\n\nATM MENU)
        1.Check Balance
        2.Depoist
        3.Withdraw
        4.View Transactions
        5.Exit''')

        op=int(input("select the option: "))

        if op==1:
            print(f"current balance: $ {data[acc]['current_balance']}")

        elif op==2:
            amount=int(input("Enter amount to deposit: "))
            data[acc]["current_balance"]+=amount
            data[acc]["history"].append(f"Deposited ${amount}")
            print(f"Successfully deposited $ {amount}")

        elif op==3:
            amount=int(input("Enter amount to withdraw: "))
            if data[acc]["current_balance"]>=amount:
                data[acc]["current_balance"]-=amount
                data[acc]["history"].append(f"withdrawn ${amount}")
                print(f"Successfully withdrawn $ {amount}")
            else:
                print("Ins blnc")

        elif op==4:
            print("Transaction History: ")
            for i in data[acc]["history"]:
                print(f"- {i}")
        elif op==5:
            break
        else:
            print("Invalid option")

else:
    print("Invalid login.")
