import numpy as np
import cv2
import skimage as ski
import sys
import getopt as gpt


input_imgfile = 'peppers.png'
boxradius = 1
reduction_rate = 2


args = sys.argv
for i, arg in enumerate(args):
	if arg == "-i":
		input_imgfile = args[i + 1]
	elif arg == "-r":
		reduction_rate = int(args[i + 1])



input_img = cv2.imread("input_images/"+input_imgfile,1)
boxsize = boxradius*2 + 1
box = np.ones((boxsize,boxsize))


imgfile_name,imgfile_extension = input_imgfile.split('.')

downsampled_img = input_img
downsampled_imgfile = '.'.join([imgfile_name+'_downsampled',imgfile_extension])

blurred_img = downsampled_img
blurred_imgfile = '.'.join([imgfile_name+'_blurred',imgfile_extension])

cv2.imwrite("output_images/"+downsampled_imgfile,downsampled_img)
cv2.imwrite("output_images/"+blurred_imgfile,blurred_img)

cv2.namedWindow('input_imgfile', cv2.WINDOW_NORMAL)
cv2.imshow("input_imgfile", input_img)

cv2.namedWindow('downsampled_imgfile', cv2.WINDOW_NORMAL)
cv2.imshow("downsampled_imgfile", downsampled_img)

cv2.namedWindow('blurred_imgfile', cv2.WINDOW_NORMAL)
cv2.imshow("blurred_imgfile", blurred_img)

cv2.waitKey()
cv2.destroyAllWindows()

# viewImage(img_out,downsampled_imgfile)

