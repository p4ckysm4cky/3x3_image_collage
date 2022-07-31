import cv2 as cv
from typing import List
from PIL import Image
import os


def outFrame(filepath: str, posMsec: int, outFilepath: str) -> None:
    """
    Extracts a frame from a video when given the position in milliseconds
    and is copied to outFilePath
    """
    cap = cv.VideoCapture(filepath)
    # CAP_PROP_FRAME_COUNT - ordinal of 7
    # (Number of frames in the video file)
    total_frames = cap.get(7)
    # CAP_PROP_POS_MSEC - ordinal of 0
    # (Current position of the video file in milliseconds.)
    cap.set(0, posMsec)
    ret, frame = cap.read()
    if ret:
        cv.imwrite(outFilepath, frame)
    else:
        raise Exception("Frame not found in video")


def outFrameFolder(filepath: str, posMsecArray: List[int], folderName: str) -> None:
    """
    Extracts multiple frames from a video and then copies it to a folder
    """
    folderPath = f"./{folderName}"
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    for index, posMsec in enumerate(posMsecArray):
        outFrame(filepath, posMsec, f"{folderName}/frame{index}.png")


def videoPosToMillisecond(videoPos: str) -> int:
    """
    Converts hh:mm:ss.ms to milliseconds
    that is used in other function
    """
    milliseconds = 0.0
    hour, minute, second = tuple([float(strNum)
                                 for strNum in videoPos.split(":")])
    milliseconds += hour * 60 * 60 * 1000
    milliseconds += minute * 60 * 1000
    milliseconds += second * 1000
    return round(milliseconds)


def makeCollage(column: int, framePaths: List[str], outFilepath) -> None:
    """
    Uses the image filepaths to create an image collage which is outputted to outFilepath
    """
    firstImage = Image.open(framePaths[0])
    width, height = firstImage.size
    frameWidth = width * column
    frameHeight = height * (round(len(framePaths) / column))
    frame = Image.new("RGBA", (frameWidth, frameHeight))
    xPos = 0
    yPos = 0
    for framePath in framePaths:
        tempImage = Image.open(framePath)
        frame.paste(tempImage, (xPos, yPos))
        xPos += width
        if xPos >= frameWidth:
            xPos = 0
            yPos += height
    # Remember to include file extension in the outFilepath as well
    frame.save(outFilepath, format="png")


if __name__ == "__main__":
    # new_array = ["00:01:00", "00:02:09.80", "00:03:00", "00:04:00",
    #              "00:05:00", "00:06:00", "00:07:00", "00:08:00", "00:09:00"]
    # new_array = [videoPosToMillisecond(string) for string in new_array]
    # outFrameFolder("./test1.mkv", new_array, "temp")
    framePaths = ["./temp/frame0.png", "./temp/frame1.png", "./temp/frame2.png", "./temp/frame3.png",
                  "./temp/frame4.png", "./temp/frame5.png", "./temp/frame6.png", "./temp/frame7.png", "./temp/frame8.png"]
    makeCollage(3, framePaths, "./out.png")
