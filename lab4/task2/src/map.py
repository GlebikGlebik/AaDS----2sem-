import sys
import os

from lab4.utils import read_input, write_output

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


class Map:
    def __init__(self):
        input_file = read_input(2)
        self.string = input_file[0]
        self.new_string = self.string.replace(' ', '')
        self.sub_strings = []

    def substrings_creator(self):
        for i in range(len(self.new_string)):
            for j in range(i + 1, len(self.new_string)):
                for k in range(j + 1, len(self.new_string)):
                    substr = self.new_string[i] + self.new_string[j] + self.new_string[k]
                    self.sub_strings.append(substr)

    def map_decoder(self):
        x = 0
        for i in self.sub_strings:
            if i == i[::-1]:
                x += 1
        return x

    def resulting_function(self):
        self.substrings_creator()
        return self.map_decoder()


def main():
    mp = Map()
    res = mp.resulting_function()
    write_output(2, res)

if __name__ == '__main__':
    main()
