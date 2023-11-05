from sorters.merge_sort import MergeSort
from sorters.two_pivot_block_quicksort import TwoPivotBlockQuicksort


merge_sort = MergeSort()
quick_sort = TwoPivotBlockQuicksort()


case_names = [
    "small_random.txt",
    "small_sorted.txt",
    "small_reversed.txt",
    "medium_random.txt",
    "medium_sorted.txt",
    "medium_reversed.txt",
    "large_random.txt",
    "large_sorted.txt",
    "large_reversed.txt",
]


for case_name in case_names:
  f = open(f"testcases/{case_name}", "r")
  case = f.read()
  f.close()
  w = open(f"results/{case_name}", "w")
  a = list(map(int, case.split()))
  print(f"Sorting {case_name} with quick sort ...")
  t = quick_sort.sort(a)
  lines = [
      f"Finished sorting {case_name} in {t} seconds with quick sort\n",
      f"Final result: {quick_sort.get_array()}\n",
      "======================================================================\n\n",
  ]
  w.writelines(lines)
  print(f"Sorting {case_name} with merge sort ...")
  t = merge_sort.sort(a)
  lines = [
      f"Finished sorting {case_name} in {t} seconds with merge sort\n",
      f"Final result: {merge_sort.get_array()}\n",
      "======================================================================\n",
  ]
  w.writelines(lines)
  w.close()
