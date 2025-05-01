import sys
import os

from lab4.utils import read_input, write_output

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


class NaiveSearch:
    def __init__(self):
        input_file = read_input(1)
        self.substr = str(input_file[0])
        self.string = str(input_file[1])

    def substring_search(self):
        indexes = []
        substr_count = 0
        for i in range(len(self.string) - len(self.substr) + 1):
            if self.string[i] == self.substr[0]:
                if self.string[i:i + len(self.substr)] == self.substr:
                    substr_count += 1
                    indexes.append(i + 1)
        return substr_count, indexes


def main():
    ns = NaiveSearch()
    count, indexes = ns.substring_search()
    res_indexes = []
    [res_indexes.append(str(i)) for i in indexes]
    res = f'''{count} 
{' '.join(res_indexes)}'''
    write_output(1, res)

if __name__ == '__main__':
    main()
