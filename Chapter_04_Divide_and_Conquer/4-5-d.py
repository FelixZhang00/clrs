#!/usr/bin/env python
# coding:utf-8

'''
假定超过n/2块芯片是好的，证明可以用O(n)次逐对检测找出一块好的芯片

将芯片两两配对，对于后三种情况（至少其中一个是坏的），可以直接将该对芯片丢弃，这样丢弃的好的一定不会超过坏的。
剩下的都是第一种情况，以及可能剩下的单个未配对的。
如果数量为偶数，即没有未配对的，那么“好好”对数一定超过“坏坏”对数，所以每对里面丢弃一个即可。
如果数量为奇数，则保留那个未配对的，并且每对丢掉一个。
'''

import unittest
import random


class Chip:
  def __init__(self, _state):
    self.state = _state

  def __str__(self):
    return '[state:' + str(self.state) + ']'

  def check(self, other):
    if self.state:
      return other.state
    else:
      return random.randint(0, 1)


def check(chip_a, chip_b):
  return chip_a.check(chip_b) and chip_b.check(chip_a)


def choose_good_chip(chips):
  if len(chips) == 1:
    return chips[0]

  mid = len(chips) / 2
  next_chips = []
  for i in range(mid):
    if check(chips[i], chips[mid + i]):
      next_chips.append(chips[i])
      # next_chips.append(chips[mid + i])
  if len(chips) % 2 == 1 and len(next_chips) % 2 == 0:
    next_chips.append(chips[-1])
  return choose_good_chip(next_chips)


class VerifyChipTestCase(unittest.TestCase):
  def random_chips(self):
    chips_num = random.randint(1, 100)
    good_num = chips_num / 2 + 1  # 使超过n/2块芯片是好的
    bad_num = chips_num - good_num
    good_chips = [Chip(True) for _ in range(good_num)]
    bad_chips = [Chip(False) for _ in range(bad_num)]
    chips = good_chips + bad_chips
    random.shuffle(chips)  # 打乱处理
    return chips

  def test_random(self):
    for _ in range(1000):
      chips = self.random_chips()
      # for item in chips:
      #   print item
      good_chip = choose_good_chip(chips)
      self.assertTrue(good_chip.state)


if __name__ == '__main__':
  unittest.main()
