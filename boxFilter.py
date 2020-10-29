import numpy as np
import cv2
import skimage as ski
import sys
import getopt as gpt


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

input_img = cv2.imread("input_images/"+imgfile_in,1)
boxsize = boxradius*2 + 1
box = np.ones((boxsize,boxsize))



downsampled_img = input_img
blurred_img = downsampled_img

cv2.imwrite("output_images/"+imgfile_out,downsampled_img)
cv2.imwrite("output_images/"+imgfile_out,blurred_img)

cv2.namedWindow('input', cv2.WINDOW_NORMAL)
cv2.imshow("input", input_img)

cv2.namedWindow('downsampled', cv2.WINDOW_NORMAL)
cv2.imshow("downsampled", downsampled_img)

cv2.namedWindow('blurred', cv2.WINDOW_NORMAL)
cv2.imshow("blurred", blurred_img)

cv2.waitKey()
cv2.destroyAllWindows()

# viewImage(img_out,imgfile_out)

