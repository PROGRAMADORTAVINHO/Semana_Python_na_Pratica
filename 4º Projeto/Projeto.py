# Bibliotecas
# pip install opencv-python
# pip install mediapipe
# pip install cvzone

import cv2
from cvzone.HandTrackingModule import HandDetector

webcam = cv2.VideoCapture(0) # VideoCapture(qual é a webcam)
rastreador = HandDetector(detectionCon=0.8, maxHands=2)
# HandDetector(detectionCon= quantos % vc quer que pareca uma mão,    => Faz o rastreamento da mão
#              maxHands= maximo de mãos para detectar)

while True:
    sucesso, imagem = webcam.read() # Retorna o Frame
    coordenadas, imagem_mao = rastreador.findHands(imagem) # Retorna as imagems da mão, com a IA analisando

    print(coordenadas)

    cv2.imshow("Projeto 4 - IA", imagem)
    
    if (cv2.waitKey(1) != -1): # .waitKey(milissegundos) => Monitora se apertou alguma tecla
        break

webcam.release() # Libera a utilização da webcam
cv2.destroyAllWindows() # Fecha todas as janelas