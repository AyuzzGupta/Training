list1 = [101, 102, 103, 104, 105]
list2 = [104, 105, 106, 107, 108]

print("List 1:", list1)
print("List 2:", list2)

merged = list1 + list2

no_dup = list(set(merged))

print("Merged list without duplicates:", no_dup)
