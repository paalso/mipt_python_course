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
    lineWidth = 4

    houseWidth = houseHeight = 200
    houseUpperLeftPoint = gr.Point(190, 190)
    houseBottomRightPoint = gr.Point(390, 390)

    houseCenter = setRectangle(window, houseUpperLeftPoint,
        houseBottomRightPoint, "#808080", 4)    # домик
    houseCenterX = houseCenter.getX()
    houseCenterY = houseCenter.getY()

    windowFrameWidth = 0.2 * houseWidth
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

    # ель
    leftX, leftY = 545, 440
    rightX, rightY = 690, 440
    topX, topY = (leftX + rightX) / 2, 360

    truncWidth = 10
    truncLen = 50
    setRectangle(window, gr.Point(topX - truncWidth / 2, leftY),
        gr.Point(topX + truncWidth / 2, leftY + truncLen), "#a52a2a", 4)

    for _ in range(3):
        setPolygon(window, [gr.Point(leftX, leftY),
            gr.Point(rightX, rightY), gr.Point(topX, topY)], "green", 4)
        leftY -= 50
        rightY -= 50
        topY -= 50

    window.getMouse()
    window.close()


if __name__ == '__main__':
    main()
