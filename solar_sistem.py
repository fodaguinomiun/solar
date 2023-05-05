import cv2


img=cv2.imread("solar-system.jpg")

cv2.imshow("resultado",img)
cv2.waitKey(0)

cv2.putText(img,
            "Sol",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,225)
            )
cv2.putText(img,
            "Mercúrio",
            (120,100),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,225)
            )
cv2.putText(img,
            "Venus",
            (150,120),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,225)
            )
cv2.putText(img,
            "Terra",
            (170,140),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,
             225)
            )
cv2.putText(img,
            "Marte",
            (190,160),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,225)
            )
cv2.putText(img,
            "Jupiter",
            (210,180),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,225)
            )
cv2.putText(img,
            "Saturno",
            (230,200),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,225)
            )
cv2.putText(img,
            "Uranos",
            (250,220),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,225)
            )
cv2.putText(img,
            "Neturno",
            (270,240),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,225)
            )
