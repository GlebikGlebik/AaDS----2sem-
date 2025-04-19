import sys
import os

from lab1.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class Removing:
    def __init__(self):
        self.input_data = []
        self.s = ''
        self.closing_brackets = ')}]'
        self.opening_brackets = "({["
        self.stack = {}
        self.indexes_to_delete = []

    def add(self, e, i):
        self.stack[i] = e

    def deleter(self, e, index):
        for i, j in list(self.stack.items())[::-1]:
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

    def unclosed_bracket(self, e):
        for i, j in list(self.stack.items())[::-1]:
            if j == '(' and e == ')':
                self.indexes_to_delete.append(i)
                break
            elif j == '[' and e == ']':
                self.indexes_to_delete.append(i)
                break
            elif j == '{' and e == '}':
                self.indexes_to_delete.append(i)
                break

    def resulting_function(self):
        for i in range(len(self.s)):
            if self.s[i] in self.opening_brackets:
                self.add(self.s[i], i)
            elif self.s[i] in self.closing_brackets:
                for j in range(len(list(self.stack.values()))):
                    arr = list(self.stack.values())[::-1]
                    if (arr[j] == '(' and self.s[i] == ')') or (arr[j] == '[' and self.s[i] == ']') or (arr[j] == '{' and self.s[i] == '}'):
                        self.deleter(self.s[i], i)
                        break
                    if self.s[i] == ')' and (arr[j] == "[" or arr[j] == '{'):
                        self.add(self.s[i], i)
                        self.unclosed_bracket(self.s[i])
                        self.deleter(self.s[i],i)
                        break
                    if self.s[i] == ']' and (arr[j] == "(" or arr[j] == '{'):
                        self.add(self.s[i], i)
                        self.unclosed_bracket(self.s[i])
                        self.deleter(self.s[i],i)
                        break
                    if self.s[i] == '}' and (arr[j] == "[" or arr[j] == '('):
                        self.add(self.s[i], i)
                        self.unclosed_bracket(self.s[i])
                        self.deleter(self.s[i],i)
                        break # 1 2 3 4 5
                else:
                    self.deleter(self.s[i], i)
        res = ''
        for i in range(len(self.s)):
            if i not in self.stack.values() and i not in self.indexes_to_delete:
                res += self.s[i]
        return res


def main():
    rem = Removing()
    rem.input_data = read_input(15)
    if rem.input_data:
        rem.s = rem.input_data[0]
        res = rem.resulting_function()
        write_output(15, res)
    else:
        res = ''
        write_output(15, res)
        return

if __name__ == '__main__':
    decorate(task = 15, task_name= 'removing_brackets')

