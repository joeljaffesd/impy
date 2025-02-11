from PIL import Image
from colorsys import hsv_to_rgb
import tkinter as tk
from tkinter import filedialog

# Open an image file
image_path = './images/test.png'
with Image.open(image_path) as img:
  # Convert the image to RGBA
  img = img.convert("RGBA")

  # Create a new image with a 1-pixel border
  bordered_img = Image.new("RGBA", (img.width + 2, img.height + 2), (0, 0, 0, 0))

  # Paste the original image onto the bordered image
  bordered_img.paste(img, (1, 1))

  # Convert HSV to RGB
  hsv_value = (0.0, 0.0, 0.0)  # Example HSV value
  rgb_value = tuple(int(i * 255) for i in hsv_to_rgb(*hsv_value))

  # Draw the border
  for x in range(bordered_img.width):
    bordered_img.putpixel((x, 0), rgb_value + (255,))
    bordered_img.putpixel((x, bordered_img.height - 1), rgb_value + (255,))
  for y in range(bordered_img.height):
    bordered_img.putpixel((0, y), rgb_value + (255,))
    bordered_img.putpixel((bordered_img.width - 1, y), rgb_value + (255,))

  # Show the image with the border
  def save_image():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
      bordered_img.save(file_path)

  # Show the image with the border
  bordered_img.show()

  # Create a pop-up to save the image
  save_image()