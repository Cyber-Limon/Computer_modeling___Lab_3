import math
import random
import matplotlib.pyplot as plt



def lambda_func(t):
    if t < 8:
        return 0

    elif 8 <= t < 12:
        return 10

    elif 12 <= t < 14:
        return 40

    elif 14 <= t < 18:
        return 20

    elif 18 <= t:
        return 30



def poisson(t, l = 40):
    while True:
        U1 = random.random()
        t  = t - 1 / l * math.log(U1)
        U2 = random.random()

        if U2 <= lambda_func(t) / l:
            return t



def exponential(l = 40):
    U = random.random()
    X = -1 / l * math.log(U)

    return X



def integral(X):
    S = t = 0
    for i in range(len(X)):
        if X[i][1] > T:
            S += X[i][0] * (T - t)
            break

        S += X[i][0] * (X[i][1] - t)
        t = X[i][1]

    return S



print("Введите:")
T = int(input("- время работы:   T = "))
N = int(input("- число итераций: N = "))



T_p = []
S_T = [0 for _ in range(N)]
W_T = [0 for _ in range(N)]
Q_T = [0 for _ in range(N)]
p_T = [0 for _ in range(N)]

for iteration in range(N):
    A = []
    V = []
    M = []
    B = []
    D = []

    t = N_A = N_D = n = 0

    T_0      = poisson(t)
    t_A, t_D = T_0, math.inf

    M.append((0, t))
    B.append((0, t))



    while True:
        # Случай 1
        if t_A <= t_D and t_A <= T:
            t    = t_A
            N_A += 1
            n   += 1

            T_t = poisson(t)
            t_A = T_t

            if n == 1:
                V.append(exponential())
                t_D = t + V[-1]

                B.append((1, t))

            A.append(t)



        # Случай 2
        elif t_D <= t_A and t_D <= T:
            t    = t_D
            N_D += 1
            n   -= 1

            if n == 0:
                t_D = math.inf
                B.append((0, t))
            else:
                V.append(exponential())
                t_D = t + V[-1]

            D.append(t)



        # Случай 3
        elif min(t_A, t_D) > T and n > 0:
            t    = t_D
            N_D += 1
            n   -= 1

            if n > 0:
                V.append(exponential())
                t_D = t + V[-1]

            D.append(t)



        # Случай 4
        elif min(t_A, t_D) > T and n == 0:
            T_p.append(max(t - T, 0))
            M.append((0, t))
            B.append((0, t))
            break

        M.append((n, t))



    for i in range(len(A)):
        S_T[iteration] += D[i] - A[i]
        W_T[iteration] += D[i] - V[i] - A[i]

    S_T[iteration] /= len(A)
    W_T[iteration] /= len(A)
    Q_T[iteration]  = integral(M) / T
    p_T[iteration]  = integral(B) / T



    if iteration == 0:
        plt.step([p[1] for p in M], [p[0] for p in M], where='post')
        plt.axhline(0,  color='r')
        plt.show()



        s = 0
        for i in range(len(A)):
            s += D[i] - A[i]
        s = s / len(A)

        print("\n\n\nВерификация: ")
        print(f"- среднее время:           {s}")
        print(f"- среднее время программы: {S_T[iteration]}")



T_Pn = sum(T_p) / N
S_Tn = sum(S_T) / N
W_Tn = sum(W_T) / N
Q_Tn = sum(Q_T) / N
p_Tn = sum(p_T) / N



print("\n\n\nРезультаты имитации:")
print(f"- среднее время после T, когда уходит последний клиент:      T_P = {T_Pn}")
print(f"- среднее время, которое клиент проводит в системе:          S_T = {S_Tn}")
print(f"- средняя задержка клиентов в очереди:                       W_T = {W_Tn}")
print(f"- среднее число клиентов в очереди:                          Q_T = {Q_Tn}")
print(f"- средний коэффициент использования устройства обслуживания: p_T = {p_Tn}")
