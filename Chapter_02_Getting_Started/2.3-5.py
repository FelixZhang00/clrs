#!/usr/bin/env python
# coding:utf-8

'''
二分查找法
'''

import random
import unittest


def binary_search(arr, v):
  n = len(arr)
  lo=0
  hi=n-1

  while lo<=hi:
    mid = lo + (hi - lo) / 2
    if arr[mid]<v:
      lo = mid+1
    elif arr[mid]>v:
      hi = mid-1
    else:
      return mid

  return None


def simpleTest():
  a = sorted([2, 1, 7, 8])
  v = 7
  print binary_search(a, v)


class LinearSearchTestCase(unittest.TestCase):
  def random_array(self):
    return [random.randint(0, 100) for _ in range(random.randint(1, 100))]

  def test_random(self):
    for _ in range(1000):
      arr = sorted(self.random_array())
      v = random.randint(0,200)
      findIdx = binary_search(arr,v)
      if findIdx is None:
        for val in arr:
          self.assertNotEqual(val,v)
      else:
        self.assertEqual(arr[findIdx],v)

if __name__ == '__main__':
  # simpleTest()
  unittest.main();