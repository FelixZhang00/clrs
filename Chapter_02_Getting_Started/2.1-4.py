#!/usr/bin/env python
# coding:utf-8

'''
两个n位二进制整数相加的问题。
两个整数分别存储在两个n元数组A和B，这两个整数的和应按二进制形式存储在一个n+1元数组C中
这里假设以小端字节序存储，即高位数字在内存的低地址，所以做了几次翻转。
'''


def add_binary(a, b):
  n = len(a)
  c = [0 for _ in range(n)]

  local_a = [item for item in a]
  local_b = [item for item in b]
  local_a.reverse()
  local_b.reverse()

  carry = 0
  for i in range(n):
    val = local_a[i] + local_b[i] + carry

    if val == 3:
      carry = 1
      val = 1
    elif val > 1:
      carry = 1
      val = 0
    else:
      carry = 0

    c[i] = val

  if carry > 0:
    c.append(carry)
  c.reverse()
  return c


def simpleTest():
  a = [1, 0, 1, 1]
  b = [0, 0, 0, 1]

  a = [1, 0, 1]
  b = [1, 1, 1]

  c = add_binary(a, b)
  print c


if __name__ == '__main__':
  simpleTest()
