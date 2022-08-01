import utils
from typing import List
import sys
import os


def main() -> None:
    # When no argument
    outfileName = "out.png"
    print(sys.argv)
    if (len(sys.argv) == 2):
        file = open(sys.argv[1], "r")
    else:
        file = open("input.txt", "r")
    videoPath = None
    videoPos: List[int] = []
    for index, line in enumerate(file):
        if index == 0:
            videoPath = line.strip()
        else:
            videoPos.append(utils.videoPosToMillisecond(line.strip()))
    file.close()
    print("Extracting frames...")
    utils.outFrameFolder(videoPath, videoPos, "temp")
    framePaths = [f"./temp/frame{i}.png" for i in range(len(videoPos))]
    print("Making collage...")
    utils.makeCollage(3, framePaths, outfileName)
    print(
        f"Collage generated at {os.path.join(os.getcwd(), outfileName)}")


if __name__ == "__main__":
    main()
