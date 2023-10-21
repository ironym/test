from sys import stdin
stdin = open("bakjoon/input.txt", "r")

lines = []


for _ in range(1):
    lines.append(stdin.readline().rstrip())

tmp = lines[0]

[nbr1, nbr2] = map(int, tmp.split(' '))
print(nbr1, nbr2)

if nbr1 > nbr2: 
    print('>')
elif nbr1 < nbr2: 
    print('<')
elif nbr1 == nbr2: 
    print('==')