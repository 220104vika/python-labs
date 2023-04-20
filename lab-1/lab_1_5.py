from array import*
count = int(input())
a = []
for i in range(count):
    word = input()
    a.append(word)
print(*a)