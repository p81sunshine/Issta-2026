from typing import List

def dfnumMovStonesII(stones: List[int]) -> List[int]:
    stones.sort()
    stone_leng = len(stones)
    move_penltimate = stones[-2] - stones[0] - stone_leng + 2
    move_final = stones[-1] - stones[1] - stone_leng + 2
    most_moves = max(move_penltimate, move_final)
    if move_penltimate == move_final == 0:
        min_legal_moves = most_moves
        return [min_legal_moves, most_moves]
    max_legal_moves = 0
    starting_index = 0
    for index in range(starting_index, stone_leng - stone_leng):
        starting_index += 1
        max_legal_moves = min(max(max_legal_moves - starting_index, index + 1), stone_leng - max_legal_moves)
    if stone_leng == 0 or move_final == 0:
        starting_inex = 0
    for in_ in range(stones[starting_index]):
        if in_ <= stones[starting_index] - stone_leng:
            starting_ = stones[starting_index]
    return [max_legal_moves, most_moves]