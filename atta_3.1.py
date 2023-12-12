import math
import numpy as np


def roun(i):
    return round(i, 13)


def float_to_binary(num):
    exponent = 0
    shifted_num = num
    while shifted_num != int(shifted_num):
        shifted_num *= 2
        exponent += 1
    if exponent == 0:
        return '{0:0b}'.format(int(shifted_num))
    binary = '{0:0{1}b}'.format(int(shifted_num), exponent + 1)
    integer_part = binary[:-exponent]
    fractional_part = binary[-exponent:].rstrip('0')
    return '{0}.{1}'.format(integer_part, fractional_part)


def float_to_decimal(num, l):
    num = list((num))
    num.remove('.')
    ans = 0
    for i in range(0, l + 1):
        ans += int(num[i]) * 2 ** (- i)
    return ans


while True:

    print('Пример ввода данных: \n p(s1), p(s2), p(s3), p(s4):'
          ' \n 0.2 0.4 0.1 0.3 \n Арифметическое кодирование последовательности s = \n 4 3 2 4 2 2 1')
    print()
    print('p(s1), p(s2), p(s3), p(s4): ')
    p = list(map(float, input().split()))
    print('Арифметическое кодирование последовательности s = ')
    s = list(map(int, input().split()))
    print()
    ss = ''

    for i in range(len(p)):
        print('p(s' + str(i + 1) + ') =', p[i])
    for i in range(len(s)):
        ss += 's' + str(s[i])
    print(ss)

    print()
    print('Кодирование:')
    print()

    print('Найдём q(si):')
    q = [0] * len(p)
    q[0] = 0
    print('q(s1) = 0')
    for i in range(1, len(p)):
        q[i] = roun(p[i - 1] + q[i - 1])
        print('q(s{}) = p(s{}) + q(s{}) = {} + {} = {}'.format(i + 1, i, i, p[i - 1], q[i - 1], q[i]))
    print()
    print('Найдём G(sik):')
    g = [0] * (len(s) + 1)
    g[0] = 1
    print('G(si0) = 1')
    for k in range(1, len(g)):
        i = s[k - 1] - 1
        g[k] = roun(p[i] * g[k - 1])
        j = s[k - 2]
        if k == 1:
            print('G(s{}{}) = p(s{}) * G(si{}) = {} * {} = {}'.format(i + 1, k, i + 1, k - 1, p[i], g[k - 1], g[k]))
        else:
            print('G(s{}{}) = p(s{}) * G(s{}{}) = {} * {} = {}'.format(i + 1, k, i + 1, j, k - 1, p[i], g[k - 1], g[k]))
    print()
    print('Найдём F(sik):')
    f = [0] * (len(s) + 1)
    f[0] = 0
    print('F(si0) = 0')
    for k in range(1, len(f)):
        i = s[k - 1] - 1
        f[k] = roun(f[k - 1] + q[i] * g[k - 1])
        j = s[k - 2]
        if k == 1:
            print(
                'F(s{}{}) = F(si{}) + q(s{}) * G(si{}) = {} + {} * {} = {}'.format(i + 1, k, k - 1, i + 1,
                                                                                     k - 1, f[k - 1], q[i], g[k - 1],
                                                                                     f[k]))
        else:
            print(
            'F(s{}{}) = F(s{}{}) + q(s{}) * G(s{}{}) = {} + {} * {} = {}'.format(i + 1, k, j, k - 1, i + 1, j,
                                                                                 k - 1, f[k - 1], q[i], g[k - 1], f[k]))
    print('\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    print('Декодирование:\n')
    l = math.ceil(-np.log2(g[k])) + 1
    print('l = -log2(' + str(g[k]) + ' + 1) = ' + str(math.ceil(-np.log2(g[k]))) + ' + 1 =', l)
    x10 = f[len(f) - 1] + g[len(g) - 1] / 2
    print('x в 10 сс: ' + 'F(s17) + (G(s17)/2) = ' + str(f[len(f) - 1]) + ' + (' + str(g[len(g) - 1]) + '/2) =', x10)

    x2 = str(float_to_binary(x10))[0:l + 2]
    print('x в 2 сс: ', x2)
    integer_part, fractional_part = x2.split('.')
    print(fractional_part)

    x10_new = float_to_decimal(x2, l)
    print('Переведем обратно в 10 сс:')
    print("Получили: ", x10_new)
    print()

    for k in range(0, len(s)):
        print()
        print('____________________________________________________________________')
        print('k = {}, F({}) = {}, G({}) = {}'.format(k + 1, k + 1, f[k], k, g[k]))
        for i in range(len(p)):
            check = roun(f[k] + q[i] * g[k])
            print('Для p(s{}) = {}  :  {} + {} * {} = {}'.format(i + 1, q[i], f[k], q[i], g[k], check))
            if check < x10_new:
                print('{} < x   ({} < {})'.format(check, check, x10_new))
                ans = i + 1
            else:
                print('{} >= x   ({} >= {})'.format(check, check, x10_new))
            print()
        print('S{}, p(s{}) = {}'.format(ans, ans, p[ans - 1]))

    print('Выйти - 1; Продолжить - другое число: ', end='')
    v = int(input())
    if v == 1:
        break
    print('\n\n')
