import os
from PIL import Image

# Folder with images
folder_path = '/Users/umairdada/Documents/GitHub/ABT-Website/downloaded_google_images/new'
base_name = 'image'

# Supported image formats (only input formats)
image_extensions = ['.jpg', '.jpeg', '.png']

# Create a list of images
images = [f for f in os.listdir(folder_path)
          if os.path.isfile(os.path.join(folder_path, f)) and os.path.splitext(f)[1].lower() in image_extensions]
images.sort()

# Process and rename images
for i, filename in enumerate(images, start=1):
    file_path = os.path.join(folder_path, filename)
    name, ext = os.path.splitext(filename)
    ext = ext.lower()
    new_name = f"{base_name}{i:02d}.jpg"
    new_path = os.path.join(folder_path, new_name)

    # Convert PNG to JPEG
    if ext == '.png':
        with Image.open(file_path) as img:
            rgb_img = img.convert('RGB')  # JPEG doesn't support transparency
            rgb_img.save(new_path, 'JPEG')
        os.remove(file_path)  # Remove the original PNG
        print(f"Converted and renamed: {filename} → {new_name}")
    else:
        os.rename(file_path, new_path)
        print(f"Renamed: {filename} → {new_name}")
