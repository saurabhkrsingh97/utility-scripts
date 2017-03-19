import os
import shutil
import sys
import cv2


def run():
    FOLDER_NAME = "crop_this"  # The folder it looks for in the current directory
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cropped_folder = "cropped_it"

    if not os.path.isdir(FOLDER_NAME):
        print("\nNo folder named '" + FOLDER_NAME + "' found in the current directory.\nExiting...")
        return

    if os.path.isdir(cropped_folder):
        shutil.rmtree(cropped_folder)

    os.mkdir(cropped_folder)
    for folder in os.listdir(FOLDER_NAME):
        i = 0
        os.chdir(FOLDER_NAME + "/" + folder)

        images = [img for img in os.listdir() if img[-4:] == ".jpg"]

        print(images)
        os.mkdir("../../" + cropped_folder + '/' + folder)

        for image in images:

            img = cv2.imread(image)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            print(image + " read.")

            faces = face_cascade.detectMultiScale(gray, 1.2, 5)

            if len(faces) is not 0:
                print("face detected")
                for (x, y, w, h) in faces:
                    cropped = img[y:y + h, x:x + w]

                    filepath = "../../" + cropped_folder + '/' + folder + '/' + image
                    cv2.imwrite(filepath, cropped)
                    break
                i += 1
            else:
                print("face not detected")

        os.chdir("../..")
        pass

    cv2.destroyAllWindows()
    sys.exit(0)


if __name__ == '__main__':
    run()
