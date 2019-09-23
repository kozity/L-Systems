class LSys:

    def __init__(self, alpha, axio, dist, angl, filePref):
        self.alphabet = alpha
        self.axiom = axio
        self.distance = dist
        self.angle = angl
        self.filePrefix = filePref
        #self.initialPosition = initPos
        #self.initialHeading = initHead


    def returnString(self, n):
        sequence = self.axiom
        for i in range(n):
        # iterate n times
            working = sequence
            sequence = ''
            # working now equals some string; sequence is now an empty string
            for j in working:
            # for each character in the working string, do the following:
                sequence = sequence + self.alphabet[j][0]
        return sequence

    def generateString(self, n):
        print(self.returnString(n))
        wait = input("\nPress ENTER to close")

    def generateFile(self, n):
        with open('C:/Code/Python/L-Systems/Text Files/'+self.filePrefix+'_n'+str(n)+'.txt', 'x') as f:
            f.write(self.returnString(n))

    def generateTurtle(self, n):
        stack = []
        import turtle
        turtle.pensize(1)
        turtle.speed(0)
        turtle.hideturtle()
        turtle.setheading(30)
        turtle.bgcolor('light gray')
        turtle.screensize(10000,10000)
        for k in self.returnString(n):
            if self.alphabet[k][1] == 'none':
                continue
            elif self.alphabet[k][1] == 'forward':
                turtle.forward(self.distance)
            elif self.alphabet[k][1] == 'left':
                turtle.left(self.angle)
            elif self.alphabet[k][1] == 'right':
                turtle.right(self.angle)
            elif self.alphabet[k][1] == 'push':
                stack.append((turtle.position(), turtle.heading()))
            elif self.alphabet[k][1] == 'pop':
                turtle.penup()
                position, heading = stack.pop()
                turtle.setposition(position)
                turtle.setheading(heading)
                turtle.pendown()
        turtle.bgcolor('white')
        turtle.exitonclick()

fractalPlant = LSys({'X': ['F+[[X]-X]-F[-FX]+X', 'none'],
                     'F': ['FF', 'forward'],
                     '+': ['+', 'left'],
                     '-': ['-', 'right'],
                     '[': ['[', 'push'],
                     ']': [']', 'pop']}, 'X', 4, 30, 'FractalPlant')

dragonHeighway = LSys({'X': ['X+YF+', 'none'],
                       'Y': ['-FX-Y', 'none'],
                       'F': ['F', 'forward'],
                       '+': ['+', 'left'],
                       '-': ['-', 'right']}, 'FX', 2, 90, 'DragonHeighway')

sierpinski = LSys({'F': ['F-G+F+G-F', 'forward'],
                   'G': ['GG', 'forward'],
                   '+': ['+', 'left'],
                   '-': ['-', 'right']}, 'F-G-G', 6, 120, 'Sierpinski')

binary = LSys({'0': ['1[+0]-0', 'forward'],
               '1': ['11', 'forward'],
               '+': ['+', 'left'],
               '-': ['-', 'right'],
               '[': ['[', 'push'],
               ']': [']', 'pop']}, '0', 3, 45, 'Binary')


# PUT COMMAND BELOW
dragonHeighway.generateTurtle(12)
