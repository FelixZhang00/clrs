#!/usr/bin/env python
# coding:utf-8

'''
最大子数组问题的暴力求解方法
'''

import sys


def find_max_subarray(arr):
  max_sum = -sys.maxint
  left = -1
  right = -1

  # 记录前n项的和
  sums = [0]
  for a in arr:
    sums.append(sums[-1] + a)

  for i in range(0, len(arr)):
    for j in range(i, len(arr)):
      # sums[j + 1] - sums[i]即为i~j之间的总和
      if sums[j + 1] - sums[i] > max_sum:
        max_sum = sums[j + 1] - sums[i]
        left = i
        right = j
  return (left, right, max_sum)


def simpleTest():
  a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
  # a = [-13, -3, -25, -20, -3, -16, -23, -18, -20, -7, -12, -5, -22, -15, -4, -7]

  (lo, hi, sum) = find_max_subarray(a)
  print (lo, hi, sum)


if __name__ == '__main__':
  simpleTest()
