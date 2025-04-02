# def calculate_sum(lst):
#     total = 0
#     for num in lst:
#         total += num
#     return total

# numbers = [1, 2, 3, 4, 5]
# print("Sum:", calculate_sum(numbers))


# def string_length(x):
#     count=0
#     for i in x:
#         count+=1
#     return count

# x=str(input("enter the string: "))
# print(string_length(x))


# def find_min(lst):
#     minimum = lst[0]
#     for num in lst:
#         if num < minimum:
#             minimum = num
#     return minimum

# numbers = [5, 2, 9, 1, 7]
# print("Min:", find_min(numbers))


# def find_max(lst):
#     maximum = lst[0]
#     for num in lst:
#         if num > maximum:
#             maximum = num
#     return maximum

# numbers = [5, 2, 9, 1, 7]
# print("Max:", find_max(numbers))

# def calculate_power(base, exponent):
#     result = 1
#     for _ in range(exponent):
#         result *= base
#     return result

# base = 2
# exponent = 3
# print("Power:", calculate_power(base, exponent))  


# def string_length(k):
#     count=0
#     for i in k:
#         count+=1
#     print(count,"is the length of the string")

# string_length('python')

# def sum(h):
#     total=0
#     for i in h:
#         total+=i
#     print(total,"is the sum of numbers in the list")

# k=[10,20,30,40]
# sum(k)



# def min_number(h):
#     minimum=h[0]
#     for i in h:
#         if (i<minimum):
#             minimum=i
#     print(minimum,"is the smallest number in the list" )

# f=[-10,10,9, 8, 4, 0]
# min_number(f)

# def max_number(h):
#     maximum=h[0]
#     for i in h:
#         if (i>maximum):
#             maximum=i
#     print(maximum,"is the largest number in the list" )

# f=[-10,10,9, 8, 4, 0, 100]
# max_number(f)


# print(pow(10,2))

# def pow_function(base, exponent):
#     pro=1
#     for i in range(exponent):
#         pro*=base
#     print(f'{pro} is the power of the base number {base} to the exponent {exponent}')
# b=int(input("enter a number: "))
# e=int(input("enter a number: "))
# pow_function(b, e)



# transactions = []

# def deposit(amount):
#     """Deposit money into the account."""
#     if amount > 0:
#         transactions.append(f"Deposited ${amount}")
#         print(f"${amount} has been deposited into your account.")
#     else:
#         print("Invalid deposit amount. Please enter a positive amount.")

# def withdraw(amount):
#     """Withdraw money from the account."""
#     if amount > 0:
#         if amount <= get_balance():
#             transactions.append(f"Withdrew ${amount}")
#             print(f"${amount} has been withdrawn from your account.")
#         else:
#             print("Insufficient funds. Please check your balance.")
#     else:
#         print("Invalid withdrawal amount. Please enter a positive amount.")

# def get_balance():
#     """Get the current balance."""
#     balance = 0
#     for transaction in transactions:
#         if "Deposited" in transaction:
#             balance += int(transaction.split()[1][1:])
#         elif "Withdrew" in transaction:
#             balance -= int(transaction.split()[1][1:])
#     return balance

# def show_transactions():
#     """Display all account transactions."""
#     if transactions:
#         print("Account transactions:")
#         for transaction in transactions:
#             print(f"- {transaction}")
#     else:
#         print("No transactions yet.")

# # Main program loop
# while True:
#     user_input = input("\nChoose an option: \n1. Deposit Money \n2. Withdraw Money \n3. Check Balance \n4. Show Transactions \n5. Exit\n")

#     if user_input == '1':
#         amount = float(input("Enter the amount to deposit: $"))
#         deposit(amount)

#     elif user_input == '2':
#         amount = float(input("Enter the amount to withdraw: $"))
#         withdraw(amount)

#     elif user_input == '3':
#         print(f"Current balance: ${get_balance()}")

#     elif user_input == '4':
#         show_transactions()

#     elif user_input == '5':
#         print("Exiting the system. Have a nice day!")
#         break

#     else:
#         print("Invalid option. Please try again.")


# balance = 0

# def deposit(amount):
#     """Deposit money into the account."""
#     global balance
#     if amount > 0:
#         balance += amount
#         print(f"${amount} has been deposited into your account.")
#     else:
#         print("Invalid deposit amount. Please enter a positive amount.")

# def withdraw(amount):
#     """Withdraw money from the account."""
#     global balance
#     if amount > 0:
#         if amount <= balance:
#             balance -= amount
#             print(f"${amount} has been withdrawn from your account.")
#         else:
#             print("Insufficient funds. Please check your balance.")
#     else:
#         print("Invalid withdrawal amount. Please enter a positive amount.")

