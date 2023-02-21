import os
from moviepy.video.io.VideoFileClip import VideoFileClip

input_dir = "C:\\Users\\khowz\\Movcon Fold"
output_dir = os.path.join(input_dir, 'output')

def convert_mov_to_mp4(input_dir, output_dir):
    # Create an output directory
    os.makedirs(output_dir, exist_ok=True)

    # Loop through all the MOV files in the input directory
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.MOV') or file_name.endswith('.mov'):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name[:-4] + '.mp4')
            print(f'Converting {file_name} to {output_path}')

            # Convert the MOV file to an MP4 file
            video_clip = VideoFileClip(input_path)
            video_clip.write_videofile(output_path)

            print(f'Converted {file_name} to {output_path}')

print(f'Input directory: {input_dir}')
print(f'Output directory: {output_dir}')

# Example usage:
convert_mov_to_mp4(input_dir, output_dir)
