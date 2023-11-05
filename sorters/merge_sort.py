from sys import setrecursionlimit
from sorters.sorter import Sorter


class MergeSort(Sorter):
  def __init__(self) -> None:
    super().__init__()
    setrecursionlimit(10**7)

  def _merge(self, l: int, mid: int, r: int):
    i, j = l, mid + 1
    result = []
    while i <= mid and j <= r:
      if self.a[i] < self.a[j]:
        result.append(self.a[i])
        i += 1
      else:
        result.append(self.a[j])
        j += 1
    while i <= mid:
      result.append(self.a[i])
      i += 1
    while j <= r:
      result.append(self.a[j])
      j += 1
    for idx in range(l, r + 1):
      self.a[idx] = result[idx - l]

  def sort_algorithm(self, l: int, r: int):
    if l >= r:
      return
    mid = (l + r) // 2
    self.sort_algorithm(l, mid)
    self.sort_algorithm(mid + 1, r)
    self._merge(l, mid, r)
