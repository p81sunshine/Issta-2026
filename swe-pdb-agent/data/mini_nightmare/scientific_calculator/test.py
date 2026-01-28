import pytest

from scientific_calculator_code import PlusTool


@pytest.fixture
def plus_tool():
    return PlusTool()


def test_use(plus_tool):
    assert plus_tool.use("```plus 1 2```") == 3
    assert plus_tool.use("```plus 3 4```") == 7
    assert plus_tool.use("```plus -3 3```") == 0
    assert plus_tool.use("```plus 1 2 3```") == "SyntaxError: invalid syntax."
    assert plus_tool.use("```plus 1 a```") == "ValueError: invalid value."
