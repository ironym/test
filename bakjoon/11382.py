from sys import stdin
stdin = open("bakjoon/input.txt", "r") # 텍스트 파일을 읽을 때 사용합니다.

lines = []

# 세 줄을 읽습니다. (이전에 읽은 줄의 다음 줄부터 읽습니다.)
for _ in range(2): 
    lines.append(stdin.readline().rstrip())

word = lines[0]

print(word[int( lines[1]) -1])