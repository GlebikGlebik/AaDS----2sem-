from lab4.utils import read_input, write_output, decorate


def z_function(s) :
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z[1:]


def main():
    data = read_input(6)
    result = z_function(data[0])
    write_output(6, ' '.join(map(str, result)))


if __name__ == '__main__':
    decorate(6, 'z_function')
