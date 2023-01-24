# https://practice.geeksforgeeks.org/problems/binary-search-1587115620/1

def binary_search(n, arr, k) -> int:
  low = 0
  high = n - 1

  while low <= high:
    middle = (low + high) // 2

    if arr[middle] == k:
      return middle

    elif arr[middle] < k:
      low = middle + 1

    elif arr[middle] > k:
      high = middle - 1

  return -1

if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().strip().split(' ')))
  k = int(input())
  print(binary_search(n, arr, k))


# input example
# 60
# 2 4 5 7 9 11 14 15 20 22 23 24 25 26 27 28 32 33 36 37 39 41 42 43 44 45 47 48 49 50 51 53 54 55 57 59 60 61 62 63 66 67 68 69 70 71 72 73 74 76 78 86 87 89 91 93 94 95 97 100
# 1
#-------------
# 62
# 1 2 3 7 8 9 11 12 13 14 16 17 18 19 23 24 26 28 30 31 32 33 34 36 37 38 39 40 44 45 46 47 52 56 57 59 60 61 62 63 64 65 68 69 70 72 73 74 76 79 80 81 82 84 89 90 93 95 96 97 99 100
# 16 
