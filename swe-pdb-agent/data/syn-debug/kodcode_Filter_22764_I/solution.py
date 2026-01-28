import cv2
import numpy as np

class ColorSelector:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        self.colors = []
        self.window_name = 'Image'
        self.prompts = ["Select color 1", "Select color 2", "Select color 3"]
        self.current_prompt_index = 1

    def select_color(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            b, g, r = self.image[y, x]
            selected_color = (b, g, r)
            print(f"{self.prompts[self.current_prompt_index - 1]} at position {(x, y)}: {selected_color}")
            self.colors.append(selected_color)
            self.current_prompt_index += 1
            if self.current_prompt_index < len(self.prompts):
                cv2.displayOverlay(self.window_name, self.prompts[self.current_prompt_index - 1], 2000)
            else:
                cv2.destroyAllWindows()

    def run(self):
        if self.image is None:
            print(f"Error: Unable to read image '{self.image_path}'")
            return

        cv2.namedWindow(self.window_name)
        cv2.setMouseCallback(self.window_name, self.select_color)

        cv2.imshow(self.window_name, self.image)
        cv2.displayOverlay(self.window_name, self.prompts[self.current_prompt_index - 1], 2000)
        cv2.waitKey(0)

        print(f"Selected colors: {self.colors}")
        with open("selected_colors.txt", "w") as file:
            for i, color in enumerate(self.colors, start=1):
                file.write(f"Color {i}: {color}\n")

if __name__ == "__main__":
    cs = ColorSelector("path_to_your_image.png")
    cs.run()