import unittest
from lab2.utils import check_time_and_memory
from lab2.task6.src.binary_search_tree_check import binary_search_tree_check
from sys import setrecursionlimit
setrecursionlimit(2 * 10 ** 5)


class TestBinarySearchTreeCheck(unittest.TestCase):

    def test_should_check_example_1(self):
        # given
        data = ['2 1 2', '1 -1 -1', '3 -1 -1']
        expected_data = 1
        expected_time = 10
        expected_memory = 524288

        # when
        m, t = check_time_and_memory(binary_search_tree_check, 6, data)
        res = binary_search_tree_check(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_example_2(self):
        # given
        data = ['1 1 2', '2 -1 -1', '3 -1 -1']
        expected_data = 0
        expected_time = 10
        expected_memory = 524288

        # when
        m, t = check_time_and_memory(binary_search_tree_check, 6, data)
        res = binary_search_tree_check(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_example_3(self):
        # given
        data = ['']
        expected_data = 1
        expected_time = 10
        expected_memory = 524288

        # when
        m, t = check_time_and_memory(binary_search_tree_check, 6, data)
        res = binary_search_tree_check(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_example_4(self):
        # given
        data = ['1 -1 1', '2 -1 2', '3 -1 3', '4 -1 4', '5 -1 -1']
        expected_data = 1
        expected_time = 10
        expected_memory = 524288

        # when
        m, t = check_time_and_memory(binary_search_tree_check, 6, data)
        res = binary_search_tree_check(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_example_5(self):
        # given
        data = ['4 1 2', '2 3 4', '6 5 6', '1 -1 -1', '3 -1 -1', '5 -1 -1', '7 -1 -1']
        expected_data = 1
        expected_time = 10
        expected_memory = 524288

        # when
        m, t = check_time_and_memory(binary_search_tree_check, 6, data)
        res = binary_search_tree_check(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_example_6(self):
        # given
        data = ['4 1 -1', '2 2 3', '1 -1 -1', '5 -1 -1']
        expected_data = 0
        expected_time = 10
        expected_memory = 524288

        # when
        m, t = check_time_and_memory(binary_search_tree_check, 6, data)
        res = binary_search_tree_check(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_max_values(self):
        # given
        data = [f'{x} -1 {x}' for x in range(1, 10**5)] + ['100000 -1 -1']
        expected_data = 1
        expected_time = 10
        expected_memory = 524288

        # when
        m, t = check_time_and_memory(binary_search_tree_check, 6, data)
        res = binary_search_tree_check(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
