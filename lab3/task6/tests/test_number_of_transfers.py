import unittest
from lab3.utils import check_time_and_memory
from lab3.task6.src.number_of_transfers import number_of_transfers


class TestNumberOfTransfers(unittest.TestCase):

    def test_should_check_example_1(self):
        # given
        data = ['4 4', '1 2', '4 1', '2 3', '3 1', '2 4']
        expected_data = 2
        expected_time = 10
        expected_memory = 524288

        # when
        m, t = check_time_and_memory(number_of_transfers, 6, data)
        res = number_of_transfers(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_example_2(self):
        # given
        data = ['5 4', '5 2', '1 3', '3 4', '1 4', '3 5']
        expected_data = -1
        expected_time = 10
        expected_memory = 524288

        # when
        m, t = check_time_and_memory(number_of_transfers, 6, data)
        res = number_of_transfers(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_simple_empty(self):
        # given
        data = ['2 0', '1 2']
        expected_data = -1
        expected_time = 10
        expected_memory = 524288

        # when
        m, t = check_time_and_memory(number_of_transfers, 6, data)
        res = number_of_transfers(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_simple(self):
        # given
        data = ['7 8', '1 2', '2 3', '3 4', '4 5', '5 6', '6 7', '1 7', '3 5', '2 6']
        # Путь: 2->1, 1->7, 7->6
        expected_data = 3
        expected_time = 10
        expected_memory = 524288

        # when
        m, t = check_time_and_memory(number_of_transfers, 6, data)
        res = number_of_transfers(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_max_values(self):
        # given
        data = ['100000 99999'] + [f'{x} {x - 1}' for x in range(10**5, 1, -1)] + ['1 100000']
        expected_data = 99999
        expected_time = 10
        expected_memory = 524288

        # when
        m, t = check_time_and_memory(number_of_transfers, 6, data)
        res = number_of_transfers(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
