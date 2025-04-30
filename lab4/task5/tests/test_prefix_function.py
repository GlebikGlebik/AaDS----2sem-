import unittest
from lab4.utils import check_time_and_memory
from lab4.task5.src.prefix_function import prefix_function


class TestNumberOfTransfers(unittest.TestCase):

    def test_should_check_example_1(self):
        # given
        data = 'aaaAAA'
        expected_data = [0, 1, 2, 0, 0, 0]
        expected_time = 2
        expected_memory = 262144

        # when
        m, t = check_time_and_memory(prefix_function, 5, data)
        res = prefix_function(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_example_2(self):
        # given
        data = 'abacaba'
        expected_data = [0, 0, 1, 0, 1, 2, 3]
        expected_time = 2
        expected_memory = 262144

        # when
        m, t = check_time_and_memory(prefix_function, 5, data)
        res = prefix_function(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_simple(self):
        # given
        data = 'abab'
        expected_data = [0, 0, 1, 2]
        expected_time = 2
        expected_memory = 262144

        # when
        m, t = check_time_and_memory(prefix_function, 5, data)
        res = prefix_function(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_max(self):
        # given
        data = 'abbabbabaa' * 10 ** 5
        expected_time = 2
        expected_memory = 262144

        # when
        m, t = check_time_and_memory(prefix_function, 5, data)

        # then
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

if __name__ == '__main__':
    unittest.main()
