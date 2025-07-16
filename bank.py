def create_account():
    acc_no = input("Enter account number: ")
    name = input("Enter name: ")
    try:
        balance = float(input("Enter initial balance: "))
    except:
        print("Invalid amount!")
        return

    with open("accounts.txt", "a") as file:
        file.write(f"{acc_no},{name},{balance}\n")
    print("Account created!")

def check_account(acc_no):
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == acc_no:
                    return data
    except:
        pass
    return None

def deposit():
    acc_no = input("Enter account number: ")
    data = check_account(acc_no)
    if not data:
        print("Account NOT FOUND! ❌" )
        return

    try:
        amount = float(input("Enter amount to deposit: "))
        data[2] = str(float(data[2]) + amount)
        update_account(acc_no, data)
        print("DEPOSTI SUCCESSFULL!! ✅")
    except:
        print("Invalid amount!")

def withdraw():
    acc_no = input("Enter account number: ")
    data = check_account(acc_no)
    if not data:
        print("Account NOT FOUND! ❌" )
        return

    try:
        amount = float(input("Enter amount to withdraw: "))
        balance = float(data[2])
        if amount > balance:
            print("Not enough balance!")
            return
        data[2] = str(balance - amount)
        update_account(acc_no, data)
        print("Withdraw successful!")
    except:
        print("Invalid amount!")

def check_balance():
    acc_no = input("Enter account number: ")
    data = check_account(acc_no)
    if data:
        print(f"Name: {data[1]}, Balance: ₹{data[2]}")
    else:
        print("Account NOT FOUND! ❌" )

def update_account(acc_no, updated_data):
    lines = []
    with open("accounts.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == acc_no:
                lines.append(",".join(updated_data) + "\n")
            else:
                lines.append(line)
    with open("accounts.txt", "w") as file:
        file.writelines(lines)

def main():
    while True:
        print("\n=== Simple Banking System ===")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            print("Exiting from Banking Management system. \n!")
            break
        else:
            print("Invalid choice. Try again.")

main()
