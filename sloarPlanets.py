import cv2
img = cv2.imread("solar-system.jpg")
text_show = "Sun"
cv2.putText(img,text_show,(10,200),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=2,color=(220,0,0))
text_show1 = "Mercury"
cv2.putText(img,text_show1,(130,170),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,0,255))
text_show2 = "Venus"
cv2.putText(img,text_show2,(200,170),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,0,255))
text_show3 = "Earth"
cv2.putText(img,text_show3,(290,170),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,0,255))
text_show4 = "Mars"
cv2.putText(img,text_show4,(390,170),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,0,255))
text_show5 = "Juipter"
cv2.putText(img,text_show5,(490,170),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))
text_show6 = "Saturn"
cv2.putText(img,text_show6,(750,170),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))
text_show7 = "Uranus"
cv2.putText(img,text_show7,(950,170),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))
text_show8 = "Neptune"
cv2.putText(img,text_show8,(1100,170),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))
cv2.imshow("OUTPUT",img)

cv2.waitKey(0)
