def dict_depth_aux(d):
    if d:
        return 1 + max(map(dict_depth_aux, d.values()))
    return 0

def dict_depth(d):
    return dict_depth_aux(d)