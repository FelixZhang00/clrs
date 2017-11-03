#!/usr/bin/env python
# coding:utf-8

'''
15.1 钢条切割
带备忘的自顶向下递归实现
'''


def memoized_cut_rod(p, n):
  aux = []
  for i in range(0, n + 1):
    aux.append(-1)  # 随便取个最小值

  return memoized_cut_rod_aux(p, n, aux)


def memoized_cut_rod_aux(p, n, aux):
  if aux[n] >= 0:
    return aux[n]

  if n == 0:
    return 0
  else:
    q = -1  # 随便取个最小值
    for i in range(1, n + 1):  # 遍历1~n
      q = max(q, p[i] + memoized_cut_rod_aux(p, n - i,aux))

  aux[n] = q
  return q


def simpleTest():
  p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

  n = 7

  value = memoized_cut_rod(p, n)
  print value


if __name__ == '__main__':
  simpleTest()
