import math

#Calculate the third angle of the triangle
def angle_Alpha(Beta, Gamma):
    alpha=180 - Beta - Gamma
    return alpha

#Calculate side b of the tringle
def side_b(a, Alpha, Beta):
    b=a * math.sin(math.radians(Beta)) / math.sin(math.radians(Alpha))
    return b

#Calculate side c of the triangle
def side_c(a, Alpha, Gamma):
    c=a * math.sin(math.radians(Gamma)) / math.sin(math.radians(Alpha))
    return c

#Calculate area of the triangle
def area(a, b, Gamma):
    area_F = 0.5 * a * b * math.sin(math.radians(Gamma))
    return area_F
