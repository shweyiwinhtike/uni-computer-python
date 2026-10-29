import turtle as t

numbers = [1,2,2,1,3,4,6,5,3,4,5,6,4,3,5,4,5,3,4,4,3,3,4,3,3,4,4,4, 10]
min_v = min(numbers)
max_v = max(numbers)
for i in range(min_v, max_v+1):
    h = numbers.count(i) * 20
    t.speed(0)
    t.fillcolor("pink")
    t.begin_fill()
    t.forward(30)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.end_fill()

    t.penup()
    t.forward(10)
    t.write(i)
    t.forward(20)
    t.pendown()

t.done()
    
            

