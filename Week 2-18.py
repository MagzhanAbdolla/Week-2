
x = - 1
Odin = 0
Dva = 0

while x != 0:
    x = int(input())
    if x > Odin and x != 0:
        Dva = Odin
        Odin = x
    elif x > Dva and x != 0:
        Dva = x
print(Dva)
