import time
from abc import ABC, abstractmethod


class Sorter(ABC):
  def __init__(self) -> None:
    self.a = []

  def get_array(self) -> list[int]:
    return self.a

  def sort(self, a: list[int]) -> float:
    self.a = a
    start_time = time.time()
    self.sort_algorithm(0, len(self.a) - 1)
    return time.time() - start_time

  @abstractmethod
  def sort_algorithm(self, l: int, r: int):
    pass
