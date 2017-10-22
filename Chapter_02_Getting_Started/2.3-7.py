#!/usr/bin/env python
# coding:utf-8

'''
Tow Sum
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

def two_sum(arr,x):
  sored_arr = sorted(arr)
  for item in sored_arr:
    val = x-item
    find = binary_search(sored_arr,val)
    if find != None:
      return (item,arr[find])
  return None

def simpleTest():
  a = [2, 1, 7, 8]
  v = 15
  print two_sum(a,v)

# class TwoSumTestCase(unittest.TestCase):
#   def random_array(self):
#     return [random.randint(0, 100) for _ in range(random.randint(1, 100))]
#
#   def test_random(self):
#     for _ in range(1000):
#       arr = self.random_array()
#       sorted_arr = sorted(arr)
#       sorted_arr.reverse()
#       insertion_sort(arr)
#       self.assertEqual(arr, sorted_arr)


if __name__ == '__main__':
  simpleTest()
  # unittest.main();
