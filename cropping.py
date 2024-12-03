# File: ai_photo_cropper.py

import cv2
import numpy as np
from tkinter import Tk, filedialog, messagebox
import os
print("3:2 type 1")
print("1:1 type 2")
op1 = input("Enter your choice")

if op1 == 2:
    def crop_to_square(image_path, output_path="cropped_image.jpg"):
    """
    Crop an image to a 1:1 aspect ratio by centering the crop.
    :param image_path: Path to the input image.
    :param output_path: Path to save the cropped image.
    """
    try:
        # Read the image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Unable to read the image. Please check the file path.")
        
        # Get dimensions
        height, width = image.shape[:2]
        
        # Determine the size of the square
        square_size = min(height, width)
        
        # Calculate the cropping region
        start_x = (width - square_size) // 2
        start_y = (height - square_size) // 2
        
        # Crop the image
        cropped_image = image[start_y:start_y + square_size, start_x:start_x + square_size]
        
        # Save the cropped image
        cv2.imwrite(output_path, cropped_image)
        print(f"Image successfully cropped and saved at {output_path}")
    except Exception as e:
        print(f"Error: {e}")
        def select_and_crop_image():
    """
    GUI-based method to select an image and crop it.
    """
    # Create a Tkinter root window
    root = Tk()
    root.withdraw()  # Hide the main window

    try:
        # Open file dialog to select an image
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
        )
        if not file_path:
            messagebox.showinfo("Info", "No file selected.")
            return

        # Generate output file path
        base_name = os.path.basename(file_path)
        name, ext = os.path.splitext(base_name)
        output_path = os.path.join(os.path.dirname(file_path), f"{name}_cropped{ext}")

        # Crop the image
        crop_to_square(file_path, output_path)

        # Notify user
        messagebox.showinfo("Success", f"Cropped image saved at: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


    

if __name__ == "__main__":
    # Uncomment the following line for CLI usage:
    # crop_to_square("path_to_image.jpg", "output_image.jpg")

    # For GUI usage
    select_and_crop_image()

    


