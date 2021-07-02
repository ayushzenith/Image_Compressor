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
        call("jpegtran -copy none -progressive -optimize " + source + " > " + destination, shell=True)
    elif filename[1] == ".png":
        call(["pngcrush", '-rem', 'alla', '-reduce', '-brute', source, destination])
    elif filename[1] == ".gif":
        call(["gifsicle", '-o3', source, "--output", destination])
    else:
        print("filetype not recognized")

lossy("input/gif40.gif","output/lossy-gif40.gif")
lossless("input/gif40.gif","output/lossless-gif40.gif")

"""
lossy("input/gif140.gif","output/lossy-gif140.gif")
lossless("input/gif140.gif","output/lossless-gif140.gif")

lossy("input/gif350.gif","output/lossy-gif350.gif")
lossless("input/gif350.gif","output/lossless-gif350.gif")

lossy("input/gif500.gif","output/lossy-gif500.gif")
lossless("input/gif500.gif","output/lossless-gif500.gif")

lossy("input/gif1000.gif","output/lossy-gif1000.gif")
lossless("input/gif1000.gif","output/lossless-gif1000.gif")

lossy("input/gif3500.gif","output/lossy-gif3500.gif")
lossless("input/gif3500.gif","output/lossless-gif3500.gif")

lossy("input/jpeg100.jpeg","output/lossy-jpeg100.jpeg")
lossless("input/jpeg100.jpeg","output/lossless-jpeg100.jpeg")

lossy("input/jpeg500.jpeg","output/lossy-jpeg500.jpeg")
lossless("input/jpeg500.jpeg","output/lossless-jpeg500.jpeg")

lossy("input/jpeg1000.jpeg","output/lossy-jpeg1000.jpeg")
lossless("input/jpeg1000.jpeg","output/lossless-jpeg1000.jpeg")

lossy("input/jpeg2500.jpeg","output/lossy-jpeg2500.jpeg")
lossless("input/jpeg2500.jpeg","output/lossless-jpeg2500.jpeg")

lossy("input/png500.png","output/lossy-png500.png")
lossless("input/png500.png","output/lossless-png500.png")

lossy("input/png1000.png","output/lossy-png1000.png")
lossless("input/png1000.png","output/lossless-png1000.png")

lossy("input/png2000.png","output/lossy-png2000.png")
lossless("input/png2000.png","output/lossless-png2000.png")

lossy("input/png3000.png","output/lossy-png3000.png")
lossless("input/png3000.png","output/lossless-png3000.png")

"""
