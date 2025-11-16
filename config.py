# config.py
"""
Configuration file for the Doodle Drawing Script

Contains settings for image, drawing mode, scaling, offsets,
approximation precision, and pause key.
"""

# --- Image Settings ---
image_file = 'example.jpg'   # Path to the image to be drawn
image_preview = True         # See image preview before drawing

# --- Pause / Resume Settings ---
pause_key = 'p'  # Hotkey to pause/resume drawing

# --- Drawing Mode ---
# Options: 'trace' - draw by tracing approximated lines of outlines(contours)
#          'linear' - draw by iterating over every pixel
draw_mode = 'trace'

# --- Scaling and Offsets ---
scale = 1          # Scale factor for the drawing
offset_x = 200     # Horizontal offset to position drawing on screen
offset_y = 500     # Vertical offset to position drawing on screen

# --- Contour Approximation ---
approx_epsilon = 2.0   # Maximum distance in pixels for curve approximation

# --- Linear drawing ---
pixel_jump = 2   # Check every n-th pixel in image

# --- Timing Settings ---
mouse_move_duration = 0.001  # Duration for smooth mouse movement
inter_contour_delay = 0.05   # Delay between drawing contours
pixel_draw_delay = 0.005     # Delay when tracing edge pixels