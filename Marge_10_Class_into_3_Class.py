import os

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        if line.strip().startswith(('0', '1', '3', '4', '5', '6', '7', '8')):
            modified_lines.append('0' + line[1:])
        elif line.strip().startswith('2'):
            modified_lines.append('2' + line[1:])
        elif line.strip().startswith('9'):
            modified_lines.append('9' + line[1:])
        else:
            modified_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            process_file(file_path)

# Specify the folder containing the text files
folder_path = r'C:\Users\soumy\PycharmProjects\GUI pYQT\labels'

# Run the script for the specified folder
process_folder(folder_path)
