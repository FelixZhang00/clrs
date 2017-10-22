#!/usr/bin/env python
# coding:utf-8

'''
4.1 最大子数组问题

'''

import sys


# 返回一个下标元组划定跨越中点的最大子数组的边界，并返回最大子数组中值的和
def find_max_crossing_subarray(arr, lo, mid, hi):
  left_sum = -sys.maxint
  sum = 0
  for i in range(lo, mid + 1)[::-1]:
    sum += arr[i]
    if sum > left_sum:
      left_sum = sum
      max_left = i

  right_sum = -sys.maxint
  sum = 0
  for i in range(mid + 1, hi + 1):
    sum += arr[i]
    if sum > right_sum:
      right_sum = sum
      max_right = i

  return (max_left, max_right, left_sum + right_sum)


'''
# 返回一个下标元组，划定了最大子数组的边界，同时返回最大数组中的值之和
'''


def find_max_subarray(arr, lo, hi):
  if lo >= hi:
    return (lo, hi, arr[lo])
  else:
    mid = lo + (hi - lo) / 2
    (left_low, left_hight, left_sum) = find_max_subarray(arr, lo, mid)
    (right_low, right_hight, right_sum) = find_max_subarray(arr, mid + 1, hi)
    (cross_low, cross_hight, cross_sum) = find_max_crossing_subarray(arr, lo, mid, hi)

    if left_sum >= right_sum and left_sum >= cross_sum:
      return (left_low, left_hight, left_sum)
    if right_sum >= left_sum and right_sum >= cross_sum:
      return (right_low, right_hight, right_sum)
    if cross_sum >= left_sum and cross_sum >= left_sum:
      return (cross_low, cross_hight, cross_sum)


def simpleTest():
  a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

  (lo,hi,sum) = find_max_subarray(a, 0, len(a) - 1)
  print (lo,hi,sum)


if __name__ == '__main__':
  simpleTest()
