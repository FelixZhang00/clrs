#!/usr/bin/env python
# coding:utf-8

'''
计算mxn的Monge阵列A每一行最左最小元素的分治算法
TODO
'''

import sys


def get_min_index_array(arr):
  pass


def get_min_index(arr):
  def get_min_index_rec(idx):
    if len(idx) == 1:
      min_idx = 0
      for j in range(1, len(arr[0])):
        if arr[idx[0]][j] < arr[idx[0]][min_idx]:
          min_idx = j
      return [min_idx]
    sub_idx = [idx[i] for i in range(len(idx)) if i % 2 == 0]
    sub_min_idx = get_min_index_rec(sub_idx)
    sub_min_idx.append(len(arr[0]) - 1)
    min_idx = [sub_min_idx[i // 2] for i in range(len(idx))]
    for i in range(1, len(idx), 2):
      for j in range(sub_min_idx[i // 2] + 1, sub_min_idx[i // 2 + 1] + 1):
        if arr[idx[i]][j] < arr[idx[i]][min_idx[i]]:
          min_idx[i] = j
    return min_idx

  return get_min_index_rec([i for i in range(len(arr))])






def mergeindex(items, evens):
  res = []
  l = len(items[0])
  for i in range(len(items)):
    left = evens[i]
    right = -1
    if i == len(items) - 1 and len(evens) == len(items):
      right = l - 1
    else:
      right = evens[i + 1]

    minimum = items[i][left]
    pos = left
    for j in range(left, right + 1):
      if items[i][j] < minimum:
        minimum = items[i][j]
        pos = j
    res.append(evens[i])
    res.append(pos)

  if len(evens) > len(items):
    res.append(evens[-1])
  return res


def findindex(items):
  if len(items) == 1:
    res = 0
    minimum = sys.maxint
    for i in range(len(items[0])):
      if items[0][i] < minimum:
        minimum = items[0][i]
        res = i
    return [res]

  evens = items[::2]
  evenres = findindex(evens)
  res = mergeindex(items[1::2], evenres)
  return res


def simpleTest():
  arr = [[10, 17, 13, 28, 23],
         [17, 22, 16, 29, 23],
         [24, 28, 22, 34, 24],
         [11, 13, 6, 17, 7],
         [45, 44, 32, 37, 23],
         [36, 33, 19, 21, 6],
         [75, 66, 51, 53, 34]]

  # result shoud be [0, 2, 2, 2, 4, 4, 4]
  result = get_min_index(arr)

  print result

  items = [[37, 23, 24, 32], [21, 6, 7, 10], [53, 34, 30, 31], [32, 13, 9, 6], [43, 21, 15, 8]]

  print findindex(arr)


if __name__ == '__main__':
  simpleTest()
