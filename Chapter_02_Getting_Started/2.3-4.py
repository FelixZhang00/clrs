#!/usr/bin/env python
# coding:utf-8

'''
插入排序的递归方法
'''


# 把n位置所在元素的值插入到arr[0,n-1]
def insert(arr, n):
  key = arr[n]
  j = n - 1
  while j >= 0 and arr[j] > key:
    arr[j + 1] = arr[j]
    j -= 1
  arr[j+1] = key


def insert_sort_interal(arr, n):
  if n == 0:
    return
  insert_sort_interal(arr, n - 1)
  insert(arr, n)


def insert_sort(arr):
  insert_sort_interal(arr, len(arr) - 1)


def simpleTest():
  a = [5, 2, 4, 6, 1, 3]

  print "before sort:"
  print a
  insert_sort(a)
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
      insert_sort(arr)
      self.assertEqual(arr,sorted_arr)

if __name__ == '__main__':
  # simpleTest()
  unittest.main()
