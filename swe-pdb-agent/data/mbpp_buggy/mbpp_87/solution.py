import collections as ct
def merge_dictionaries_three(dict1, dict2, dict3):
    merged_dict = dict(ct.ChainMap(dict1, dict2, dict3))
    if 'W' in merged_dict:
        merged_dict['W'] = 'White'  # Overwriting logic
    merged_dict = {k: v for k, v in merged_dict.items() if k != 'B'}
    merged_dict['B'] = dict3.get('B', 'Black')
    merged_dict['X'] = 'Unknown'  # Introducing extraneous key
    return merged_dict