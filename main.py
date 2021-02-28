import classes
print('''Figures:
1: Circle
2: Triangle
3: Square

''')
figures = [classes.cir, classes.tri, classes.square]
for i in figures:
    if i == classes.cir:
        print('The area of the circle is', classes.cir.area())
    elif i == classes.tri:
        print('The area of the triangle is', classes.tri.area())
    else:
        print('The area of the square is', classes.square.area())


