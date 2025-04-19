import sys
import os
import time

from lab1.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

start = time.perf_counter()

class AlmostPalindrome:
    def __init__(self):
        """
        n - длина слова
        k - параметр К
        s - слово
        """
        input_data = read_input(20)
        self.n, self.k = map(int, input_data[0].split())
        self.s = input_data[1]
        self.changes = [[0] * self.n for _ in range(self.n)]

    def preprocess_palindrome_changes(self):
        for length in range(2, self.n + 1):  # длина подстроки
            for left in range(self.n - length + 1):
                right = left + length - 1
                self.changes[left][right] = self.changes[left + 1][right - 1] + (self.s[left] != self.s[right])

        return self.changes

    def can_form_palindrome_with_k_changes(self, start, end):
        return self.changes[start][end] <= self.k

    def almost_palindromes_counter(self):
        self.changes = self.preprocess_palindrome_changes()
        count = 0

        for length in range(1, self.n + 1):  # длина подстроки
            for start in range(self.n - length + 1):
                end = start + length - 1
                if self.can_form_palindrome_with_k_changes(start, end):
                    count += 1

        return count


def main():
    ap = AlmostPalindrome()
    res = ap.almost_palindromes_counter()

    end = time.perf_counter()

    write_output(20, res)

    print("Время работы: ", end - start, "секунд")


if __name__ == '__main__':
    main()

