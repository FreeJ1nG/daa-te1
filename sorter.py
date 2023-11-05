from abc import ABC, abstractmethod

import time


class Sorter(ABC):
  def __init__(self) -> None:
    self.a = []

  def sort(self, a: list[int]):
    self.a = a
    start_time = time.time()
    self.sort_algorithm(0, len(self.a) - 1)
    print(f"finished sorting in {time.time() - start_time} seconds")

  @abstractmethod
  def sort_algorithm(self, l: int, r: int):
    pass
