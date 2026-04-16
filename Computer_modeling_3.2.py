import random



print("Введите:")
N        =        int(input("- число итераций:                                          N          = "))
I_0      =      float(input("- начальный уровень запасов:                               I_0        = "))
i        =      float(input("- затраты на заказ единицы продукции:                      i          = "))
K        =      float(input("- затраты на заказ:                                        K          = "))
h        =      float(input("- затраты на хранение единицы продукции в единицу времени: h          = "))
w        =      float(input("- издержки, связанные с отложенными поставками:            w          = "))
t_1, t_2 = map(float, input("- диапазон времени доставки продукции:                     [t_1, t_2] = ").split())
m        =        int(input("- количество стратегий управления запасами:                m          = "))

s_S = []
for j in range(m):
    s, S = 0, 0
    while s >= S:
        s, S = map(float, input(f"    - стратегия управления запасами {str(i + 1) + ':':<22} (s_{i + 1}, S_{i + 1}) = ").split())
    s_S.append((s, S))



T_D = [random.uniform(1, 5)]
for j in range(N):
    T_D.append(random.uniform(1, 5) + T_D[-1])



C_p = [0.0 for _ in range(m)]
C_x = [0.0 for _ in range(m)]
C_d = [0.0 for _ in range(m)]
C   = [0.0 for _ in range(m)]

for j in range(m):
    s = s_S[j][0]
    S = s_S[j][1]

    I_t       = I_0
    I_t_plus  = []
    I_t_minus = []
    T         = []
    Q         = []

    T_d = T_D.copy()

    for t in range(N):
        if I_t < s:
            T.append(random.uniform(t_1, t_2) + t)
            Q.append(S - I_t)
            C_p[j] += K + i * Q[-1]

        if t >= min(T_d):
            while t >= min(T_d):
                T_d = T_d[1:]
                D = random.randint(1, 100)
                I_t -= D

        if len(Q) > 0 and t >= min(T):
            I_t += Q[0]
            T = T[1:]
            Q = Q[1:]

        I_t_plus.append(I_t)
        I_t_minus.append(sum(Q))

    C_x[j] = h * sum(I_t_plus)  / N
    C_d[j] = w * sum(I_t_minus) / N

    C[j] = C_p[j] + C_x[j] + C_d[j]



length     = max(max(len(str(j)) for j in C + C_p + C_x + C_d), 6)
length_s_S = max(max(len(str(j)) for j in s_S), 20)

print(f"\n\n\n{"Стратегия (s_j, S_j)":<{length_s_S}} | {"С_об":<{length}} | {"С_п":<{length}} | {"С_х":<{length}} | {"С_D":<{length}}")
print('-' * (length_s_S + 1) + ('|' + '-' * (length + 2)) * 4)
for j in range(m):
    print(f"{s_S[j]!s:<{length_s_S}} | {C[j]:<{length}} | {C_p[j]:<{length}} | {C_x[j]:<{length}} | {C_d[j]:<{length}}")

print(f"\n(s*, S*) = {s_S[C.index(min(C))]}")



print("\n\n\n\n\n")
