import locale
import numpy as np
locale.setlocale(locale.LC_ALL, '')

while True:

    print('Расположение данных: \np(a|a) = 0.5    p(a|b) = 0.6    p(a|c) = 0.4 '
          '\np(b|a) = 0.35    p(b|b) = 0.2    p(b|c) = 0.1 '
          '\np(c|a) = 0.15    p(c|b) = 0.2    p(c|c) = 0.5 ')
    print('Желаемый вывод - с использованием "." (0); "," (1): ', end='')
    ch = int(input())
    print('Пример ввода данных: \n0.5 0.6 0.4 \n0.35 0.2 0.1 \n0.15 0.2 0.5\n')



    matrix, matrix_new, temp = [], [], []
    H_Xi, H_Xi_Xi1, Ha, Hb, Hc, Usl_entr, one, two = 0, 0, 0, 0, 0, 0, 97, 97
    Habc = [0, 0, 0]


    def roun(i):
        return round(i, 6)


    def choice(ch, m):
        if ch == 0:
            return m
        if ch == 1:
            return locale.str(m)


    for i in range(3):
        a = list(map(float, input().split()))
        matrix.append(a)
    print()
    for i in range(3):
        for j in range(3):
            print('p(' + chr(one + i) + '|' + chr(two + j) + ') =', choice(ch, matrix[i][j]), end='    ')

        print()
    print()

    left_side = np.array([[matrix[0][0] - 2, matrix[0][1] - 1, matrix[0][2] - 1],
                          [matrix[1][0], matrix[1][1] - 1, matrix[1][2]],
                          [matrix[2][0], matrix[2][1], matrix[2][2] - 1]])

    right_side = np.array([-1, 0, 0])
    pabc = np.linalg.solve(left_side, right_side)

    for i in range(3):
        now = pabc[i]
        H_Xi -= now * np.log2(now)
        print('p' + chr(one + i), '=', choice(ch, roun(now)))

    print()
    print('H(Xi) = ', choice(ch, roun(H_Xi)))
    print()

    for i in range(3):
        for j in range(3):
            temp.append(matrix[i][j] * pabc[j])
            print('p(' + chr(one + j) + chr(two + i) + ') =', choice(ch, roun(temp[j])))
        matrix_new.append(temp)
        temp = []

    for i in range(3):
        for j in range(3):
            now_1 = matrix_new[i][j]
            now_2 = matrix[i][j]
            H_Xi_Xi1 -= now_1 * np.log2(now_1)
            Habc[i] -= now_2 * np.log2(now_2)
        Habc[i] = roun(Habc[i])

    for i in range(3):
        Usl_entr += pabc[i] * Habc[i]

    print()
    print('H(Xi,Xi+1) = ', choice(ch, roun(H_Xi_Xi1)))
    print()
    for i in range(3):
        print('H' + chr(one + i) + '=', choice(ch, Habc[i]))

    print()
    print('Способ с Ha, Hb, Hc: ')
    print('1) HXi(Xi+1) = ', choice(ch, roun(Usl_entr)))

    print('Способ с вычитанием из H(Xi,Xi+1) энтропию H(Xi): ')
    print('2) HXi(Xi+1) = ', choice(ch, roun(roun(H_Xi_Xi1) - roun(H_Xi))))

    '''
    0.5 0.6 0.4
    0.35 0.2 0.1
    0.15 0.2 0.5
    '''
    print('Выйти - 1; Продолжить - что-нибудь другое: ', end='')
    v = int(input())
    if v == 1:
        break

