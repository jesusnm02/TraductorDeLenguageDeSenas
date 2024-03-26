import cv2
import numpy as np
import posicion as mano
import countFinger as fingers
import senas
import alfabetic

cap=cv2.VideoCapture(0)
detectot=mano.handDetector(detectionCon=0.7)
    
while True:
    success, img = cap.read()
    img, hand_positions = detectot.findHands(img, True)
    posicion=senas.klm()
    id=[4,8,12,16,20]

    if len(hand_positions) >= 2:
        hand_1 = hand_positions[0]
        hand_2 = hand_positions[1]
        img=posicion.mano2(img, hand_1, hand_2)[0]

    if len(hand_positions) >=1:
        hand_1 = hand_positions[0]
        img=posicion.mano1(img, hand_1)[0]
                
        #contar numeros con los dedos   
        contar1=fingers.Fingers()
        letras=alfabetic.letras()
        if hand_1:
            img=contar1.finger1_5(img, hand_1)[0]
            img=letras.alfaticos(img, hand_1)[0]


    cv2.imshow("Img",img)
    key=cv2.waitKey(1)
    
    if key == 13:
        break;

cap.release()
cv2.destroyAllWindows()    