import random
import os
import shutil

def f2():
    txts_path = "labels"
    images_path = "images"

    txts = os.listdir(txts_path)
    images = os.listdir(images_path)

    # print(txts)

    txt_image = []

    # Matching text and image files based on filenames
    for txt_file in txts:
        if txt_file.endswith(".txt"):  # Assuming text files have .txt extension
            image_file = txt_file.replace(".txt", ".jpg")  # Assuming images have .jpg extension
            txt_image.append([os.path.join(txts_path, txt_file), os.path.join(images_path, image_file)])

    # Shuffling the list
    random.shuffle(txt_image)
    # print(txt_image)

    # Splitting into train and validation sets
    train_size = int(len(txt_image) * 0.8)
    train_data = txt_image[:train_size]
    val_data = txt_image[train_size:]

    # Destination directories
    train_image_path = r"train\images"
    train_label_path = r"train\labels"
    val_image_path = r"val\images"
    val_label_path = r"val\labels"

    # Creating directories if they don't exist
    os.makedirs(train_image_path, exist_ok=True)
    os.makedirs(train_label_path, exist_ok=True)
    os.makedirs(val_image_path, exist_ok=True)
    os.makedirs(val_label_path, exist_ok=True)

    # Copying files to respective directories
    for i, (txt_file, img_file) in enumerate(train_data):
        shutil.copy(img_file, os.path.join(train_image_path, f"image_{i}.jpg"))
        shutil.copy(txt_file, os.path.join(train_label_path, f"image_{i}.txt"))

    for i, (txt_file, img_file) in enumerate(val_data):
        shutil.copy(img_file, os.path.join(val_image_path, f"image_{i+len(train_data)}.jpg"))
        shutil.copy(txt_file, os.path.join(val_label_path, f"image_{i+len(train_data)}.txt"))
