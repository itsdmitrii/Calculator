from art import logo

def add(x1,x2):
  return x1 + x2


def subtract(x1,x2):
  return x1 - x2
  

def multiply(x1,x2):
  return x1 * x2
  

def devide(x1,x2):
  return x1 / x2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": devide
}
def calculator():
  logo
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)

  should_continue = True
  while should_continue:
    operation_symbol = input("\nPick an operation: ")
    num2 = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"\nResult: {num1}{operation_symbol}{num2}={answer}\n")
    
    should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
    if should_continue == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()