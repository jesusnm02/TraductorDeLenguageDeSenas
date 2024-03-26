import cv2
import math
class klm():
  def mano1(self, img, hand_1):
    tipIds=[4,8,12,16,20]
    distancia_0=[]
    counterx=0
    countery=0
    contenido=""
    
    angle=[]
    w1, q1=hand_1[tipIds[0]][1], hand_1[tipIds[0]][2]
    w2, q2=hand_1[tipIds[1]][1], hand_1[tipIds[1]][2]
    w3, q3=hand_1[tipIds[1]-3][1], hand_1[tipIds[1]-3][2]
    
    #calculate the angle
    angle=math.degrees(math.atan2(q3-q2,w3-w2)-
    math.atan2(q1-q2,w1-w2))
    print(angle)
      #creamos el acumulador de condiciones de señas
      #--------------------------------------------
    if(hand_1[tipIds[0]][1]>hand_1[tipIds[0]-1][1]):
        countery+=1
          
    if isinstance(hand_1, list) and len(hand_1) > 0:
      #thumb fingers 4
      for id in range(1,5):
        #-----------------------Determina los dedos levantados en Lado (Y)-----------------------------------
        if hand_1[tipIds[id]][2]<hand_1[tipIds[id]-2][2]:
          countery+=1  
        #-----------------------Determina los dedos levantados en Lado (X)-----------------------------------
        if hand_1[tipIds[id]][1]>hand_1[tipIds[id]-2][1]:
          counterx+=1
          
        x1, y1 = hand_1[tipIds[0]][1], hand_1[tipIds[0]][2]
        x2, y2 = hand_1[tipIds[id]][1], hand_1[tipIds[id]][2]
        #------------------------------------------------------------------------------------
        distancia_0.insert(id-1,round((((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5, 2))  
        if id==4:
          #para decir (HOLA)
            if(countery==3 and angle<42 and angle>35):
                contenido="Hola"
            #para decir (Yo)
            if(counterx==1 and hand_1[tipIds[1]][1]>hand_1[tipIds[1]-1][1]):
                contenido="Yo"
            if(distancia_0[0]<45 and distancia_0[1]<45 and distancia_0[2]<45
              and distancia_0[3]<45):
              contenido="Comer"    
              
              
        cv2.putText(img, contenido, (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                    2, (255, 0, 0), 5)    
      return [img, contenido]
      
  #definimos la entrega de la posicion de la mano 1-----
  #----------------------------------------------------------------------
  
  
  
  
  
  
  
  def mano2(self, img, hand_1, hand_2):
      id=[4,8,12,16,20]
      contenido=""
      x1, y1 = hand_1[id[0]][1], hand_1[id[0]][2]
      x2, y2 = hand_2[id[0]][1], hand_2[id[0]][2]

      distancia = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5

      x1, y1 = hand_1[id[1]][1], hand_1[id[1]][2]
      x2, y2 = hand_2[id[1]][1], hand_2[id[1]][2]
      distancia2 = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
      if distancia<20 and distancia2<20:
        contenido="¿Como"

      #con esto decimo (estas?)
      if hand_1[id[1]-3][2]<hand_1[id[4]-3][2] and hand_2[id[1]-3][2]<hand_2[id[4]-3][2]:
        contenido="estas?"
      
      
      cv2.putText(img, contenido, (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                      2, (255, 0, 0), 5)
          
      return [img,contenido]    
        
  #definimos la entrega de la posicion de la mano 1 y 2      