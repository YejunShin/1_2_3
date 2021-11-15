#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image="pear.gif"
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
wn.bgpic("background.gif")
apple = trtl.Turtle()
pear=trtl.Turtle()
drawer=trtl.Turtle()
pear.hideturtle()
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
def draw_pear(active_pear):
  active_pear.shape(pear_image)
  wn.update()
def drop_apple():
	apple.penup()
	apple.goto(0,-150)
def draw_an_A():
	drawer.penup()
	drawer.goto(0,100)
	drawer.color("white")
	drawer.write("A", font=("Arial", 74, "bold"))
def events():
	drop_apple()
	drawer.clear()
	apple.clear()
#-----function calls-----
draw_apple(apple)
draw_an_A()
wn.onkeypress(events, "a")
wn.listen()
wn.mainloop()