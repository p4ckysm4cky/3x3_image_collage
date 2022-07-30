import cv2 as cv


def getFrame(filepath: str, posMsec: int, outFilepath: str) -> None:
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


if __name__ == "__main__":
    getFrame("./test1.mkv", (6 * 60 + 51) * 1000, "./test1.png")
