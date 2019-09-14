import cv2
import os

# img = cv2.imread("/Users/eric/Desktop/eye_cascade/sanitizer100x100.jpg")

pic_num = 0

for name in os.listdir("purell_og"):
    if name == ".DS_Store":
        continue

    print (name)
    img = cv2.imread("purell_og/"+str(name))
    resize = cv2.resize(img, (100, 200))
    cv2.imwrite("purell_new/"+str(pic_num)+'.jpg', resize)
    pic_num += 1
# cv2.imwrite("/Users/eric/Desktop/eye_cascade/sanitizer100100.jpg", resize)

#cv2.imshow("re", resize)
# cv2.waitKey(0)
