#Given an array of integers.

#Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

#If the input array is empty or null, return an empty array.

def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [pos, neg]