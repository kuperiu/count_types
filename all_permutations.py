#!/usr/bin/env python
import sys

'''
print all the possible permutations of a string in a length lexicographic order

./all_permutations.py abc will output "a b c ab ac bc abc"
'''
def all_permutations(str):
    res = []
    length = len(str)
    if length == 1:
        return str
    else:
        for i in reversed(xrange(length)):
            sub_arr = all_permutations(str[:i]+str[i+1:])
            for j in sub_arr:
                res.append(j)
        res.append(str)
    return list(set(res))

str = sys.argv[1]
res = sorted(sorted(all_permutations(str)),key=len)
print " ".join(res)
