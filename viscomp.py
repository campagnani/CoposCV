import cv2 as cv
import libOpenClient as loc

oc = loc.libOpenClient('200.128.140.12')

#Resolucao de captura:
webcam = cv.VideoCapture(1, cv.CAP_V4L2)
webcam.set(cv.CAP_PROP_FRAME_WIDTH, 800)
webcam.set(cv.CAP_PROP_FRAME_HEIGHT, 600)
webcam.set(cv.CAP_PROP_FPS, 10)

#Identificando a mesa:
#Obter imagem:
ret, frame = webcam.read()

#Conversao para tons de cinza:
image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#Aplicando Blur a imagem:
image = cv.blur(image, (7, 7), 0)

#Binarização com limiar:
T = 150
bin = image.copy()
bin[bin > T] = 255
bin[bin < 255] = 0
bin = cv.bitwise_not(bin)

y = -1

#Fazer ROI


while(True):
#for i in range(100):

    #Obter imagem:
    ret, frame = webcam.read()

    #Conversao para tons de cinza:
    image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #Aplicando Blur a imagem:
    image = cv.blur(image, (7, 7), 0)

    #Binarização com limiar:
    T = 150
    bin = image.copy()
    bin[bin > T] = 255
    bin[bin < 255] = 0
    bin = cv.bitwise_not(bin)

    #cv.imshow("Output", bin)
    #cv.imshow("hsadiof", frame)
    #cv.waitKey(1)

    #Aplicacao da transformada de Rough:
    circles = cv.HoughCircles(bin,cv.HOUGH_GRADIENT,1,1000,param1=300,param2=1,minRadius=20,maxRadius=40)

    #Desenhando os circulos identificados:
    #for i in range(len(circles)):
    cv.circle(frame, (int(circles[0][0][0]), int(circles[0][0][1])), int(circles[0][0][2]), (0, 0, 255), 2)

    coordenadas_Cartesianas = oc.listen_cart()

    print("U: "+str(circles[0][0][0])+"\t\tV: "+str(circles[0][0][1]) + "\t\tX: " + str(coordenadas_Cartesianas.x) + "\tY: " +  str(coordenadas_Cartesianas.y))

    with open('moving.txt', 'a') as file:
        file.write(str(circles[0][0][0])+",\t"+str(circles[0][0][1]) + ",\t" + str(coordenadas_Cartesianas.x) + ",\t" +  str(coordenadas_Cartesianas.y)+";\n")

    cv.imshow("Output", frame)
    cv.waitKey(30)
    
    