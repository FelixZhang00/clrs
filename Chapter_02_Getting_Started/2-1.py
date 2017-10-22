#!/usr/bin/env python
# coding:utf-8

'''
混合归并排序和插入排序
'''

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


def insertion_sort(a, lo, hi):
  for i in range(lo + 1, hi + 1):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
      a[j + 1] = a[j]
      j -= 1
    a[j + 1] = key


def mix_sort_internal(arr, aux, lo, hi):
  if lo >= hi:
    return
  # k = 20
  if hi - lo > 20:
    insertion_sort(arr, lo, hi)
  else:
    mid = lo + (hi - lo) / 2
    mix_sort_internal(arr, aux, lo, mid)
    mix_sort_internal(arr, aux, mid + 1, hi)
    merge(arr, aux, lo, mid, hi)


def mix_sort(arr):
  aux = [0 for _ in arr]
  mix_sort_internal(arr, aux, 0, len(arr) - 1)


import random
import unittest

def simpleTest():
  a = [5, 2, 4, 6, 1, 3]

  print "before sort:"
  print a
  mix_sort(a)
  print "after sort:"
  print a


class InsertSortTestCase(unittest.TestCase):
  def random_array(self):
    return [random.randint(0,100) for _ in range(random.randint(1,100))]

  def test_random(self):
    for _ in range(1000):
      arr = self.random_array()
      sorted_arr = sorted(arr)
      mix_sort(arr)
      self.assertEqual(arr,sorted_arr)

if __name__ == '__main__':
  # simpleTest()

  unittest.main()