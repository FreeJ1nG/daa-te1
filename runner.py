from merge_sort import MergeSort
from two_pivot_block_quicksort import TwoPivotBlockQuicksort


merge_sort = MergeSort()
quick_sort = TwoPivotBlockQuicksort()


case_names = [
    "testcases/small_random.txt",
    "testcases/medium_random.txt",
    "testcases/large_random.txt",
    "testcases/small_sorted.txt",
    "testcases/medium_sorted.txt",
    "testcases/large_sorted.txt",
    "testcases/small_reversed.txt",
    "testcases/medium_reversed.txt",
    "testcases/large_reversed.txt",
]


for case_name in case_names:
  f = open(case_name, "r")
  case = f.read()
  a = list(map(int, case.split()))
  print(f"Sorting {case_name} with quick sort ...")
  quick_sort.sort(a)
  print(f"Sorting {case_name} with merge sort ...")
  merge_sort.sort(a)
