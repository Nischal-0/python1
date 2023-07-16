# ATM System

# Database of user accounts (username: [pin, balance])
accounts = {
    'Nischal': ['1234', 5000],
    'Simran': ['5678', 2000],
    'Bhupesh': ['9876', 10000]
}

# Function to validate the user's PIN
def validate_pin(username, pin):
    if username in accounts:
        if accounts[username][0] == pin:
            return True
    return False

# Function to perform withdrawal
def withdraw(username, amount):
    if username in accounts:
        if amount <= accounts[username][1]:
            accounts[username][1] -= amount
            print(f"Withdrawal successful! New balance: NPR.{accounts[username][1]}")
        else:
            print("Insufficient balance.")
    else:
        print("Invalid username.")

# Function to perform deposit
def deposit(username, amount):
    if username in accounts:
        accounts[username][1] += amount
        print(f"Deposit successful! New balance: NPR. {accounts[username][1]}")
    else:
        print("Invalid username.")

#ATM program
isExit=False
while not isExit:
    print("===== Welcome to the Mero Sathi ATM =====")
    username = input("Enter your username: ")
    pin = input("Enter your PIN: ")

    if validate_pin(username, pin):
        while True:
            print("\n===== ATM Menu =====")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Exit")

            choice = input("\nEnter your choice (1-4): ")

            if choice == '1':
                print(f"\nYour current balance is: NPR. {accounts[username][1]}")

            elif choice == '2':
                amount = float(input("\nEnter the amount to withdraw: NPR. "))
                withdraw(username, amount)

            elif choice == '3':
                amount = float(input("\nEnter the amount to deposit: NPR. "))
                deposit(username, amount)

            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                isExit = True
                break  # Exit from the inner loop

            else:
                print("Invalid choice. Please try again.")

    else:
        print("Invalid username or PIN. Please try again.")
