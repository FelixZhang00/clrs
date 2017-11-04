#!/usr/bin/env python
# coding:utf-8

'''
15.1 钢条切割
自底向上
每个子问题只需要求解一次，当我们求解它（也是第一次遇到它）时，它的所有前提子问题都已求解完成。
还保存对应的切割方法
'''


def extended_bottom_up_cut_rod(p, n):
  aux = []  # 新数组用来保存子问题的解
  s = []  # 将一段钢条的最优切割长度i保存在s[j]中
  for i in range(0, n + 1):
    aux.append(0)
    s.append(0)

  for j in range(1, n + 1):  # 1~n
    q = -1
    for i in range(1, j + 1):
      if q < (p[i] + aux[j - i]):
        q = (p[i] + aux[j - i])
        s[j] = i
    aux[j] = q

  return (aux,s)


def print_extended_bottom_up_cut_rod(p, n):
  (r, s) = extended_bottom_up_cut_rod(p, n)
  print 'max value='+ str(r[n])
  print 'solution:'
  while n>0:
    print str(s[n])
    n = n - s[n]



def simpleTest():
  p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

  n = 7

  print_extended_bottom_up_cut_rod(p, n)


if __name__ == '__main__':
  simpleTest()
