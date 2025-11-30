expenses = []   

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # ADD EXPENSE
    if choice == "1":
        item = input("Enter expense name: ")
        amount = float(input("Enter amount spent: "))
        category = input("Enter category (Food/Travel/Others): ")

        expense = {
            "item": item,
            "amount": amount,
            "category": category
        }

        expenses.append(expense)
        print("✓ Expense added successfully!")

    # VIEW ALL EXPENSES
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("\n--- All Expenses ---")
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}. {exp['item']} - ₹{exp['amount']} ({exp['category']})")

    # VIEW TOTAL SPENDING
    elif choice == "3":
        total = 0
        for exp in expenses:
            total += exp["amount"]
        print(f"\nTotal Spending: ₹{total}")

    # EXIT PROGRAM
    elif choice == "4":
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
