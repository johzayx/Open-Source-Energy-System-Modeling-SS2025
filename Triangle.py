import math


# Calculate the third angle of the triangle
def angle_Alpha(Beta, Gamma):
    alpha = round(180 - Beta - Gamma, 2)
    return alpha


# Calculate side b of the tringle
def side_b(a, Alpha, Beta):
    b = round(a * math.sin(math.radians(Beta)) / math.sin(math.radians(Alpha)), 2)
    return b


# Calculate side c of the triangle
def side_c(a, Alpha, Gamma):
    c = round(a * math.sin(math.radians(Gamma)) / math.sin(math.radians(Alpha)), 2)
    return c


# Calculate area of the triangle
def area(a, b, Gamma):
    area_F = round(0.5 * a * b * math.sin(math.radians(Gamma)), 2)
    return area_F
