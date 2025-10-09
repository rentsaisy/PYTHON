# # # def is_valid_partition(original_set, partitions):
# # #     combined = set()
# # #     for part in partitions:
# # #         combined.update(part)

# # #     if combined == original_set and all(len(part) > 0 for part in partitions):
# # #         return True
# # #     return False

# # # original_set = {'Adam', 'Bella', 'Charlie', 'Deny', 'Eko', 'Farid'}
# # # partitions = [{'Adam', 'Bella', 'Charlie'}, {'Deny', 'Eko', 'Farid'}]
# # # print(is_valid_partition(original_set, partitions))

# # def verify_proposition(A, B):
# #     union_result = A.union(B)
# #     intersection_result = A.intersection(union_result)
# #     return intersection_result == A

# # A = {2, 4, 6}
# # B = {4, 6, 8}
# # print(verify_proposition(A, B))

# from collections import Counter

# def multiset_count(elements):
#     count = Counter(elements)
#     return count

# food_orders = ['Nasi Goreng', 'Nasi Goreng', 'Sate', 'Sate', 'Sate', 'Soto']
# print(multiset_count(food_orders))

def fuzzy_union(fuzzy_set_a, fuzzy_set_b):
    return {k: max(fuzzy_set_a.get(k, 0), fuzzy_set_b.get(k, 0)) for k in set(fuzzy_set_a) | set(fuzzy_set_b)}

def fuzzy_intersection(fuzzy_set_a, fuzzy_set_b):
    return {k: min(fuzzy_set_a.get(k, 0), fuzzy_set_b.get(k, 0)) for k in set(fuzzy_set_a) & set(fuzzy_set_b)}

def fuzzy_complement(fuzzy_set):
    return {k: 1 - v for k, v in fuzzy_set.items()}

fuzzy_math = {'Edo': 0.9, 'Rina': 0.7, 'Tari': 0.8}
fuzzy_physics = {'Edo': 0.6, 'Rina': 0.9, 'Tari': 0.5}

union_result = fuzzy_union(fuzzy_math, fuzzy_physics)
intersection_result = fuzzy_intersection(fuzzy_math, fuzzy_physics)
complement_result = fuzzy_complement(fuzzy_math)

print(f"Union Fuzzy: {union_result}")
print(f"Intersection Fuzzy: {intersection_result}")
print(f"Complement Fuzzy Matematika: {complement_result}")
