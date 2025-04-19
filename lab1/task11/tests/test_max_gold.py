import unittest
from lab1.utils import check_time_and_memory
from lab1.task11.src.max_gold import max_gold


class TestMaxGold(unittest.TestCase):

    def test_should_check_example(self):
        # given
        w = 10
        data = [1, 4, 8]
        expected_data = 9
        expected_time = 5
        expected_memory = 262144

        # when
        m, t = check_time_and_memory(max_gold, 11, w, data)
        res = max_gold(w, data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_simple(self):
        # given
        w = 14
        data = [1, 4, 8, 3]
        expected_data = 13
        expected_time = 5
        expected_memory = 262144

        # when
        m, t = check_time_and_memory(max_gold, 11, w, data)
        res = max_gold(w, data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_max_values_1(self):
        # given
        w = 10000
        data = 299 * [100000] + [10001]
        expected_data = 0
        expected_time = 5
        expected_memory = 262144

        # when
        m, t = check_time_and_memory(max_gold, 11, w, data)
        res = max_gold(w, data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_max_values_2(self):
        # given
        w = 10000
        data = 294 * [34] + [5]
        expected_data = 9996
        expected_time = 5
        expected_memory = 262144

        # when
        m, t = check_time_and_memory(max_gold, 11, w, data)
        res = max_gold(w, data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

if __name__ == '__main__':
    unittest.main()
