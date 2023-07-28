from functions import *


a = get_images()
count = 0
for i in a:
    x = frame_mask(i)
    x = apply_mask(i, x)
    x = thresholding(x)
    x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    try:
        x = hough_line_transformation(x, i)
        cv2.imwrite('output/' + str(count) + '.png', x)
    except TypeError:
        cv2.imwrite('output/' + str(count) + '.png', i)
    count += 1
to_video()
