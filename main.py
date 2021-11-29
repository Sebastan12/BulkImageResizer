import os
from PIL import Image


def createDirectoryIfNotExist(name):
    if not os.path.exists(name):
        os.makedirs(name)


def starting_point():
    impfolername = "import"
    exprtfoldername = "export"
    outputsize = (800, 800)

    createDirectoryIfNotExist(impfolername)
    createDirectoryIfNotExist(exprtfoldername)

    print("put desired images into the " + impfolername + " folder then hit enter")
    input()

    for currentfile in os.listdir(impfolername):
        background = Image.new("RGBA", outputsize, (255, 255, 255))
        foreground = Image.open(impfolername + "/" + currentfile)
        #thumbnail resizes and protects aspect ratio
        foreground.thumbnail(background.size, Image.ANTIALIAS)
        background.paste(
            foreground, (int((background.size[0] - foreground.size[0]) / 2), int((background.size[1] - foreground.size[1]) / 2))
        )
        #jpg can only output RGB (no aplha channel)
        background = background.convert("RGB")
        background.save(exprtfoldername + "/" + currentfile)


if __name__ == '__main__':
    starting_point()


#---PROCESS BY HAND---
# open gimp
# create white layer 800 x 800
# import image
# scale largest side down to 800 keeping aspect ratio
# export finsihed image
