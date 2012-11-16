from sys import stdin

def get_input():
    while True:
        n = int(stdin.readline())
        if n == 0: raise StopIteration()

        a = map(int, stdin.readline().split())

        yield (n, a)

# define irange to be an inclusive range function
irange = lambda l,u: xrange(l,u+1)

def solve(n, a):
    C = [[0]*n]*n
    for k in irange(2,n):
        for i in irange(0, n-k):
            C[i][i+k-1] = min(C[i][j] + C[j+1][i+k-1] + a[i]*a[j+1]*a[i+k-1] for j in irange(i, i+k-2))
    print C[0][n-1]

for case in get_input():
    solve(*case)

