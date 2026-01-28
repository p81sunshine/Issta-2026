import pytest
from acecode_evol_30725_llama3_1_instruct_32_code import convert_xml_to_dict

def test_case_0():
    assert convert_xml_to_dict('<parent><child><sub_child>First subchild</sub_child><sub_child>Second subchild</sub_child></child><child>Second child</child></parent>') == {'parent': {'child': {'sub_child': 'Second subchild'}, 'child': 'Second child'}}

def test_case_1():
    assert convert_xml_to_dict('<parent><child></child></parent>') == {'parent': {'child': None}}

def test_case_2():
    assert convert_xml_to_dict('<root><child><sub_child>Text</sub_child></child></root>') == {'root': {'child': {'sub_child': 'Text'}}}

def test_case_3():
    assert convert_xml_to_dict('<data><item>Value</item><item><sub_item>Subvalue</sub_item></item></data>') == {'data': {'item': 'Value', 'item': {'sub_item': 'Subvalue'}}}

def test_case_4():
    assert convert_xml_to_dict('<a><b><c>Content</c></b></a>') == {'a': {'b': {'c': 'Content'}}}

def test_case_5():
    assert convert_xml_to_dict('<parent><child>Child Text</child></parent>') == {'parent': {'child': 'Child Text'}}

def test_case_6():
    assert convert_xml_to_dict('<parent><child><sub_child>Only Subchild</sub_child></child></parent>') == {'parent': {'child': {'sub_child': 'Only Subchild'}}}

def test_case_7():
    assert convert_xml_to_dict('<parent><child><sub_child>1</sub_child><sub_child>2</sub_child></child></parent>') == {'parent': {'child': {'sub_child': '2'}}}

def test_case_8():
    assert convert_xml_to_dict('<level1><level2><level3>Deep Value</level3></level2></level1>') == {'level1': {'level2': {'level3': 'Deep Value'}}}

def test_case_9():
    assert convert_xml_to_dict('<company><employee><name>John</name><age>30</age></employee><employee><name>Jane</name></employee></company>') == {'company': {'employee': {'name': 'Jane'}}}

def test_case_10():
    assert convert_xml_to_dict('<parent><child><sub_child>1</sub_child><sub_child>2</sub_child></child><child><sub_child>3</sub_child></child></parent>') == {'parent': {'child': {'sub_child': '2'}, 'child': {'sub_child': '3'}}}

def test_case_11():
    assert convert_xml_to_dict('<root><child><sub_child>Text 1</sub_child></child><child><sub_child>Text 2</sub_child><sub_child>Text 3</sub_child></child></root>') == {'root': {'child': {'sub_child': 'Text 1'}, 'child': {'sub_child': 'Text 3'}}}

def test_case_12():
    assert convert_xml_to_dict('<data><item>Item 1</item><item>Item 2</item></data>') == {'data': {'item': 'Item 2'}}

def test_case_13():
    assert convert_xml_to_dict('<parent><child><sub_child>First</sub_child></child><child><sub_child>Second</sub_child></child></parent>') == {'parent': {'child': {'sub_child': 'Second'}}}

def test_case_14():
    assert convert_xml_to_dict('<outer><inner><most_inner>Final Value</most_inner></inner></outer>') == {'outer': {'inner': {'most_inner': 'Final Value'}}}

def test_case_15():
    assert convert_xml_to_dict('<container><box><item>Item 1</item></box><box><item>Item 2</item></box></container>') == {'container': {'box': {'item': 'Item 2'}}}

def test_case_16():
    assert convert_xml_to_dict('<parent><child><sub_child>First</sub_child><sub_child>Second</sub_child></child><child>Child Text</child></parent>') == {'parent': {'child': {'sub_child': 'Second'}, 'child': 'Child Text'}}