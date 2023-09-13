from moviepy.editor import *
from moviepy import *
import random 



def image_resizer(videoclip,image):
    print("function has started")
    
    print("the height is", videoclip.h ,", the wirthd is ", videoclip.w)
    while videoclip.h - image.h > 100 and videoclip.w - image.w > 80:
        print("loop has started")
        image = image.resize(1.1)
       # print("heigh is "+ image_h ", the wirth is "+ image_w)
        print("the height is", image.h ,", the wirthd is ", image.w)

folder_path = "D:\Sarab youtube\\automated videos\\automated videos"

for file in os.listdir(folder_path):
    if file.endswith(".png") or file.endswith(".jpg"):
        a = random.randint(1,50)
        print("progran has started")

        clip = VideoFileClip("parkour.mp4").subclip(a,a+4) # choosing a radom 4 second portion from the input video
        image = ImageClip(file)
        image = image.set_duration(clip.duration)

        print("the height is", image.h ,", the wirthd is ", image.w)
        while clip.h - image.h > 300 and clip.w - image.w > 100:
                print("loop has started")
                image = image.resize(1.1)
                # print("heigh is "+ image_h ", the wirth is "+ image_w)
                print("the height is", image.h ,", the wirthd is ", image.w)

        image_position = ((clip.w - image.w)/2, (clip.h - image.h)/2)
        image = image.set_position(image_position)

        composite_clip = CompositeVideoClip([clip,image])
        composite_clip.write_videofile(file + "_edited.mp4")
     
     















