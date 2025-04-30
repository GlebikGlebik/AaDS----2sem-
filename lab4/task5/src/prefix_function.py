from lab4.utils import read_input, write_output, decorate


def prefix_function(s):
    n = len(s)
    p = [0] * n
    for i in range(1, n):
        j = p[i-1]
        while j > 0 and s[i] != s[j]:
            j = p[j-1]
        if s[i] == s[j]:
            j += 1
        p[i] = j
    return p


def main():
    data = read_input(5)
    result = prefix_function(data[0])
    write_output(5, ' '.join(map(str, result)))


if __name__ == '__main__':
    decorate(5, 'prefix_function')
