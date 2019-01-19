
import numpy as np
import cv2

# @author Mason Hawver
# @ version 1
# The purpose of this class is to be able to represent regular polygons
# Note: will help if you understand basic Geometry and Law of sines
class Regular_Polygon:

    # @param side_number is the number of sides of the reg poly
    # (precondition: side_number >= 3)
    #
    # @param side_length is the length of side
    # (precondition: side_length > 0)

    def __init__(self, side_number, side_length):
        self.side_num = side_number
        self.side_len = side_length

    # calculates the perimeter of the regular polygon
    # @return gives perimeter of reg poly
    def find_perimeter(self):
        return self.side_len * self.side_num

    # calculates the area of the regular polygon
    # @return gives area of reg poly
    def find_area(self):
        angle_a = ((self.side_num - 2) * 180) / (self.side_num * 2)
        angle_b = (360 / (self.side_num * 2))
        side_b = self.side_len / 2
        side_a = (side_b * np.sin(np.deg2rad(angle_a))) / np.sin(np.deg2rad(angle_b))

        area = side_b * side_a * self.side_num
        return area

    # calculates the radius of the circumcircle
    # the circumcircle is the circle that is tangent to all verticies of the regular polygon
    # Note: in to_img() method the circumcircle is the red circle
    # @return radius of circumcircle
    def find_circumcircle_radius(self):
        angle_b = ((self.side_num - 2) * 180) / (self.side_num * 2)
        angle_a = 360 / self.side_num
        side_a = self.side_len

        radius = (side_a * np.sin(np.deg2rad(angle_b))) / np.sin(np.deg2rad(angle_a))
        return radius

    # calculates the radius of the incircle
    # the incircle is the circle tangent with all the sides of the regular polygon
    # Note: it is the green circle in to img method
    # @return radius of incircle
    def find_incircle_radius(self):
        side_a = self.find_circumcircle_radius()
        side_b = self.side_len / 2

        radius = np.sqrt((side_a ** 2 - side_b ** 2))
        return radius

    # calculates the length of a side from side length and circumcircle radius
    # @return new side length
    @staticmethod
    def find_side_len(side_num, radius):
        angle_a = ((side_num - 2) * 180) / (side_num * 2)
        angle_b = (360 / (side_num))

        side_len = radius * np.sin(np.deg2rad(angle_b))
        side_len /= np.sin(np.deg2rad(angle_a))
        return side_len

    # calculates the exact coordinate on circle based of circle origin and circle radius
    # Note: this requires advanced trig skills to understand
    # @return coordinate in np array
    @staticmethod
    def find_point_on_circle(origin, radius, angle):
        x_point = origin[0] + (radius * np.cos(np.deg2rad(angle)))
        y_point = origin[1] + (radius * np.sin(np.deg2rad(angle)))

        return np.array([x_point, y_point])

    # converts regular polygon to img array
    # @param starting_angle is the beginning angle for first point
    # @param circumcircle is a bool (True -> draws circumcircle)
    # @param incircle is a bool (True -> draws incircle)
    #
    # @return gives img arr (you need to save it or display it with cv2)

    def to_img(self, starting_angle=0, circumcircle=True, incircle=True):
        angle_sum = starting_angle
        radius = self.find_circumcircle_radius()
        diameter = radius * 2

        points = np.zeros((self.side_num, 2), dtype=np.int64)

        for i in range(self.side_num):
            point = Regular_Polygon.find_point_on_circle((int(radius), int(radius)), radius, angle_sum)
            point = point.astype(np.int64)
            points[i, :] = point

            angle_sum += 360 / self.side_num

        arr = np.zeros((int(np.ceil(diameter)) + 1, int(np.ceil(diameter)) + 1, 3))

        radius = int(radius)
        inner_radius = int(self.find_incircle_radius())
        if incircle:
            cv2.circle(arr, (radius, radius), inner_radius + 1, [0, 255, 0], 1)
        if circumcircle:
            cv2.circle(arr, (radius, radius), radius + 1, [0, 0, 255], 1)
        cv2.polylines(arr, [points], 1, (255, 255, 255))

        return arr

