income_title=[]
income_amount=[]

expense_title=[]
expense_amount=[]

v=True
while(v):
    service=input("enter income or expense:")
    if(service=="income"):
        title=input("enter income name:")
        amount=float(input('enter amount:'))
        income_title.append(title)
        income_amount.append(amount)
        print("Added success")
        for x in range(len(income_title)):
            print(income_title[x]+" -> ",income_amount[x])
        
    elif(service=='expense'):
        title=input("enter expense name:")
        amount=float(input('enter amount:'))
        expense_title.append(title)
        expense_amount.append(amount)
        print("Added success")
        for x in range(len(expense_title)):
            print(expense_title[x]+" -> "+str(expense_amount[x]))
    else:
        print('sorry its wrong selection')
        v=False

        
