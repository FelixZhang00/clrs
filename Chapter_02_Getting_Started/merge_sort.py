#!/usr/bin/env python
# coding:utf-8

'''
归并排序

'''

import random
import unittest

"""
将涉及的所有元素复制到一个辅助数组中，
再把归并的结果放回原数组中。
"""


def merge(arr, aux, lo, mid, hi):
  i = lo
  j = mid + 1
  for k in range(lo, hi + 1):
    aux[k] = arr[k]

  for k in range(lo, hi + 1):
    if i > mid:
      arr[k] = aux[j]
      j += 1
    elif j > hi:
      arr[k] = aux[i]
      i += 1
    elif aux[i] < aux[j]:
      arr[k] = aux[i]
      i += 1
    else:
      arr[k] = aux[j]
      j += 1


def merge_sort_internal(arr, aux, lo, hi):
  if lo >= hi:
    return
  mid = lo + (hi - lo) / 2
  merge_sort_internal(arr, aux, lo, mid)
  merge_sort_internal(arr, aux, mid + 1, hi)
  merge(arr, aux, lo, mid, hi)


def merge_sort(a):
  aux = [0 for _ in a]
  merge_sort_internal(a, aux, 0, len(a) - 1)


def simpleTest():
  a = [5, 2, 4, 6, 1, 3]

  print "before sort:"
  print a
  merge_sort(a)
  print "after sort:"
  print a


class InsertSortTestCase(unittest.TestCase):
  def random_array(self):
    return [random.randint(0,100) for _ in range(random.randint(1,100))]

  def test_random(self):
    for _ in range(1000):
      arr = self.random_array()
      sorted_arr = sorted(arr)
      merge_sort(arr)
      self.assertEqual(arr,sorted_arr)

if __name__ == '__main__':
  # simpleTest()

  unittest.main()
