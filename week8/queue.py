import sys

class Queue:
    def __init__(self):
        self.len = 0
        self.q = []

    def push(self, number):
        self.q.append(number)
        self.len += 1

    def front(self):
        if self.empty():
            return -1
        return self.q[0]

    def back(self):
        if self.empty():
            return -1
        return self.q[self.len - 1]

    def empty(self):
        if self.len == 0:
            return 1
        return 0

    def pop(self):
        if self.empty():
            return -1
        self.len -= 1
        return self.q.pop(0)

    def size(self):
        return self.len

def main():
    queue = Queue()
    command_func = {"push" : queue.push,
                    "pop"  : queue.pop,
                    "front" : queue.front,
                    "back" : queue.back,
                    "empty" : queue.empty,
                    "size" : queue.size,
                    }
    number_command = int(input())
    for i in range(number_command):
        command = sys.stdin.readline().split()
        if len(command) == 1:
            print(command_func[command[0]]())
        else:
            command_func[command[0]](command[1])

main()
