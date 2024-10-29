import os
from typing import List


def get_subdirectorie_path(categorie: str) -> List:
    """
    Retrieves the names of all subdirectories within the specified category directory.

    Parameters:
        categorie (str): The category for which to retrieve subdirectory names.

    Returns:
        list: A list of subdirectory names within the specified category directory.
    """
    #root = f"/final-project/terorist-scrape/images/{categorie}"
    root = f"./images/{categorie}"
    try:
        return [root + "/" + name for name in os.listdir(root) if os.path.isdir(os.path.join(root, name))]
    except FileNotFoundError:
        print(f"The directory '{root}' does not exist.")
        return []


def get_images(subdirectories: List[str]) -> List:
    """
    Retrieves the images of all subdirectories within the specified subdirectories.

    Parameters:
        subdirectories (str): Display path to retrieve subdirectory names.

    Returns:
        list: A list of subdirectory names within the specified category directory.
    """
    image_paths = []

    if isinstance(subdirectories, list):
        for subdirectory in subdirectories:
            if os.path.exists(subdirectory):
                image_paths.extend([
                    os.path.join(subdirectory, file) for file in os.listdir(subdirectory)
                    if os.path.isfile(os.path.join(subdirectory, file))
                ])
    else:  # Tek bir dizin durumu
        if os.path.exists(subdirectories):
            image_paths = [
                os.path.join(subdirectories, file) for file in os.listdir(subdirectories)
                if os.path.isfile(os.path.join(subdirectories, file))
            ]

    return image_paths
