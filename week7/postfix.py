import sys

OPERATOR_LOW = ['+', '-']
OPERATOR_HIGH = ['*', '/']
OPEN_BRACKET = '('
CLOSE_BRACKET = ')'
stack = []
output = []

def main():
    calculation = [*sys.stdin.readline().strip()]
    for c in calculation:
        if c in OPERATOR_LOW or c == CLOSE_BRACKET:
           while len(stack) != 0:
               temp = stack.pop()
               if temp == OPEN_BRACKET:
                   break
               print(temp, end='')
               
           if c in OPERATOR_LOW:        
               stack.append(c)
        elif c == OPEN_BRACKET or c in OPERATOR_HIGH:
            stack.append(c)
        else:
            print(c, end='')
    while len(stack) != 0:
        temp = stack.pop()
        if temp != OPEN_BRACKET:
            print(temp, end='')

main()
