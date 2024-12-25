from mathPainter import Canvas, Rectangle, Square



if __name__ == "__main__":
    # Assigning either black or white color to canvas
    color = 'white'
    if color.lower() == 'white':
        color_val = (255,255,255)
    elif color.lower() == 'black':
        color_val = (0,0,0)

    cv = Canvas(500, 1200, color_val)
    rc = Rectangle(3, 3, 100, 600, color=(150,10,50))
    rc.draw_rect(cv)
    sq = Square(6, 6, 50, color=(10,60,100))
    sq.draw_sqr(cv)
    cv.make_canvas('abc.png')