from sys import stdin
# stdin = open("bakjoon/input.txt", "r")

lines = []


for _ in range(1):
    lines.append(stdin.readline().rstrip())

tmp = lines[0].split('')

array = []

for _ in range(5):
  # 'tmp에서 pop으로 하나 뽑고, 그걸 array 넣는다' 
  arrary.append(tmp.pop())

print(' '.join (array))