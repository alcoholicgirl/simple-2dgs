import glob
from PIL import Image
import os

def make_gif(frame_folder):
    files = glob.glob(f"{frame_folder}/*.png")
    files.sort(key=lambda x: int(os.path.basename(x).split('.')[0]))
    
    frames = [Image.open(image) for image in files]
    
    if frames:
        frame_one = frames[0]
        frame_one.save(
            "output.gif", 
            format="GIF", 
            append_images=frames[1:],
            save_all=True, 
            duration=50,
            loop=0
        )
        print(f"GIF saved as output.gif with {len(frames)} frames.")
    else:
        print("No PNG files found in the specified folder.")

if __name__ == "__main__":
    make_gif("outputs")
