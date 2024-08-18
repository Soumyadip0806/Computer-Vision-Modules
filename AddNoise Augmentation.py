import os
import cv2
import numpy as np
import random


def add_salt_pepper_noise(image, amount=0.02):
    row, col, ch = image.shape
    noisy = np.copy(image)
    num_salt = np.ceil(amount * image.size * 0.5)
    num_pepper = np.ceil(amount * image.size * 0.5)

    # Salt
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy[coords[0], coords[1], :] = 255

    # Pepper
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy[coords[0], coords[1], :] = 0
    return noisy


def draw_noisy_lines(image, num_lines=5, line_thickness=1):
    row, col, _ = image.shape
    noisy = np.copy(image)
    horizontal = random.choice([True, False])

    for _ in range(num_lines):
        intensity = np.random.randint(200, 256)
        if horizontal:
            y = np.random.randint(0, row)
            cv2.line(noisy, (0, y), (col, y), (intensity, intensity, intensity), line_thickness)
        else:
            x = np.random.randint(0, col)
            cv2.line(noisy, (x, 0), (x, row), (intensity, intensity, intensity), line_thickness)
    return noisy


def add_fog_noise(image, ksize=(5, 5)):
    return cv2.GaussianBlur(image, ksize, 0)


def add_film_grain(image, amount=0.02):
    row, col, ch = image.shape
    gauss = np.random.normal(0, 1, (row, col, ch))
    noisy = image + image * gauss * amount
    noisy = np.clip(noisy, 0, 255)
    return noisy.astype(np.uint8)


def augment_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    noise_functions = [add_salt_pepper_noise, draw_noisy_lines, add_fog_noise, add_film_grain]

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(input_folder, filename)
            image = cv2.imread(img_path)
            noise_func = random.choice(noise_functions)
            noisy_image = noise_func(image)
            output_path = os.path.join(output_folder, f"{filename}")
            cv2.imwrite(output_path, noisy_image)



# Example usage
input_folder = r'C:\Users\soumy\PycharmProjects\DeepSort\Arijit'
output_folder = r'C:\Users\soumy\PycharmProjects\DeepSort\output_images'
augment_images(input_folder, output_folder)
