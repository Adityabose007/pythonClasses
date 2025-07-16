# main.py
from deci_to_binary import decimal_to_binary
from bin_to_deci import binary_to_decimal

def main():
    print("Choose an option:")
    print("1. Convert decimal to binary")
    print("2. Convert binary to decimal")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        decimal_ = int(input("Enter a decimal number: "))
        print(f"Binary: {decimal_to_binary(decimal_)}")
    elif choice == "2":
        binary = input("Enter a binary number: ")
        print(f"Decimal: {binary_to_decimal(binary)}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
