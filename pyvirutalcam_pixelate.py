# This scripts uses OpenCV to capture webcamera output, applies a filter,
# and sends it to the virtual cameraera.
# It also shows how to use BGR as pixel format.

import argparse
import cv2
import pyvirtualcam
from pyvirtualcam import PixelFormat

parser = argparse.ArgumentParser()
parser.add_argument("--camera", type=int, default=0, help="ID of webcamera device (default: 0)")
parser.add_argument("--fps", action="store_true", help="output fps every second")
parser.add_argument("--filter", choices=["shake", "none"], default="shake")
args = parser.parse_args()

color=(255,0,0)
thickness=2

# Set up webcamera capture.
cap = cv2.VideoCapture(args.camera)

if not cap.isOpened():
    raise RuntimeError('Could not open video source')

pref_width = 1280
pref_height = 720
pref_fps_in = 30
cap.set(cv2.CAP_PROP_FRAME_WIDTH, pref_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, pref_height)
cap.set(cv2.CAP_PROP_FPS, pref_fps_in)

# Query final capture device values (may be different from preferred settings).
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps_in = cap.get(cv2.CAP_PROP_FPS)
print(f'Webcamera capture started ({width}x{height} @ {fps_in}fps)')

fps_out = 20

with pyvirtualcam.Camera(width, height, fps_out, fmt=PixelFormat.BGR, print_fps=args.fps) as camera:
    print(f'Virtual camera started: {camera.device} ({camera.width}x{camera.height} @ {camera.fps}fps)')

    while True:
        # Read frame from webcamera.
        ret, frame = cap.read()
        if not ret:
            raise RuntimeError('Error fetching frame')

        # height, width = frame.shape[:2]
        height = pref_height
        width = pref_width

        # Desired "pixelated" size
        w, h = (70, 40)

        # Resize input to "pixelated" size
        temp = cv2.resize(frame, (w, h), interpolation=cv2.INTER_LINEAR)

        # Initialize output image
        output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

        # Send to virtual camera.
        camera.send(output)

        # Wait until it's time for the next frame.
        camera.sleep_until_next_frame()