from pyautogui import *
import cv2 as cv
import time
import os
import numpy as np
import keyboard
import config

# Load image
if not os.path.exists(config.image_file):
    print(f"The file {config.image_file} does not exist.")
    exit()

img = cv.imread(config.image_file, cv.IMREAD_GRAYSCALE)
img = cv.GaussianBlur(img, (3, 3), 0)
edges = cv.Canny(img, 130, 200, None, 3)

# Pause logic
paused = False
def toggle_pause(e=None):
    global paused
    paused = not paused
    print("|| Paused" if paused else "▶ Resumed")

keyboard.add_hotkey(config.pause_key, toggle_pause)

if config.image_preview:
    cv.imshow('Edges', edges)
    cv.waitKey()

paused = True

lines, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

def trace_lines():
    contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    scale = config.scale          # adjust size
    offset_x = config.offset_x    # horizontal offset
    offset_y = config.offset_y    # vertical offset
    duration = config.mouse_move_duration

    for contour in contours:
        if len(contour) == 0:
            continue

        epsilon = config.approx_epsilon  # maximum distance in pixels to approximate the curve
        approx_contour = cv.approxPolyDP(contour, epsilon, False)

        # Start drawing
        x0, y0 = approx_contour[0][0]
        moveTo(x0*scale + offset_x, y0*scale + offset_y)
        mouseDown(button='left')

        # Move smoothly along the rest of the contour
        for point in approx_contour[1:]:
            while paused:
                time.sleep(0.1)
            mouseDown(button='left')
            x, y = point[0]
            moveTo(x*scale + offset_x, y*scale + offset_y, duration)
            mouseUp()
        
        time.sleep(0.05)  # small pause between contours


def draw_by_line():
    height, width = edges.shape
    scale = config.scale            # adjust size
    offset_x = config.offset_x      # horizontal offset
    offset_y = config.offset_y      # vertical offset
    duration = config.mouse_move_duration

    pixel_jump = config.pixel_jump  # check every x pixels

    for y in range(0, height, pixel_jump):
        for x in range(0, width, pixel_jump):
            if edges[y, x] != 0:
                moveTo((x+offset_x) * scale, (y+offset_y) * scale, duration)
                mouseDown(button='left')
                time.sleep(0.005)
                mouseUp()

if(config.draw_mode == "trace"):
    trace_lines()
elif(config.draw_mode == "linear"):
    draw_by_line()

