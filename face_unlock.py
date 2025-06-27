import cv2
import random
import time

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

roasts = [
    "Not Zain 😂", "Error 404: Boss Missing", "Nice try imposter!", 
    "Go back to where you came from 😆", "Zain only, please!"
]
last_time = 0
current_roast = random.choice(roasts)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (200, 200))
        label, confidence = recognizer.predict(face)

        if label == 0 and confidence < 60:
            text = "Welcome Boss Zain 👑"
            color = (0, 255, 0)
        else:
            if time.time() - last_time > 3:
                current_roast = random.choice(roasts)
                last_time = time.time()
            text = current_roast
            color = (0, 0, 255)

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 3)
        cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.85, color, 2)

    cv2.imshow("Zain's Face Unlock", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
