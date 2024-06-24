from collections import deque

q = deque()

n = int(input())

for i in range(n):
    command = input().split()
    order = command[0]

    if order == "push_back":
        number = int(command[1])
        q.append(number)
    elif order == "pop_back":
        if len(q) > 0:
            q.pop()
    elif order == "size":
        print(len(q))
    elif order == "get":
        index = int(command[1]) - 1  # 1-based index
        if 0 <= index < len(q):
            print(q[index])
        else:
            print("Index out of range")