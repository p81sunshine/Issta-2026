import random
from collections import defaultdict

def build_chain(text: str) -> dict:
    chain = defaultdict(lambda: defaultdict(int))

    for i in range(len(text) - 1):
        current_char = text[i]
        next_char = text[i + 1]
        chain[current_char][next_char] += 1

    # Convert frequencies to probabilities
    for current_char, transitions in chain.items():
        total = sum(transitions.values())
        for next_char in transitions:
            transitions[next_char] /= total

    return dict(chain)

def generate_text(chain: dict, initial_char: str, length: int) -> str:
    current_char = initial_char
    generated = [current_char]

    for _ in range(length - 1):
        if current_char in chain:
            next_char = random.choices(
                list(chain[current_char].keys()),
                list(chain[current_char].values())
            )[0]
            generated.append(next_char)
            current_char = next_char
        else:
            break

    return ''.join(generated)