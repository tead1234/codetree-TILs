n = int(input())

name = []
score1 = []
score2 = []
index = []

c= 0
for _ in range(n):
    c += 1
    키, 몸무게 = map(int, input().split())
    name.append(키)
    score1.append(몸무게)
    # score2.append(int(student_input[2]))
    index.append(c)

# Please write your code here.

L = list(zip(name, score1,index))

L.sort(key = lambda x: (-x[0], -x[1], x[2]))

for i in L:
    print(i[0], end =" ")
    print(i[1], end =" ")
    print(i[2], end =" ")

    print()