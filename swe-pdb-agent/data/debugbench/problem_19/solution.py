from collections import deque

stack = []
q = deque()

def addText(text: str) -> None:
    for c in text:
        q.append(c)

def deleteText(k: int) -> int:
    i = 0
    while stack and i < k:
        stack.pop()
        i += 1
    return i

def cursorLeft(k: int) -> str:
    i = 0
    while stack and i < k:
        q.appendleft(stack.pop())
        i += 1
    return "".join(stack[-10:]) if len(stack) >= 10 else "".join(stack)

def cursorRight(k: int) -> str:
    i = 0
    while q and i < k:
        stack.append(q.popleft())
        i += 1
    return "".join(stack[-10:]) if len(stack) >= 10 else "".join(stack)