import cv2
from pyzbar.pyzbar import decode
linkedin=cv2.imread('qrimages/linkedin.jpg')
instagram=cv2.imread('qrimages/instagram.jpg')
facebook=cv2.imread('qrimages/facebook.jpg')
snap=cv2.imread('qrimages/snap.jpg')

"""
cap=cv2.VideoCapture(1)
 بي استعمال الكميراء( qrcode )هذا لي قرائت ال
while True:
    _,img=cap.cap.red()
    
cv2.imshow('Barcode Reader', img)
cv2.waitKey(1)

"""

for barcode in decode(linkedin):
    myqrcode = barcode.data.decode('utf-8')
    barcodeType=barcode.type
    print ('linkedin')
    (x,y,w,h)=barcode.rect
    cv2.rectangle(linkedin,(x,y),(x+w,y+h),(0,0,255,2))
    text="{}({})".format(myqrcode,barcodeType)
    cv2.putText(linkedin,text,(x,  y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255,),2)\
    ###################################
   
for barcode in decode(instagram):    
    myqrcode = barcode.data.decode('utf-8')
    barcodeType=barcode.type
    print ('instagram')
    (x,y,w,h)=barcode.rect
    cv2.rectangle(instagram,(x,y),(x+w,y+h),(0,0,255,2))
    text="{}({})".format(myqrcode,barcodeType)
    cv2.putText(instagram,text,(x,  y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255,),2)
   
for barcode in decode(facebook):    
    myqrcode = barcode.data.decode('utf-8')
    barcodeType=barcode.type
    print ('instagram')
    (x,y,w,h)=barcode.rect
    cv2.rectangle(facebook,(x,y),(x+w,y+h),(0,0,255,2))
    text="{}({})".format(myqrcode,barcodeType)
    cv2.putText(facebook,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255,),2)
    
for barcode in decode(snap):    
    myqrcode = barcode.data.decode('utf-8')
    barcodeType=barcode.type
    print ('snap')
    (x,y,w,h)=barcode.rect
    cv2.rectangle(instagram,(x,y),(x+w,y+h),(0,0,255,2))
    text="{}({})".format(myqrcode,barcodeType)
    cv2.putText(snap,text,(x,  y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255,),2)

 

cv2.imshow('linkedin',linkedin)
#cv2.imshow('instagram',instagram)
#cv2.imshow('facebook',facebook)
cv2.imshow('snap',snap)
cv2.waitKey(0)