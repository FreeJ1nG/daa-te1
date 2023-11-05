from sys import setrecursionlimit
from sorters.sorter import Sorter


class TwoPivotBlockQuicksort(Sorter):
  def __init__(self) -> None:
    super().__init__()
    setrecursionlimit(10**7)
    self.B = 128

  def _swap_values(self, i: int, j: int):
    self.a[i], self.a[j] = self.a[j], self.a[i]

  def _double_pivot_block_lomuto(self, a: list[int]):
    n = len(a)
    if n <= 1:
      return
    p, q = a[0], a[-1]
    block = self.B * [None]
    i, j, k = 1, 1, 1
    num_p, num_q = 0, 0
    while k < n - 1:
      t = min(self.B, n - k - 1)
      for c in range(t):
        block[num_q] = c
        num_q = num_q + (q >= a[k + c])
      for c in range(num_q):
        self._swap_values(j + c, k + block[c])
      k += t
      for c in range(num_q):
        block[num_p] = c
        num_p = num_p + (p > a[j + c])
      for c in range(num_p):
        self._swap_values(i, j + block[c])
        i += 1
      j += num_q
      num_p, num_q = 0, 0
    self._swap_values(0, i - 1)
    self._swap_values(j, n - 1)
    return (i - 1, j)

  def sort_algorithm(self, l: int, r: int):
    if l >= r:
      return
    if (self.a[l] > self.a[r]):
      self._swap_values(l, r)
    i, j = self._double_pivot_block_lomuto(self.a[l: r + 1])
    i += l
    j += l
    if l <= i - 1:
      self.sort_algorithm(l, i - 1)
    if i + 1 <= j - 1:
      self.sort_algorithm(i + 1, j - 1)
    if j + 1 <= r:
      self.sort_algorithm(j + 1, r)
