import os

# Get the path to the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Folder names
folders = [f"Folder_{i+1}" for i in range(5)]

# Create the folders
for folder in folders:
    folder_path = os.path.join(desktop_path, folder)
    try:
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")
    except FileExistsError:
        print(f"Folder already exists: {folder_path}")
