import cv2
import os

#accessing the webcam
cam = cv2.VideoCapture(0)
#setting width and height of camera frame
cam.set(3,640)
cam.set(4,480)

#open cv can detect faces and store it in a variable
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('\n Enter user id and press enter')

print("\n [INFO] Initialising face capture.")
# Initialize individual sampling face count
count = 0

while(True):

    ret, img=cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #image detection takes place in grayscale image only
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y),(x+w, y+h), (255,0,0), 2)
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User."+str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h, x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff
    if k==27:
        break
    elif count>=30:
        break

# Bit of cleanup
print("\n [INFO] Exiting program")
cam.release()
cv2.destroyAllWindows()