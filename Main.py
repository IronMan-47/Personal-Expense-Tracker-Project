import Modules2 as m
if __name__ == '__main__':
    Expense = m.load_from_csv()
    i = 101
    for k in Expense:
        if k != 'ID':
            try:
                if int(k) >= i:
                    i = int(k) + 1
            except:
                pass
print('Hi There! This is a Personal Expense Tracker')
print("Enjoy all it Features")
print('Created by Adit Prasad')
Q=0
while Q>=0:
    if not(Q==0):
        print('----------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print('What Next Would You like to do:')
    print('1.Add New Expense')
    print('2.View all Expenses')
    print('3.Search Expense')
    print('4.Edit Expense')
    print('5.Delete Expense')
    print('6.Show Total Spent')
    print('7.Show Category total')
    print('8. Clear Csv file')
    print('9.Save & Exit')
    choice = int(input('Enter the Choice: '))
    if choice == 1:
        d = m.Add_Expense(Expense)
        while True:
            if i in Expense:
                i += 1
            else:
                Expense[i] = d[0]
                m.save_to_csv(Expense)
                d.pop(0)
            if d==[]:
                break
    elif choice == 2:
        m.View_Expenses(Expense)
    elif choice == 3:
        m.search_Expense(Expense)
    elif choice == 4:
        m.Edit_Expense(Expense)
        m.save_to_csv(Expense)
    elif choice == 5:
        m.Delete_Expense(Expense)
        m.save_to_csv(Expense)
    elif choice == 6:
        m.total_spent(Expense)
    elif choice == 7:
        m.Category_Total_Spent(Expense)
    elif choice == 8:
        m.clear_file()
    elif choice == 9:
        m.save_to_csv(Expense)
        print('Saved to expenses.csv')
        print("Thank you For using the Program")
        break
    else:
        print('Invaild Choice')
    Q+=1

