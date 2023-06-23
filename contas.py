The exercise was solved during the Brazilian Computer Olympiad (OBI), this is a very simple problem in which the person had a certain amount to pay 3 bills, but if the money was not enough, he would need to see how many bills he can pay (For the resolution of the exercise, only conditionals were used)




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


