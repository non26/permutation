from typing import List, Dict

def calNbrOfFirstIndex(length:int, choose:int) -> int:
    # assume_index = 0
    idx = [i for i in range(length, length-choose, -1)]
    multi = 1
    for i in idx:
        multi *= i
    return int(multi / length)


def removeIndex(lst: List[int], value:int):
    try:
        lst.remove(value)
    except:
        lst.pop()

def searchBeforeTargetIndex(lst: List[int], value: int) -> int:
    i: int
    try:
        i = lst.index(value)
    except:
        i = len(lst)
    return i

def initParent(length: int, first_index:int, choose:int) -> List[List[int]] :
    all: List[List[int]] = []
    init = [i for i in range(choose)]
    removeIndex(init, first_index)
    init = [first_index] + init
    increase_index = searchBeforeTargetIndex(init, length) - 1
    all.append(init.copy())
    repeat = False
    while True and choose != length:
        if max(init) < length and init not in all and not repeat:
            all.append(init.copy())
        repeat = False
        new_value = init[increase_index]
        for i in range(increase_index, choose):
            new_value = new_value + 1
            init[i] = new_value
            if len(set(init)) < choose:
                repeat = True
        increase_index = searchBeforeTargetIndex(init, length)
        if increase_index == 1:
            break
        else:
            increase_index -= 1
    return all

def permutation(word: str, choose = None) -> Dict[int, List[List[int]]]:
    length = len(word)
    choose = length if choose is None else choose
    index_at_first_place = [i for i in range(length)]
    permutations: Dict[int, List[List[int]]] = {}
    number_of_first_index = calNbrOfFirstIndex(length, choose)

    for first_index in index_at_first_place:
        lst_permutation_at_first_index: List[List[int]] = []
        permutations[first_index] = []
        at_parent: int = 0
        index_for_swap: int = choose - 1

        parent_permutation = initParent(length, first_index, choose)
        lst_permutation_at_first_index.extend(parent_permutation)
        parent_permutation = parent_permutation[at_parent]
        count_permutation_per_first_index = len(lst_permutation_at_first_index)

        child_permutation: List[int] = parent_permutation.copy()

        while True:
            if count_permutation_per_first_index == number_of_first_index:
                permutations[first_index].extend(lst_permutation_at_first_index)
                break
            else:
                if child_permutation not in lst_permutation_at_first_index:
                    lst_permutation_at_first_index.append(child_permutation.copy())
                    count_permutation_per_first_index += 1
                if index_for_swap == 1 and choose != 2:
                    index_for_swap = choose - 1
                    at_parent += 1
                    child_permutation = lst_permutation_at_first_index[at_parent].copy()
                    continue
                elif choose == 2 and child_permutation[1] == length-1:
                    break
                else:
                    left_value = child_permutation[index_for_swap-1]
                    right_value = child_permutation[index_for_swap]
                    child_permutation[index_for_swap] = left_value
                    child_permutation[index_for_swap-1] = right_value
                    index_for_swap -= 1
    return permutations