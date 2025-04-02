# # # Library Management:

# class Library:
#     def __init__(self):
#         # Initialize an empty list to store available books
#         self.books = []

#     def add_book(self, book_name):
#         """Add a book to the library."""
#         self.books.append(book_name)
#         print(f'Book "{book_name}" has been added to the library.')

#     def borrow_book(self, book_name):
#         """Borrow a book from the library."""
#         if book_name in self.books:
#             self.books.remove(book_name)
#             print(f'You have borrowed "{book_name}".')
#         else:
#             print(f'Sorry, "{book_name}" is not available in the library.')

#     def return_book(self, book_name):
#         """Return a book to the library."""
#         self.books.append(book_name)
#         print(f'You have returned "{book_name}".')

#     def show_available_books(self):
#         """Display the list of available books."""
#         if self.books:
#             print("Available books in the library:")
#             for book in self.books:
#                 print(f"- {book}")
#         else:
#             print("No books are currently available in the library.")

# # Create an instance of the Library class
# library = Library()

# # Start the menu-driven loop
# while True:
#     user_input = input("\nChoose an option: \n1. Add a Book \n2. Borrow a Book \n3. Return a Book \n4. Show Available Books \n5. Exit\n")

#     if user_input == '1':
#         book = input("Enter the name of the book to add: ")
#         library.add_book(book)

#     elif user_input == '2':
#         book = input("Enter the name of the book to borrow: ")
#         library.borrow_book(book)

#     elif user_input == '3':
#         book = input("Enter the name of the book to return: ")
#         library.return_book(book)

#     elif user_input == '4':
#         library.show_available_books()

#     elif user_input == '5':
#         print("Exiting the system. Have a nice day!")
#         break

#     else:
#         print("Invalid option. Please try again.")
# # # Bank Account


# class Bankaccount:
#     def __init__(self):
#         self.a = 0  
 

#     def amount_to_deposit(self, amount):
#         self.a += amount
#         print(f"Amount deposited: {amount}")

#     def withdraw(self, amount):
#         if amount > self.a:
#             print("Insufficient balance.")
#         else:
#             self.a -= amount
#             print(f"Amount withdrawn: {amount}")

#     def balance(self):
#         print(f"Balance amount: {self.a}")

# b1 = Bankaccount()

# while True:
#     x = input("What do you want to do?: \n1. Deposit \n2. Withdraw \n3. Balance enquiry \n4. Exit\n")

#     if x == '1':  
#         amount = int(input("Enter amount to deposit: "))
#         b1.amount_to_deposit(amount)

#     elif x == '2':  
#         amount = int(input("Enter amount to withdraw: "))
#         b1.withdraw(amount)

#     elif x == '3':  
#         b1.balance()

#     elif x == '4': 
#         print("Exit process and return card.")
#         break

#     else:
#         print("Invalid option, please try again.")


# BAnking Management System


# import random

# class BankAccount:
#     def __init__(self, account_holder, initial_balance=0):
#         self.account_number = random.randint(10000, 99999) 
#         self._balance = initial_balance  
#         self.account_holder = account_holder

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited {amount}. New balance is {self._balance}.")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         raise NotImplementedError("Withdraw method must be implemented in derived classes.")

#     def check_balance(self):
#         print(f"Current balance: {self._balance}")
#         return self._balance

# class SavingsAccount(BankAccount):
#     def __init__(self, account_holder, initial_balance=0, interest_rate=0.02):
#         super().__init__(account_holder, initial_balance)
#         self.interest_rate = interest_rate

#     def withdraw(self, amount):
#         if amount <= self._balance:
#             self._balance -= amount
#             print(f"Withdrew {amount}. New balance is {self._balance}.")
#         else:
#             print("Insufficient balance.")

#     def calculate_interest(self):
#         interest = self._balance * self.interest_rate
#         self._balance += interest
#         print(f"Interest of {interest} added. New balance is {self._balance}.")
#         return interest

# class CheckingAccount(BankAccount):
#     def __init__(self, account_holder, initial_balance=0, overdraft_limit=500):
#         super().__init__(account_holder, initial_balance)
#         self.overdraft_limit = overdraft_limit  

#     def withdraw(self, amount):
#         if self._balance - amount >= -self.overdraft_limit:
#             self._balance -= amount
#             print(f"Withdrew {amount}. New balance is {self._balance}.")
#         else:
#             print("Overdraft limit exceeded. Transaction denied.")

#     def apply_fees(self):
#         if self._balance < 0:
#             fee = 35  
#             self._balance -= fee
#             print(f"Overdraft fee of {fee} applied. New balance is {self._balance}.")
# class Bank:
#     def __init__(self):
#         self.accounts = []

#     def open_account(self, account_type, account_holder):
#         if account_type == "savings":
#             account = SavingsAccount(account_holder)
#         elif account_type == "checking":
#             account = CheckingAccount(account_holder)
#         else:
#             print("Invalid account type.")
#             return None

#         self.accounts.append(account)
#         print(f"{account_type.capitalize()} Account for {account_holder} opened with account number: {account.account_number}")
#         return account

#     def get_account_by_number(self, account_number):
#         for account in self.accounts:
#             if account.account_number == account_number:
#                 return account
#         return None


# bank = Bank()

# while True:
#     action = input("\nChoose an action: \n1. Open Account \n2. Deposit \n3. Withdraw \n4. Check Balance \n5. Calculate Interest (Savings Only) \n6. Apply Fees (Checking Only) \n7. Exit\n")

#     if action == '1':  
#         name = input("Enter account holder's name: ")
#         account_type = input("Enter account type (savings/checking): ").lower()
#         account = bank.open_account(account_type, name)

#     elif action == '2': 
#         account_number = int(input("Enter account number: "))
#         account = bank.get_account_by_number(account_number)
#         if account:
#             amount = float(input("Enter amount to deposit: "))
#             account.deposit(amount)
#         else:
#             print("Account not found.")

#     elif action == '3':  
#         account_number = int(input("Enter account number: "))
#         account = bank.get_account_by_number(account_number)
#         if account:
#             amount = float(input("Enter amount to withdraw: "))
#             account.withdraw(amount)
#         else:
#             print("Account not found.")

#     elif action == '4': 
#         account_number = int(input("Enter account number: "))
#         account = bank.get_account_by_number(account_number)
#         if account:
#             account.check_balance()
#         else:
#             print("Account not found.")

#     elif action == '5':  
#         account_number = int(input("Enter savings account number: "))
#         account = bank.get_account_by_number(account_number)
#         if isinstance(account, SavingsAccount):
#             account.calculate_interest()
#         else:
#             print("This is not a savings account.")

#     elif action == '6':  
#         account_number = int(input("Enter checking account number: "))
#         account = bank.get_account_by_number(account_number)
#         if isinstance(account, CheckingAccount):
#             account.apply_fees()
#         else:
#             print("This is not a checking account.")

#     elif action == '7':  
#         print("Exiting the system.")
#         break

#     else:
#         print("Invalid option. Please try again.")



# class Library:
    
#     def __init__(self):
#         self.books=[]

#     def addbook():
#         pass
#     def borrowbook():
#         pass
#     def showbooks():
#         pass

# obj=Library()

# while True:
#     input