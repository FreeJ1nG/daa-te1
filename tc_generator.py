import numpy as np
from enum import Enum


SMALL_SIZE = 2 ** 9
MEDIUM_SIZE = 2 ** 13
LARGE_SIZE = 2 ** 16


class CaseType(Enum):
  SORTED = "sorted"
  RANDOM = "random"
  REVERSED = "reversed"


def write_case_to_file(filename: str, case: list[int]):
  f = open(filename, "w")
  for i in range(len(case)):
    case[i] = str(case[i])
  f.write(" ".join(case))
  f.close()


def generate_case(size: int, type: CaseType) -> list[int]:
  a = size * [None]
  for i in range(size):
    a[i] = i + 1
  if type == CaseType.RANDOM:
    a = list(np.random.permutation(a))
  elif type == CaseType.SORTED:
    pass
  elif type == CaseType.REVERSED:
    a = a[::-1]
  return a


write_case_to_file("testcases/small_random.txt",
                   generate_case(SMALL_SIZE, CaseType.RANDOM))
write_case_to_file("testcases/medium_random.txt",
                   generate_case(MEDIUM_SIZE, CaseType.RANDOM))
write_case_to_file("testcases/large_random.txt",
                   generate_case(LARGE_SIZE, CaseType.RANDOM))
write_case_to_file("testcases/small_sorted.txt",
                   generate_case(SMALL_SIZE, CaseType.SORTED))
write_case_to_file("testcases/medium_sorted.txt",
                   generate_case(MEDIUM_SIZE, CaseType.SORTED))
write_case_to_file("testcases/large_sorted.txt",
                   generate_case(LARGE_SIZE, CaseType.SORTED))
write_case_to_file("testcases/small_reversed.txt",
                   generate_case(SMALL_SIZE, CaseType.REVERSED))
write_case_to_file("testcases/medium_reversed.txt",
                   generate_case(MEDIUM_SIZE, CaseType.REVERSED))
write_case_to_file("testcases/large_reversed.txt",
                   generate_case(LARGE_SIZE, CaseType.REVERSED))
