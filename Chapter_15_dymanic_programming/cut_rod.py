#!/usr/bin/env python
# coding:utf-8

'''
15.1 钢条切割
自顶向下递归实现
'''


def cut_rod(p, n):
  if n== 0:
    return 0

  q = -1 #随便取个最小值
  for i in range(1,n+1): # 遍历1~n
    q = max(q,p[i] + cut_rod(p,n-i))
  return q

def simpleTest():
  p = [0,1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

  n = 7

  value = cut_rod(p,n)
  print value

if __name__ == '__main__':
  simpleTest()
