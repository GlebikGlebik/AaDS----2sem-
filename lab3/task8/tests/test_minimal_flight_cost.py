import unittest
from lab3.utils import check_time_and_memory
from lab3.task8.src.minimal_flight_cost import minimal_flight_cost


class TestMinimalFlightCost(unittest.TestCase):

    def test_should_check_example_1(self):
        # given
        data = ['4 4', '1 2 1', '4 1 2', '2 3 2', '1 3 5', '1 3']
        expected_data = 3
        expected_time = 10
        expected_memory = 524288

        # when
        m, t = check_time_and_memory(minimal_flight_cost, 8, data)
        res = minimal_flight_cost(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_example_2(self):
        # given
        data = ['5 9', '1 2 4', '1 3 2', '2 3 2', '3 2 1', '2 4 2', '3 5 4', '5 4 1', '2 5 3', '3 4 4', '1 5']
        expected_data = 6
        expected_time = 10
        expected_memory = 524288

        # when
        m, t = check_time_and_memory(minimal_flight_cost, 8, data)
        res = minimal_flight_cost(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_example_3(self):
        # given
        data = ['3 3', '1 2 7', '1 3 5', '2 3 2', '3 2']
        expected_data = -1
        expected_time = 10
        expected_memory = 524288

        # when
        m, t = check_time_and_memory(minimal_flight_cost, 8, data)
        res = minimal_flight_cost(data)

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
        m, t = check_time_and_memory(minimal_flight_cost, 8, data)
        res = minimal_flight_cost(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_simple(self):
        # given
        data = ['7 8', '1 2 5', '2 3 3', '3 4 2', '4 5 4', '5 6 5', '6 7 4', '1 7 1', '3 5 3', '2 6']
        # Путь: 2->3 (3), 3->5 (3), 5->6 (5)
        expected_data = 11
        expected_time = 10
        expected_memory = 524288

        # when
        m, t = check_time_and_memory(minimal_flight_cost, 6, data)
        res = minimal_flight_cost(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_should_check_max_values(self):
        # given
        data = ['10000 99900'] + [f'{x} {x - y} {10 ** 8 - y}' for x in range(10**4, 10, -1) for y in range(1, 6)] + \
               [f'{x - y} {x} {10 ** 8 - 5 - y}' for x in range(10 ** 4, 10, -1) for y in range(1, 6)] + ['9995 10000']
        expected_data = 99999990
        expected_time = 10
        expected_memory = 524288

        # when
        m, t = check_time_and_memory(minimal_flight_cost, 8, data)
        res = minimal_flight_cost(data)

        # then
        self.assertEqual(res, expected_data)
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
