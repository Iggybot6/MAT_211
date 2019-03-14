import turtle
import random

turtle.setup(1920, 1080)
wn = turtle.Screen()
wn.bgcolor("antique white")


def applyRules(leftChar):
    """ apply rule transforming leftChar to rightStr """
    rightStr = ""
    if leftChar == 'F':
        rightStr = 'F-F++F-F'
    elif leftChar == "+":
        rightStr = "F-FGF"
    elif leftChar == "G":
        rightStr = "F----F"
    else:
        rightStr = leftChar    # no rules apply so keep the character
    return rightStr


def processString(oldStr):
    """ given a string oldStr transform it into newStr with rules """
    newStr = ""
    for ch in oldStr:
        newStr = newStr + applyRules(ch)

    return newStr


def executeLSystem(numIters,axiom):
    resultString = axiom
    for i in range(numIters):
        newString = processString(resultString)
        resultString = newString

    return resultString


def goTurtleStep(turtleIn, cmd):
    """potato"""
    if cmd == "F":
        turtleIn.forward(5)
    elif cmd == "-":
        turtleIn.left(60)
    elif cmd == "+":
        turtleIn.right(60)
    elif cmd == "G":
        rVal = random.random()
        gVal = random.random()
        bVal = random.random()
        tup = (rVal, gVal, bVal)
        turtleIn.pencolor(tup)


def goTurtleGo(turtleIn, cmdStr):
    """rhubarb"""
    for char in cmdStr:
        goTurtleStep(turtleIn, char)


donatello = turtle.Turtle()
donatello.speed(0)
# print(executeLSystem(3, "F"))
goTurtleGo(donatello, executeLSystem(4, "FG"))
wn.exitonclick()
