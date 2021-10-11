import numpy as np

inputs = open('inputs.txt', 'r')
output = open('output.txt', 'w')

asum = 0
bsum = 0
n = 100
N = 2 * n
a = [0] * N
b = [0] * n
inp = [' '] * N
i = 0
while i < N:
    inp[i] = inputs.readline()
    if inp[i] != '':
        a[i] = int(inp[i])
        i += 1

for i in range(0, n, 1):
    b[i] = a[2 * i] + a[2 * i + 1]
    print(' &', b[i], end='', file=output)
    if i % int(np.sqrt(n)) == int(np.sqrt(n)) - 1:
        print('', file=output)

print('\n', file=output)
c = [0] * 51
d = [0] * 91

for i in range(0, N, 1):
    asum += a[i]
    c[a[i]] += 1

while c[-1] == 0:
    c.pop(-1)

for i in range(1, len(c), 1):
    print(c[i], end=' ', file=output)

print('\n', file=output)

for i in range(0, n, 1):
    d[b[i]] += 1

while d[-1] == 0:
    d.pop(-1)

for i in range(1, len(d), 1):
    print(d[i], end=' ', file=output)

for i in range(0, N, 1):
    bsum += (a[i] - (asum / N)) ** 2

print('\n', file=output)
print('Среднее 20 с: ', asum / N, file=output)
print('Средняя ошибка 20 с: ', np.sqrt(1 / N * bsum), file=output, end='\n')

for i in range(0, N, 1):
    print(' &', a[i], end='', file=output)
    if i % int(np.sqrt(n)) == int(np.sqrt(n)) - 1:
        print('', file=output)

inputs.close()
output.close()
