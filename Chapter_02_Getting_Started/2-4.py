#!/usr/bin/env python
# coding:utf-8

'''
给出一个确定在n个元素的任何排列中逆序对数量的算法
（提示：修改归并排序）
'''

"""
将涉及的所有元素复制到一个辅助数组中，
再把归并的结果放回原数组中。
"""


def merge(arr, aux, lo, mid, hi):
  i = lo
  j = mid + 1

  Ln = mid-lo+1
  Rn = hi-mid
  ret = 0

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
      ret += mid-i+1
  return ret


def merge_sort_internal(arr, aux, lo, hi):
  if lo >= hi:
    return 0
  inversion = 0
  mid = lo + (hi - lo) / 2
  inversion += merge_sort_internal(arr, aux, lo, mid)
  inversion += merge_sort_internal(arr, aux, mid + 1, hi)
  inversion += merge(arr, aux, lo, mid, hi)
  return inversion


def merge_sort(a):
  aux = [0 for _ in a]
  inversion = merge_sort_internal(a, aux, 0, len(a) - 1)
  return inversion


def simpleTest():
  a = [2,3,8,6,1]

  print "before sort:"
  print a
  inversion = merge_sort(a)
  print "after sort:"
  print a
  print inversion


# class InsertSortTestCase(unittest.TestCase):
#   def random_array(self):
#     return [random.randint(0,100) for _ in range(random.randint(1,100))]
#
#   def test_random(self):
#     for _ in range(1000):
#       arr = self.random_array()
#       sorted_arr = sorted(arr)
#       merge_sort(arr)
#       self.assertEqual(arr,sorted_arr)

if __name__ == '__main__':
  simpleTest()

  # unittest.main()