import turtle as t

t.speed(50)

def cross(width, times):
    if times == 0:
        t.dot(6)
        return
    else:
        t.forward(width)
        t.backward(width)
        t.left(90)
        for i in range(4):
            cross(width / 2, times - 1)
            t.forward(width)
            

cross(100, 4)
t.done()