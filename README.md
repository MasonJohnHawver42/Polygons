# Polygons
A class representing all regular polygons:

# Needs:
Numpy and opencv

# How to use me:

    import RegularPolygons
    import cv2
    
    Regular_Polygon = RegularPolygons.Regular_Polygon
    
    side_num = 6
    side_len = 120
    
    test_poly = Regular_Polygon(side_num, side_len)
    
    perimeter = test_poly.find_perimeter()
    area = test_poly.find_area()
    
    print("poly perimeter: ", perimeter)
    print("poly area: ", area)
    
    poly_img = test_poly.to_img()
    
    cv2.imshow("polygon", poly_img)
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()


