
import cv2 as cv

# Lendo Imagens/Reading Images
img = cv.imread('Photos/cats.jpg')   #cv.comando('NOME_JANELA')
cv.imshow('Cats', img)               #cv.comando('NOME_JANELA',VARIAVEL)

cv.waitKey(0) #espera o usuário apertar o teclado

# Lendo Videos/Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4') 

while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release() #desassocia a variavel 'capture' do video
cv.destroyAllWindows()
