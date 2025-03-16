from lab1.utils import read_input, write_output, decorate


def souvenirs(n, values):
    total = sum(values)
    if total % 3 != 0:
        return 0

    target = total // 3
    if any(x > target for x in values):
        return 0

    masks = []

    def backtrack(idx, curr_sum, mask):
        if curr_sum == target:
            masks.append(mask)
            return
        if idx >= n or curr_sum > target:
            return
        backtrack(idx + 1, curr_sum + values[idx], mask | (1 << idx))
        backtrack(idx + 1, curr_sum, mask)

    backtrack(0, 0, 0)

    for mask in masks:
        remaining = []
        for i in range(n):
            if not (mask & (1 << i)):
                remaining.append(values[i])
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in remaining:
            for j in range(target, num - 1, -1):
                if dp[j - num] == 1:
                    dp[j] = 1
        if dp[target] == 1:
            return 1
    return 0


def main():
    data = read_input(13)
    n = int(data[0].split()[0])
    values = [int(x) for x in data[1].split()]
    res = souvenirs(n, values)
    write_output(13, res)

if __name__ == '__main__':
    decorate(13, 'souvenirs')
