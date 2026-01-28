# Function to check if data conforms to a schema
def is_valid(data: dict, schema: dict) -> bool:
    """
    This function checks whether a given data structure, represented as a dictionary, 
    is valid according to a specified schema. The schema is defined as another dictionary.

    Args:
        data (dict): The data to be checked.
        schema (dict): The schema to check against.

    Returns:
        bool: True if the data conforms to the schema, False otherwise.
    """

    # Iterate over each field in the schema
    for field, field_schema in schema.items():
        # Check if the field is required
        if field_schema == 'required':
            # If the field is required, it must be present in the data
            if field not in data:
                return False

        # If the field is not required, check its type
        elif field in data:
            # Check the type of the field
            if field_schema == 'string':
                # If the field is a string, check if it's a valid string
                if not isinstance(data[field], str):
                    return False

            elif field_schema == 'integer':
                # If the field is an integer, check if it's a valid integer
                if not isinstance(data[field], int):
                    return False

            elif field_schema == 'boolean':
                # If the field is a boolean, check if it's a valid boolean
                if not isinstance(data[field], bool):
                    return False

            # If the field is an object, recursively check its properties
            elif isinstance(data[field], dict):
                # If the field is an object, check if it conforms to its schema
                if not is_valid(data[field], {k: v for k, v in schema.items() if k != field}):
                    return False

    # If we've checked all fields and haven't returned False, the data is valid
    return True