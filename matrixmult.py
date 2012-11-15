from sys import stdin

def get_input():
    while True:
        n = int(stdin.readline())
        if n == 0: raise StopIteration()

        a = map(int, stdin.readline().split())

        yield (n, a)

def solve(n, a):
    C = [[0]*n]*n
    for k in xrange(2,n+1):
        for i in xrange(0, n-k+1)):
            C[i][i+k-1] = min(C[i][j] + C[j+1][i+k-1] + a[i]*a[j+1]*a[i+k] for j in xrange(i, i+k-2))
    return C[0][n-1]

for case in get_input():
    solve(*case)

