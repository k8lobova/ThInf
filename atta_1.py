print('Пример ввода данных: 0.14 0.35 0.21 0.06 0.15 0.09 2 3')
import math

a = list(map(float, input().split()))
n = int(a[-2])
m = int(a[-1])
count, H_X, H_Y, H_XY, Hxi_Y, Hyi_X, Hx_Y, Hy_X = 0, 0, 0, 0, 0, 0, 0, 0
# print(n,m) # n = x = 3, m = y = 4
matrix = [[0 for j in range(m)] for i in range(n)]
p_xiy = [[0 for j in range(m)] for i in range(n)]
p_yix = [[0 for j in range(m)] for i in range(n)]

p_x_1234, p_y_1234, Hx_1234_Y, Hy_1234_X = [0] * n, [0] * m, [0] * n, [0] * m
for i in range(0, n):
    for j in range(0, m):
        matrix[i][j] = a[count]
        count += 1


# print(matrix)

def roun(i):
    return round(i, 6)


for i in range(0, n):
    for j in range(0, m):
        p_x_1234[i] += matrix[i][j]
    p_x_1234[i] = roun(p_x_1234[i])
    print('p( x', i + 1, ') =', p_x_1234[i])
print()
for j in range(0, m):
    for i in range(0, n):
        p_y_1234[j] += matrix[i][j]
    p_y_1234[j] = roun(p_y_1234[j])
    print('p( y', j + 1, ') =', p_y_1234[j])

print()
# print('p(x1234) = ', p_x_1234)
# print('p(y1234) = ', p_y_1234)
print()
count = 0
for j in range(0, m):
    for i in range(0, n):
        print('p( x', i + 1, ') * p( y', j + 1, ') =', roun(p_x_1234[i] * p_y_1234[j]),
              ';      p( x', i + 1, 'y', j + 1, ') =', roun(matrix[i][j]))
        if (matrix[i][j] - roun(p_x_1234[i] * p_y_1234[j])) == 0:
            count += 1
    print()
if count == n * m:
    print("Ансамбли не зависимы")
else:
    print("Ансамбли зависимы")
print()

for j in range(0, m):
    for i in range(0, n):
        p_xiy[i][j] = roun(matrix[i][j] / p_y_1234[j])
        print('p( x', i + 1, '| y', j + 1, ') =', p_xiy[i][j])
    print()
# print(p_xiy)

print()
print()

for i in range(0, n):
    for j in range(0, m):
        p_yix[i][j] = roun(matrix[i][j] / p_x_1234[i])
        print('p( y', j + 1, '| x', i + 1, ') =', p_yix[i][j])
    print()
# print(p_yix)

# Энтропия


for i in range(0, n):
    H_X += - p_x_1234[i] * math.log2(p_x_1234[i])

for j in range(0, m):
    H_Y += - p_y_1234[j] * math.log2(p_y_1234[j])

for i in range(0, n):
    for j in range(0, m):
        H_XY += - matrix[i][j] * math.log2(matrix[i][j])

H_X = roun(H_X)
H_Y = roun(H_Y)
H_XY = roun(H_XY)

print('H(X) =', H_X)
print('H(Y) =', H_Y)
print('H(XY) =', H_XY)
print()

for i in range(0, n):
    Hxi_Y = 0
    for j in range(0, m):
        Hxi_Y += - p_yix[i][j] * math.log2(p_yix[i][j])
    Hx_1234_Y[i] = roun(Hxi_Y)
    print('Hx', i + 1, '(Y) =', Hx_1234_Y[i])

    Hx_Y += p_x_1234[i] * Hx_1234_Y[i]
print()
Hx_Y = roun(Hx_Y)
print('Hx(Y) =', Hx_Y)

# print(Hx_1234_Y)
print()

for j in range(0, m):
    Hyi_X = 0
    for i in range(0, n):
        Hyi_X += - p_xiy[i][j] * math.log2(p_xiy[i][j])
    Hy_1234_X[j] = roun(Hyi_X)
    print('Hy', j + 1, '(X) =', Hy_1234_X[j])

    Hy_X += p_y_1234[j] * Hy_1234_X[j]
print()
Hy_X = roun(Hy_X)
print('Hy(X) =', Hy_X)

# print(Hx_1234_Y)
input()