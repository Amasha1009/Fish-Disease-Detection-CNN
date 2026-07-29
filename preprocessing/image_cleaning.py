import os
from PIL import Image

def remove_corrupted_images(folder_path):
    """
    Remove corrupted or unreadable images from a folder.
    """

    deleted = 0
    checked = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            checked += 1

            try:
                with Image.open(file_path) as img:
                    img.verify()

            except Exception:
                print(f"Deleting corrupted image: {filename}")
                os.remove(file_path)
                deleted += 1

    print("\nCleaning completed.")
    print(f"Images checked : {checked}")
    print(f"Images removed : {deleted}")


if __name__ == "__main__":
    dataset_folder = "dataset"
    remove_corrupted_images(dataset_folder)