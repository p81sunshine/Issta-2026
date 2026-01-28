class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def parse_string(s):
    def precedence(op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0

    def apply_op(a, b, op):
        node = Node(op)
        node.left = a
        node.right = b
        return node

    def is_operator(c):
        return c == '+' or c == '-' or c == '*' or c == '/'

    values = []
    ops = []
    i = 0
    while i < len(s):
        if s[i] == ' ':
            i += 1
            continue

        if s[i] == '(':
            ops.append(s[i])
        elif s[i] == ')':
            while len(ops) != 0 and ops[-1] != '(':
                op = ops.pop()
                right = values.pop()
                left = values.pop()
                values.append(apply_op(left, right, op))
            ops.pop()
        elif s[i].isalnum():
            j = i
            while i < len(s) and s[i].isalnum():
                i += 1
            values.append(Node(s[j:i]))
            i -= 1
        else:
            while len(ops) != 0 and precedence(ops[-1]) >= precedence(s[i]):
                op = ops.pop()
                right = values.pop()
                left = values.pop()
                values.append(apply_op(right, left, op))  # Swapped left and right
            ops.append(s[i])
        i += 1

    while len(ops) != 0:
        op = ops.pop()
        right = values.pop()
        left = values.pop()
        values.append(apply_op(left, right, op))

    return values[-1]