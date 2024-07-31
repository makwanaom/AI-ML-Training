import cv2
import cv2.data

# img = cv2.imread('./bat.jpg')
cam = cv2.VideoCapture(0)




while True:
    status, img  = cam.read()
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces  = classifier.detectMultiScale(img, 1.3, 5)
    for face in faces:
        x = face[0]
        y = face[1]
        w = face[2]
        h = face[3]
        xl = x + w
        yl = y + h
        cv2.rectangle(img, (x ,y), (xl, yl), (255, 0, 0), 2)

    cv2.imshow(" new image", img)
    if cv2.waitKey(1) == ord("q"):
        break