import cv2
import os
import time
import HandTrankingModule as htm


def getNumber(ar):
    s = ""
    for i in ar:
        s += str(ar[i]);

    if (s == "00000"):
        k3 = "hold"
        return [k3]
    elif (s == "01000"):
        k4 = "out"
        return [k4]
    elif (s == "01100"):
        k2 = "peace"
        return [k2]
    elif (s == "01001"):
        k5 = "swag"
        return [k5]
    elif (s == "11111"):
        k1="stop"
        return [k1]

wcam, hcam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)
pTime = 0
detector = htm.handDetector(detectionCon=0.75)
while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)
    tipId = [4, 8, 12, 16, 20]
    if (len(lmList) != 0):
        fingers = []
        # thumb
        if (lmList[tipId[0]][1] > lmList[tipId[0] - 1][1]):
            fingers.append(1)
        else:
            fingers.append(0)
        # 4 fingers
        for id in range(1, len(tipId)):

            if (lmList[tipId[id]][2] < lmList[tipId[id] - 2][2]):
                fingers.append(1)

            else:
                fingers.append(0)
        x=getNumber(fingers)
        cv2.rectangle(img, (20, 255), (300, 375), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, str(x), (25, 325), cv2.FONT_HERSHEY_SIMPLEX,2, (255,255,255), 5)
    cv2.imshow("image", img)
    z = cv2.waitKey(2) & 0xFF
    if z == 27:
        break
        cv2.destroyAllWindows
