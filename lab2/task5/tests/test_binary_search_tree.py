import unittest
from lab2.utils import check_time_and_memory
from lab2.task5.src.binary_search_tree import binary_search_tree
from random import randint


class TestBinarySearchTree(unittest.TestCase):

    def test_should_check_example(self):
        # given
        data = ['insert 2', 'insert 5', 'insert 3', 'exists 2', 'exists 4', 'next 4', 'prev 4', 'delete 5', 'next 4', 'prev 4']
        expected_data = ['true', 'false', '5', '3', 'none', '3']
        expected_time = 2
        expected_memory = 524288

        # when
        m, t = check_time_and_memory(binary_search_tree, 5, data)
        res = binary_search_tree(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_simple(self):
        # given
        data = ['next 3', 'insert 3', 'insert 4', 'insert 5', 'delete 4', 'delete 4', 'next 3', 'prev 3', 'insert 4', 'insert 4', 'exists 4']
        expected_data = ['none', '5', 'none', 'true']
        expected_time = 2
        expected_memory = 524288

        # when
        m, t = check_time_and_memory(binary_search_tree, 5, data)
        res = binary_search_tree(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_max_values(self):
        # given
        arr = [randint(0, 1000000000) for _ in range(16)]
        data = ['insert 1000000000',
                'insert 999999999',
                'insert -10000000000',
                'insert -999999998',
                'insert -999999999',
                'insert 0',
                'insert 999999995',
                'insert 999999997',
                'insert 5',
                'insert 999999996']
        for x in arr:
            data += [f'prev {x}', f'next {x}', f'prev {-x}', f'next {-x}', f'insert {x}']
        expected_data = binary_search_tree(data)
        expected_time = 2
        expected_memory = 524288

        # when
        m, t = check_time_and_memory(binary_search_tree, 5, data)
        res = binary_search_tree(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

if __name__ == '__main__':
    unittest.main()
