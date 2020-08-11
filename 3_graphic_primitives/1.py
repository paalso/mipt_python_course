import graphics as gr

def setRectangle(window, upperLeftX, upperLeftY, bottomRightX, bottomRightY, color):
    rectangle = gr.Rectangle(gr.Point(upperLeftX, upperLeftY),
                            gr.Point(bottomRightX, bottomRightY))
    rectangle.draw(window)
    rectangle.setFill(color)


def main():
    window = gr.GraphWin("A cosy landscape", 788, 584)
    setRectangle(window, 0, 0, 788, 292, "blue")    # небо
    setRectangle(window, 0, 293, 788, 788, "#d9d9d9")    # земля
    setRectangle(window, 190, 190, 390, 390, "#808080")    # домик



    window.getMouse()
    window.close()


if __name__ == '__main__':
    main()
