import math
from typing import List, Dict

def initParent(length: int, first_index:int) -> List[int]:
    init: List[int] = [i for i in range(length)]
    init.remove(first_index)
    f = [first_index] + init
    return f

def matchIndex(word: str, list_of_index: List[int]) -> str:
    resutl = ""
    for idx in list_of_index:
        resutl += word[idx]
    return resutl

def permutation(word: str) -> Dict[int, List[List[int]]]:
    length = len(word)
    index_at_first_place = [str(i) for i in range(length)]
    permutations: Dict[int, List[List[int]]] = {}
    number_of_first_index = math.factorial(length-1)
    for first_index in index_at_first_place:
        first_index = int(first_index)
        at_parent: int = 0
        index_for_swap: int = length - 1
        lst_permutation_at_first_index: List[List[int]] = []
        permutations[first_index] = []
        count_permutation_per_first_index = 0
        parent_permutaion = initParent(length, first_index)
        while True:
            if count_permutation_per_first_index == number_of_first_index:
                permutations[first_index].extend(lst_permutation_at_first_index)
                break
            else:
                child_permutation: List[int] = parent_permutaion.copy()
                if child_permutation not in lst_permutation_at_first_index:
                    lst_permutation_at_first_index.append(child_permutation.copy())
                    count_permutation_per_first_index += 1
                if index_for_swap == 1:
                    index_for_swap = length - 1
                    at_parent += 1
                    parent_permutaion = lst_permutation_at_first_index[at_parent]
                    continue
                else:
                    left_value = child_permutation[index_for_swap-1]
                    right_value = child_permutation[index_for_swap]
                    child_permutation[index_for_swap] = left_value
                    child_permutation[index_for_swap-1] = right_value
                    parent_permutaion = child_permutation.copy()
                    index_for_swap -= 1
    return permutations





