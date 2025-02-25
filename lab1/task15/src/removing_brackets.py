import sys
import os

from lab1.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class Removing:
    def __init__(self):
        input_data = read_input(15)
        self.s = input_data[0]
        self.closing_brackets = ')}]'
        self.opening_brackets = "({["
        self.stack = {}

    def add(self, e, i):
        self.stack[i] = e

    def deleter(self, e, index):
        for i, j in self.stack.items():
            if j == '(' and e == ')':
                del self.stack[i]
                break
            elif j == '[' and e == ']':
                del self.stack[i]
                break
            elif j == '{' and e == '}':
                del self.stack[i]
                break
        else:
            self.add(e, index)


def main():
    rem = Removing()
    for i in range(len(rem.s)):
        if rem.s[i] in rem.opening_brackets:
            rem.add(rem.s[i], i)
        elif rem.s[i] in rem.closing_brackets:
            rem.deleter(rem.s[i], i)

    res = ''
    for i in range(len(rem.s)):
        if i not in rem.stack.keys():
            res += rem.s[i]


    write_output(15, res)

if __name__ == '__main__':
    decorate(task = 15, task_name= 'removing_brackets')

