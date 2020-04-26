n = int(input())
N = n

while n != 0:
    n = int(input())
    if n == 0:
        break
    if n > N:
        N = n
print(N)
