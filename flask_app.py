from flask import Flask, render_template,Response
import cv2
import cv2
import numpy as np
import posicion as mano
import countFinger as fingers
import senas
import alfabetic

app=Flask(__name__)

camera=cv2.VideoCapture(0)  # Inicia la cámara
dates = []


def reset_dates():
    global dates
    dates = []

@app.route('/start-basicos', methods=['GET'])
def start_camera():
    global camera
    global dates
    reset_dates()
    camera=cv2.VideoCapture(0)
    detectot=mano.handDetector(detectionCon=0.7)
    
        
    while True:
        success, img = camera.read()
        img, hand_positions = detectot.findHands(img, True)
        posicion=senas.klm()

        if len(hand_positions) >= 2:
            hand_1 = hand_positions[0]
            hand_2 = hand_positions[1]
            img=posicion.mano2(img, hand_1, hand_2)[0]
            dates=posicion.mano2(img, hand_1, hand_2)[1]

        if len(hand_positions) >=1:
            hand_1 = hand_positions[0]
            img=posicion.mano1(img, hand_1)[0]
            dates=posicion.mano1(img, hand_1)[1]

        cv2.imshow("Img",img)
        key=cv2.waitKey(1)
        
        if key == 13:
            break;
        

    camera.release()
    cv2.destroyAllWindows()   


@app.route('/start-numeros', methods=['GET'])
def start_numeros():
    global camera
    global dates
    reset_dates()
    camera=cv2.VideoCapture(0)
    detectot=mano.handDetector(detectionCon=0.7)
        
    while True:
        success, img = camera.read()
        img, hand_positions = detectot.findHands(img, True)
        
        if len(hand_positions) >=1:
            hand_1 = hand_positions[0]
            contar1=fingers.Fingers()
            if hand_1:
                img=contar1.finger1_5(img, hand_1)[0]
                dates=contar1.finger1_5(img, hand_1)[1]
        cv2.imshow("Img",img)
        key=cv2.waitKey(1)
        
        if key == 13:
            break;

    camera.release()
    cv2.destroyAllWindows()
        
@app.route('/start-alfabeticos', methods=['GET'])
def start_alfabeticos():
    global camera
    global dates
    reset_dates()
    camera=cv2.VideoCapture(0)
    detectot=mano.handDetector(detectionCon=0.7)
        
    while True:
        success, img = camera.read()
        img, hand_positions = detectot.findHands(img, True)
        
        if len(hand_positions) >=1:
            hand_1 = hand_positions[0]
            letras=alfabetic.letras()
            if hand_1:
                img=letras.alfaticos(img, hand_1)[0]
                dates=letras.alfaticos(img, hand_1)[1]
        cv2.imshow("Img",img)
        key=cv2.waitKey(1)
        
        if key == 13:
            break;

    camera.release()
    cv2.destroyAllWindows()
    
    
    
@app.route('/stop-camera', methods=['GET'])
def stop_camera():
    global camera
    camera.release()
    cv2.destroyAllWindows()
    return 'Cámara detenida'


@app.route('/get-dates', methods=['GET'])
def get_dates():
    global dates
    return {'dates': dates}


@app.route('/video-feed')
def video_feed():
    global camera

    def generate_frames():
        while True:
            success, frame = camera.read()
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                if ret:
                    frame = buffer.tobytes()
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

