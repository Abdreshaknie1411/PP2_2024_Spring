from itertools import permutations
def print_permut(string):
    all_permutation=permutations(string)
    for perm in all_permutation:
        print(''.join(perm))
user_input=input()
print_permut(user_input)
