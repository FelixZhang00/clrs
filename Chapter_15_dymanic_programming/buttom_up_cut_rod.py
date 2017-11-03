#!/usr/bin/env python
# coding:utf-8

'''
15.1 钢条切割
自底向上
每个子问题只需要求解一次，当我们求解它（也是第一次遇到它）时，它的所有前提子问题都已求解完成。
'''

def bottom_up_cut_rod(p, n):
  aux = [] # 新数组用来保存子问题的解
  for i in range(0,n+1):
    aux.append(0)

  for j in range(1,n+1): # 1~n
    q = -1
    for i in range(1,j+1):
      q = max(q,p[i]+aux[j-i]) #直接访问数组来获得子问题的解
    aux[j] = q

  return aux[n]




def simpleTest():
  p = [0,1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

  n = 7

  value = bottom_up_cut_rod(p,n)
  print value

if __name__ == '__main__':
  simpleTest()