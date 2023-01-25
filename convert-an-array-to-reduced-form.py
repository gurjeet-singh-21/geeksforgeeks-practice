# Convert an array to reduced form
##################################
# Input:
# N = 3
# Arr[] = {10, 40, 20}
# Output: 0 2 1
# Explanation: 10 is the least element so it
# is replaced by 0. 40 is the largest
# element so it is replaced by 3-1 = 2. And
# 20 is the 2nd smallest element so it is
# replaced by 1.
# 
# Input:
# N = 5
# Arr[] = {5, 10, 40, 30, 20}
# Output: 0 1 4 3 2
# Explanation: As 5 is smallest element,
# it's replaced by 0. Then 10 is 2nd
# smallest element, so it's replaced by 1.
# Then 20 is 3rd smallest element, so it's
# replaced by 2. And so on.
############################################
# in place change the array not return it.

def convert(self,arr, n):

    d = dict()
    arr1 = sorted(arr)
    for i, j in enumerate(arr1):
        d[j] = i

    for i in range(n):

        arr[i] = d[arr[i]]
    return arr


