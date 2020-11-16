import numpy as np
import cv2
import skimage as ski
import sys
import getopt as gpt

def box_blur(img,box_size,r):
	"""
	Applies a box_blur of size box_size by box_size to img

	Returns an image with the same dimensions as img
	"""
	blurred_img = []
	blurred_row = []

	for row in range(0,img.shape[0]-box_size,r):
		for col in range(0,img.shape[1]-box_size,r):
			box = make_box(img,box_size,row,col)
			box_sum = sum_elements(box,box_size)
			blurred_row.append(box_sum)
		blurred_img.append(blurred_row)
		blurred_row = []

	return np.array(blurred_img,dtype=np.uint8)

def make_box(img,box_size,row,col):
	return img[row:row+box_size,col:col+box_size,:3]

def sum_elements(box, box_size):
	
	box_sum = [0,0,0]

	for row in box:
		for col in row:
			for color in range(3):
				box_sum[color] += col[color]
	for color in range(3):
		box_sum[color] = int(box_sum[color] / (box_size * box_size))
	return box_sum


def downsample(img, r):
	return img[::r,::r]

def upsample(img, r):
	upsampled_img = np.repeat(img, r, axis=1)
	return np.repeat(upsampled_img, r, axis=0)

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



# imagem original
input_img = cv2.imread("input_images/"+input_imgfile,1)
imgfile_name,imgfile_extension = input_imgfile.split('.')
cv2.namedWindow('input_imgfile', cv2.WINDOW_NORMAL)
cv2.imshow("input_imgfile", input_img)

#imagem pos-downsampling
downsampled_imgfile = '.'.join([imgfile_name+'_downsampled',imgfile_extension])
downsampled_img = downsample(input_img,reduction_rate)
upsampled_img = upsample(downsampled_img,reduction_rate)
cv2.imwrite("output_images/"+downsampled_imgfile,upsampled_img)
cv2.namedWindow('downsampled_imgfile', cv2.WINDOW_NORMAL)
cv2.imshow("downsampled_imgfile", upsampled_img)

# img com box filter
blurred_img = box_blur(input_img,box_size,reduction_rate)
blurred_imgfile = '.'.join([imgfile_name+'_blurred',imgfile_extension])
cv2.imwrite("output_images/"+blurred_imgfile,blurred_img)
cv2.namedWindow('blurred_imgfile', cv2.WINDOW_NORMAL)
cv2.imshow("blurred_imgfile", blurred_img)

cv2.waitKey()
cv2.destroyAllWindows()

# viewImage(img_out,downsampled_imgfile)

