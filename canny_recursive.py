
import cv2
import numpy as np



def recursiveCanny(image):
  (H,W) = image.shape[:2]

  th1 = 100
  th2 = 200

  blur1 = cv2.GaussianBlur(image, (1,1), 0)
  cann1 = cv2.Canny(blur1, th1,th2)

  blur2 = cv2.GaussianBlur(image, (3,3), 0)
  cann2 = cv2.Canny(blur2, th1,th2)

  blur3 = cv2.GaussianBlur(image, (5,5), 0)
  cann3 = cv2.Canny(blur3, th1,th2)

  blur4 = cv2.GaussianBlur(image, (7,7), 0)
  cann4 = cv2.Canny(blur4, th1,th2)

  #canny = ((cann1*.1)+(cann2*.2)+(cann3*.3)+(cann4*.4)).astype(np.uint8)
  #canny = ((cann1*.4)+(cann2*.3)+(cann3*.2)+(cann4*.1)).astype(np.uint8)
  canny = ((cann1/4)+(cann2/4)+(cann3/4)+(cann4/4)).astype(np.uint8)

  if H>2 or W>2:
  #if False:
    half  = cv2.resize(image, (int(W/2),int(H/2)) )
    accum = recursiveCanny(half)
    accum = cv2.resize(accum, (W,H) )
  else:
    accum = np.zeros((H,W),np.uint8)
  
  #return canny + accum
  return ((canny*.35)+(accum*.65)).astype(np.uint8)



def makeRecursiveCanny(image):
  # convert the image to grayscale, blur it, and perform Canny
  # edge detection
  print("[INFO] performing Canny edge detection...")
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  canny = recursiveCanny(gray)
  return canny
