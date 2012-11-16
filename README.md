# Matrix Multiplication Optimization

Given two matrices of dimensions pxq and qxr, it requires pqr scalar
multiplications to compute the product of the two matrices.

Given the dimensions of `n` matrices, what is the minimum number of scalar
multiplications required to compute the product of the matrices?

## Input

Each test case will consist of a line containing a single integer `n`,
indicating the number of matrices, and one line containing `n+1` space-separated
integers `a0` through `an`, where the `i`th matrix is of dimension `a(i)` by
`a(i+1)`.

Input will be terminated by a line containing a single `0`.

## Output

Output for each test case a single integer representing the minimum number of
scalar multiplications required to find the product of the described matrices.

## Sample

In:

```
5
1 2 3 4 5
5
200 1 1 200 500
0
```

Out:

```
302
50241302
```

