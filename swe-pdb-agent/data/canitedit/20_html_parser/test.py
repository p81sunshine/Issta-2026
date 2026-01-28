from solution import *
import math

def test_all():
    content = "<div>Hello <span>world</span></div>"
    elements = parse(content)
    assert "\n".join(str(elem) for elem in elements) == content

    ex2 = """<head>
<title>My awesome page</title>
</head>
<body>
<div>
<h1>Super awesome page</h1>
<p>This is my awesome page.</p>
</div>
</body>"""
    elements = parse(ex2)
    assert "\n".join(str(elem) for elem in elements) == ex2

    ex3 = """<div>
<h1>Super awesome page</h1>
<p>This is my awesome page.</p>
</div>"""
    elements = parse(ex3)
    assert "\n".join(str(elem) for elem in elements) == ex3

    ex4 = """<div>
<h1>Super awesome page</h1>
<div>
<p>This is my awesome page.</p>
<div>
<p>This is my awesome page.</p>
<p>This is my awesome page.</p>
</div>
<div>
<p>This is my awesome page.</p>
<p>This is my awesome page.</p>
<p>This is my awesome page.</p>
</div>
</div>
</div>"""
    elements = parse(ex4)
    assert "\n".join(str(elem) for elem in elements) == ex4

    ex5 = """<div>
<h1 title="Hello world">Super awesome page</h1>
</div>"""
    elements = parse(ex5)
    assert "\n".join(str(elem) for elem in elements) == ex5

    ex6 = """<div>
<h1 title="Hello world" class="header">Super awesome page</h1>
</div>"""
    elements = parse(ex6)
    assert "\n".join(str(elem) for elem in elements) == ex6

    ex7 = """<div>
<h1 title="Hello world" class="header" id="title">Super awesome page</h1>
<p class="content">This is my awesome page.</p>
<h2 class="header">This is a header</h2>
<p class="content">This is my awesome page.</p>
<div class="footer">
<p class="content">This is my awesome page.</p>
<p class="content">This is my awesome page.</p>
</div>
</div>"""
    elements = parse(ex7)
    assert "\n".join(str(elem) for elem in elements) == ex7

    # just make sure that __repr__ works
    assert "HTMLElement" in repr(elements[0])