import os


def change_class_labels_to_zero(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()

            new_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) > 0:
                    parts[0] = '0'  # Change the class label to 0
                    new_lines.append(' '.join(parts))

            with open(file_path, 'w') as file:
                file.write('\n'.join(new_lines))


# Specify the directory containing the YOLO annotation files
directory_path = r'C:\Users\soumy\PycharmProjects\DeepSort\obj_train_data'
change_class_labels_to_zero(directory_path)
