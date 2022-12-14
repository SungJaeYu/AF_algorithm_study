import sys

OPERATOR_HIGH = ['*', '/']

OPERATOR = ['+', '-', '*', '/', '(', ')']


stack = []

def proc_operator_low(c):
    while len(stack) != 0:
        if stack[-1] == '(':
            break;
        print(stack.pop(), end='')
    stack.append(c)

def proc_operator_high(c):
    while len(stack) != 0:
        if stack[-1] not in OPERATOR_HIGH:
            break;
        print(stack.pop(), end='')
    stack.append(c)

def proc_open_bracket(c):
    stack.append(c)

def proc_close_bracket(c):
     while len(stack) != 0:
        temp = stack.pop()
        if temp == '(':
            break;
        print(temp, end='')

proc_func = {'+': proc_operator_low,
             '-': proc_operator_low,
             '*': proc_operator_high,
             '/': proc_operator_high,
             '(': proc_open_bracket,
             ')': proc_close_bracket,
             }


def main():
    calculation = [*sys.stdin.readline().strip()]
    for c in calculation:
        if c in OPERATOR:
            proc_func[c](c)
        else: # Alphabet
            print(c, end='')
    while len(stack) != 0:
        print(stack.pop(), end='')

main()
