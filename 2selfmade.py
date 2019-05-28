#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;
from scipy.misc import bytescale
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller

driver = webdriver.Firefox()
driver.get("http://whale.hacking-lab.com:3555")
wait = WebDriverWait(driver,10)
time.sleep(10)
count = 0
Eggs = "0"
while count < 1000:
	#get screenshot
	time.sleep(6)
    	#elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "img1")))
	#driver.get_screenshot_as_file("picture.png")
	

        #logic for picture analyzing
	frame40 = cv2.imread('picture.jpg')
	fgbg = cv2.createBackgroundSubtractorKNN() # for mask
	fgmask = fgbg.apply(frame40)

	hsv = cv2.cvtColor(frame40, cv2.COLOR_BGR2HSV)
	th, bw = cv2.threshold(hsv[:, :, 2], 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
	morph = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
	dist = cv2.distanceTransform(morph, cv2.DIST_L2, cv2.DIST_MASK_PRECISE)
	img8 = cv2.subtract(255, dist) 
	img8 = bytescale(img8) 
	# Setup SimpleBlobDetector parameters.
	params = cv2.SimpleBlobDetector_Params()

	# Change thresholds
	params.minThreshold = 0 #default 10
	params.maxThreshold = 255 #defaul 200

	# Filter by Area.
	params.filterByArea = True
	params.minArea =650

	# Filter by Circularity
	params.filterByCircularity = True
	params.minCircularity = 0.3

	# Filter by Convexity
	params.filterByConvexity = True
	params.minConvexity = 0.87
	    
	# Filter by Inertia
	params.filterByInertia = True
	params.minInertiaRatio = 0.2

	# Create a detector with the parameters
	ver = (cv2.__version__).split('.')
	if int(ver[0]) < 3 :
		detector = cv2.SimpleBlobDetector(params)
	else : 
		detector = cv2.SimpleBlobDetector_create(params)


	# Detect blobs.
	keypoints = detector.detect(img8)
	print len(keypoints)
	elem2 = driver.find_element_by_id("s")
    	elem2.clear()
        Eggs = len(keypoints)
    	elem2.send_keys(Eggs)
	time.sleep(1)
        elem2.send_keys(Keys.RETURN)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

#im_with_keypoints = cv2.drawKeypoints(img8, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
#cv2.imshow("Keypoints2", im_with_keypoints)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
