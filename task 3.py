import os
import shutil

# Folder path to organize
folder_path = input("Enter folder path: ")

# File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Programs": [".py", ".java", ".c", ".cpp"]
}

def create_folder(folder_name):
    path = os.path.join(folder_path, folder_name)

    if not os.path.exists(path):
        os.mkdir(path)


def organize_files():

    for folder in file_types:
        create_folder(folder)

    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(file)[1].lower()

        moved = False

        for folder, extensions in file_types.items():
            if file_extension in extensions:

                destination = os.path.join(folder_path, folder, file)

                shutil.move(file_path, destination)

                print(file, "moved to", folder)
                moved = True
                break

        if not moved:
            print(file, "does not match any category")


# Run automation
organize_files()

print("\nFile organization completed successfully!")