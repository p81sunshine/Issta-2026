#!/usr/bin/env python

def format(boolean_validation: bool, message: str, return_dict: dict, config_data: dict) -> None:
    """A configuration data validator that populates the provided dictionary with validated values."""
    if not boolean_validation:
        # Load the configuration data without performing any validation if the flag is false
        return_dict.update(config_data)
    else:
        # Perform validation and populate the provided dictionary with validated values
        try:
            # Validate the configuration data
            base_directory = config_data['base_directory']
            num_pictures = int(config_data['num_pictures'])
            num_masks = int(config_data['num_masks'])
            num_markers = int(config_data['num_markers'])
            mask_names = config_data['mask_names']
            marker_names = config_data['marker_names']

            # Check if the base directory exists
            if not os.path.exists(base_directory):
                raise ValueError(f"The base directory '{base_directory}' does not exist")

            # Check if the number of pictures is positive
            if num_pictures <= 0:
                raise ValueError(f"The number of pictures '{num_pictures}' must be positive")

            # Check if the number of masks is positive
            if num_masks <= 0:
                raise ValueError(f"The number of masks '{num_masks}' must be positive")

            # Check if the number of markers is positive
            if num_markers <= 0:
                raise ValueError(f"The number of markers '{num_markers}' must be positive")

            # Check if the mask names are valid
            if not all(isinstance(name, str) for name in mask_names):
                raise ValueError(f"The mask names must be a list of strings")

            # Check if the marker names are valid
            if not all(isinstance(name, str) for name in marker_names):
                raise ValueError(f"The marker names must be a list of strings")

            # Populate the dictionary with validated values
            return_dict.update({
                'base_directory': base_directory,
                'num_pictures': num_pictures,
                'num_masks': num_masks,
                'num_markers': num_markers,
                'mask_names': mask_names,
                'marker_names': marker_names
            })

        except ValueError as error:
            # If validation fails, display the provided message and raise an error
            print(message)
            raise error

# Tests