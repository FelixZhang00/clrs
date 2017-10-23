#!/usr/bin/env python
# coding:utf-8

'''
两个nxn矩阵相乘

'''

# O(n^3)的暴力求解法
def square_matrix_multiply(A,B):
  n = len(A)
  C = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      c = 0
      for k in range(n):
        c += A[i][k]*B[k][j]
      C[i][j] = c

  return C


# 一个简单的分治法求解，时间复杂度同样是O(n^3)
def square_matrix_multiply_recursive(A,B):
  pass

def simpleTest():
  A = [[2,4],[3,5]]
  B = [[1,2],[2,4]]

  C = square_matrix_multiply(A,B)
  print C

if __name__ == '__main__':
  simpleTest()