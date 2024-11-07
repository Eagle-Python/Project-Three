# from PIL import Image
# import turtle
#
# # Step 1: Open and resize the warrior using Pillow
# original_image = Image.open("turtle_resized_50x50.gif")
# resized_image = original_image.resize((50, 50))  # Resize to desired dimensions
# resized_image.save("turtle_resized_50x50.gif")  # Save resized warrior as a new GIF
#
# # Step 2: Initialize turtle screen and load the resized custom shape
# screen = turtle.Screen()
# screen.addshape("turtle_resized_50x50.gif")
#
# # Step 3: Create a turtle and set it to use the resized shape
# t = turtle.Turtle()
# t.shape("turtle_resized_50x50.gif")
#
# # Sample movement
# t.forward(100)
#
# # Keep the window open until closed by the user
# turtle.done()
#
#

# from PIL import Image
#
# img = Image.open("")


# # Open the warrior
# img = Image.open("background.png")
#
# # Apply blur effect
# blurred_img = img.filter(ImageFilter.GaussianBlur(3))  # Adjust the blur radius
#
# # Save the blurred warrior
# blurred_img.save("blurred_background.gif")


# # For Changing Blurred Effect
# from PIL import Image, ImageFilter
#
# img = Image.open("enemy.gif")
#
# blurred_img = img.filter(ImageFilter.GaussianBlur(3))
# blurred_img.save("")

# from Animation to each photo
from PIL import Image
import os

# Load the GIF file
gif_path = "background.gif"  # Replace with the path to your GIF file
output_folder = "gif_frames"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Open the GIF
with Image.open(gif_path) as gif:
    # Loop through each frame in the GIF
    for frame_number in range(gif.n_frames):
        # Select the frame
        gif.seek(frame_number)

        # Save the current frame as a separate warrior file
        frame_path = os.path.join(output_folder, f"frame_{frame_number}.png")
        gif.save(frame_path, format="PNG")
        print(f"Saved {frame_path}")

# from PIL import Image
#
# img = Image.open('test-one-c.jpg')
# img.save("test-one-c.gif")