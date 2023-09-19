import turtle

mainCircleRadius = 300
semiCircleRadius = mainCircleRadius / 2
smallCircleRadius = mainCircleRadius / 5
distanceBetweenCenterAndSmallCircle = 105

fullTurn = 360
halfTurn = 180
quaterTurn = 90

turtle.tracer(10, None)
brush = turtle.Turtle()
brush.shape("turtle")

def DrawSemiCircle(mainColor, additionalColor):
    brush.pensize(2)
    brush.color("black", mainColor)
    
    brush.begin_fill()
    brush.circle(semiCircleRadius, halfTurn)
    brush.circle(mainCircleRadius, halfTurn)
    brush.left(halfTurn)
    brush.circle(-semiCircleRadius, halfTurn)
    brush.end_fill()

    brush.left(90)

    brush.up()
    brush.forward(distanceBetweenCenterAndSmallCircle)
    brush.right(90)
    brush.down()
    
    brush.color(mainColor, additionalColor)
    
    brush.begin_fill()
    brush.circle(smallCircleRadius)
    brush.end_fill()

    brush.left(90)

    brush.up()
    brush.backward(distanceBetweenCenterAndSmallCircle)
    brush.down()
    
    brush.left(90)

DrawSemiCircle("black","white")
DrawSemiCircle("white","black")
turtle.done()