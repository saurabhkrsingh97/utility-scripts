The script looks for a folder named 'crop_this' (by default) in the same folder as the script
and extracts the cropped faces from the pics, storing them in 'cropped_it' folder with
a pre-defined directory structure.

The following directory structure is recommended for proper functioning:

crop_this
    .
    ...enroll_no_1
        .
        ...one.jpg
        ...two.jpg
        ...three.jpg
    .
    ...enroll_no_2
        .
        ...one.jpg
        ...two.jpg

Output is:
cropped_it
    .
    ...enroll_no_1
        .
        ...one.jpg
        ...two.jpg
        ...three.jpg
    .
    ...enroll_no_2
        .
        ...one.jpg
        ...two.jpg
