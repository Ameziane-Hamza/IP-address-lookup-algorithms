from from_txt_to_multi_tree import *
######################################
from turtle import *

screen=Screen()
screen.title("Multi-Bit Trie")
screen.setup(width=0.99,height=0.99)
t=Turtle()
######################################
t.up()
t.goto(0,250)
t.write("root", align="center", font=("Arial", 15, "normal"))
t.goto(0,240)
t.down()
t.circle(25)
t.right(90)
x=t.position()
##########################
root=arbre_multi.root
level=-1
##########################
def draw_node(angle,forward,level,word=""):
    t.right(angle/(2**level))
    t.down()
    if level == 0:
        t.forward(forward)
    else:
        t.forward(forward/(2**(level+1)))
    t.left(90+(angle/(2**level)))
    t.up()
    a_x, a_y = t.position()
    t.goto(a_x, a_y - 40)
    t.write(word[:2], align="center", font=("Arial", 15, "normal"))
    t.goto(a_x, a_y - 50)
    t.down()
    t.circle(25)
    t.right(90)
    t.up()
###########################
dic_1={}
dic_2={}
###########################
def draw_1(position,level,curr_node):
    t.up()
    t.goto(position)
    if curr_node._00 != None :
        c=curr_node._00
        if c.route == None :
            draw_node(81, 550, level)
        else:
            draw_node(81, 550, level, c.route)
        dic_1[t.position()]=c
        t.goto(position)
    if curr_node._01 != None :
        c=curr_node._01
        if c.route == None:
            draw_node(61, 240, level)
        else:
            draw_node(61,240,level,c.route)
        dic_1[t.position()] = c
        t.goto(position)
    if curr_node._10 != None :
        c=curr_node._10
        if c.route == None:
            draw_node(-61, 240, level)
        else:
            draw_node(-61, 240, level, c.route)
        dic_1[t.position()] = c
        t.goto(position)
    if curr_node._11 != None :
        c=curr_node._11
        if c.route == None :
            draw_node(-81, 550, level)
        else:
            draw_node(-81, 550, level, c.route)
        dic_1[t.position()] = c
        t.goto(position)
###########################################################
def draw_2(position,level,curr_node):
    t.up()
    t.goto(position)
    if curr_node._00 != None :
        c=curr_node._00
        if c.route == None:
            draw_node(81, 550, level)
        else:
            draw_node(81, 550, level, c.route)
        dic_2[t.position()]=c
        t.goto(position)
    if curr_node._01 != None :
        c=curr_node._01
        if c.route == None:
            draw_node(61, 240, level)
        else:
            draw_node(61,240,level,c.route)
        dic_2[t.position()] = c
        t.goto(position)
    if curr_node._10 != None :
        c=curr_node._10
        if c.route == None:
            draw_node(-61, 240, level)
        else:
            draw_node(-61,240,level,c.route)
        dic_2[t.position()] = c
        t.goto(position)
    if curr_node._11 != None :
        c=curr_node._11
        if c.route == None:
            draw_node(-81, 550, level)
        else:
            draw_node(-81, 550, level, c.route)
        dic_2[t.position()] = c
        t.goto(position)
###########################################################

def dessin(position,curr_node):
    global level
    level+=1
    draw_1(position,level,curr_node)
    return dessin_1()
############################################################
def dessin_1():
    global level
    level += 1
    for k in dic_1:
        draw_2(k,level,dic_1[k])
    dic_1.clear()

#############################################################
def dessin_2():
    global level
    level += 1
    for k in dic_2:
        draw_1(k,level,dic_2[k])
    dic_2.clear()

#############################################################

t.speed(0)
dessin(x,root)
done()