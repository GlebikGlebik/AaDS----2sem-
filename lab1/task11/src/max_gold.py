from lab1.utils import read_input, write_output, decorate


def max_gold(w, weights):
    dp = [0] * (w + 1)
    dp[0] = 1

    for weight in weights:
        for j in range(w, weight - 1, -1):
            if dp[j - weight] == 1:
                dp[j] = 1

    for j in range(w, -1, -1):
        if dp[j] == 1:
            max_weight = j
            return max_weight


def main():
    data = read_input(11)
    capacity = int(data[0].split()[0])
    weights = [int(x) for x in data[1].split()]
    res = max_gold(capacity, weights)
    write_output(11, res)

if __name__ == '__main__':
    decorate(11, 'max_gold')
