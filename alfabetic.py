import cv2
import math

class letras():
  def alfaticos(self, img, hand_1):
    tipIds=[4,8,12,16,20]
    distancia_0=[]
    counterx=0
    countery=0
    letras=""
    
    #-----Obtenemos angulos------------
    angle=[]
    w1, q1=hand_1[tipIds[0]][1], hand_1[tipIds[0]][2]
    w2, q2=hand_1[tipIds[1]][1], hand_1[tipIds[1]][2]
    w3, q3=hand_1[tipIds[1]-3][1], hand_1[tipIds[1]-3][2]
    
    #calculate the angle
    angle=math.degrees(math.atan2(q3-q2,w3-w2)-
    math.atan2(q1-q2,w1-w2))
    print(angle)
        
    #angle.insert(0, )
    #thumb contar el pulgar
    if(hand_1[tipIds[0]][1]>hand_1[tipIds[0]-1][1]):
          counterx+=1
          
    if isinstance(hand_1, list) and len(hand_1) > 0:
      #thumb fingers 4
      for id in range(1,5):
        #-----------------------Determina los dedos levantados en Lado (Y)-----------------------------------
        if hand_1[tipIds[id]][2]<hand_1[tipIds[id]-2][2]:
          counterx+=1  
        #-----------------------Determina los dedos levantados en Lado (X)-----------------------------------
        if hand_1[tipIds[id]][1]>hand_1[tipIds[id]-2][1]:
          countery+=1
          
        x1, y1 = hand_1[tipIds[0]][1], hand_1[tipIds[0]][2]
        x2, y2 = hand_1[tipIds[id]][1], hand_1[tipIds[id]][2]
        #------------------------------------------------------------------------------------
        distancia_0.insert(id-1,round((((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5, 2))  
        if id==4:
          
          #para decir (C)
          if(distancia_0[0]<85 and distancia_0[1]<85 and distancia_0[2]<85
              and distancia_0[3]<85):
              letras="C"
            
          #para decor (O)    
          if(distancia_0[0]<45 and distancia_0[1]<45 and distancia_0[2]<45
              and distancia_0[3]<45):
              letras="O"  
              
          if(counterx==1):    
            #para decir (D)
            if(distancia_0[1]<80 and distancia_0[2]<80
                and distancia_0[3]<80):
              letras="D" 
            #para decir (I)
            if(distancia_0[0]<60 and distancia_0[1]<60
                and distancia_0[2]<60 and hand_1[tipIds[4]][2]<hand_1[tipIds[4]-2][2]):
              letras="I"
            #para decir (G)
            if(distancia_0[0]<65 and counterx==1 and hand_1[tipIds[0]][1]>hand_1[tipIds[0]-1][1]):
              letras="G"
            
          if(counterx==0):
            #para decir (E)
            if(distancia_0[0]<50 and distancia_0[1]<60 and distancia_0[2]<60
                and distancia_0[3]<60 and hand_1[tipIds[0]][1]<hand_1[tipIds[1]-1][1]):
              letras="E" 
            if(hand_1[tipIds[1]][2]>hand_1[tipIds[1]-1][2] and hand_1[tipIds[1]][2]<hand_1[tipIds[0]-1][2]):  
              letras="X" 
          if(counterx==3):
            #para decir (F)
            if(distancia_0[0]<40):
              letras="F"
            #para decir (W)
            if(distancia_0[3]<40):
              letras="W"  
          
          if(counterx==2):
            #para decir (U)
            if(distancia_0[1]<60 and distancia_0[2]<60):
              letras="U"   
            #para decir (V)
            if(distancia_0[2]<50 and distancia_0[3]<50):
              letras="V"  
            #para decir (Y)   
            if(hand_1[tipIds[0]][1]>hand_1[tipIds[0]-1][1] and hand_1[tipIds[4]][2]<hand_1[tipIds[4]-1][2]):
              letras="Y" 
        #---------------------------------------------------------------------------
      #encontrar (A)
      z1, l1 = hand_1[tipIds[0]-1][1], hand_1[tipIds[0]-1][2] 
      z2, l2 = hand_1[tipIds[1]-2][1], hand_1[tipIds[1]-2][2] 
      
      
      distancia3_6=(round((((z1 - z2) ** 2) + ((l1 - l2) ** 2)) ** 0.5, 2))
      if distancia3_6<48:
        if counterx == 1 and hand_1[tipIds[0]][1]>hand_1[tipIds[0]-1][1]:
          letras="A"
          
      #Encontrar (B)
      if counterx==4 and hand_1[tipIds[0]][1]<hand_1[tipIds[0]-1][1]:
        letras="B"   
      #Encontrar (H)
      #if(countery==2 and counterx!=0 and counterx!=1):
      #  letras="H"  
      #para encontrar (L)
      if(counterx==2):
        if(angle<42 and angle>35):
          letras="L"  
                
                
      cv2.putText(img, letras, (480, 50), cv2.FONT_HERSHEY_COMPLEX,
                      2, (255, 0, 0), 5)
        
      return [img, letras]
    # Procesar lmlist aqui
    else:
        print("La lista lmlist está vacía o no es una lista válida.")
       