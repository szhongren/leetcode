from typing import List


def get_index_of_first_greater(arr: List[int], k: int):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return 0 if arr[0] > k else -1

    def get_index_of_first_greater_recur(l: int, r: int):
        mid = (l + r) // 2
        if arr[mid] <= k and arr[mid + 1] > k:
            return mid + 1
        if l == r:
            return -1
        if arr[mid] <= k and arr[mid + 1] <= k:
            return get_index_of_first_greater_recur(mid + 1, r)
        if arr[mid] > k and arr[mid + 1] > k:
            return get_index_of_first_greater_recur(l, mid)

    return get_index_of_first_greater_recur(0, len(arr) - 2)


print(get_index_of_first_greater([1, 2, 3, 4, 5], 3))  # Should return 3
print(get_index_of_first_greater([1, 1, 1, 2, 2], 1))  # Should return 3
print(get_index_of_first_greater([5, 5, 5, 5, 5], 5))  # Should return -1
print(get_index_of_first_greater([], 1))  # Should return -1
print(get_index_of_first_greater([1], 0))  # Should return 0

"""
cases
1.
[  ]
     [  ]
2.
[  ]
  [  ]
3.
 []
[  ]
4.
  [  ]
[  ]
5.
     [  ]
[  ]
"""
