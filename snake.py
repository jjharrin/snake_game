# Yo coding a rad snake game



import turtle
import time
import random


delay = 0.1

# setup the screen
wn = turtle.Screen()
wn.title("Snake by Sir Jayzalot")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) #turns off the screen updates

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
#head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-290,290), random.randint(-290,290))
food.direction = "stop"

#segment list
segments = []

# functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    
    if head.direction == "left":
        head.setx(head.xcor() - 20)

    if head.direction == "right":
        head.setx(head.xcor() + 20)

#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"c")
wn.onkeypress(go_right,"v")

#main game loop
while True:
    wn.update()

    #check for collision with border
    if head.xcor() > 290 or head.xcor()< -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        #hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        #clear the segments list
        segments.clear()

    #check for collision with food
    if head.distance(food) < 20:

        #move food to random place
        food.goto(random.randint(-290,290),random.randint(-290,290))
    
        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        #new_segment.penup()
        segments.append(new_segment)
        delay -= .002

    #move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    
    #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    #check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.diredtion = "stop"

            
            #hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            #clear the segments list
            segments.clear()
            
    time.sleep(delay)

wn.mainloop()
