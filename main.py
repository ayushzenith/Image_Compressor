import os
import shutil
from subprocess import call


def lossy(source, destination):
    filename = os.path.splitext(source)

    if filename[1] == ".jpeg" or filename[1] == ".jpg":
        shutil.copyfile(source, destination)
        call(["jpegoptim","--max=75", destination])
    elif filename[1] == ".png":
        call(["crunch", source])
        os.rename(filename[0]+"-crunch"+filename[1],destination)
    elif filename[1] == ".gif":
        call(["gifsicle", '-O3', '--lossy=75',source, "--output",destination])
    else:
        print("filetype not recognized")



def lossless(source, destination):
    filename = os.path.splitext(source)

    if filename[1] == ".jpeg" or filename[1] == ".jpg":
        call(["jpegtran", '-copy', 'exif', '-optimize', '-perfect', '-outfile', source, destination])
    elif filename[1] == ".png":
        call(["pngcrush", '-rem', 'alla', '-reduce', '-brute', source, destination])
    elif filename[1] == ".gif":
        call(["gifsicle", '-o3', source, "--output", destination])
    else:
        print("filetype not recognized")

lossy("input/png.png","output/lossypng.png")
lossless("input/png.png","output/losslesspng.png")


