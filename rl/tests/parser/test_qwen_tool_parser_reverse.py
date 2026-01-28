import pytest

from rllm.parser import QwenToolParser
from rllm.tools.tool_base import ToolCall


class TestQwenToolParserReverse:
    """
    Test cases for QwenToolParser with reverse parsing logic.
    The parser now finds the last tool_call_end and matches it with the nearest tool_call_begin,
    only parsing the last complete tool call.
    """

    @pytest.fixture
    def parser(self):
        return QwenToolParser()

    def test_empty_response(self, parser):
        """Test parsing empty response."""
        result = parser.parse("")
        assert len(result) == 0

    def test_no_tool_calls(self, parser):
        """Test response with no tool calls."""
        response = "This is a normal response without any tool calls."
        result = parser.parse(response)
        assert len(result) == 0

    def test_no_tool_call_end(self, parser):
        """Test response with only tool_call_begin but no tool_call_end."""
        response = '<tool_call>{"name": "search", "arguments": {"query": "test"}}'
        result = parser.parse(response)
        assert len(result) == 0

    def test_single_valid_tool_call(self, parser):
        """Test parsing a single valid tool call."""
        response = '<tool_call>{"name": "search_weather", "arguments": {"location": "New York", "unit": "celsius"}}</tool_call>'
        result = parser.parse(response)
        assert len(result) == 1
        assert isinstance(result[0], ToolCall)
        assert result[0].name == "search_weather"
        assert result[0].arguments == {"location": "New York", "unit": "celsius"}

    def test_multiple_tool_calls_parse_last(self, parser):
        """Test that only the last complete tool call is parsed."""
        response = """
        <tool_call>{"name": "search_weather", "arguments": {"location": "New York"}}</tool_call>
        <tool_call>{"name": "search_restaurants", "arguments": {"location": "New York", "cuisine": "Italian"}}</tool_call>
        <tool_call>{"name": "read_file", "arguments": {"path": "/tmp/test.txt"}}</tool_call>
        """
        result = parser.parse(response)
        # Should only parse the last tool call
        assert len(result) == 1
        assert result[0].name == "read_file"
        assert result[0].arguments == {"path": "/tmp/test.txt"}

    def test_multiple_tool_calls_with_text_between(self, parser):
        """Test parsing when there's text between tool calls."""
        response = """
        Some text before
        <tool_call>{"name": "first", "arguments": {"arg": "value1"}}</tool_call>
        Some text in between
        <tool_call>{"name": "second", "arguments": {"arg": "value2"}}</tool_call>
        More text after
        """
        result = parser.parse(response)
        assert len(result) == 1
        assert result[0].name == "second"
        assert result[0].arguments == {"arg": "value2"}

    def test_incomplete_first_tool_call(self, parser):
        """Test when first tool call is incomplete but last one is complete."""
        response = """
        <tool_call>{"name": "incomplete", "arguments": {"arg": "value"}
        <tool_call>{"name": "complete", "arguments": {"arg": "value"}}</tool_call>
        """
        result = parser.parse(response)
        assert len(result) == 1
        assert result[0].name == "complete"

    def test_only_tool_call_end_no_begin(self, parser):
        """Test when there's only tool_call_end but no matching tool_call_begin before it."""
        response = 'Some text </tool_call>'
        result = parser.parse(response)
        assert len(result) == 0

    def test_empty_content_between_tags(self, parser):
        """Test when tool_call tags are present but content is empty."""
        response = '<tool_call></tool_call>'
        result = parser.parse(response)
        assert len(result) == 0

    def test_whitespace_only_content(self, parser):
        """Test when tool_call tags contain only whitespace."""
        response = '<tool_call>   </tool_call>'
        result = parser.parse(response)
        assert len(result) == 0

    def test_invalid_json(self, parser):
        """Test parsing tool call with invalid JSON."""
        response = '<tool_call>{"name": "search", "arguments": {invalid json}}</tool_call>'
        result = parser.parse(response)
        assert len(result) == 0

    def test_json_not_dict(self, parser):
        """Test when JSON is valid but not a dictionary."""
        response = '<tool_call>["not", "a", "dict"]</tool_call>'
        result = parser.parse(response)
        assert len(result) == 0

    def test_missing_name_field(self, parser):
        """Test when JSON is valid but missing 'name' field."""
        response = '<tool_call>{"arguments": {"arg": "value"}}</tool_call>'
        result = parser.parse(response)
        assert len(result) == 0

    def test_missing_arguments_field(self, parser):
        """Test when JSON is valid but missing 'arguments' field."""
        response = '<tool_call>{"name": "search"}</tool_call>'
        result = parser.parse(response)
        assert len(result) == 0

    def test_complex_arguments(self, parser):
        """Test parsing tool call with complex nested arguments."""
        response = '''<tool_call>{"name": "complex_tool", "arguments": {"nested": {"key": "value", "list": [1, 2, 3]}, "string": "test"}}</tool_call>'''
        result = parser.parse(response)
        assert len(result) == 1
        assert result[0].name == "complex_tool"
        assert result[0].arguments["nested"]["key"] == "value"
        assert result[0].arguments["nested"]["list"] == [1, 2, 3]

    def test_multiple_tool_calls_last_incomplete(self, parser):
        """Test when there are multiple tool calls but the last one is incomplete."""
        response = """
        <tool_call>{"name": "complete1", "arguments": {"arg": "value1"}}</tool_call>
        <tool_call>{"name": "incomplete", "arguments": {"arg": "value2"}
        """
        result = parser.parse(response)
        # Should parse the last complete one (complete1)
        assert len(result) == 1
        assert result[0].name == "complete1"

    def test_tool_call_with_newlines(self, parser):
        """Test parsing tool call that spans multiple lines."""
        response = """<tool_call>
{"name": "multiline", "arguments": {"arg": "value"}}
</tool_call>"""
        result = parser.parse(response)
        assert len(result) == 1
        assert result[0].name == "multiline"
        assert result[0].arguments == {"arg": "value"}

    def test_nested_tool_call_tags_in_text(self, parser):
        """Test when tool_call tags appear in the JSON content itself."""
        response = '<tool_call>{"name": "test", "arguments": {"text": "contains <tool_call> tag"}}</tool_call>'
        result = parser.parse(response)
        assert len(result) == 1
        assert result[0].name == "test"
        assert "<tool_call>" in result[0].arguments["text"]

    def test_multiple_tool_calls_with_last_valid(self, parser):
        """Test multiple tool calls where only the last one is valid."""
        response = """
        <tool_call>{"name": "invalid1", "arguments": invalid}</tool_call>
        <tool_call>{"name": "invalid2"}</tool_call>
        <tool_call>{"name": "valid", "arguments": {"arg": "value"}}</tool_call>
        """
        result = parser.parse(response)
        assert len(result) == 1
        assert result[0].name == "valid"

    def test_real_world_example(self, parser):
        """Test a realistic example with multiple tool calls and text."""
        response = """
        I need to search for information and then read a file.
        <tool_call>{"name": "search", "arguments": {"query": "Python programming"}}</tool_call>
        Based on the search results, I'll read the documentation.
        <tool_call>{"name": "read_file", "arguments": {"path": "/docs/python.md"}}</tool_call>
        """
        result = parser.parse(response)
        assert len(result) == 1
        assert result[0].name == "read_file"
        assert result[0].arguments == {"path": "/docs/python.md"}

    def test_arguments_with_special_characters(self, parser):
        """Test tool call with arguments containing special characters."""
        # Use double quotes with escaped sequences to match JSON format
        response = '<tool_call>{"name": "write_file", "arguments": {"path": "/tmp/file.txt", "content": "Line 1\\nLine 2\\tTabbed"}}</tool_call>'
        result = parser.parse(response)
        assert len(result) == 1
        assert result[0].name == "write_file"
        assert "\n" in result[0].arguments["content"]
        assert "\t" in result[0].arguments["content"]

    def test_empty_arguments(self, parser):
        """Test tool call with empty arguments dictionary."""
        response = '<tool_call>{"name": "no_args", "arguments": {}}</tool_call>'
        result = parser.parse(response)
        assert len(result) == 1
        assert result[0].name == "no_args"
        assert result[0].arguments == {}

