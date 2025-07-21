# Voting eligibility check based on age

def check_eligibility():
    print("=== Voting Eligibility Checker ===")
    name = input("Enter your name: ")
    
    try:
        age = int(input("Enter your age: "))
        
        if age >= 18:
            print(f"✅ Hello {name}, you are eligible to vote.")
        else:
            print(f"❌ Sorry {name}, you are not eligible to vote. You must be at least 18 years old.")
    except ValueError:
        print("⚠️ Invalid input. Please enter a valid age in numbers.")

# Main Program
check_eligibility()
