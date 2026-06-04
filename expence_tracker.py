#!/usr/bin/env python3
"""
Advanced Expense Tracker with Kill Switch and Graceful Shutdown
=====================================================================
Features:
- Multiple transaction handling (5+ transactions)
- Graceful shutdown with kill switch function
- Sentinel value for program termination
- State management (total initialized outside loop)
- Comprehensive error handling (ValueError, etc.)
- Final total display on exit
"""

import sys
from typing import List, Optional


# Constants
SENTINEL_VALUE = "exit"  # Kill switch sentinel value
INITIAL_TOTAL = 0.0  # State initialized outside loop
MIN_TRANSACTIONS = 5  # Stability: supports 5+ transactions
PROGRAM_VERSION = "1.0"


class ExpenseTracker:
    """
    A robust expense tracker with kill switch functionality,
    graceful shutdown, and comprehensive error handling.
    """
    
    def __init__(self):
        """Initialize the expense tracker with state management."""
        self.expenses: List[float] = []
        self.total: float = INITIAL_TOTAL  # State initialized outside loop
        self.transaction_count: int = 0
        self.is_running: bool = True
        
    def graceful_shutdown(self, reason: str = "User requested shutdown") -> None:
        """
        Graceful shutdown function with kill switch.
        Prints final total and cleanup information.
        
        Args:
            reason (str): Reason for shutdown
        """
        self.is_running = False
        
        print("\n" + "=" * 60)
        print("        GRACEFUL SHUTDOWN INITIATED")
        print("=" * 60)
        print(f"Reason: {reason}")
        print(f"Status: Processing {self.transaction_count} transactions...")
        print()
        
        # Display all expenses before shutdown
        if self.expenses:
            self._display_summary(is_shutdown=True)
        else:
            print("⚠ No transactions were recorded.")
        
        print("=" * 60)
        print("Thank you for using Expense Tracker v{}".format(PROGRAM_VERSION))
        print("Program terminated gracefully.")
        print("=" * 60)
    
    def _display_summary(self, is_shutdown: bool = False) -> None:
        """
        Display expense summary with transactions.
        
        Args:
            is_shutdown (bool): Whether this is being called during shutdown
        """
        print("\n" + "=" * 60)
        print("        EXPENSE SUMMARY")
        print("=" * 60)
        
        for i, expense in enumerate(self.expenses, 1):
            print(f"{i}. ${expense:>10.2f}")
        
        print("-" * 60)
        print(f"Total Transactions: {len(self.expenses)}")
        print(f"Total Spent: ${self.total:>53.2f}")
        print("=" * 60)
        
        if is_shutdown:
            print("✓ Final total preserved during shutdown")
    
    def validate_input(self, user_input: str) -> Optional[float]:
        """
        Validate user input and return amount or None.
        Defense: Catches ValueError and other input errors.
        
        Args:
            user_input (str): User input string
            
        Returns:
            Optional[float]: Valid amount or None if invalid
        """
        user_input = user_input.strip()
        
        # Check for kill switch (sentinel value)
        if user_input.lower() == SENTINEL_VALUE:
            return None  # Signal to shutdown
        
        try:
            # Defense: Convert to float
            amount = float(user_input)
            
            # Validate amount is positive
            if amount < 0:
                print("❌ Error: Amount cannot be negative. Please try again.\n")
                return None
            
            if amount == 0:
                print("⚠ Warning: Zero amount not recorded. Please enter a valid amount.\n")
                return None
            
            return amount
            
        except ValueError as ve:
            print(f"❌ ValueError: '{user_input}' is not a valid number.")
            print("   Please enter a numeric value (e.g., 100, 50.25)\n")
            return None
        except Exception as e:
            print(f"❌ Unexpected Error: {type(e).__name__}: {str(e)}\n")
            return None
    
    def add_expense(self, amount: float) -> bool:
        """
        Add expense to tracker and update total.
        
        Args:
            amount (float): Expense amount
            
        Returns:
            bool: True if added successfully
        """
        try:
            self.expenses.append(amount)
            self.total += amount  # Update state (total)
            self.transaction_count += 1
            
            print(f"✓ Added: ${amount:.2f} (Transaction #{self.transaction_count})")
            print(f"  Running Total: ${self.total:.2f}\n")
            
            return True
            
        except Exception as e:
            print(f"❌ Error adding expense: {type(e).__name__}: {str(e)}\n")
            return False
    
    def display_help(self) -> None:
        """Display help and available commands."""
        print("\n" + "=" * 60)
        print("        HELP & COMMANDS")
        print("=" * 60)
        print(f"• Enter expense amount (e.g., 100, 50.25)")
        print(f"• Type '{SENTINEL_VALUE.upper()}' to shutdown (kill switch)")
        print(f"• Type 'summary' to view current summary")
        print(f"• Type 'help' to display this help")
        print("=" * 60 + "\n")
    
    def run(self) -> None:
        """Main execution loop with state management and stability."""
        self._print_banner()
        
        print(f"Expense Tracker v{PROGRAM_VERSION}")
        print(f"State Initialization: Total = ${self.total:.2f}\n")
        print(f"Kill Switch Enabled (Type '{SENTINEL_VALUE.upper()}' to shutdown)\n")
        
        self.display_help()
        
        # Main loop - Handles 5+ transactions with state management
        while self.is_running:
            try:
                # Get user input
                user_input = input("Enter expense amount (or '{}' to exit): ".format(
                    SENTINEL_VALUE.upper()
                )).strip()
                
                # Handle special commands
                if user_input.lower() == "help":
                    self.display_help()
                    continue
                
                if user_input.lower() == "summary":
                    if self.expenses:
                        self._display_summary()
                    else:
                        print("⚠ No transactions recorded yet.\n")
                    continue
                
                # Check for kill switch (sentinel value)
                if user_input.lower() == SENTINEL_VALUE:
                    self.graceful_shutdown(
                        "Kill switch activated (sentinel value received)"
                    )
                    break
                
                # Validate and process input
                amount = self.validate_input(user_input)
                
                if amount is not None:
                    self.add_expense(amount)
                    
                    # Stability: Confirm 5+ transactions capacity
                    if self.transaction_count == MIN_TRANSACTIONS:
                        print(f"✓ Milestone: {MIN_TRANSACTIONS}+ transactions handled successfully!\n")
                
            except KeyboardInterrupt:
                # Handle Ctrl+C gracefully
                print()
                self.graceful_shutdown("Keyboard interrupt (Ctrl+C) detected")
                break
            except EOFError:
                # Handle EOF gracefully
                print()
                self.graceful_shutdown("End of file reached")
                break
            except Exception as e:
                print(f"❌ Unexpected error in main loop: {type(e).__name__}: {str(e)}\n")
                continue
    
    @staticmethod
    def _print_banner() -> None:
        """Print program banner."""
        print("\n" + "=" * 60)
        print("   ADVANCED EXPENSE TRACKER WITH KILL SWITCH")
        print("=" * 60)


def main() -> None:
    """Entry point for the application."""
    try:
        tracker = ExpenseTracker()
        tracker.run()
        
    except Exception as e:
        print(f"\n❌ Critical Error: {type(e).__name__}: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
