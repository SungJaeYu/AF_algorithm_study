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
        if c in OPERATOR_LOW:
           while len(stack) != 0:
               if stack[-1] == OPEN_BRACKET:
                   break
               temp = stack.pop()
               print(temp, end='')
               
           if c in OPERATOR_LOW:        
               stack.append(c)
        elif c == CLOSE_BRACKET:
            while len(stack) != 0:
                temp = stack.pop()
                if temp == OPEN_BRACKET:
                    break;
                print(temp, end='')
        elif c == OPEN_BRACKET:
            stack.append(c)
        elif c in OPERATOR_HIGH:
            while len(stack) != 0:
                if stack[-1] not in OPERATOR_HIGH:
                    break;
                temp = stack.pop()
                print(temp, end='')
            stack.append(c)
        else:
            print(c, end='')
    while len(stack) != 0:
        temp = stack.pop()
        if temp != OPEN_BRACKET:
            print(temp, end='')

main()
