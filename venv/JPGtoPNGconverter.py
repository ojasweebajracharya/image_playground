import sys
import os
from PIL import Image

# Function: Convert to png
def loopAndConvert(directory, convertTo):
    for imagefile in os.listdir(directory):
        if imagefile.endswith(".jpg"):
            imageName = str(imagefile[:-4]) # Gets rid of the .jpg
            image = directory + "/" + imagefile
            imgOpened = Image.open(image)
            imgOpened.save(f"./new/{imageName}.png", "png")
            print("Done")


def main():
    # check if new exists, if not create it:
    isExist = os.path.exists(convertTo)
    if isExist:
        print("It exists!!!!")
        # Loop through folder for all jpg files:
        loopAndConvert(directory,convertTo)
    else:
        print("I have created a new directory called new.")
        os.mkdir(convertTo)
        main()

# grab first and second argument
directory = sys.argv[1]
convertTo = sys.argv[2]
main()




