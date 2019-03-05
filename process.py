


import cv2, time

#from yolo import Yolo
#yolo = Yolo({
#  "config":  "yolo-coco/yolov3.cfg",
#  "weights": "yolo-coco/yolov3.weights",
#  "names":   "yolo-coco/coco.names"
#})


from maximize_contrast import maximizeContrast
from canny_recursive import makeRecursiveCanny



##################

src = "images/MuleDeer.mp4"

src_scale = 1
src_mirror = False
src_skip = 3

show_fps = 10  # 


# do you need to initialize the filter?
#filter.init()


# load the input image and grab its dimensions
vid = cv2.VideoCapture(src)
t0 = time.time()

for skip in range(2000):
  grabbed, frame = vid.read()


while True:
  count = src_skip

  while count>=1:
    count -= 1
    grabbed, frame = vid.read()
    if not grabbed: break
    if src_mirror: 
      frame = cv2.flip(frame, 1)
    if src_scale!=1:
      frame = cv2.resize(frame,(0,0),fx=src_scale,fy=src_scale)



  # use the imported filter here
  #filtered = maximizeContrast(frame)
  #yolo.detect(frame)
  #yolo.annotate(frame)
  pass1 = maximizeContrast(frame)
  filtered = makeRecursiveCanny(pass1)

  t1 = time.time()
  elap = t1-t0

  # make up the diff
  if show_fps>0:
    wait = 1/show_fps - elap
    if wait>0: 
      time.sleep(wait)

  # recalc elapsed
  t1 = time.time()
  elap = t1-t0
  t0 = t1

  fps = round(1/elap)
  text = ("%d fps"%fps)
  cv2.putText(frame,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, [0,128,255], 2)

  cv2.imshow('Frame', frame)
  cv2.imshow('Filtered', filtered )

  if cv2.waitKey(1) == 27: 
    break  # esc to quit




cv2.destroyAllWindows()


