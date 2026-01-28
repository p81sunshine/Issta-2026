from collections import defaultdict, deque

def isTransformable(s: str, t: str) -> bool:
    indexes = defaultdict(deque)
    for index, character in enumerate(s):
        indexes[int(character)].append(index)

    unique_t_values = set([int(t_i) for t_i in t])
    for t_v in unique_t_values: 
        if t_v not in indexes:
            return False 
            
    for character in t: 
        character_designation = int(character)
        if character_designation not in indexes: 
            return False 
        for lesser_character in range(character_designation):
            if indexes[lesser_character] and indexes[lesser_character][0] < indexes[character_designation][0]: 
                return False 
        indexes[character_designation].popleft()
        if len(indexes[character_designation]) == 0: 
            indexes.pop(character_designation)
        
    # if all characters able to sort, return it 
    return False