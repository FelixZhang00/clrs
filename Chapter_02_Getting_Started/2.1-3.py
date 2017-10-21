#!/usr/bin/env python
# coding:utf-8

'''
线性查找算法
'''

import random
import unittest


def linear_search(arr, v):
  for i in range(len(arr)):
    if arr[i] == v:
      return i
  return None


def simpleTest():
  a = [2, 1, 7, 8]
  v = 7
  print linear_search(a, v)


class LinearSearchTestCase(unittest.TestCase):
  def random_array(self):
    return [random.randint(0, 100) for _ in range(random.randint(1, 100))]

  def test_random(self):
    for _ in range(1000):
      arr = self.random_array()
      v = random.randint(0,200)
      findIdx = linear_search(arr,v)
      if findIdx is None:
        for val in arr:
          self.assertNotEqual(val,v)
      else:
        self.assertEqual(arr[findIdx],v)

if __name__ == '__main__':
  # simpleTest()
  unittest.main();
