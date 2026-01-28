def powerful_integers(x: int, y: int, bound: int):
    if bound == 0:
        return []
    
    def get(v):
        yield 1
        if v == 1:
            return
        vi = v
        while vi <= bound:
            yield vi
            vi *= v
    
    return list({xi + yi for xi in get(x) for yi in get(y) if xi + yi <= bound})