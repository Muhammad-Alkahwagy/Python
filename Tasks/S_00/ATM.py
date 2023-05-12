# Define a dictionary of usernames and passwords and balances
users = {
    "Ahmed": {"password": "123", "balance": 1000},
    "Sarah": {"password": "456", "balance": 500},
    "Walid": {"password": "789", "balance": 2000}
}

# Define a function to check account balance
def check_balance(username):
    print(f"Account balance: ${users[username]['balance']}")

# Define a function to withdraw money
def withdraw(username):
    # Loop to prompt the user to enter a valid amount to withdraw
    while True:
        # Ask the user to enter the amount to withdraw
        amount = int(input("Enter amount to withdraw: "))
        # Check if the amount is valid
        if amount % 5 != 0:
            print("Amount must be a multiple of 5.")
        elif amount > users[username]["balance"]:
            print("Insufficient funds in account.")
        else:
            # Update the user's account balance and print the dispensed amount
            users[username]["balance"] -= amount
            print(f"Withdrew ${amount}. Account balance: ${users[username]['balance']}")
            break

# Define a function to deposit money
def deposit(username):
    # Loop to prompt the user to enter a valid amount to deposit
    while True:
        # Ask the user to enter the amount to deposit
        amount = int(input("Enter amount to deposit: "))
        # Update the user's account balance and print the deposited amount
        users[username]["balance"] += amount
        print(f"Deposited ${amount}. Account balance: ${users[username]['balance']}")
        break

# Define a function to handle the ATM user interface
def atm():
    # Loop to prompt the user to enter a valid username and password
    while True:
        # Ask the user to enter a username and password
        username = input("Enter username: ")
        password = input("Enter password: ")
        # Check if the username and password are valid
        if username in users and users[username]["password"] == password:
            print(f"Welcome, {username}!")
            break
        else:
            print("Invalid username or password.")

    # Loop to allow the user to withdraw, deposit, or check balance
    while True:
        # Ask the user to select an option
        option = input("Enter 'w' to withdraw, 'd' to deposit, 'c' to check balance, or 'q' to quit: ")
        if option.lower() == 'w':
            # Withdraw money
            withdraw(username)
        elif option.lower() == 'd':
            # Deposit money
            deposit(username)
        elif option.lower() == 'c':
            # Check account balance
            check_balance(username)
        elif option.lower() == 'q':
            # Quit the program
            break
        else:
            print("Invalid option.")

# Call the ATM function to start the program
atm()