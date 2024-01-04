# 🖼️ Image Processing and Organization Script

This Python script is a versatile tool for efficiently processing and organizing images in a specified folder. It provides several functionalities to enhance your image management experience.

## Crop and Rename Images by Aspect Ratio 📐

The script allows you to crop images based on specified aspect ratios and organizes them into folders. The `crop_image_by_ratio` function takes an input image, calculates the desired crop dimensions, and saves the cropped images with new names based on the specified aspect ratios.

## Copy and Rename Images with Subfolders 📁

The `copy_and_rename_images` function organizes images into subfolders, renaming them in a structured manner. It creates a main folder named "images" and subfolders for each image, with names like "image_1," "image_2," etc. The script renames the images based on the desired ratio and saves both the original and cropped images.

## Choose Random Images 🎲

The `choose_random_images` function randomly selects a specified number of images from a source folder and copies them to a destination folder. This functionality is useful for creating a random set of images for various purposes.

## Usage 🚀

1. **Setup:**
   - Install the required libraries: `PIL` (Pillow).
   - Ensure the script is in the same directory as your images or provide the correct source path.

2. **Configuration:**
   - Set the `src_path` variable to the path containing your original images.
   - Specify the `desktop_folder` where the main "images" folder will be created.
   - Adjust the `image_amount` for the number of randomly chosen images.
   - Set the `valid_image_extensions` for the image file types you want to process.
   - Specify the `desired_ratios` for cropping images.

3. **Run the Script:**
   - Execute the script to organize and process your images.

## Example 🌈

```python
# Specify the folder containing the original files
src_path = "/Users/ahmedefepetek/Desktop/Studio Ghibli Inspired Arts"
desktop_folder = "/Users/ahmedefepetek/Desktop"

# Random image amount
image_amount = 5
dst_path_for_random_images = (
    f"/Users/ahmedefepetek/Desktop/Random {image_amount} Images"
)

# Specify the valid image extensions
valid_image_extensions = [".png", ".jpg", ".webp"]

# Specify the desired aspect ratios
desired_ratios = [(9, 16), (3, 4), (4, 5)]

# Call the function with the specified folder and valid extensions
copy_and_rename_images(src_path, valid_image_extensions)

# Choose desired amount of images randomly and copy them to the destination folder
choose_random_images(src_path, dst_path_for_random_images, image_amount)
