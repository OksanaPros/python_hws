"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are
    such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(
    a: List[int],
    b: List[int],
    c: List[int],
    d: List[int],
) -> int:
    ab = list()
    cd = list()
    for index_a, item_a in enumerate(a):
        for index_b, item_b in enumerate(b):
            ab.append(item_a + item_b)

    for index_c, item_c in enumerate(c):
        for index_d, item_d in enumerate(d):
            cd.append(item_c + item_d)

    result = 0
    for item_ab in ab:
        for item_cd in cd:
            if (item_ab + item_cd) == 0:
                result += 1
    return result


print(check_sum_of_four([5, 6], [1, 2], [3, 4], [-9, -12]))
