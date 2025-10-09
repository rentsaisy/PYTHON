# # # def is_valid_partition(original_set, partitions):
# # #     combined = set()
# # #     for part in partitions:
# # #         combined.update(part)

# # #     if combined == original_set and all(len(part) > 0 for part in partitions):
# # #         return True, f"Benar, ini Merupakan Partisi"
# # #     return False

# # # original_set = {'Alya', 'Budi', 'Chandra', 'Deny', 'Eka', 'Farhan'}
# # # partitions = [{'Alya', 'Budi'}, {'Chandra', 'Deny'}, {'Eka', 'Farhan'}]

# # # print(is_valid_partition(original_set, partitions))

# # def verify_proposition(A, B):
# #     union_result = A.union(B)
# #     intersection_result = A.intersection(union_result)
# #     return intersection_result == A

# # A = {1, 2, 3}
# # B = {3, 4, 5}

# # print(verify_proposition(A, B))

# from collections import Counter

# def multiset_count(elements):
#     count = Counter(elements)
#     return count

# students = ['Alya', 'Alya', 'Budi', 'Deny', 'Deny', 'Deny']
# print(multiset_count(students))

def fuzzy_union(fuzzy_set_a, fuzzy_set_b):
    return {k: max(fuzzy_set_a.get(k, 0), fuzzy_set_b.get(k, 0)) for k in set(fuzzy_set_a) | set(fuzzy_set_b)}

def fuzzy_intersection(fuzzy_set_a, fuzzy_set_b):
    return {k: min(fuzzy_set_a.get(k, 0), fuzzy_set_b.get(k, 0)) for k in set(fuzzy_set_a) & set(fuzzy_set_b)}

def fuzzy_complement(fuzzy_set):
    return {k: 1 - v for k, v in fuzzy_set.items()}

fuzzy_matkom = {'Deny': 0.7, 'Budi': 0.5, 'Chandra': 0.9}
fuzzy_strukdat = {'Deny': 0.6, 'Budi': 0.8, 'Chandra': 0.4}

union_result = fuzzy_union(fuzzy_matkom, fuzzy_strukdat)
intersection_result = fuzzy_intersection(fuzzy_matkom, fuzzy_strukdat)
complement_result = fuzzy_complement(fuzzy_matkom)

print(f"Union Fuzzy: {union_result}")
print(f"Intersection Fuzzy: {intersection_result}")
print(f"Complement Fuzzy Matkom: {complement_result}")
