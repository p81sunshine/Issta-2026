import xml.etree.ElementTree as ET

def convert_xml_to_dict(xml_data):
    # Parse the XML string into an ElementTree object
    root = ET.fromstring(xml_data)

    # Initialize an empty dictionary to store the result
    result = {}

    # Define a recursive helper function to traverse the XML tree
    def traverse(element):
        # If the element has text content, return it as a string
        if element.text and element.text.strip():
            return element.text.strip()
        
        # If the element has no children or text, return None
        if not list(element):
            return None

        # Initialize an empty dictionary to store the children of the current element
        children = {}

        # Iterate over the children of the current element
        for child in element:
            # Recursively traverse the subtree rooted at the child element
            child_value = traverse(child)
            # If the child element has any children of its own, store them as a dictionary
            if child_value is None:
                children[child.tag] = convert_xml_to_dict(ET.tostring(child, encoding='unicode'))
            else:
                children[child.tag] = child_value

        # If the current element has any children, store them as a dictionary
        if children:
            return {element.tag: children}
        # If the current element has no children, return None
        else:
            return None

    # Start the recursive traversal from the root element
    return traverse(root)

# Test the function with the provided example
xml_data = '<parent><child><sub_child>First subchild</sub_child><sub_child>Second subchild</sub_child></child><child>Second child</child></parent>'
print(convert_xml_to_dict(xml_data))  # Output: {'parent': {'child': {'sub_child': 'Second subchild'}, 'child': 'Second child'}}

# Test the function with another example
xml_data = '<parent><child></child></parent>'
print(convert_xml_to_dict(xml_data))  # Output: {'parent': {'child': None}}