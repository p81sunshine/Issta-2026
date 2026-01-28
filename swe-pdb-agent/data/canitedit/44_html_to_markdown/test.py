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
    assert translate_html_to_markdown(
        [HTMLElement(name="empty", content=[""], attributes={})]) == ""
    assert translate_html_to_markdown(
        parse("<h1>Super awesome page</h1>")) == "# Super awesome page"

    ex_1 = """<div>
<h1 title="Hello world" class="header" id="title">Super awesome page</h1>
<p class="content">This is my awesome page.</p>
<h2 class="header">This is a header</h2>
<p class="content">This is my awesome page.</p>
<div class="footer">
<p class="content">This is my awesome page.</p>
<p class="content">This is my awesome page.</p>
</div>
</div>"""
    exp_1 = """# Super awesome page

This is my awesome page.

## This is a header

This is my awesome page.

This is my awesome page.

This is my awesome page."""
    assert translate_html_to_markdown(parse(ex_1)) == exp_1

    ex_1 = """<div>
<h1 title="Hello world" class="header" id="title">Super awesome page</h1>
<p class="content">This is my awesome page.</p>
<h3 class="header">This is a header</h3>
<p class="content">This is my awesome page.</p>
<div class="footer">
<p class="content">This is my awesome page.</p>
<p class="content">This is my awesome page.</p>
</div>
</div>"""
    exp_1 = """# Super awesome page

This is my awesome page.

### This is a header

This is my awesome page.

This is my awesome page.

This is my awesome page."""
    assert translate_html_to_markdown(parse(ex_1)) == exp_1

    ex_1 = """<div>
<h1 title="Hello world" class="header" id="title">Super awesome page</h1>
<p class="content">This is my awesome page.</p>
<h4 class="header">This is a header</h4>
<p class="content">This is my awesome page.</p>
<div class="footer">
<p class="content">This is my awesome page.</p>
<p class="content">This is my awesome page.</p>
</div>
</div>"""
    exp_1 = """# Super awesome page

This is my awesome page.

#### This is a header

This is my awesome page.

This is my awesome page.

This is my awesome page."""
    assert translate_html_to_markdown(parse(ex_1)) == exp_1

    ex_1 = """<div>
<h1 title="Hello world" class="header" id="title">Super awesome page</h1>
<p class="content">This is my awesome page.</p>
<h5 class="header">This is a header</h5>
<p class="content">This is my awesome page.</p>
<div class="footer">
<p class="content">This is my awesome page.</p>
<p class="content">This is my awesome page.</p>
</div>
</div>"""
    exp_1 = """# Super awesome page

This is my awesome page.

##### This is a header

This is my awesome page.

This is my awesome page.

This is my awesome page."""
    assert translate_html_to_markdown(parse(ex_1)) == exp_1

    ex_1 = """<div>
<h1 title="Hello world" class="header" id="title">Super awesome page</h1>
<p class="content">This is my awesome page.</p>
<h6 class="header">This is a header</h6>
<p class="content">This is my awesome page.</p>
<div class="footer">
<p class="content">This is my awesome page.</p>
<p class="content">This is my awesome page.</p>
</div>
</div>"""
    exp_1 = """# Super awesome page

This is my awesome page.

###### This is a header

This is my awesome page.

This is my awesome page.

This is my awesome page."""
    assert translate_html_to_markdown(parse(ex_1)) == exp_1

    # Tests to ensure that the proper edit was made

    ex_2 = """<div>
<h1 title="Hello world" class="header" id="title">Super awesome page</h1>
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
</ul>
<p class="content">This is my awesome page.</p>
<h2 class="header">This is a header</h2>
<p class="content">This is my awesome page.</p>
<div class="footer">
<p class="content">This is my awesome page.</p>
<p class="content">This is my awesome page.</p>
</div>
</div>"""
    exp_2 = """# Super awesome page

* Item 1
* Item 2

This is my awesome page.

## This is a header

This is my awesome page.

This is my awesome page.

This is my awesome page."""
    assert translate_html_to_markdown(parse(ex_2)) == exp_2

    ex_3 = """<div>
<h1 title="Hello world" class="header" id="title">Super awesome page</h1>
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
    <li>Item 4</li>
    <li>Item 5</li>
</ul>
<p class="content">This is my awesome page.</p>
<h2 class="header">This is a header</h2>
<p class="content">This is my awesome page.</p>
<div class="footer">
<p class="content">This is my awesome page.</p>
<p class="content">This is my awesome page.</p>
</div>
</div>"""
    exp_3 = """# Super awesome page

* Item 1
* Item 2
* Item 3
* Item 4
* Item 5

This is my awesome page.

## This is a header

This is my awesome page.

This is my awesome page.

This is my awesome page."""
    assert translate_html_to_markdown(parse(ex_3)) == exp_3

    ex_4 = """<div>
<h1 title="Hello world" class="header" id="title">Super awesome page</h1>
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
    <li>Item 4</li>
    <li>Item 5</li>
    <li>Item 6</li>
</ul>
<p class="content">This is my awesome page.</p>
<h2 class="header">This is a header</h2>
<p class="content">This is my awesome page.</p>
<div class="footer">
<p class="content">This is my awesome page.</p>
<p class="content">This is my awesome page.</p>
</div>
</div>"""
    exp_4 = """# Super awesome page

* Item 1
* Item 2
* Item 3
* Item 4
* Item 5
* [see more](/see-more)

This is my awesome page.

## This is a header

This is my awesome page.

This is my awesome page.

This is my awesome page."""
    assert translate_html_to_markdown(parse(ex_4)) == exp_4

    ex_5 = """<div>
<h1 title="Hello world" class="header" id="title">Super awesome page</h1>
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
    <li>Item 4</li>
    <li>Item 5</li>
</ul>
<p class="content">This is my awesome page.</p>
<h2 class="header">This is a header</h2>
<p class="content">This is my awesome page.</p>
<div class="footer">
<p class="content">This is my awesome page.</p>
<ol>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ol>
<p class="content">This is my awesome page.</p>
</div>
</div>"""
    exp_5 = """# Super awesome page

* Item 1
* Item 2
* Item 3
* Item 4
* Item 5

This is my awesome page.

## This is a header

This is my awesome page.

This is my awesome page.

1. Item 1
2. Item 2
3. Item 3

This is my awesome page."""
    assert translate_html_to_markdown(parse(ex_5)) == exp_5

    ex_6 = """<div>
<h1 title="Hello world" class="header" id="title">Super awesome page</h1>
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
    <li>Item 4</li>
    <li>Item 5</li>
</ul>
<p class="content">This is my awesome page.</p>
<h2 class="header">This is a header</h2>
<p class="content">This is my awesome page.</p>
<div class="footer">
<p class="content">This is my awesome page.</p>
<ol>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
    <li>Item 4</li>
    <li>Item 5</li>
    <li>Item 6</li>
    <li>Item 7</li>
</ol>
<p class="content">This is my awesome page.</p>
</div>
</div>"""
    exp_6 = """# Super awesome page

* Item 1
* Item 2
* Item 3
* Item 4
* Item 5

This is my awesome page.

## This is a header

This is my awesome page.

This is my awesome page.

1. Item 1
2. Item 2
3. Item 3
4. Item 4
5. Item 5
6. [see more](/see-more)

This is my awesome page."""
    assert translate_html_to_markdown(parse(ex_6)) == exp_6