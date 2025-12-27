import turtle
WIDTH, HEIGHT = 1000, 600
screen = turtle.Screen()
screen.title("Pong Game")
screen.setup(width = WIDTH, height = HEIGHT)
screen.bgcolor('green')

#Left Paddle
lp = turtle.Turtle()
lp.speed(0)
lp.shape('square')
lp.color('black')
lp.shapesize(stretch_wid = 6, stretch_len = 2)
lp.penup()
lp.goto(-(WIDTH/2) + 100, 0)

		#Right paddle
rp = turtle.Turtle()
rp.speed(0)
rp.shape('square')
rp.color('blue')
rp.shapesize(stretch_wid = 6, stretch_len = 2)
rp.penup()
rp.goto((WIDTH/2) - 100, 0)

		# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape('circle')
ball.color('black')
ball.penup()
ball.goto(0, 0)
ball.dx = 6.5
ball.dy = -6.5

Home = 0
Guest = 0

score = turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0, 250)
score.write('GUEST: 0 HOME: 0', align = 'center', font = ('Courier', 24,'normal'))

		#paddle movement
def left_up():
	y = lp.ycor()
	y += 20
	lp.sety(y)
	if(lp.ycor() > 300):
		lp.sety(300)
def left_down():
	y = lp.ycor()
	y -= 20
	lp.sety(y)
	if(lp.ycor() < -300):
		lp.sety(-300)

def right_up():
	y = rp.ycor()
	y += 20
	rp.sety(y)
	if(rp.ycor() > 300):
		rp.sety(300)
def right_down():
	y = rp.ycor()
	y -= 20
	rp.sety(y)
	if(rp.ycor() < -300):
		rp.sety(-300)

screen.listen()
screen.onkeypress(left_up, 'w')
screen.onkeypress(left_down, 's')
screen.onkeypress(right_up, 'Up')
screen.onkeypress(right_down, 'Down')
#Game Loop
while True:
	screen.update()
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)
	if ball.ycor() > 280:
			ball.sety(280)
			ball.dy *= -1
	if ball.ycor() < -280:
		ball.sety(-280)
		ball.dy *= -1
	if ball.xcor() > 500:
		ball.goto(0, 0)
		ball.dy += 1
		Guest += 1
		score.clear()
		score.write('Guest: {} Home: {}'.format(Guest, Home), align = 'center', font = ('Courier', 24, 'normal'))
	if ball.xcor() < -500:
		ball.goto(0, 0)
		ball.dy *= -1
		Home += 1
		score.clear()
		score.write('Guest: {} Home: {}'.format(Guest, Home), align = 'center', font = ('Courier', 24, 'normal'))


	if ((ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < rp.ycor() + 100 and ball.ycor() > rp.ycor() -100)):
		ball.setx(360)
		ball.dx *= -1

	if ((ball.xcor() < -360 and ball.xcor() > -370) and (ball.ycor() < lp.ycor() + 100 and ball.ycor() > lp.ycor() -100)):
		ball.setx(-360)
		ball.dx *= -1