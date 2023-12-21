import os
import shutil
import random

def delete_folder(folder_path):
    """Delete a folder and its contents."""
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f"Deleted folder: {folder_path}")
    else:
        print(f"Folder does not exist: {folder_path}")

def keep_subset_of_images_and_labels(image_folder_path, label_folder_path, num_images_to_keep):
    """Keep only a subset of images and their corresponding labels."""
    image_files = os.listdir(image_folder_path)

    # Shuffle the list of images
    random.shuffle(image_files)

    # Keep only the first num_images_to_keep images
    images_to_keep = image_files[:num_images_to_keep]

    # Remove the rest of the images and their corresponding labels
    for image_name in image_files:
        image_path = os.path.join(image_folder_path, image_name)
        label_path = os.path.join(label_folder_path, image_name.replace('.jpg', '.txt'))  # Assuming labels have the same name with .txt extension

        if image_name not in images_to_keep:
            os.remove(image_path)
            os.remove(label_path)

    print(f"Kept {num_images_to_keep} images and labels in folder: {image_folder_path}")

# Specify the paths to your train images and labels folders
train_images_path = 'C:/Users/Ahmed/Sections/Tomato-Detection/data/train/images'
train_labels_path = 'C:/Users/Ahmed/Sections/Tomato-Detection/data/train/labels'

# Keep only 1000 images and their labels in the 'train' folder
num_images_to_keep = 1000
keep_subset_of_images_and_labels(train_images_path, train_labels_path, num_images_to_keep)
