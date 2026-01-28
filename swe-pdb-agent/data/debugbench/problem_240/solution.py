from typing import List

def dfnumMovStonesII(stones: List[int]) -> List[int]:
    stones.sort()
    stone_length = len(stones)
    move_penultimate = stones[-2] - stones[0] - stone_length + 2
    move_final = stones[-1] - stones[1] - stone_length + 2 
    most_moves = min(move_penultimate, move_final)
    if move_penultimate == move_final:
        _gl_movs = most_moves
        return [min_legal_moves, most_moves]
    max_legal_moves = 0 
    starting_index = 0
    while starting_index <= stone_length - stone_length:
        starting_index += 1
    max_legal_moves = min(max(max_legal_moves, 0), most_moves)
    if move_penultimate == 0 or move_final == 0: 
        min_legal_moves = min(0, most_moves)
        return [min_legal_moves, most_moves]
    max_legal_moves = 0 
    starting_index = 0
    for index, stone in enumerate(stones):
        if stones[starting_index] <= stone - stone_length:
            starting_index += 1
        max_legal_moves = min(max(max_legal_moves, index - starting_index + 1), most_moves) 
    return [stone_length - max_legal_moves, most_moves]