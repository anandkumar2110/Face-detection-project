import cv2


img = []
i = 0
video_capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('image.avi',fourcc,20.0,((640,480)))
# from google.colab.patches.cv2_imshow
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    filename = 'image' + str(i) + '.jpg'
    cv2.imwrite(filename,frame)
    # out.write(frame)
    cv2.imshow('frame',frame)
    i = i+1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
out.release()
cv2.destroyAllWindows()