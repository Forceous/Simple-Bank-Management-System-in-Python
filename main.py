class Account:
    def __init__(self, username, password):
        # Initialize account attributes
        self.username = username
        self.password = password
        self.balance = 0  # Set initial balance to 0

# Function to handle the login process
def login(username, password):
    attempts = 3  # Allow 3 login attempts
    while attempts > 0:
        entered_username = input("Username: ")
        entered_password = input("Password: ")

        if entered_username == username and entered_password == password:
            print("Login successful!")
            return True  # Return True if login successful
        else:
            print("Invalid username or password. Please try again.")
            attempts -= 1
    print("Too many failed attempts. Exiting.")
    return False  # Return False if login unsuccessful after 3 attempts

# Function to create a new account
def create_account():
    new_username = input("Please enter a username: ")
    new_password = input("Please enter a password: ")
    return Account(new_username, new_password)  # Return a new Account object

# Function to display the menu options
def menu():
    print("Welcome to your bank account. What services would you like to proceed with?")
    print("1- Check account balance")
    print("2- Deposit")
    print("3- Withdraw")
    print("4- Exit")

# Function to handle depositing funds into the account
def deposit(account):
    while True:
        amount_str = input("Enter the amount of money you would like to deposit: ")
        if amount_str.isdigit():
            amount = int(amount_str)
            if amount > 0:
                account.balance += amount  # Add the deposited amount to the account balance
                print(f"You have deposited ${amount}.")
                return
            else:
                print("You can only deposit an amount larger than $0.")
        else:
            print("Please enter a valid number.")

# Function to display the current account balance
def balance(account):
    print(f"Your account balance is: ${account.balance}")

# Function to withdraw funds from the account
def withdraw(account):
    while True:
        withdraw_str = input("Enter the amount of money you would like to withdraw: ")
        if withdraw_str.isdigit():
            withdraw = int(withdraw_str)
            if withdraw > 0 and withdraw <= account.balance:
                account.balance -= withdraw  # Deduct the withdrawn amount from the account balance
                print(f"You have withdrawn ${withdraw}.")
                return
            elif withdraw > account.balance:
                print("Insufficient funds.")
            else:
                print("You can only withdraw an amount larger than $0.")
        else:
            print("Please enter a valid number.")

# Main function to control the flow of the program
def main():
    existing_account = Account("existing_username", "existing_password")  # Create an existing account object
    while True:
        option_num = input("Would you like to login or create an account? (Enter 1 for login or 2 for creating an account): ")
        if option_num.isdigit():
            option = int(option_num)
            if option == 1:
                if login(existing_account.username, existing_account.password):
                    while True:
                        menu()
                        choice_num = input("Enter your choice: ")
                        if choice_num.isdigit():
                            choice = int(choice_num)
                            if choice == 1:
                                balance(existing_account)
                            elif choice == 2:
                                deposit(existing_account)
                            elif choice == 3:
                                withdraw(existing_account)
                            elif choice == 4:
                                print("Goodbye!")
                                return
                            else:
                                print("Invalid choice. Please enter a valid option.")
                        else:
                            print("Invalid choice. Please enter a valid number.")
                else:
                    print("Login failed. Exiting.")
                    return
            elif option == 2:
                new_account = create_account()  # Create a new account
                print("Account created successfully!")
                existing_account = new_account  # Set the existing account to the newly created account
            else:
                print("Invalid choice. Please enter 1 for login or 2 for creating an account.")
        else:
            print("Invalid choice. Please enter a valid number.")

if __name__ == "__main__":
    print("Welcome to your bank management system!")
    main()
