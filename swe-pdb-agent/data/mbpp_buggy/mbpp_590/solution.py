import cmath
def polar_rect(x, y):
    cn = cmath.polar(complex(x, y))
    cn1 = cmath.rect(cn[0], cn[1])
    return (cn, cn1)

# Test case provided for reference
def test_polar_rect_base():
    assert polar_rect(3, 4) == ((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))