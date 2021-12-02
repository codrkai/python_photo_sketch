import imageio # for handling our photos
import cv2 # outputting modified photo
import os # filesystem

photo_dir = './photo'
output_dir = './output'

for filename in os.listdir(photo_dir):
    # only jpg files
    if filename.lower().endswith('.jpg'):

        # current_dir/photo/image.jpg
        file = os.path.join(photo_dir, filename)

        # read image
        img = imageio.imread(file)
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        edges = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

        cartoon_img = cv2.bilateralFilter(img, 9, 250, 250)

        final_img = cv2.bitwise_and(cartoon_img, cartoon_img, mask=edges)

        # get only the name of the file (without the path or the file extension)
        basename = os.path.splitext(filename)[0]

        # output our new file as a png
        cv2.imwrite(output_dir + '/' + basename + '_toon.png', final_img)
    else:
        continue