# Expense Tracker Project

expenses = []  #list of all expenses of the user

print("Welcome to Expense Tracker || Supervising your Wallet")

while True:
    print("\n=== Menu ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Totals Amonunt Sepnt")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice : "))

    # 1. Add Expense
    if choice == 1:
        date = str(input("Enter The Date (DD-MM-YYYY): "))
        category = str(input("Enter the Category: "))
        description = str(input("Enter short Description: "))
        amount = float(input("Enter the Amount: "))

        expense = {
            "Date": date,
            "Category": category,
            "Description": description,
            "Amount": amount
        }

        expenses.append(expense)   #list.append()
        print("✅ Expense Added Successfully!")

    # 2. View All Expenses
    elif choice == 2:
        if len(expenses)==0:
            print("⚠ No expenses added yet. Your wallet seems heavy 😄")
        else:
            print("\n____ Your Expenses ____")
            count = 1
            for e in expenses:
                print(f"Expense Number {count} -> {e['Date']} , {e['Category']} , {e['Description']} , ₹{e['Amount']}")
                count += 1

    # 3. View Total Expense
    elif choice == 3:
        total = 0
        for e in expenses:
            total += e["Amount"]
        print(f"💰 Total Amount You Spent: ₹{total}")

    # 4. Exit
    elif choice == 4:
        print("🙏 Thank you for using Expense Tracker")
        print("📊 Keep tracking your spendings. Goodbye!")
        break

    else:
        print("❌ Invalid input! Please enter a number between 1 and 4.")

