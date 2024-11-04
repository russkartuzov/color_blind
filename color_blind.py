#TODO

from math import sqrt
from PIL import ImageGrab

import pyautogui


color_distances = {}

base_colors = {
    'Red' : (255, 0, 0),
    'Green' : (0, 255, 0),
    'Blue' : (0, 0, 255),
    'Yellow' : (255, 255, 0),
    'Cyan' : (0, 255, 255),
    'Magenta' : (255, 0, 255),
    'Orange' : (255, 165, 0),
    'Black' : (0, 0, 0),
    'White' : (255, 255, 255)
}

def get_color_at_cursor():
    x, y = pyautogui.position()
    screen = ImageGrab.grab(bbox=(x, y, x + 1, y + 1))
    color = screen.getpixel((0, 0))

    return color

def get_distance(color1, color2):
    r_diff = (color1[0] - color2[0])**2
    g_diff = (color1[1] - color2[1])**2
    b_diff = (color1[2] - color2[2])**2
    distance = sqrt(r_diff + g_diff + b_diff)

    return distance

def find_shortest_dist(numbers):
    smallest_key = next(iter(numbers))
    smallest_value = numbers[smallest_key]
    
    for name, val in numbers.items():
        if val < smallest_value:
            smallest_value = val
            smallest_key = name
            
    return smallest_key, smallest_value


# MAIN
while True:
    color_at_cursor = get_color_at_cursor()

    for color_name, color_rgb in base_colors.items():
        distance = get_distance(color_at_cursor, color_rgb)
        color_distances[color_name] = distance

    closest_color = find_shortest_dist(color_distances)

    closest_color_name = next(iter(closest_color))
    print(closest_color_name)