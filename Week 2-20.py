prev = -1
RepLen = 0
MaxRepLen = 0
x = int(input())  # 20 #zadach


while x != 0:
    if prev == x:
        RepLen += 1
    else:
        prev = x
        MaxRepLen = max(MaxRepLen, RepLen)
        RepLen = 1
    x = int(input())
MaxRepLen = max(MaxRepLen, RepLen)
print(MaxRepLen)
