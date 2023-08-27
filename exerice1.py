# Problem 2: Grade Calculator

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

try:
    score = float(input("Enter the student's test score: "))
    if 0 <= score <= 100:
        grade = calculate_grade(score)
        print(f"The student's grade is: {grade}")
    else:
        print("Invalid score. Please enter a score between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a numeric score.")

# Problem 3: Number Comparison

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if num1 > num2:
        comparison = "greater than"
    elif num1 < num2:
        comparison = "less than"
    else:
        comparison = "equal to"
    
    print(f"The first number is {comparison} the second number.")
except ValueError:
    print("Invalid input. Please enter numeric values.")


# Problem 4: Leap Year Checker

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

try:
    year = int(input("Enter a year: "))
    if year > 0:
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print("Invalid year. Please enter a positive year.")
except ValueError:
    print("Invalid input. Please enter a valid year.")


# Problem 5: ATM Transaction Simulator

def display_menu():
    print("\nMenu:")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Exit")

def main():
    try:
        balance = float(input("Enter your current account balance: "))
        while True:
            display_menu()
            choice = int(input("Enter your choice (1/2/3/4): "))
            
            if choice == 1:
                withdraw_amount = float(input("Enter the amount to withdraw: "))
                if withdraw_amount <= balance:
                    balance -= withdraw_amount
                    print(f"Withdrawal successful. Your updated balance is: {balance}")
                else:
                    print("Insufficient funds.")
            elif choice == 2:
                deposit_amount = float(input("Enter the amount to deposit: "))
                if deposit_amount > 0:
                    balance += deposit_amount
                    print(f"Deposit successful. Your updated balance is: {balance}")
                else:
                    print("Invalid deposit amount.")
            elif choice == 3:
                print(f"Your current balance is: {balance}")
            elif choice == 4:
                print("Exiting ATM.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()


