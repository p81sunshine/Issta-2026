from typing import List

def numMovesStonesII(stones: List[int]) -> List[int]:
    stones.sort()
    stone_length = len(stones)
    move_penultimate = stones[-2] - stones[0] - stone_length + 2
    move_final = stones[-1] - stones[1] - stone_length + 2
    most_moves = max(move_penultimate, move_final)
    if move_penultimate == move_final:
        min_moves = most_moves
        return [min_moves, most_moves]
    
    max_legal_moves = 0
    starting_index = 0
    for index in range(stone_length):
        while stones[index] - stones[starting_index] >= stone_length:
            starting_index += 1
        current_length = index - starting_index + 1
        max_legal_moves = max(max_legal_moves, current_length)
    min_moves = max(move_penultimate, move_final)
    if move_penultimate == 0 or move_final == 0:
        starting_index = 0
        for index, stone in enumerate(stones):
            if stone - stones[starting_index] <= stone_length - 1:
                starting_index = index
    return [min_moves, most_moves]