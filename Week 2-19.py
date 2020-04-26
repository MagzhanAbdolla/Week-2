a = 0
num_maximal = 0
b = -1

while b != 0:
    b = int(input())
    if b > a:
        maximum, num_maximal = b, 1
    elif b == a:
        num_maximal += 1
print(num_maximal)
