## face_cropper

The script looks for a folder named *crop_this* (by default) in the same folder as the script
and extracts the cropped faces from the pics, storing them in *cropped_it* folder with
a pre-defined directory structure.

The following directory structure is recommended for proper functioning:

    crop_this
        ├── enroll_1
        │   ├── image_1.jpg
        │   ├── image_2.jpg
        │   └── image_3.jpg
        └── enroll_2
            ├── image_1.jpg
            └── image_2.jpg


Output is:

    cropped_it
        ├── enroll_1
        │   ├── image_1.jpg
        │   ├── image_2.jpg
        │   └── image_3.jpg
        └── enroll_2
            ├── image_1.jpg
            └── image_2.jpg


Default folder name can be changed by changing the value of FOLDER_NAME variable.

Requires cv2 for face detection using the Haar Cascade file provided.
