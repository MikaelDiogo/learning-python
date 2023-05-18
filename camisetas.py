N = int(input("digite quantas camisas"" "))
T = input("sequencia de tamanhos").replace(" ", "")
qp = T.count('1')
qm = T.count('2')
tp = int(input("quantas camisas p"))
tm = int(input("quantas camisas m"))

if N == len(T) and qp == tp and qm == tm:
    print('S')
else:
    print('N')

    
    #This code verified if the number of shirts it's equal the your number, and how many are in sizes Small and Medium.

