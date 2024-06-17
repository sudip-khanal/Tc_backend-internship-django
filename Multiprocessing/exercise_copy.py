import copy
li1 = [1, 2, [3, 5], 4]
li2 = copy.copy(li1)
print("li1 ID: ", id(li2), "Value: ", li1)
print("li2 ID: ", id(li2), "Value: ", li2)
li3 = copy.deepcopy(li1)
print("li3 ID: ", id(li3), "Value: ", li3)

# original_list = [1, 2, [3, 4]]

# # Create a shallow copy
# shallow_copied_list = copy.copy(original_list)

# # Modify the nested list in the shallow copy
# shallow_copied_list[2][0] = 'changed'

# print("Original list:", original_list)
# print("Shallow copied list:", shallow_copied_list)


# # list = [1, 2, [3, 4]]

# # # Create a deep copy
# # deep_copied_list =copy.deepcopy(list)

# # # Modify the nested list in the deep copy
# # deep_copied_list[2][0] = 1000

# # print("Original list:", list)
# # print("Deep copied list:", deep_copied_list)

