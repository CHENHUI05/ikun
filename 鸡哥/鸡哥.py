import turtle as t
frame=[]
t1=t.Turtle();t1.speed(10)
t1.shape("turtle")
t1.shapesize(4,4)
t1.pu();t1.goto(-600,0);t1.down()
for i in range(9):
    frame.append(f"{i}.gif")
#print(frame)
b=-1 
def s(x,y):
    global b
    b+=1
    t.goto(0,0)
    t.addshape(frame[b])
    t.shape(frame[b])
    if b==8:
        b=0
t1.onclick(s,1)
t.mainloop()
