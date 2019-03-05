

import cv2



def maximizeContrast(image):

  #auto adjust contrast of image
  clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))
  lab = cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
  l,a,b = cv2.split(lab)

  l2 = clahe.apply(l)

  lab = cv2.merge((l2,a,b))
  return cv2.cvtColor(lab,cv2.COLOR_LAB2BGR)
