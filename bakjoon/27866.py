from sys import stdin
stdin = open("bakjoon/input.txt", "r")
lines = []

for _ in range(2):
    lines.append(stdin.readline().rstrip())


word =lines[0]
print(word[int(lines[1]) - 1])