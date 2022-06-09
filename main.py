import cv2 as cv
import numpy as np

#Importa a imagem em escala de cinza:
im = cv.imread('frame.jpeg', 0)

#Reduzindo o tamanho da imagem:
image = cv.resize(im, (int(len(im[0])/2), int(len(im)/2)))

#Equalizacao de histograma:
#eq_im = cv.equalizeHist(image) 

#Brilho e contraste:
#alpha = 1
#beta = 100
#bc_im = np.uint8(np.clip((alpha * image + beta), 0, 255))

#Aplicando um limiar de luminosidade:
threshold = 130
for i in range(len(image)):
    for j in range(len(image[0])):
        if(image[i][j] > threshold):
            image[i][j] = 255
        else:
             image[i][j] = 0



cv.imshow('Visualizacao', image)
cv.waitKey(0)