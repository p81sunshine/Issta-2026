from solution import *

import math

from solution import *

import math

from solution import *

import math

def test_color_selector_initialization():
    cs = ColorSelector("path_to_your_image.png")
    assert cs.image_path == "path_to_your_image.png"
    assert cs.colors == []
    assert cs.window_name == 'Image'
    assert cs.prompts == ["Select color 1", "Select color 2", "Select color 3"]
    assert cs.current_prompt_index == 0

def test_image_loading():
    cs = ColorSelector("path_to_a_valid_image.png")
    image = cv2.imread("path_to_a_valid_image.png")
    assert np.array_equal(cs.image, image)

# Create other test functions as necessary to simulate clicks and verify the selected colors