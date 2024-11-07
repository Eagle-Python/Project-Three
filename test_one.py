from PIL import Image

# Load the sprite sheet
sprite_sheet_path = 'Attack1.png'
sprite_sheet = Image.open(sprite_sheet_path)

# Define frame dimensions (based on visual inspection of the warrior)
frame_width = 200 # Width of each frame
frame_height = 200 # Height of each frame (assuming all frames are the same height)

# Calculate the number of frames
num_frames = sprite_sheet.width // frame_width

# Extract each frame and save as individual images
frame_paths = []
for i in range(num_frames):
    left = i * frame_width
    right = left + frame_width
    frame = sprite_sheet.crop((left, 0, right, frame_height))
    frame_path = f"frame_{i}.gif"  # Save each frame as a GIF for turtle compatibility
    frame.save(frame_path, format="GIF")
    frame_paths.append(frame_path)

# img = Image.open('l4r.jpg')
# img.save('l4.gif')