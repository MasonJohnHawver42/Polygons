import RegularPolygons
import numpy as np
import cv2

Regular_Polygon = RegularPolygons.Regular_Polygon


def nothing(x):
    pass


img = np.zeros((64, 256, 3), np.uint8)
cv2.namedWindow('UI')

cv2.createTrackbar('side_num', 'UI', 3, 128, nothing)
cv2.createTrackbar('size', 'UI', 10, 1024, nothing)
cv2.createTrackbar('turn_speed', 'UI', 1, 256, nothing)

cv2.createTrackbar('circumcircle', 'UI', 1, 1, nothing)
cv2.createTrackbar('incircle', 'UI', 0, 1, nothing)

angle = 0
while True:
    side_num = cv2.getTrackbarPos('side_num', 'UI')
    size = cv2.getTrackbarPos('size', 'UI')

    angle_change = cv2.getTrackbarPos('turn_speed', 'UI')

    circumcircle = bool(cv2.getTrackbarPos('circumcircle', 'UI'))
    incircle = bool(cv2.getTrackbarPos('incircle', 'UI'))

    if side_num < 3:
        side_num = 3
    if size < 1:
        side_len = 1

    side_len = Regular_Polygon.find_side_len(side_num, size)

    test = Regular_Polygon(side_num, side_len)
    poly_img = test.to_img(angle, circumcircle, incircle)

    cv2.imshow("Polygons!", poly_img)
    cv2.imshow("UI", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    angle -= angle_change / 20

