import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont

# Create the main application window
root = tk.Tk()
root.title("Image Watermark Tool")

# Create a StringVar to store and update the watermark text
watermark_text_var = tk.StringVar()
watermark_text_var.set("Your Watermark")  # Set the initial watermark text


# Function to open a file dialog for selecting an image file
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")])
    if file_path:
        add_watermark(file_path)


# Function to calculate font size based on a percentage of the image size
def calculate_font_size(image_size, percentage):
    return int(min(image_size) * percentage / 100)


# Function to add a watermark to the selected image
def add_watermark(image_path):
    try:
        # Open the selected image
        original_image = Image.open(image_path)
        img_width, img_height = original_image.size

        # Create a transparent image for the watermark text
        watermark_image = Image.new("RGBA", original_image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(watermark_image)

        # Get the watermark text from the StringVar
        watermark_text = watermark_text_var.get()

        # Calculate the font size as a percentage of image size
        font_size_percentage = 18  # Change the percentage as needed
        font_size = calculate_font_size(original_image.size, font_size_percentage)

        # Use a custom TrueType font file with a larger font size
        font_path = "louis_george_cafe/LouisGeorgeCafe.ttf"  # Replace with the path to your custom font file
        font = ImageFont.truetype(font_path, font_size)

        # Calculate the position to center the watermark
        text_bbox = draw.textbbox((0, 0), watermark_text, font)
        x = (img_width - text_bbox[2]) / 2
        y = (img_height - text_bbox[3]) / 2

        # Set the watermark text color and opacity (RGBA format)
        text_color = (255, 255, 255, 80)  # White with opacity (0-255)

        # Add the watermark text to the transparent image
        draw.text((x, y), watermark_text, font=font, fill=text_color)

        # Composite the watermark image onto the original image
        watermarked_image = Image.alpha_composite(original_image.convert("RGBA"), watermark_image)

        # Save the watermarked image
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            watermarked_image.save(save_path)
            messagebox.showinfo("Success", "Watermark added and image saved successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Create a label and text entry field for changing the watermark text
text_label = tk.Label(root, text="Watermark Text:")
text_label.pack()
text_entry = tk.Entry(root, textvariable=watermark_text_var)
text_entry.pack()

# Create the "Open Image" button
open_button = tk.Button(root, text="Open Image", command=open_file)
open_button.pack(pady=20)

# Run the application
root.mainloop()
