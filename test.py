from main import *
import unittest
from typing import List, Tuple

class TestPermutation(unittest.TestCase):
    def test_calNbrOfFirstIndex(self):
        # calNbrOfFirstIndex(length:int, choose:int)

        self.assertEqual(calNbrOfFirstIndex(4,1), 1)
        self.assertEqual(calNbrOfFirstIndex(4,2), 3)
        self.assertEqual(calNbrOfFirstIndex(4,3), 6)
        self.assertEqual(calNbrOfFirstIndex(4,4), 6)

    def test_removeIndex(self):
        # removeIndex(lst: List[int], value:int)

        lst = [0,1,2,3,4,5]
        value = 4
        actual = [0,1,2,3,5]
        removeIndex(lst, value)
        self.assertEqual(actual, lst)

        lst = [0,1,2,3,4,5]
        value = 6
        actual = [0,1,2,3,4]
        removeIndex(lst, value)
        self.assertEqual(actual, lst)

        lst = [0, 1, 2, 3, 4, 5]
        value = 0
        actual = [1,2,3,4,5]
        removeIndex(lst, value)
        self.assertEqual(actual, lst)

    def test_searchBeforeTargetIndex(self):
        # searchBeforeTargetIndex(lst: List[int], value: int)

        lst = [1,2,3,4,5]
        value = 3
        actual = 2
        self.assertEqual(searchBeforeTargetIndex(lst, value), actual)

        lst = [1,2,3,4,5]
        value = 7
        actual = 5
        self.assertEqual(searchBeforeTargetIndex(lst, value), actual)

        lst = [1,2,5,4,3]
        value = 5
        actual = 2
        self.assertEqual(searchBeforeTargetIndex(lst, value), actual)

    def test_initParent(self):
        # initParent(length: int, first_index:int, choose:int)

        length = 5
        first_index = 0
        choose = 1
        expected = initParent(length, first_index,choose)
        expected_len = len(expected)
        actual = [
                [0]
            ]
        actual_len = len(actual)
        self.assertEqual(actual, expected)
        self.assertEqual(actual_len, expected_len)

        length = 5
        first_index = 0
        choose = 2
        expected = initParent(length, first_index,choose)
        expected_len = len(expected)
        actual = [
                [0,1],
                [0,2],
                [0,3],
                [0,4],
            ]
        actual_len = len(actual)
        self.assertEqual(actual, expected)
        self.assertEqual(actual_len, expected_len)

        length = 5
        first_index = 0
        choose = 3
        expected = initParent(length, first_index,choose)
        expected_len = len(expected)
        actual = [
                [0,1,2],
                [0,1,3],
                [0,1,4],
                [0,2,3],
                [0,2,4],
                [0,3,4],
            ]
        actual_len = len(actual)
        self.assertEqual(actual, expected)
        self.assertEqual(actual_len, expected_len)

        length = 5
        first_index = 0
        choose = 4
        expected = initParent(length, first_index,choose)
        expected_len = len(expected)
        actual = [
                [0,1,2,3],
                [0,1,2,4],
                [0,1,3,4],
                [0,2,3,4]
            ]
        actual_len = len(actual)
        self.assertEqual(actual, expected)
        self.assertEqual(actual_len, expected_len)

        length = 5
        first_index = 0
        choose = 5
        expected = initParent(length, first_index,choose)
        expected_len = len(expected)
        actual =[
                [0,1,2,3,4]
            ]
        actual_len = len(actual)
        self.assertEqual(actual, expected)
        self.assertEqual(actual_len, expected_len)

        length = 5
        first_index = 1
        choose = 2
        expected = initParent(length, first_index,choose)
        expected_len = len(expected)
        actual = [
                [1,0],
                [1,2],
                [1,3],
                [1,4]
            ]
        actual_len = len(actual)
        self.assertEqual(actual, expected)
        self.assertEqual(actual_len, expected_len)

        length = 5
        first_index = 2
        choose = 2
        expected = initParent(length, first_index, choose)
        expected_len = len(expected)
        actual = [
                [2,0],
                [2,1],
                [2,3],
                [2,4]
            ]
        actual_len = len(actual)
        self.assertEqual(actual, expected)
        self.assertEqual(actual_len, expected_len)

        length = 5
        first_index = 3
        choose = 2
        expected = initParent(length, first_index, choose)
        expected_len = len(expected)
        actual = [
                [3,0],
                [3,1],
                [3,2],
                [3,4]
            ]
        actual_len = len(actual)
        self.assertEqual(actual, expected)
        self.assertEqual(actual_len, expected_len)

        length = 5
        first_index = 4
        choose = 2
        expected = initParent(length, first_index, choose)
        expected_len = len(expected)
        actual = [
                [4,0],
                [4,1],
                [4,2],
                [4,3]
            ]
        actual_len = len(actual)
        self.assertEqual(actual, expected)
        self.assertEqual(actual_len, expected_len)

    def test_permutation(self):
        # params = permutation(word: str, choose = None)

        word = "0123"
        choose = 1
        expected: List[List[int]]= []
        result = permutation(word, choose)
        for k in result.keys():
            expected.extend(result[k])
        expected_len = len(expected)
        actual = [
                [0],
                [1],
                [2],
                [3]
            ]
        actual_len = len(actual)
        self.assertEqual(actual_len, expected_len)
        self.assertEqual(actual, expected)
        self.assertEqual(expected_len, 4)

        word = "0123"
        choose = 2
        expected: List[List[int]] = []
        result = permutation(word, choose)
        for k in result.keys():
            expected.extend(result[k])
        expected_len = len(expected)
        actual =  [
                [0,1],
                [0,2],
                [0,3],
                [1,0],
                [1,2],
                [1,3],
                [2,0],
                [2,1],
                [2,3],
                [3,0],
                [3,1],
                [3,2],
            ]
        actual_len = len(actual)
        self.assertEqual(actual_len, expected_len)
        self.assertEqual(actual, expected)
        self.assertEqual(expected_len, 12)

        word = "0123"
        choose = 3
        expected: List[List[int]] = []
        result = permutation(word, choose)
        for k in result.keys():
            expected.extend(result[k])
        expected_len = len(expected)
        actual =[
                [0,1,2],
                [0,1,3],
                [0, 2, 3],
                [0,2,1],
                [0,3,1],
                [0,3,2],
                [1,0,2],
                [1,0,3],
                [1,2,3],
                [1,2,0],
                [1,3,0],
                [1,3,2],
                [2,0,1],
                [2,0,3],
                [2, 1, 3],
                [2,1,0],
                [2,3,0],
                [2,3,1],
                [3,0,1],
                [3,0,2],
                [3, 1, 2],
                [3,1,0],
                [3,2,0],
                [3,2,1],
            ]
        actual_len = len(actual)
        self.assertEqual(actual_len, expected_len)
        self.assertEqual(actual, expected)
        self.assertEqual(expected_len, 24)

        word = "0123"
        choose = 4
        expected: List[List[int]] = []
        result = permutation(word, choose)
        for k in result.keys():
            expected.extend(result[k])
        expected_len = len(expected)
        actual =   [
                [0,1,2,3],
                [0,1,3,2],
                [0,3,1,2],
                [0, 2, 1, 3],
                [0,3,2,1],
                [0,2,3,1],
                [1, 0, 2, 3],
                [1, 0, 3, 2],
                [1, 3, 0, 2],
                [1, 2, 0, 3],
                [1, 3, 2, 0],
                [1, 2, 3, 0],
                [2,0,1,3],
                [2,0,3,1],
                [2,3,0,1],
                [2, 1, 0, 3],
                [2,3,1,0],
                [2,1,3,0],
                [3,0,1,2],
                [3,0,2,1],
                [3,2,0,1],
                [3, 1, 0, 2],
                [3,2,1,0],
                [3,1,2,0],

            ]
        actual_len = len(actual)
        self.assertEqual(actual_len, expected_len)
        self.assertEqual(actual, expected)
        self.assertEqual(expected_len, 24)
