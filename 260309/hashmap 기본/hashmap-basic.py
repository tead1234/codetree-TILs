n = int(input())
commands = []
d = dict()
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        d[k] = v
        # commands.append((cmd, k, v))
    elif cmd == "remove":
        if k in d:
            d.pop(k)
    else:
        if k in d:
            print(d[k])
        else:
            print("None")

        # commands.append((cmd, k))

# Please write your code here.

