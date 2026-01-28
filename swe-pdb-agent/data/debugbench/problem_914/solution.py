from collections import deque

def text_editor():
    stack = []
    q = deque()

    def add_text(text: str) -> None:
        for c in text:
            stack.append(c)

    def delete_text(k: int) -> int:
        i = 0
        while stack and i < k:
            stack.pop()
            i += 1
        return i

    def cursor_left(k: int) -> str:
        i = 0
        while stack and i < k:
            q.appendleft(stack.pop())
            i += 1
        return "".join(stack[-10:]) if len(stack) >= 10 else "".join(stack)

    def cursor_right(k: int) -> str:
        i = 0
        while q and i < k:
            stack.append(q.popleft())
            i += 1
        return "".join(stack[-10:]) if len(stack) >= 10 else "".join(stack)

    return locals()