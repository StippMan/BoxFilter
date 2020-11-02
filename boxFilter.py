import numpy as np
import cv2
import skimage as ski
import sys
import getopt as gpt

def box_blur(img,box_size):
	"""
	Applies a box_blur of size box_size to img

	Returns an image of the same dimensions as img
	"""
	img_length, img_height, img_depth = img.shape
	print(img_length, img_height, img_depth)
	box = np.ones((box_size,box_size))
	blurred_img = img[:]


	

	return blurred_img


input_imgfile = 'peppers.png'
reduction_rate = 2
box_size = 3

args = sys.argv
for i, arg in enumerate(args):
	if arg == "-i":
		input_imgfile = args[i + 1]
	elif arg == "-r":
		reduction_rate = int(args[i + 1])
	elif arg == "-b":
		box_size = int(args[i + 1])

input_img = cv2.imread("input_images/"+input_imgfile,1)


imgfile_name,imgfile_extension = input_imgfile.split('.')

downsampled_img = input_img[::reduction_rate,::reduction_rate]
downsampled_imgfile = '.'.join([imgfile_name+'_downsampled',imgfile_extension])

blurred_img = box_blur(downsampled_img,box_size)
blurred_imgfile = '.'.join([imgfile_name+'_blurred',imgfile_extension])

cv2.imwrite("output_images/"+downsampled_imgfile,downsampled_img)
cv2.imwrite("output_images/"+blurred_imgfile,blurred_img)

cv2.namedWindow('input_imgfile', cv2.WINDOW_NORMAL)
cv2.namedWindow('downsampled_imgfile', cv2.WINDOW_NORMAL)
cv2.namedWindow('blurred_imgfile', cv2.WINDOW_NORMAL)

cv2.imshow("input_imgfile", input_img)
cv2.imshow("downsampled_imgfile", downsampled_img)
cv2.imshow("blurred_imgfile", blurred_img)

cv2.waitKey()
cv2.destroyAllWindows()

# viewImage(img_out,downsampled_imgfile)

