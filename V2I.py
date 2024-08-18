import cv2
import os


def create_output_directory(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)



def extract_and_resize_frames(video_path, output_dir, frame_skip=20, size=(500, 500)):
    create_output_directory(output_dir)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Unable to open video file {video_path}")
        return

    frame_count = 0
    saved_frame_count = 0

    while True:
        while frame_count < 3000:
            ret, frame = cap.read()
            if not ret:
                break

            if frame_count % frame_skip == 0:
                if frame is not None:
                    resized_frame = cv2.resize(frame, size)
                    output_path = os.path.join(output_dir, f"Mark_APlalb2_{saved_frame_count:03d}.jpg")
                    cv2.imwrite(output_path, resized_frame)
                    saved_frame_count += 1

            frame_count += 1

    cap.release()
    print(f"Saved {saved_frame_count} frames to {output_dir}")


# Example usage
video_path = r'C:\Users\soumy\PycharmProjects\DeepSort\ArijitMark\lalb2.mkv'
output_dir = 'Video_LALB2'
extract_and_resize_frames(video_path, output_dir)
