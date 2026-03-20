n = int(input())
name = []
height = []
weight = []
o = []

for _ in range(n):
    n_i, h_i, w_i, o_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))
    o.append(int(o_i))

# Please write your code here.
L = list(zip(name, height, weight, o))
L.sort(key = lambda x: (-x[1], -x[2], -x[3]))

for  i in L:
    print(i[0], end = " ")
    print(i[1], end = " ")
    print(i[2], end = " ")
    print(i[3], end = " ")
    print()