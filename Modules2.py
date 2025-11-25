import csv
CSV_FILE = 'expenses.csv'

def Add_Expense(n):
    print("So, Want to enter Expenses")
    print("How many??")
    a = int(input("Enter here: "))
    d = []
    for i in range(a):
        P = input("Enter Product Name: ")
        PC = input("Enter the Product Category(Food,Study,Utility,Travel,Others): ")
        PC = PC.upper()
        PP = int(input("Enter the Product Price: "))
        DP = input("Enter the Date of Purchase: ")
        L = [P, PC, PP, DP]
        d.append(L)
        print("Done", i+1)
        print("-----------------------------------------------------------------")
    return d


def View_Expenses(n):
    for i in n:
        print(i, n[i])


def search_Expense(n):
    searchby = int(input("Enter the Product ID: "))
    flag = False
    for i in n:
        if i == searchby:
            print(i, n[i])
            flag = True
    if not flag:
        print("Record Not found")


def Edit_Expense(n):
    searchby = int(input("Enter the Product ID to Edit: "))
    flag = False
    for i in n:
        if i == 'ID':
            continue
        if i == searchby:
            print("What do you want to change")
            print("1. Product Name")
            print("2. Product Category")
            print("3. Product Price")
            print("4. Product Date")
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                a = input("Enter New Product Name: ")
                n[searchby][0] = a
                flag = True
                break
            elif choice == 2:
                a = input("Enter New Product Category: ")
                n[searchby][1] = a
                flag = True
                break
            elif choice == 3:
                a = int(input("Enter New Product Price: "))
                n[searchby][2] = a
                flag = True
                break
            elif choice == 4:
                a = input("Enter New Product Date: ")
                n[searchby][3] = a
                flag = True
                break
            else:
                print("Invaild Input")
                flag = True
                break
    if not flag:
        print("Record Not found")


def Delete_Expense(n):
    DelItem = int(input("Enter the Product ID to delete: "))
    if DelItem in n:
        print(DelItem," ",n[DelItem])
        n.pop(DelItem)
    else:
        print("Record Not found")


def total_spent(n):
    total_spent = 0
    for i in n:
        if i == 'ID':
            continue
        total_spent += n[i][2]
    print("Total Spent:", total_spent)


def Category_Total_Spent(n):
    totals = {}
    for i in n:
        if i == 'ID':
            continue
        cat = n[i][1]
        price = n[i][2]
        if cat in totals:
            totals[cat] += price
        else:
            totals[cat] = price

    print('Category   Total Spent')
    for cat in totals:
        print(cat, '  ', totals[cat])



def load_from_csv():
    Expense = {'ID': ['Product Name', 'Product Category', 'Product Price', 'Date of Purchase']}

    try:
        f = open(CSV_FILE, 'r', newline='', encoding='utf-8')
    except:
        return Expense

    reader = csv.reader(f)
    rows = list(reader)
    f.close()

    if len(rows) == 0:
        return Expense

    start_index = 1
    if len(rows[0]) < 5 or rows[0][0].upper() != 'ID':
        start_index = 0

    for row in rows[start_index:]:
        if len(row) < 5:
            continue
        try:
            ID = int(row[0])
            price = int(row[3])
        except:
            continue
        name = row[1]
        cat = row[2]
        date = row[4]
        Expense[ID] = [name, cat, price, date]

    return Expense


def save_to_csv(n):
    f = open(CSV_FILE, 'w', newline='', encoding='utf-8')
    writer = csv.writer(f)
    writer.writerow(['ID', 'Product Name', 'Product Category', 'Product Price', 'Date of Purchase'])
    Keys=[]
    for k in n.keys():
        if k != 'ID':
            Keys.append(k)
    for key in Keys:
        if key == 'ID':
            continue
        row = [key, n[key][0], n[key][1], n[key][2], n[key][3]]
        writer.writerow(row)
    f.close()

def clear_file():
    f = open(CSV_FILE, 'w', newline='', encoding='utf-8')
    writer = csv.writer(f)
    writer.writerow(['ID', 'Product Name', 'Product Category', 'Product Price', 'Date of Purchase'])
    f.close()
    print("File is clear now ")


