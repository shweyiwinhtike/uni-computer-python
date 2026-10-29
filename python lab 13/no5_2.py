import turtle as t

t.speed(0)

def cross(width, times):
    if times == 0:
        t.dot(6)
        return
    else:
        for i in range(4):
            t.forward(width)
            cross(width / 2, times - 1)
            t.right(180)
            t.forward(width)
            t.left(90)
            
            # t.forward(width/2)
            # t.right(180)
            # cross(width / 2, times - 1)
            # t.left(90)

        # for i in range(4):
        #     t.forward(width)
    
            
        #     cross(width / 2, times - 1)
        #     t.right(180)
        #     t.forward(width)
        #     t.left(90)

cross(100, 4)
t.done()