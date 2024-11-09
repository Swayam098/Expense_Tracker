class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.expense = []  # Corrected: Use singular 'expense'
    
    def add_expense(self, expense):
        self.expense.append(expense)  # Corrected: Use 'expense' instead of 'expenses'
    
    def remove_expense(self, index):
        if 0 <= index < len(self.expense):  # Corrected: Use 'expense' instead of 'expenses'
            del self.expense[index]
            print("Expense removed successfully.")
        else:
            print("Invalid Expense Index.")
    
    def view_expenses(self):
        if len(self.expense) == 0:  # Corrected: Use 'expense' instead of 'expenses'
            print("No expense found")
        else:
            print("Expense List:")
            for i, expense in enumerate(self.expense, start=1):  # Corrected: Use 'expense'
                print(f"{i}. Date: {expense.date}, Description: {expense.description}, Amount: {expense.amount}")
    
    def total_expenses(self):
        total = sum(exp.amount for exp in self.expense)  # Corrected: Use 'expense'
        print(f"Total Expense: ${total:.2f}")

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. Total Expenses")
        print("5. Exit")
        
        choice = input("Enter Your Choice (1-5): ")
        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            description = input("Enter the description: ")
            amount = float(input("Enter the Amount: "))
            expense = Expense(date, description, amount)  # Corrected: Use 'Expense' class
            tracker.add_expense(expense)
            print("Expense added successfully.")
        elif choice == "2":
            index = int(input("Enter the expense index to remove: ")) - 1
            tracker.remove_expense(index)
        elif choice == "3":
            tracker.view_expenses()
        elif choice == "4":
            tracker.total_expenses()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
