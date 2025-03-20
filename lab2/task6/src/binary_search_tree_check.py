from lab2.utils import read_input, write_output, decorate


def binary_search_tree_check(lines):
    tree = []
    if lines == ['']:
        return 1
    for line in lines:
        key, left, right = map(int, line.split())
        tree.append((key, left, right))

    def check_node(node_index, min_key, max_key):
        if node_index == -1:
            return 1

        node = tree[node_index]
        key = node[0]

        if not (min_key < key < max_key):
            return 0

        return check_node(node[1], min_key, key) and check_node(node[2], key, max_key)

    return check_node(0, float('-inf'), float('inf'))


def main():
    data = read_input(6)
    n = data[0]
    nodes = data[1:]
    print(nodes)
    res = binary_search_tree_check(nodes)
    if res == 1:
        write_output(6, 'CORRECT')
    else:
        write_output(6, 'INCORRECT')

if __name__ == '__main__':
    decorate(6, 'binary_search_tree_check')
