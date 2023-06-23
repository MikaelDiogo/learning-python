V = int(input())
A = int(input())
F = int(input())
P = int(input())

vtotal = int(A+F+P)


if vtotal <= V:
    print(3)
elif vtotal > V:
    if A+F <= V:
        print(2)
    elif A+P <= V:
        print(2)
    elif F+P <= V:
        print(2)
    elif vtotal > V and P <= V:
        print(1)
    elif vtotal > V and F <= V:
        print(1)
    elif vtotal > V and A <= V:
        print(1)
    else:
        print(0)
