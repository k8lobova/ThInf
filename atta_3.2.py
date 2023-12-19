import math


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


def roun(i):
    return round(i, 6)


while True:
    print('Пример ввода данных: \n'
          ' 0.355 0.03 0.01 0.1 0.28 0.073 0.034 0.046 0.018 0.054')
    print('Ввод: ')
    p = list(map(float, input().split()))
    # p = [0.355, 0.03, 0.01, 0.1, 0.28, 0.073, 0.034, 0.046, 0.018, 0.054]
    print()
    for i in range(len(p)):
        print('z' + str(i + 1) + ' =', p[i])
    print()

    print('Найдём qm:')
    q = [0] * len(p)
    q[0] = 0
    print('q(1) = 0')
    for i in range(1, len(p)):
        q[i] = roun(p[i - 1] + q[i - 1])
        print('q({}) = q({}) + p({}) = {} + {} = {}'.format(i + 1, i, i, q[i - 1], p[i - 1], q[i]))
    print()

    print('Найдём σm:')
    σ = [0] * len(p)
    for i in range(len(p)):
        σ[i] = roun(q[i] + p[i] / 2)
        print('σ({}) = q({}) + p({}) / 2 = {} + {} / 2 = {}'.format(i + 1, i + 1, i + 1, q[i], p[i], σ[i]))
    print()

    print('Найдём lm и li:')
    lm = [0] * len(p)
    li = [0] * len(p)
    for i in range(len(p)):
        lm[i] = roun(-math.log2(p[i]))
        li[i] = math.ceil(lm[i]) + 1
        print('l{} = -log2(p{})= -log2({}) = {} ≈ {} => li = lm + 1 = {} + 1 = {}'
              .format(i + 1, i + 1, p[i], lm[i], math.ceil(lm[i]), math.ceil(lm[i]), li[i]))
    print()
    print('Перевод в двоичную систему счисления: ')
    for i in range(len(p)):
        x2 = str(float_to_binary(σ[i]))[0:10 + 2]
        x2_li = str(float_to_binary(σ[i]))[0:li[i] + 2]
        integer_part, fractional_part = x2_li.split('.')
        print('σ({}) = {} = {} -> {} (li = {})'.format(i + 1, σ[i], x2, fractional_part, li[i]))
    print()

    l, h, k = 0, 0, 0
    l_str1, l_str2, h_str1, h_str2, k_str1, k_str2 = '', '', '', '', '', ''
    for i in range(len(p)):
        l += li[i] * p[i]
        l_str1 += 'l({}) * p({}) + '.format(i + 1, i + 1)
        l_str2 += '{} * {} + '.format(li[i], p[i])

        h -= p[i] * math.log2(p[i])
        h_str1 += 'p({}) * log2(p({})) + '.format(i + 1, i + 1)
        h_str2 += '{} * log2({}) + '.format(p[i], p[i])

        k += 2 ** (-li[i])
        k_str1 += '2^(-l{}) + '.format(i + 1)
        k_str2 += '2^(-{}) + '.format(li[i])
    l = roun(l)
    print('L = {} =\n  = {} = {}\n'.format(l_str1[:-3], l_str2[:-3], l))

    h = roun(h)
    print('H = -({}) =\n  = -({}) ≈ {}\n'.format(h_str1[:-3], h_str2[:-3], h))

    l_h = roun(l - h)
    print('L - H = {} - {} = {}\n'.format(l, h, l_h))
    print('K = {} =\n  = {} ≈ {}\n'.format(k_str1[:-3], k_str2[:-3], k))

    print('Выйти - 1; Продолжить - что-нибудь другое: ', end='')
    v = int(input())
    print()
    if v == 1:
        break
# 0.355 0.03 0.01 0.1 0.28 0.073 0.034 0.046 0.018 0.054
# 0.164 0.16 0.185 0.185 0.13 0.07 0.028 0.018 0.01 0.05
