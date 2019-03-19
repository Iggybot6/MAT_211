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
        rightStr = "-G-"
    elif leftChar == "G":
        rightStr = "----"
    else:
        rightStr = leftChar    # no rules apply so keep the character
    return rightStr


def processString(oldStr, rule):
    """ given a string oldStr transform it into newStr with rules """
    newStr = ""
    for ch in oldStr:
        newStr = newStr + ruler(rule, ch)

    return newStr


def executeLSystem(numIters, rule, axiom):
    resultString = axiom
    for i in range(numIters):
        newString = processString(resultString, rule)
        resultString = newString
        print("doot")

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


def stringRules(strIn):
    """jellybean"""
    ruleLst = []
    lst = strIn.split("\n")
    for index in range(len(lst)):
        ruleLst.append(lst[index].split(" > "))
    return ruleLst


def ruler(rule, leftchar):
    """ice scream sammich"""
    rightStr = ""
    lstIn = stringRules(rule)
    for index in range(len(lstIn)):
        if leftchar == lstIn[index][0]:
            rightStr = lstIn[index][1]
    return rightStr


# MAIN BODY
rules = "F > F-F++F-F\n+ > -G-\nG > ----"
donatello = turtle.Turtle()
donatello.speed(0)
print(ruler(rules, "G"))
# print(executeLSystem(3, "F"))
goTurtleGo(donatello, executeLSystem(5, rules, "FG"))
wn.exitonclick()
