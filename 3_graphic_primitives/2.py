import graphics as gr


def shiftArray(array, delta):
    for i, el in enumerate(array):
        array[i] = el + delta


def setRectangle(window, upperLeftPoint, bottomRightPoint, color, lineWidth=1):
    rectangle = gr.Rectangle(upperLeftPoint, bottomRightPoint)
    rectangle.draw(window)
    rectangle.setFill(color)
    rectangle.setWidth(lineWidth)
    return rectangle.getCenter()


def setPolygon(window, vertices, color, lineWidth=1):
    polygon = gr.Polygon(vertices)
    polygon.draw(window)
    polygon.setFill(color)
    polygon.setWidth(lineWidth)


def setCircle(window, centerPoint, radius, color, lineWidth=1):
    circle = gr.Circle(centerPoint, radius)
    circle.draw(window)
    circle.setFill(color)
    circle.setWidth(lineWidth)


def drawClouds(window, firstCenter, radius, color, number):
    import random
    shiftX = 2.5
    shiftY = 1.5
    x = firstCenter.getX()
    y = firstCenter.getY()
    for _ in range(number):
        print(x, y)
        setCircle(window, gr.Point(x, y), radius, color)
        x = x + radius * shiftX * (0.5 - random.random())
        y = y + radius * shiftY * (0.5 - random.random())


def drawHouse(window, houseUpperLeftPoint, houseWidth, houseHeight, houseColor="#808080", lineWidth = 4):
    windowFrameWidthQuotient = 0.2

    houseBottomRightPoint = gr.Point(
        houseUpperLeftPoint.getX() + houseWidth,
        houseUpperLeftPoint.getY() + houseHeight)

    houseCenter = setRectangle(window, houseUpperLeftPoint,
        houseBottomRightPoint, houseColor, 4)    # домик
    houseCenterX = houseCenter.getX()
    houseCenterY = houseCenter.getY()

    windowFrameWidth = windowFrameWidthQuotient * houseWidth
    windowTopLeftX = houseCenterX - windowFrameWidth
    windowTopLeftY = houseCenterY - windowFrameWidth
    windowBottomRightX = houseCenterX + windowFrameWidth
    windowBottomRightY = houseCenterY + windowFrameWidth

    # оконная рама в целом
    setRectangle(window, gr.Point(windowTopLeftX, windowTopLeftY),
        gr.Point(windowBottomRightX, windowBottomRightY), "black", lineWidth)

    # отдельные стекла в раме
    setRectangle(window, gr.Point(windowTopLeftX, windowTopLeftY),
        gr.Point(houseCenterX, houseCenterY), "yellow", lineWidth)
    setRectangle(window, gr.Point(houseCenterX, windowTopLeftY),
        gr.Point(windowBottomRightX, houseCenterY), "yellow", lineWidth)
    setRectangle(window, gr.Point(windowTopLeftX, houseCenterY),
        gr.Point(houseCenterX, windowBottomRightY), "yellow", lineWidth)
    setRectangle(window, gr.Point(houseCenterX, houseCenterY),
        gr.Point(windowBottomRightX, windowBottomRightY), "yellow", lineWidth)

    # крыша
    houseTopVertex = gr.Point(houseUpperLeftPoint.getX() + houseWidth / 2,
        houseUpperLeftPoint.getY() - houseWidth / 2)

    setPolygon(window,
        [houseTopVertex, houseUpperLeftPoint,
        gr.Point(houseUpperLeftPoint.getX() + houseWidth,
        houseUpperLeftPoint.getY())], "#a52a2a", 4)

def drawFirTree(window, branchLeftEnd, branchRightEnd, branchTop, branchHeight,
    truncWidth, truncLen, branchesQty, treeColor="green"):
        leftX, leftY = branchLeftEnd.getX(), branchLeftEnd.getY()
        rightX, rightY = branchRightEnd.getX(), branchRightEnd.getY()
        topX, topY = branchTop.getX(), branchTop.getY()

        setRectangle(window, gr.Point(topX - truncWidth / 2, leftY),
            gr.Point(topX + truncWidth / 2, leftY + truncLen), "#a52a2a", 4)

        for _ in range(branchesQty):
            setPolygon(window, [gr.Point(leftX, leftY),
                gr.Point(rightX, rightY), gr.Point(topX, topY)], treeColor, 4)
            leftY -= branchHeight
            rightY -= branchHeight
            topY -= branchHeight


def main():
    window = gr.GraphWin("A cosy landscape", 788, 584)
    setRectangle(window, gr.Point(0, 0), gr.Point(788, 292), "blue")    # небо
    setRectangle(window, gr.Point(0, 293), gr.Point(788, 788), "#d9d9d9")    # земля

    # облака (три группы)
    drawClouds(window, gr.Point(90, 90), 25, "white", 5)
    drawClouds(window, gr.Point(350, 110), 25, "white", 6)
    drawClouds(window, gr.Point(600, 170), 20, "white", 5)

    # солнце
    setCircle(window, gr.Point(590, 85), 50, "yellow", 2)

    # дом
    houseWidth = 200
    houseHeight = 200
    houseUpperLeftPoint = gr.Point(220, 230)
    drawHouse(window, houseUpperLeftPoint, houseWidth, houseHeight)

    # ель № 1
    leftX, leftY = 500, 410
    branchLeftEnd = gr.Point(leftX, leftY)
    rightX, rightY = 620, 410
    branchRightEnd = gr.Point(rightX, rightY)
    topX, topY = (leftX + rightX) / 2, 370
    branchTop = gr.Point(topX, topY)
    truncWidth = 8
    truncLen = 45
    branchHeight = 45
    branchesQty = 3

    drawFirTree(window, branchLeftEnd, branchRightEnd, branchTop, branchHeight,
        truncWidth, truncLen, branchesQty, treeColor="green")

    # ель № 2
    leftX, leftY = 545, 440
    branchLeftEnd = gr.Point(leftX, leftY)
    rightX, rightY = 690, 440
    branchRightEnd = gr.Point(rightX, rightY)
    topX, topY = (leftX + rightX) / 2, 360
    branchTop = gr.Point(topX, topY)
    truncWidth = 10
    truncLen = 50
    branchHeight = 50
    branchesQty = 4

    drawFirTree(window, branchLeftEnd, branchRightEnd, branchTop, branchHeight,
        truncWidth, truncLen, branchesQty, treeColor="green")

    window.getMouse()
    window.close()


if __name__ == '__main__':
    main()
