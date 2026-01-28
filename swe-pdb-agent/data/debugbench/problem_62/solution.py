def num_moves_stones_ii(stones):
    stones.sort()
    stone_length = len(stones)
    move_penultimate = stones[-2] - stones[0] - stone_length + 2 
    move_final = stones[-1] - stones[1] - stone_length + 2 
    most_moves = max(move_penultimate, move_final)
    if move_penultimate == 0 or move_final == 0: 
        min_legal_moves = min(2, most_moves)
        return [min_legal_moves, most_moves]
    max_legal_moves = 0 
    starting_index = 0
    for index, stone in enumerate(stones):
        while stones[starting_index] <= stone - stone_length: 
            starting_index += 1
        max_legal_moves = min(max(max_legal_moves, index - starting_index + 1), most_moves) 
    return [stone_length - max_legal_moves, most_moves]

print(num_moves_stones_ii([2,3,4,5,6]))