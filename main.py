import sys
from services import BankService

def main():
    bank = BankService()
    print("=== Vityarthi Bank Management System ===")
    
    while True:
        print("\n1. Create Account\n2. Login\n3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            pin = input("Set 4-digit PIN: ")
            acc_num = bank.create_account(name, pin)
            print(f"Account Created! Your Account Number is: {acc_num}")

        elif choice == '2':
            acc_num = input("Enter Account Number: ")
            pin = input("Enter PIN: ")
            user = bank.login(acc_num, pin)

            if user:
                print(f"\nWelcome, {user.name}")
                while True:
                    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. History\n5. Logout")
                    sub_choice = input("Choice: ")
                    
                    if sub_choice == '1':
                        amt = float(input("Amount to deposit: "))
                        success, msg = bank.perform_transaction(user, amt, 'deposit')
                        print(msg)
                    elif sub_choice == '2':
                        amt = float(input("Amount to withdraw: "))
                        success, msg = bank.perform_transaction(user, amt, 'withdraw')
                        print(msg)
                    elif sub_choice == '3':
                        print(f"Current Balance: ${user.balance}")
                    elif sub_choice == '4':
                        print("--- Transaction History ---")
                        for record in user.history:
                            print(record)
                    elif sub_choice == '5':
                        break
            else:
                print("Invalid Credentials")

        elif choice == '3':
            sys.exit()

if __name__ == "__main__":
    # Ensure data dir exists
    if not os.path.exists('data'):
        os.makedirs('data')
    main()
