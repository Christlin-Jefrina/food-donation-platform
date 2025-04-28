def nested_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += nested_sum(item)
        else:
            total += item
    return total

# Test cases
print(nested_sum([1, 2, [3, 4]]) == 10)
print(nested_sum([[-1, 2], [3, [4, -5]]]) == 3)
print(nested_sum([]) == 0)
