from turtle import Turtle, Screen
import random
import colorgram

#sets the screen mode to accept 255 rbg instead of named colours.
screen = Screen()
screen.colormode(255)

t = Turtle()
t.shape('classic')
t.color(0,0,0)
t.width(10)
t.speed(1)


rgb_colors = []
colours = colorgram.extract('wreck.jpg', 100)

# Used to populate the list above. 
for color in colours:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)



screen.bgcolor(rgb_colors[random.randint(0,33)])













screen.exitonclick()


















