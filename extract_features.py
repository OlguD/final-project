import cv2 as cv
from core import get_subdirectorie_path, get_images

def extract_feature(imgPath: str, categorie: str):
    """
    param: {
        imgPath: str
    }
    extracts features for given img
    """
    gray_img = cv.imread(imgPath, cv.COLOR_BGR2GRAY)
    if gray_img is None:
        print(f"Error: Unable to open image at {imgPath}")


    xml_path = "cvFaceDetection/haarcascade_frontalface_default.xml"
    # Loading the required haar-cascade xml classifier file
    haar_cascade = cv.CascadeClassifier(xml_path)

    # Applying the face detection method on the grayscale image
    faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)

    # Iterating through rectangles of detected faces
    rgb = None
    if categorie == "red":
        rgb = (0, 0, 255)
    elif categorie == "orange":
        rgb = (0, 165, 255)
    elif categorie == "grey":
        rgb = (128, 128, 128)
    elif categorie == "yellow":
        rgb = (0, 255, 255)

    for (x, y, w, h) in faces_rect:
        cv.rectangle(gray_img, (x, y), (x+w, y+h), rgb, 2)

    cv.imshow('Detected faces', gray_img)

    # wait any key to destroy window
    cv.waitKey(0)
    cv.destroyAllWindows()



# print(get_subdirectorie_path("yellow"))
# print(get_subdirectorie_path("orange"))
# print(get_subdirectorie_path("red"))
#print(get_subdirectorie_path("grey"))
#print(get_images(get_subdirectorie_path("grey")))
categorie = "yellow"
images = get_images(get_subdirectorie_path(categorie))
if images:
    extract_feature(images[11], categorie=categorie)
else:
    print("No images found in the specified directory.")
