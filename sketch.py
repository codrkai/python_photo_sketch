import imageio # for handling our photos
import numpy as np # adjusting photo colors
import scipy.ndimage # photo filters
import cv2 # outputting modified photo
import os # filesystem

def dodge(front, back):
    try:
        result = (front*255) / (255-back)
        result[result>255] = 255
        result[back==255] = 255
    except Exception as e:
        print(e)
    return result.astype('uint8')

photo_dir = './photo'
output_dir = './output'

for filename in os.listdir(photo_dir):
    # only jpg files
    if filename.lower().endswith('.jpg'):

        # current_dir/photo/image.jpg
        file = os.path.join(photo_dir, filename)

        # read image
        img = imageio.imread(file)
        
        gray_img = np.dot(img[...,:3], [0.299, 0.587, 0.114])

        invert_img = 255 - gray_img

        blur_img = scipy.ndimage.filters.gaussian_filter(invert_img, sigma=10)

        final_img = dodge(blur_img, gray_img)

        # get only the name of the file (without the path or the file extension)
        basename = os.path.splitext(filename)[0]

        # output our new file as a png
        cv2.imwrite(output_dir + '/' + basename + '.png', final_img)
    else:
        continue