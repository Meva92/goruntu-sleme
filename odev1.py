# görüntü işleme  inverting ödevi
import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('ters.jpg',0)
inverted = np.invert(image)
cv2.imshow("original",image)
cv2.imshow("inverted",inverted)
# cv2.waitKey()
negimage = 255 - image
cv2.imshow("negimage",negimage)
cv2.waitKey()

