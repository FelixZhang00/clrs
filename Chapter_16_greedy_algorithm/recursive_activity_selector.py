# !/usr/bin/env python
# coding:utf-8

'''
16.1 贪心算法
它在每一步都做出当时看起来最佳的选择。它总是做出局部最优的选择，寄希望这样的选择能导致全局最优解。
递归贪心算法

活动选择问题
'''

# 输入数组s,f表示活动的开始和结束时间，下标k指出要求解的子问题，n指出问题规模
# 返回一个Sk最大兼容活动集
def recursive_activity_selector(s,f,k,n):
  m = k+1
  # find the first activity in Sk to finish
  while m<=n and s[m] < f[k]:
    m = m+1
  if m <= n:
    return [m] + recursive_activity_selector(s,f,m,n)
  else:
    return []


def simpleTest():
  # s数组存放地i个活动的开始时间
  # f数组存放地i个活动的结束时间
  # 活动按结束时间从早到晚排序好
  # 第0个元素是个虚拟元素，从0开始到0结束
  s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
  f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

  n = 11

  ret = recursive_activity_selector(s,f,0,n)

  print ret


if __name__ == '__main__':
  simpleTest()
