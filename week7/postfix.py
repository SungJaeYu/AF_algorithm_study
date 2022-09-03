import sys

OPERATOR_LOW = ['+', '-']
OPERATOR_HIGH = ['*', '/']
BRACKET = ['(', ')']
stack = []
output = []
def main():
    calculation = [*sys.stdin.readline().strip()]
    for c in calculation:
        if c in OPERATOR_LOW:
           if stack[-1] in OPERATOR_HIGH:
               stack.pop()
           stack.append(c)
        elif c in BRACKET:
            pass
        else:
            output.append(c)
    if len(stack) != 0:
        while len(stack) != 0:
            output.append(stack.pop())
    for c in output:
        print(c, end='')

main()
