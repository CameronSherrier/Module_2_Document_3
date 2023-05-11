def squareRoot():
    length = float(input("What is the length(ft)?: "))
    width = float(input("What is the width(ft)?: "))
    area = length * width
    return f'The total square footage is {area}.'

def myCircumference():
    diameter = float(input("What is the total diameter(in) of the circle?: "))
    radius = diameter / 2
    c = 2 * 3.14 * radius
    return f'The total circumference of the cirlce is {c} inches.'