#!/usr/bin/env python
# coding:utf-8

'''
选择排序算法：
①：找出数组A中最小元素并将其与A[0]交换；
②：找出数组A中次小元素并将其与A[1]交换；
③：对A中前n-1个元素按该方式继续
'''

import sys
import random
import unittest

def find_min(a,_start,_end):
  min = sys.maxint
  ret = None
  for i in range(_start,_end):
    if a[i] < min:
      min = a[i]
      ret = i
  return ret

def select_sort(a):
  n = len(a)
  for i in range(0,n-1):
    min_idx = find_min(a,i,n)
    min = a[min_idx]
    a[min_idx] = a[i]
    a[i] = min


def simpleTest():
  a = [5, 2, 4, 6, 1, 3]

  print "before sort:"
  print a
  select_sort(a)
  print "after sort:"
  print a


class InsertSortTestCase(unittest.TestCase):
  def random_array(self):
    return [random.randint(0, 100) for _ in range(random.randint(1, 100))]

  def test_random(self):
    for _ in range(1000):
      arr = self.random_array()
      sorted_arr = sorted(arr)
      # sorted_arr.reverse()
      select_sort(arr)
      self.assertEqual(arr, sorted_arr)

if __name__ == '__main__':
  # simpleTest()
  unittest.main();