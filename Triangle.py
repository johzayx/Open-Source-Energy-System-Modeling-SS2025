import math

#Calculate the third angle of the triangle
def W(Beta, Gamma):
    alpha=180 - Beta - Gamma
    return alpha

#Calculate side b of the tringle
def b(a, Alpha, Beta):
    b=a * math.sin(math.radians(Beta)) / math.sin(math.radians(Alpha))
    return b

#Calculate side c of the triangle
def c(a, Alpha, Gamma):
    c=a * math.sin(math.radians(Gamma)) / math.sin(math.radians(Alpha))
    return c

#Calculate area of the triangle
def F(a, b, Gamma):
    area_F = 0.5 * a * b * math.sin(math.radians(Gamma))
    return area_F
