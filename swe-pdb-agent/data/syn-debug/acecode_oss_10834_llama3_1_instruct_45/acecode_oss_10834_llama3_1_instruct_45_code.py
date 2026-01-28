def run_experiments(experiments):
    """
    Execute experiments based on the provided descriptions.

    Args:
    experiments (list): A list of strings representing experiment descriptions.

    Returns:
    list: A list of results where each result corresponds to the successful execution of its respective experiment.
    """
    results = []
    for experiment in experiments:
        # Split the experiment description into name and parameters
        name, params = experiment.split(':')
        if not name.strip():  # Check if the name is not empty
            results.append('Error')
            continue

        params = params.split(',')
        params_dict = {}
        for param in params:
            # Check if the parameter is in the correct format (key-value pair)
            if '=' in param:
                key, value = param.split('=')
                try:
                    value = int(value)  # Try to convert the value to an integer
                except ValueError:
                    pass  # If not an integer, just store it as a string
                params_dict[key] = value
            else:
                results.append('Error')
                break  # If a parameter is not in the correct format, skip the rest of the experiment
        else:
            # If the experiment is valid, format the result and append it to the list
            results.append(f'{name} executed with parameters {params_dict}')

    return results