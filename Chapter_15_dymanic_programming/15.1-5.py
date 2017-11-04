#!/usr/bin/env python
# coding:utf-8

'''
15.1-5 求第n个斐波那契数列数
0,1,1,2,3,5,8,13,21,34,55,...

自底向上
每个子问题只需要求解一次，当我们求解它（也是第一次遇到它）时，它的所有前提子问题都已求解完成。
'''


def fb_sub(n,a):
  if n < len(a):
    return a[n]

  a.append(fb_sub(n-1,a)+fb_sub(n-2,a))
  return a[n]

def fb(n):
  a = [0,1]

  return fb_sub(n,a)


def simpleTest():
  n = 10
  value = fb(n)
  print value

if __name__ == '__main__':
  simpleTest()