#!/usr/bin/env python
# coding:utf-8

'''
15.1 钢条切割
带备忘的自顶向下递归实现
并且返回切割方案
'''


def memoized_cut_rod(p, n):
  aux = []
  s = []  # 将一段钢条的最优切割长度i保存在s[j]中
  for i in range(0, n + 1):
    aux.append(-1)  # 随便取个最小值
    s.append(0)

  r = memoized_cut_rod_aux(p, n, aux, s)

  print s
  subs = []
  while n>0:
    subs.append(s[n])
    n = n - s[n]

  return (r,subs)


def memoized_cut_rod_aux(p, n, aux,s):
  if aux[n] >= 0:
    return aux[n]

  if n == 0:
    return 0
  else:
    q = -1  # 随便取个最小值
    for i in range(1, n + 1):  # 遍历1~n
      temp_q = p[i] + memoized_cut_rod_aux(p, n - i, aux,s)
      if q < temp_q:
        q = temp_q
        s[n] = i

  aux[n] = q
  return q


def print_extended_bottom_up_cut_rod(p, n):
  (r, s) = memoized_cut_rod(p, n)
  print 'max value='+ str(r)
  print 'solution:'
  print s

def simpleTest():
  p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

  n = 7

  print_extended_bottom_up_cut_rod(p,n)


if __name__ == '__main__':
  simpleTest()
