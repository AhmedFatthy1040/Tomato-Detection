import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np

# Function to read labels
def read_labels(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

# Function to read labels and count the occurrences of each class
def count_class_occurrences(label_path, class_names):
    class_counts = {class_name: 0 for class_name in class_names}

    with open(label_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            label = line.strip().split()
            label_class = int(label[0])
            class_name = class_names[label_class]
            class_counts[class_name] += 1

    return class_counts

# Function to visualize images with bounding boxes
def visualize_image(image_path, label_path, class_names):
    image = Image.open(image_path)
    labels = read_labels(label_path)

    fig, ax = plt.subplots(1)
    ax.imshow(image)

    for label in labels:
        label = label.strip().split()
        label_class = int(label[0])
        x, y, width, height = map(float, label[1:])
        
        # Display bounding boxes for specific classes
        if class_names[label_class] == 'Rotten Tomato':
            rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='r', facecolor='none')
            ax.add_patch(rect)

    plt.show()

# Function to visualize a subset of images
def visualize_sample_images(images_path, labels_path, class_names, num_samples=5):
    sample_counter = 0

    for image_file in os.listdir(images_path):
        if image_file.endswith(".jpg") and sample_counter < num_samples:
            image_path = os.path.join(images_path, image_file)
            label_path = os.path.join(labels_path, image_file.replace(".jpg", ".txt"))

            visualize_image(image_path, label_path, class_names)

            sample_counter += 1
            
# Function to plot the distribution of classes
def plot_class_distribution(dataset_name, class_counts):
    fig, ax = plt.subplots()
    ax.bar(class_counts.keys(), class_counts.values())
    ax.set_xlabel('Class')
    ax.set_ylabel('Count')
    ax.set_title(f'Distribution of Classes in the {dataset_name} Dataset')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Function to explore and visualize a dataset
def explore_dataset(dataset_name, images_path, labels_path, class_names, num_samples=5):
    total_class_counts = {class_name: 0 for class_name in class_names}

    for label_file in os.listdir(labels_path):
        if label_file.endswith(".txt"):
            label_path = os.path.join(labels_path, label_file)
            class_counts = count_class_occurrences(label_path, class_names)

            # Update total class counts
            for class_name, count in class_counts.items():
                total_class_counts[class_name] += count

    plot_class_distribution(dataset_name, total_class_counts)
    visualize_sample_images(images_path, labels_path, class_names, num_samples)

# Define the paths to your datasets
train_images_path = 'path/to/train/images'
train_labels_path = 'path/to/train/labels'
val_images_path = 'path/to/val/images'
val_labels_path = 'path/to/val/labels'
test_images_path = 'path/to/test/images'
test_labels_path = 'path/to/test/labels'

# Load class names from data.yaml
class_names = ["0", "1", "Fresh Tomato", "Rotten Tomato", "object"]

# Explore and visualize the training dataset
explore_dataset('Training', train_images_path, train_labels_path, class_names)

# Explore and visualize the validation dataset
explore_dataset('Validation', val_images_path, val_labels_path, class_names)

# Explore and visualize the test dataset
explore_dataset('Test', test_images_path, test_labels_path, class_names)
