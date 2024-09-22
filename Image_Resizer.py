from PIL import Image
import io
import imageio
import numpy as np

def resize_image(image, target_height_px, target_width_px):
    return image.resize((target_width_px, target_height_px), Image.LANCZOS)

def calculate_image_size(image, quality=85):
    buffer = io.BytesIO()
    image.save(buffer, format='JPEG', quality=quality)
    size_kb = buffer.tell() / 1024
    return size_kb

def add_noise_to_image(image, intensity=10):
    img_array = np.array(image)
    noise = np.random.randint(-intensity, intensity, img_array.shape, dtype='int16')
    noisy_img_array = np.clip(img_array + noise, 0, 255).astype('uint8')
    noisy_img = Image.fromarray(noisy_img_array)
    return noisy_img

def adjust_image_size(image, min_size_kb, max_size_kb):
    # Initial size check
    initial_size_kb = calculate_image_size(image)
    
    # If the image is already within the desired size range
    if min_size_kb <= initial_size_kb <= max_size_kb:
        return image, initial_size_kb
    
    # Adjust quality to achieve the desired file size
    quality = 85
    final_size_kb = initial_size_kb
    
    # Increase or decrease the image size by adding noise if it's smaller than the desired range
    if final_size_kb < min_size_kb:
        while final_size_kb < min_size_kb:
            image = add_noise_to_image(image)
            final_size_kb = calculate_image_size(image, quality=quality)
            
            if final_size_kb >= min_size_kb:
                return image, final_size_kb
    
    else:
        while final_size_kb > max_size_kb or final_size_kb < min_size_kb:
            buffer = io.BytesIO()
            image.save(buffer, format='JPEG', quality=quality)
            final_size_kb = buffer.tell() / 1024
            
            if min_size_kb <= final_size_kb <= max_size_kb:
                return image, final_size_kb
            
            if final_size_kb < min_size_kb:
                quality -= 1 
            elif final_size_kb > max_size_kb:
                quality -= 5 
            
            if quality < 1:
                return image, final_size_kb

def process_image(image_path, output_path, target_height_px, target_width_px, min_size_kb, max_size_kb):
    img = Image.open(image_path)
    # Step 1: Resize image dimensions
    img = resize_image(img, target_height_px, target_width_px)
    # Step 2: Adjust image file size (increase or decrease)
    img, final_size_kb = adjust_image_size(img, min_size_kb, max_size_kb)
    # Step 3: Save the final image
    img.save(output_path, format='JPEG')
    
    print(f"Image saved at {output_path} with final size: {final_size_kb:.2f} KB")



image_path = 'input.jpg'
output_path = 'final_output.jpg'

# Resize dimensions in pixels
target_height_px = 300 
target_width_px = 450  

# Target file size range in KB
min_size_kb = 50  
max_size_kb = 100  

process_image(image_path, output_path, target_height_px, target_width_px, min_size_kb, max_size_kb)
