import turtle

class Circuito():
    corredores = []
    __posStartY = (-60, -20, 20, 60)
    __colorTurtle = ('red','blue', 'green', 'orange')
    
    def __init__(self, width, height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__starline = -width/2 + 20
        self.__finishline = width/ - 20
        
        self.__createRunners()

    def __createRunners(self):
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle')            
            new_turtle.penup()
            new_turtle.setpos(self.__starline, self.__posStartY[i])
            new_turtle.color(self.__colorTurtle[i])
            
            self.corredores.append(new_turtle)
        
        
        
        
        
        
        
if __name__ == '__main__':
    circuito = Circuito(640, 480)
    
    