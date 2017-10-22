#!/usr/bin/env python
# coding:utf-8

'''
最大子数组：
线性时间
从数组的左边开始，由左至右处理，记录到目前为止已经处理过的最大子数组。
'''

import sys


def find_max_subarray(arr):
  max_sum = -sys.maxint
  max_left, max_right = -1, -1
  sum = 0
  last_left = 0
  for i in range(len(arr)):
    sum += arr[i]
    if sum > max_sum:
      max_sum = sum
      max_left = last_left
      max_right = i
    if sum < 0:
      sum = 0
      last_left = i + 1

  return (max_left, max_right, max_sum)


def simpleTest():
  a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
  # a = [-13, -3, -25, -20, -3, -16, -23, -18, -20, -7, -12, -5, -22, -15, -4, -7]

  # a = []

  (lo, hi, sum) = find_max_subarray(a)
  print (lo, hi, sum)


if __name__ == '__main__':
  simpleTest()
