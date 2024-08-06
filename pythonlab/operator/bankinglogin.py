def main():
    print("Welcome to the Bank System")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if authenticate(username, password):
        print("Login successful!")
        while True:
            print("\nChoose an option:")
            print("1. Change password")
            print("2. Check balance")
            print("3. Deposit amount")
            print("4. Withdraw amount")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                new_password = input("Enter your new password: ")
                change_password(new_password)
            elif choice == "2":
                check_balance()
            elif choice == "3":
                amount = float(input("Enter amount to deposit: "))
                deposit_amount(amount)
            elif choice == "4":
                amount = float(input("Enter amount to withdraw: "))
                withdraw_amount(amount)
            elif choice == "5":
                print("Thank you for using the Bank System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid username or password.")