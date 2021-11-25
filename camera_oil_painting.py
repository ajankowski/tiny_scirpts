import cv2

cap = cv2.VideoCapture(1)

while True:
    ret, img = cap.read()

    res = cv2.xphoto.oilPainting(img, 5, 3)
  
    cv2.imshow("oilpaint", res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
