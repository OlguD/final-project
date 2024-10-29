import cv2 as cv
from core import get_subdirectorie_path, get_images


def extract_feature(imgPath: str):
    """
    param: {
        imgPath: str
    }
    extracts features for given img
    """
    img = cv.imread(imgPath, cv.IMREAD_COLOR)
    if img is None:
        print(f"Error: Unable to open image at {imgPath}")

    # show image
    cv.imshow("image", img)

    # wait any key to destroy window
    cv.waitKey(0)
    cv.destroyAllWindows()



# print(get_subdirectorie_path("yellow"))
# print(get_subdirectorie_path("orange"))
# print(get_subdirectorie_path("red"))
#print(get_subdirectorie_path("grey"))
#print(get_images(get_subdirectorie_path("grey")))
images = get_images(get_subdirectorie_path("grey"))
if images:
    extract_feature(images[5])
else:
    print("No images found in the specified directory.")
