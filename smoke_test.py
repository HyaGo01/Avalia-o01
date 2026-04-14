import cv2

# carregar imagem
img = cv2.imread('Debi02.jpeg')

# converter para cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# mostrar imagem
cv2.imshow('Imagem em Cinza', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
