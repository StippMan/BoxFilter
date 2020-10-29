import numpy as np
import cv2 as cv
import skimage as ski
import sys
import getopt as gpt

def viewImages(images, names_of_window):

	for i, name in enumerate(names_of_window):
		cv.namedWindow(name, cv.WINDOW_NORMAL)
		cv.imshow(name, images[i])

	cv.waitKey(0)
	cv.destroyAllWindows()

imgfile_in = 'peppers.png'
boxradius = 1

reduction_rate = 2

args = sys.argv
for i, arg in enumerate(args):
	if arg == "-i":
		imgfile_in = args[i + 1]
	elif arg == "-r":
		reduction_rate = int(args[i + 1])

imgfile_out = imgfile_in

input_img = cv.imread("input_images/"+imgfile_in,1)
boxsize = boxradius*2 + 1
box = np.ones((boxsize,boxsize))



downsampled_img = input_img
blurred_img = downsampled_img

cv.imwrite("output_images/"+imgfile_out,img_out)
cv.imwrite("output_images/"+imgfile_out,img_out)

viewImages([input_img, img_out], [imgfile_in,imgfile_out])
# viewImage(img_out,imgfile_out)

