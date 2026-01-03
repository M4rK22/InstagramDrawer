import pyautogui
import cv2 as cv
import numpy as np
import time
from config import clean_image

def main():
	# Setup emulator
	print("Setup the drawing mode...")
	time.sleep(5)

	# Image path
	img_path = "InstagramDrawer/pics/pinguini.jpg" #Here put your path
	#reading it in gray scale
	img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
	if img is None:
		print("Image not found!")
		exit()

	edges, width, height,x1,y1 = clean_image(img)
	distance_min = 3  # minimal distance from two consecutive points, to keep the script fast
	last_x, last_y = -distance_min*2, -distance_min*2  # out of canva to be sure that the the 1st point will be drew

	print("Starting...")

	for y in range(height):
		for x in range(width):
			#checks if the pixel exists
			if edges[y,x] > 0:
				dx = x - last_x
				dy = y - last_y
				if dx*dx + dy*dy >= distance_min*distance_min:
					pyautogui.click(x+x1,y+y1)
					last_x = x
					last_y = y
	print("Finished drawing")

