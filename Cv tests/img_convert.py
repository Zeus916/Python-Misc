import cv2

image = cv2.imread('dog.jpg')
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#dst_gray, dst_color = cv2.pencilSketch(image, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
dst = cv2.stylization(image, sigma_s=60, sigma_r=0.01)
cv2.imshow('Output', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()