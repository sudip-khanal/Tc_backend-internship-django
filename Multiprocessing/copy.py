import copy

original_list = [1, 2, [3, 4]]

# Create a shallow copy
shallow_copied_list = copy.copy(original_list)

# Modify the nested list in the shallow copy
shallow_copied_list[2][0] = 'changed'

print("Original list:", original_list)
print("Shallow copied list:", shallow_copied_list)


# list = [1, 2, [3, 4]]

# # Create a deep copy
# deep_copied_list =copy.deepcopy(list)

# # Modify the nested list in the deep copy
# deep_copied_list[2][0] = 1000

# print("Original list:", list)
# print("Deep copied list:", deep_copied_list)
