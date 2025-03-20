from lab2.utils import read_input, write_output, decorate


def insert(root, key):
    if root is None:
        return {'key': key, 'left': None, 'right': None}
    if key < root['key']:
        root['left'] = insert(root['left'], key)
    elif key > root['key']:
        root['right'] = insert(root['right'], key)
    return root


def delete(root, key):
    if root is None:
        return None
    if key < root['key']:
        root['left'] = delete(root['left'], key)
    elif key > root['key']:
        root['right'] = delete(root['right'], key)
    else:
        if root['left'] is None:
            return root['right']
        if root['right'] is None:
            return root['left']
        successor = find_min(root['right'])
        root['key'] = successor['key']
        root['right'] = delete(root['right'], successor['key'])
    return root


def find_min(node):
    while node['left'] is not None:
        node = node['left']
    return node


def exists(root, key):
    if root is None:
        return False
    if key == root['key']:
        return True
    return exists(root['left'], key) if key < root['key'] else exists(root['right'], key)


def find_next(root, key):
    result = None
    while root:
        if root['key'] > key:
            result = root['key']
            root = root['left']
        else:
            root = root['right']
    return result


def find_prev(root, key):
    result = None
    while root:
        if root['key'] < key:
            result = root['key']
            root = root['right']
        else:
            root = root['left']
    return result


def binary_search_tree(lines):
    root = None
    output = []

    for line in lines:
        if not line.strip():
            continue
        cmd, x = line.split()
        x = int(x)

        if cmd == 'insert':
            root = insert(root, x)
        elif cmd == 'delete':
            root = delete(root, x)
        elif cmd == 'exists':
            res = exists(root, x)
            output.append('true' if res else 'false')
        elif cmd == 'next':
            res = find_next(root, x)
            output.append(str(res) if res is not None else 'none')
        elif cmd == 'prev':
            res = find_prev(root, x)
            output.append(str(res) if res is not None else 'none')

    return output


def main():
    data = read_input(5)
    res = binary_search_tree(data)
    res = '\n'.join(map(str, res))
    write_output(5, res)

if __name__ == '__main__':
    decorate(5, 'binary_search_tree')
