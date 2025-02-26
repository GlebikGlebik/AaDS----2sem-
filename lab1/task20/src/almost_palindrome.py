import sys
import os

from lab1.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


class AlmostPalindrome:
    def __init__(self):
        """
        n - длина слова
        k - параметр К
        s - слово
        """
        input_data = read_input(20)
        self.n,self.k = map(int, input_data[0].split())
        self.s = input_data[1]
        self.subwords = []

    def subword_finder(self):
        for i in range(self.n):
            for j in range(self.n - i):
                self.subwords.append(self.s[j: j + i + 1])
        return self.subwords

    def counter_almost_palindrome(self):
        counter = 0
        for i in self.subwords:
            mismatch_counter = 0
            if len(i) == 1:
                counter += 1
                continue
            for j in range(len(i) - 1):
                if i[j] != i[len(i) - 1 - j]:
                    mismatch_counter += 1
                    if mismatch_counter > self.k:
                        break
            else:
                counter += 1
        return counter

    def resulting_function(self):
        self.subword_finder()
        return self.counter_almost_palindrome()

def main():
    ap = AlmostPalindrome()
    res = ap.resulting_function()
    write_output(20, res)

if __name__ == '__main__':
    decorate(task=20, task_name='almost_palindrome')
