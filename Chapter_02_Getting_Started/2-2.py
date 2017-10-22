#!/usr/bin/env python
# coding:utf-8

'''
冒泡排序：
反复交换相邻的未按次序排列的元素
'''


def exch(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp


def bubble_sort(arr):
  for i in range(0, len(arr) - 1):
    # 反向遍历数组
    for j in range(i + 1, len(arr))[::-1]:
      if arr[j] < arr[j - 1]:
        exch(arr, j, j - 1)


def simpleTest():
  a = [5, 2, 4, 6, 1, 3]

  print "before sort:"
  print a
  bubble_sort(a)
  print "after sort:"
  print a

import random
import unittest

class InsertSortTestCase(unittest.TestCase):
  def random_array(self):
    return [random.randint(0,100) for _ in range(random.randint(1,100))]

  def test_random(self):
    for _ in range(1000):
      arr = self.random_array()
      sorted_arr = sorted(arr)
      bubble_sort(arr)
      self.assertEqual(arr,sorted_arr)

if __name__ == '__main__':
  # simpleTest()

  unittest.main()