# def check_balance():
#     """Check the current balance."""
#     print(f"Current balance: ${balance}")

# # Main program loop
# while True:
#     user_input = input("\nChoose an option: \n1. Deposit Money \n2. Withdraw Money \n3. Check Balance \n4. Exit\n")

#     if user_input == '1':
#         amount = float(input("Enter the amount to deposit: $"))
#         deposit(amount)

#     elif user_input == '2':
#         amount = float(input("Enter the amount to withdraw: $"))
#         withdraw(amount)

#     elif user_input == '3':
#         check_balance()

#     elif user_input == '4':
#         print("Exiting the system. Have a nice day!")
#         break

#     else:
#         print("Invalid option. Please try again.")




import random
import re

# Bank System
bank_name = "Global Bank"
branch_name = "Main Branch"

# Bank Account
accounts = {}

def generate_account_number():
    """Generate a unique 5-digit account number."""
    return random.randint(10000, 99999)

def is_valid_phone_number(phone_number):
    """Check if the phone number is valid (10 digits)."""
    pattern = r"^\d{10}$"
    if re.match(pattern, phone_number):
        return True
    return False

def create_account():
    """Create a new bank account."""
    account_number = generate_account_number()
    
    # Check if the account number already exists (in case of randomness, though rare)
    while account_number in accounts:
        account_number = generate_account_number()

    name = input("Enter your full name: ")
    phone_number = input("Enter your phone number (10 digits): ")
    
    while not is_valid_phone_number(phone_number):
        print("Invalid phone number format. Please enter exactly 10 digits.")
        phone_number = input("Enter your phone number (10 digits): ")

    # Create a new account with initial balance and store information
    accounts[account_number] = {
        "name": name,
        "phone_number": phone_number,
        "balance": 0,
        "transactions": []
    }

    print(f"\nAccount created successfully! Your account number is: {account_number}")
    print(f"Bank: {bank_name}, Branch: {branch_name}")

def deposit(account_number, amount):
    """Deposit money into the account."""
    if amount > 0:
        accounts[account_number]["balance"] += amount
        transaction_id = random.randint(1000, 9999)
        accounts[account_number]["transactions"].append(f"Deposit: ${amount}, ID: {transaction_id}")
        print(f"${amount} has been deposited into your account.")
    else:
        print("Invalid deposit amount. Please enter a positive amount.")

def withdraw(account_number, amount):
    """Withdraw money from the account."""
    if amount > 0:
        if amount <= accounts[account_number]["balance"]:
            accounts[account_number]["balance"] -= amount
            transaction_id = random.randint(1000, 9999)
            accounts[account_number]["transactions"].append(f"Withdraw: ${amount}, ID: {transaction_id}")
            print(f"${amount} has been withdrawn from your account.")
        else:
            print("Insufficient funds. Please check your balance.")
    else:
        print("Invalid withdrawal amount. Please enter a positive amount.")

def check_balance(account_number):
    """Check the current balance."""
    balance = accounts[account_number]["balance"]
    print(f"Current balance: ${balance}")

def show_transactions(account_number):
    """Show all recent transactions."""
    if accounts[account_number]["transactions"]:
        print("\nRecent transactions:")
        for transaction in accounts[account_number]["transactions"][-5:]:  # Show only the last 5 transactions
            print(f"- {transaction}")
    else:
        print("No transactions yet.")

# Main program loop
while True:
    print("\nWelcome to Global Bank!")
    print("Bank: Global Bank, Branch: Main Branch")

    # Ask for account number (simulation of login)
    account_number = input("Please enter your account number (5-digit): ")

    # Check if the account exists
    if int(account_number) not in accounts:
        print("Account number not found. Please create an account first.")
        create_new_account = input("Do you want to create a new account? (yes/no): ").lower()
        if create_new_account == 'yes':
            create_account()
        continue

    # Once the account is verified or created, show options
    while True:
        print("\nChoose an option:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Show Recent Transactions")
        print("5. Logout")

        user_input = input("Enter the option number: ")

        if user_input == '1':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                deposit(int(account_number), amount)
            except ValueError:
                print("Invalid input! Please enter a valid number.")
            
        elif user_input == '2':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                withdraw(int(account_number), amount)
            except ValueError:
                print("Invalid input! Please enter a valid number.")
            
        elif user_input == '3':
            check_balance(int(account_number))

        elif user_input == '4':
            show_transactions(int(account_number))

        elif user_input == '5':
            print("Logging out... Have a nice day!")
            break

        else:
            print("Invalid option. Please try again.")
