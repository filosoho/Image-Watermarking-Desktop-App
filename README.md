# Image-Watermarking-Desktop-App
This Python application allows you to easily add watermarks to your images. You can choose an image file, specify the watermark text, adjust the font size and opacity, and save the watermarked image.  

## Features

- Open and select an image file in common formats such as JPG, JPEG, PNG, GIF, and BMP.
- Customize the watermark text to your liking.
- Adjust the font size as a percentage of the image size.
- Set the opacity (transparency) of the watermark text.
- Use a custom TrueType font file for the watermark text.

## Prerequisites

Before running the program, ensure you have the following prerequisites installed:

- Python 3.x
- Pillow (PIL Fork) library: You can install it using pip with the following command:

~~~
pip install Pillow
~~~


## How to Use

1. Clone or download this repository to your local machine.

2. Run the program:

~~~
Image_Watermarking.py
~~~


3. Specify the watermark text in the input field.   

4. Click the "Open Image" button to select an image file.

5. Choose a destination folder and enter a filename for the watermarked image.


## Customizing Watermarks

You can customize the watermark by modifying the following parameters in the code:

- `font_size_percentage`: Adjust the font size as a percentage of the image size.
- `font_path`: Specify the path to your custom TrueType font file.
- `text_color`: Set the watermark text color and opacity (in RGBA format).


## License

Feel free to use and modify the code as per your requirements.

## Acknowledgments

- This program uses the Pillow (PIL Fork) library for image processing.
- Special thanks to the open-source community for their contributions to the Python ecosystem.


