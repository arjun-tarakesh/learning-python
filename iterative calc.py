



def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operations = {
    '+':add,
    '-':sub,
    '*':multiply,
    '/':div,
}
def calculator():
    num1 = float(input("Enter the first num : "))

    # A flag in Python acts as a signal to the program to determine whether or not the program as 
    # a whole or a specific section of the program should run.
    # In other words, you can set the flag to True and the program will run continuously until 
    # any type of event makes it False.

    should_continue = True

    while should_continue: 
        for symbol in operations:
            print("\n",symbol)
        op = input("\n enter an operator from the above list : ")

        num2 = float(input("Enter the second num : "))

        calc_func = operations[op]
        ans = calc_func(num1,num2)
        print(f"{num1} {op} {num2} = {ans}")
        if input(f"to continue with the result hit Y to end Hit N : ") == 'Y' or 'y':
            num1 = ans
        else:
            should_continue = False
            calculator()
            
calculator()


