#This will be a simple text-based calculator
#built for practice, but its also very functional.


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2


operations = {
    "+": add, 
    "-": sub, 
    "*": mult,
    "/": div
    }

print("""
  _____________________
|  _________________  |
| | WELCOME         | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|     
      
      """)

def calculator():

    n1 = float(input('Whats the first number?'))

    for i in operations:
            print(i) 
        
    turnedon = True

    while turnedon:
        
        op = input('Which operations above would you like to make?')

        n2 = float(input('Whats the next number?'))

        opfunction = ''

        for i in operations:
            if i == op:
                opfunction = operations[i]
                
        answer = opfunction(n1, n2)

        print(f"{n1} {op} {n2} = {answer}")
        
        if input ('Do you wanna make another operation? ("y" to keep going or "n" to restart) ') == "y":
            n1 = answer
        else:
            turnedon = False
            calculator()

calculator()

