import qrcode
image=qrcode.make(input("\Enter your link or text here...."))
image.save("QRcode1.jpg")
import cv2
cv2_object=cv2.QRCodeDetector()
val,points,straight_qrcode=cv2_object.detectAndDecode(cv2.imread("QRcode.jpg"))
print(val)