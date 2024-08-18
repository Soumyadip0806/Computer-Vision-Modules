import os
import shutil

def separate_files(source_folder, jpg_folder, txt_folder):
    # Create folders if they don't exist
    for folder in [jpg_folder, txt_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Loop through files in source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        if os.path.isfile(source_path):
            # Determine file type based on extension
            if filename.lower().endswith('.jepg'):
                shutil.move(source_path, os.path.join(jpg_folder, filename))
            elif filename.lower().endswith('.xml'):
                shutil.move(source_path, os.path.join(txt_folder, filename))

# Replace these paths with your actual source folder, JPG folder, and TXT folder paths
source_folder = "archive"
jpg_folder = "images"
txt_folder = "labels"

# Call the function
separate_files(source_folder, jpg_folder, txt_folder)

