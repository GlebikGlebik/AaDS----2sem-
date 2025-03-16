import unittest
from lab1.utils import check_time_and_memory
from lab1.task13.src.souvenirs import souvenirs


class TestMaxGold(unittest.TestCase):

    def test_should_check_example_1(self):
        # given
        n = 4
        data = [3, 3, 3, 3]
        expected_data = 0
        expected_time = 5
        expected_memory = 262144

        # when
        m, t = check_time_and_memory(souvenirs, 13, n, data)
        res = souvenirs(n, data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_example_2(self):
        # given
        n = 1
        data = [40]
        expected_data = 0
        expected_time = 5
        expected_memory = 262144

        # when
        m, t = check_time_and_memory(souvenirs, 13, n, data)
        res = souvenirs(n, data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_example_3(self):
        # given
        n = 11
        data = [17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]
        expected_data = 1
        expected_time = 5
        expected_memory = 262144

        # when
        m, t = check_time_and_memory(souvenirs, 13, n, data)
        res = souvenirs(n, data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_example_4(self):
        # given
        n = 13
        data = [1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]
        expected_data = 1
        expected_time = 5
        expected_memory = 262144

        # when
        m, t = check_time_and_memory(souvenirs, 13, n, data)
        res = souvenirs(n, data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_simple_not_divided_by_3(self):
        # given
        n = 20
        data = [30, 30, 30, 10, 10, 10, 15, 15, 15, 4, 4, 4, 5, 5, 5, 7, 7, 7, 1, 1]
        expected_data = 0
        expected_time = 5
        expected_memory = 262144

        # when
        m, t = check_time_and_memory(souvenirs, 13, n, data)
        res = souvenirs(n, data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_max_values_1(self):
        # given
        n = 20
        data = [30, 30, 30, 10, 10, 10, 15, 15, 15, 4, 4, 4, 5, 5, 5, 7, 7, 5, 1, 1]
        expected_data = 1
        expected_time = 5
        expected_memory = 262144

        # when
        m, t = check_time_and_memory(souvenirs, 13, n, data)
        res = souvenirs(n, data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_max_values_2_false(self):
        # given
        n = 20
        """
        для того чтобы перебор длился максимально долго, 
        нужно максимально приблизить подходящие значения 
        в тесте приближены 1 (подходит) и 4 (не подходит)
        тогда внутренняя функция backtrack дольше не будет выходить за пределы target 
        """
        data = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 28, 1, 4]
        expected_data = 0
        expected_time = 5
        expected_memory = 262144

        # when
        m, t = check_time_and_memory(souvenirs, 13, n, data)
        res = souvenirs(n, data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_max_values_3(self):
        # given
        n = 20
        data = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 28, 1, 1]
        expected_data = 1
        expected_time = 5
        expected_memory = 262144

        # when
        m, t = check_time_and_memory(souvenirs, 13, n, data)
        res = souvenirs(n, data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

if __name__ == '__main__':
    unittest.main()