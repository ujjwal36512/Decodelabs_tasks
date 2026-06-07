# Expense Tracker
# This module provides functionality for tracking and managing expenses.

class ExpenseTracker:
    """A simple expense tracker to manage and analyze expenses."""
    
    def __init__(self):
        self.expenses = []
    
    def add_expense(self, category, amount, description=""):
        """Add a new expense to the tracker.
        
        Args:
            category (str): Category of the expense
            amount (float): Amount spent
            description (str): Optional description of the expense
        """
        expense = {
            "category": category,
            "amount": amount,
            "description": description
        }
        self.expenses.append(expense)
        print(f"Expense added: {category} - ${amount}")
    
    def get_total(self):
        """Calculate total expenses."""
        return sum(expense["amount"] for expense in self.expenses)
    
    def get_by_category(self, category):
        """Get total expenses for a specific category."""
        return sum(expense["amount"] for expense in self.expenses 
                   if expense["category"].lower() == category.lower())
    
    def display_expenses(self):
        """Display all recorded expenses."""
        if not self.expenses:
            print("No expenses recorded.")
            return
        
        print("\n--- Expense Report ---")
        for i, expense in enumerate(self.expenses, 1):
            print(f"{i}. {expense['category']}: ${expense['amount']} - {expense['description']}")
        print(f"Total: ${self.get_total()}")


if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.add_expense("Food", 15.50, "Lunch")
    tracker.add_expense("Transport", 5.00, "Bus fare")
    tracker.add_expense("Food", 8.75, "Coffee")
    tracker.display_expenses()
    print(f"Food expenses: ${tracker.get_by_category('Food')}")
