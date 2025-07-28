import cv2


img = cv2.imread("image.jpg")


#cap = cv2.VideoCapture(0)

#while True:
#    ret, frame= cap.read()
#    if not ret:
#        break
#    cv2.imshow("Video", frame)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break

#cv2.imshow("Windows", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

cv2.imshow("Gray Image", gray)
cv2.imshow("Blurred Image", blur)


edges = cv2.Canny(img, 100, 200)
cv2.imshow("Window", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

#TASK-1: cv making process



