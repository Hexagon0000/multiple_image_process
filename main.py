import os
import time
from PIL import Image
import random


def crop_image_by_ratio(src_path, dst_path, aspect_ratio):
    # Open the image
    image = Image.open(src_path)

    # Get the wiüth and height of the image
    width, height = image.size

    # Calculate the desired crop dimensions based on the aspect ratio
    aspect_ratio_value = aspect_ratio[0] / aspect_ratio[1]
    if width / aspect_ratio_value > height:
        new_width = int(height * aspect_ratio_value)
        new_height = height
    else:
        new_width = width
        new_height = int(width / aspect_ratio_value)

    # Calculate the crop box coordinates (left, upper, right, lower)
    left = (width - new_width) / 2
    upper = (height - new_height) / 2
    right = (width + new_width) / 2
    lower = (height + new_height) / 2

    # Crop the image
    cropped_image = image.crop((left, upper, right, lower))

    # Save the cropped image
    cropped_image.save(dst_path)


def copy_and_rename_images(path, valid_extensions):
    # Get folder count in desired path
    folders_count = get_folders_count()

    # Filter only files with valid image extensions
    files_to_rename = [
        filename
        for filename in os.listdir(path)
        if any(filename.lower().endswith(ext) for ext in valid_extensions)
    ]

    for count, filename in enumerate(files_to_rename):
        # Create directory first for main folder
        directory = os.path.join(desktop_folder, "images")
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        # Construct new file names
        new_filename = f"image_{str(folders_count+count+1)}(original_ratio).png"

        # Create subfolder for better organization
        sub_directory = os.path.join(directory, f"image_{str(folders_count+count+1)}")
        os.makedirs(sub_directory, exist_ok=True)

        # Create source and destination paths
        src = os.path.join(path, filename)
        dst = os.path.join(sub_directory, new_filename)

        if os.path.isfile(src):
            # Copy the file to a new destination
            with open(src, "rb") as src_file, open(dst, "wb") as dst_file:
                dst_file.write(src_file.read())

        # Crop and save the image with the desired ratios
        for ratio in desired_ratios:
            new_filename = f"image_{str(count+1)}({ratio[0]}_{ratio[1]}_ratio).png"
            dst = os.path.join(sub_directory, new_filename)
            crop_image_by_ratio(src, dst, ratio)

        print(
            f"All images were renamed and resized by the desired ratio to {directory}"
        )
        print(
            "Don't forget to change source path next time beacuse you didn't write yet:)"
        )


def get_folders_count(path):
    # Use os.listdir() to get a list of all items in the specified path
    items = os.listdir(path)

    # Use a list comprehension to filter out only the folders
    folders = [item for item in items if os.path.isdir(os.path.join(path, item))]

    return len(folders)


def choose_random_images(scr_path, dst_path, image_amount):
    # Get a list of all files (images) in the source folder
    all_images = [
        file
        for file in os.listdir(scr_path)
        if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp"))
    ]

    # Choose 'num_images_to_copy' random images
    selected_images = random.sample(all_images, min(image_amount, len(all_images)))

    # Create the destination folder if it doesn't exist
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)

    # Copy selected images to the destination folder
    for image in selected_images:
        source_path = os.path.join(scr_path, image)
        destination_path = os.path.join(dst_path, image)

        # Open the image using PIL
        with Image.open(source_path) as img:
            # Save the image to the destination folder
            img.save(destination_path)


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

# Choose desird amount of images random and copy them to the destination folder
choose_random_images(src_path, dst_path_for_random_images, image_amount)
