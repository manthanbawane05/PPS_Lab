d = int(input())
m = int(input())
y = int(input())

flag = True

if y < 0 or m < 1 or m > 12:
    flag = False

if m in (1, 3, 5, 7, 8, 10, 12):
    maxdays = 31
elif m in (4, 6, 9, 11):
    maxdays = 30
elif m == 2:
    if y % 4 == 0:
        maxdays = 29
    else:
        maxdays = 28
else:
    flag = False

if d < 1 or d > maxdays:
    flag = False

if flag:
    d += 1

    if d > maxdays:
        d = 1
        m += 1

        if m > 12:
            m = 1
            y += 1

    print(f"{d:02d}-{m:02d}-{y}")
