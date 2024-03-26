import cv2
import mediapipe as mp

class handDetector():
    def __init__(self,mode = False, maxHands = 2, model_complexity=1, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.model_complexity=model_complexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.model_complexity, self.detectionCon,
                                        self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        hand_positions = []
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:

                hand_position = []
                x_min, y_min = float('inf'), float('inf')  # Inicializa con valores grandes
                x_max, y_max = 0, 0
                
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    hand_position.append([id, cx, cy])
                    
                    if id == 0 or id == 12:
                        # Actualiza las coordenadas mínimas y máximas para el rectángulo
                        x_min = min(x_min, cx-80)
                        y_min = min(y_min, cy)
                        x_max = max(x_max, cx+80)
                        y_max = max(y_max, cy)
                        
                    if draw:
                        cv2.circle(img, (cx, cy), 3, (255, 0, 255), cv2.FILLED)
                        
                cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)        
                hand_positions.append(hand_position)
        return img, hand_positions


def main():
    cap = cv2.VideoCapture(0)
    detector=handDetector()
    while True:
        success, img = cap.read()
        # Crear una instancia de la clase handDetector
        detector = handDetector()

        # Obtener la imagen y las posiciones de las manos
        img, hand_positions = detector.findHands(img)

        # Acceder a las posiciones de las dos manos
        if len(hand_positions) >= 2:
            hand_1 = hand_positions[0]
            hand_2 = hand_positions[1]
            print(f'mano 1{hand_1[4]}')
            print(f'mano 2{hand_2}')


        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__=="__main__":
    main()