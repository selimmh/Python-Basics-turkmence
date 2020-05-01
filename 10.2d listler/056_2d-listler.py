# 2d listler we goşa looplar

# ulanyjy 2d listiň uzynlygyny girizýär
m = int(input('V[?][?]: '))
n = int(input('V[' + str(m) + '][?]: '))

print('Matrix size: V[' + str(m) + '][' + str(n) + ']')

matrix = []


for i in range(0,m):
    matrix += [0]


for i in range (0,m):
    matrix[i] = [0]*n

# goşa loop
for i in range (0,m):
    for j in range (0,n):

        matrix[i][j] = int(input('[' + str(i+1) + ':' + str(j+1) + ']: '))

print("\n")

# 2d listiň elementlerini tablisa görnüşinde print edýär
for num_grid in matrix:
    print(num_grid)