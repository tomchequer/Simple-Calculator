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


n1 = int(input('Whats the first number?'))
n2 = int(input('Whats the second number?'))

for i in operations:
    print(i) 

op = input('Which operations above would you like to make?')

opfunction = ''

for i in operations:
    if i == op:
        opfunction = operations[i]


        
answer = opfunction(n1, n2)



print(f"{n1} {op} {n2} = {answer}")