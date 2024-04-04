def symmetric_difference(set1, set2):
  difference = set()

  for element in set1:
    if element not in set2:
      difference.add(element)

  for element in set2:
    if element not in set1:
      difference.add(element)

  return difference

set1 = {5, 10, 15, 20}
set2 = {10, 20, 30, 40}
symmetric_difference_set = symmetric_difference(set1, set2)
print(symmetric_difference_set)