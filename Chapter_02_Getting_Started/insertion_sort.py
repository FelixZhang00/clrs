import random
import unittest


def insertion_sort(a):
  for i in range(1, len(a)):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
      a[j + 1] = a[j]
      j -= 1
    a[j + 1] = key


def simpleTest():
  a = [5, 2, 4, 6, 1, 3]

  print "before sort:"
  print a
  insertion_sort(a)
  print "after sort:"
  print a

class InsertSortTestCase(unittest.TestCase):
  def random_array(self):
    return [random.randint(0,100) for _ in range(random.randint(1,100))]

  def test_random(self):
    for _ in range(1000):
      arr = self.random_array()
      sorted_arr = sorted(arr)
      insertion_sort(arr)
      self.assertEqual(arr,sorted_arr)

if __name__ == '__main__':
  # simpleTest()

  unittest.main()