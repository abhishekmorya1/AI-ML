# input two list

list1 = list(map(int,input("Enter first list Elements: ").split()))
list2 = list(map(int, input("Enter second list Elements: ").split()))

merged_list = list1 + list2
merged_list.sort()

print("Sorted Merged List:", merged_list)