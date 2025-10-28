# ANSI color codes for prettier output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def print_header():
    """Print a prettier header for the calculator"""
    print("\n" + "="*50)
    print(f"{Colors.BOLD}{Colors.HEADER}{'✨ SIMPLE CALCULATOR ✨':^50}{Colors.ENDC}")
    print("="*50 + "\n")

def print_menu():
    """Print a prettified menu with options"""
    print(f"{Colors.OKBLUE}{Colors.BOLD}📋 Available Operations:{Colors.ENDC}\n")
    print(f"  {Colors.OKCYAN}[1]{Colors.ENDC} ➕  Add")
    print(f"  {Colors.OKCYAN}[2]{Colors.ENDC} ➖  Subtract")
    print(f"  {Colors.OKCYAN}[3]{Colors.ENDC} ✖️  Multiply")
    print(f"  {Colors.OKCYAN}[4]{Colors.ENDC} ➗  Divide")
    print()

def print_result(result):
    """Print the result in a formatted way"""
    print("\n" + "-"*50)
    print(f"{Colors.OKGREEN}{Colors.BOLD}✓ Result: {result}{Colors.ENDC}")
    print("-"*50 + "\n")

def print_error(message):
    """Print error message in a formatted way"""
    print(f"\n{Colors.FAIL}{Colors.BOLD}✗ {message}{Colors.ENDC}\n")

def main():
    print_header()
    print_menu()
    
    choice = input(f"{Colors.BOLD}Enter choice (1/2/3/4): {Colors.ENDC}")
    
    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input(f"{Colors.BOLD}Enter first number: {Colors.ENDC}"))
            num2 = float(input(f"{Colors.BOLD}Enter second number: {Colors.ENDC}"))
            
            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            
            print_result(result)
        except ValueError:
            print_error("Invalid input! Please enter valid numbers.")
    else:
        print_error("Invalid choice! Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()