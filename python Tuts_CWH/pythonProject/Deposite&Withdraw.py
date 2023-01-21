def deposite(amount):
    global balance
    balance = balance+amount
    print("deposite number",balance)

def withdraw(amount):
    global balance
    if(balance>amount):
        balance = balance-amount
        print("After withdraw balance is",balance)

        balance =0
        banklog =[]
        while True :
            data = input("Enter trans")
            if data == 'N':
                break
            banklog.append(data.split())
        print(banklog)

        for trans in banklog :
            if trans[0] =='D':
                deposite(int(trans[1]))
            elif trans[0] =='W':
                withdraw(int(trans[1]))
        print("Final Balance",balance)


