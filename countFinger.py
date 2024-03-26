import cv2
class Fingers():
    def finger1_5(self, img, hand_1):
        tipIds=[4,8,12,16,20]
        counter=0
        distancia_0=[]
        #thumb contar el pulgar
        if hand_1[tipIds[0]][1]>hand_1[tipIds[0]-1][1]:
            counter+=1
            
        if isinstance(hand_1, list) and len(hand_1) > 0:
            #thumb fingers 4
            for id in range(1,5):
                
                #contar numero cero(0)
                x1, y1 = hand_1[tipIds[0]][1], hand_1[tipIds[0]][2]
                x2, y2 = hand_1[tipIds[id]][1], hand_1[tipIds[id]][2]
                distancia_0.insert(id-1,round((((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5, 2))
                if id==4:
                    if(distancia_0[0]<28 and distancia_0[1]<28 and distancia_0[2]<28
                        and distancia_0[3]<28):
                        counter=0
                    
                #-------------------------------------------------------------------------
                if hand_1[tipIds[id]][2]<hand_1[tipIds[id]-2][2]:
                    counter+=1
                    if counter == 3:
                        #contar numero 6
                        x1, y1 = hand_1[tipIds[0]][1], hand_1[tipIds[0]][2]
                        x2, y2 = hand_1[tipIds[4]][1], hand_1[tipIds[4]][2]
                        distancia4_20=round((((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5, 2)
                        if(distancia4_20<20):
                            counter+=3
                            #contar numero 7
                        x1, y1 = hand_1[tipIds[0]][1], hand_1[tipIds[0]][2]
                        x2, y2 = hand_1[tipIds[3]][1], hand_1[tipIds[3]][2]
                        distancia4_16=round((((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5, 2)
                        #contar numero 8
                        if(distancia4_16<20):
                            counter+=4 
                        x1, y1 = hand_1[tipIds[0]][1], hand_1[tipIds[0]][2]
                        x2, y2 = hand_1[tipIds[2]][1], hand_1[tipIds[2]][2]
                        distancia4_12=round((((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5, 2)
                        #contar numero 9
                        if(distancia4_12<20):
                            counter+=5    
                        x1, y1 = hand_1[tipIds[0]][1], hand_1[tipIds[0]][2]
                        x2, y2 = hand_1[tipIds[1]][1], hand_1[tipIds[1]][2]
                        distancia4_8=round((((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5, 2)
                        if(distancia4_8<35):
                            counter+=6     

            #print(fingers)
            #muestra la cantidad de dedos que estan de pie
            cv2.rectangle(img,(20,223),(170,450),(0,255,0),cv2.FILLED)
            cv2.putText(img,str(counter),(45,375),cv2.FONT_HERSHEY_PLAIN,
                        10,(255,0,0),25)
        
            return [img, counter]
    # Procesar lmlist aquí
        else:
            print("La lista lmlist está vacía o no es una lista válida.")
            

            