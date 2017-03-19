import os
import shutil
import sys
import cv2


def run():
    FOLDER_NAME = "crop_this"
    cropped_folder = "cropped_it"

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    if not os.path.isdir(FOLDER_NAME):
        print("\nNo folder named '" + FOLDER_NAME + "' found in the current directory.\nExiting...")
        return

    if os.path.isdir(cropped_folder):
        shutil.rmtree(cropped_folder)

    os.mkdir(cropped_folder)

    for folder in os.listdir(FOLDER_NAME):

        os.chdir(FOLDER_NAME + "/" + folder)

        # '.jpg' can be changed to the required file format to look for.
        images = [img for img in os.listdir() if img[-4:] == ".jpg"]

        os.mkdir("../../" + cropped_folder + '/' + folder)

        for image in images:

            img = cv2.imread(image)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            print("Processing " + image)

            # Scale factor (2nd parameter) can be varied according to application - default 1.2
            faces = face_cascade.detectMultiScale(gray, 1.2, 5)

            if len(faces) is not 0:

                print("Face detected")

                for (x, y, w, h) in faces:
                    cropped = img[y:y + h, x:x + w]
                    file_path = "../../" + cropped_folder + '/' + folder + '/' + image
                    cv2.imwrite(file_path, cropped)

                    break
            else:
                print("NO face detected")

        os.chdir("../..")

    sys.exit(0)


if __name__ == '__main__':
    run()
