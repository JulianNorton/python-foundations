import turtle

def draw_square(some_turtle):
    for i in range(0,4):
        some_turtle.forward(200)
        some_turtle.left(20)

def draw_art():
    print('test')
    window = turtle.Screen()
    window.bgcolor("#ee5555")
    # window.delay(50)
    brad = turtle.Turtle()
    brad.speed(100)
    brad.color("#0000ff")
    brad.shape("arrow")
    for i in range(0,36):
        draw_square(brad)
        brad.left(10)
    # 
    # angie = turtle.Turtle()
    # angie.color("#00ff00")
    # angie.circle(200)
    window.exitonclick()

draw_art()