import turtle


def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string


def draw_l_system(t, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)


def main(iterations, axiom, rules, angle, length=5, size=2, y_offset=0,
         x_offset=0, offset_angle=0, width=450, height=450):
    inst = create_l_system(iterations, axiom, rules)

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)

    t.up()
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    draw_l_system(t, inst, angle, length)
    t.hideturtle()

    wn.exitonclick()


# Ковер серпинского
# axiom = "YF"
# rules = {"X":"YF+XF+Y", "Y":"XF-YF-X"}
# iterations = 1 # TOP: 10
# angle = 60
# Фрактал Вичека
# axiom = "F-F-F-F"
# rules = {"F":"F-F+F+F-F"}
# iterations = 4 # TOP: 6
# angle = 90
# Анклеты Кришны
# axiom = " -X--X"
# rules = {"X":"XFX--XFX"}
# iterations = 3 # TOP: 9
# angle = 45
# Квадратный фрактал Госпера
# axiom = "YF"
# rules = {"X": "XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF-",
#          "Y": "+FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY"}
# iterations = 2
# angle = 90
# Кривая Мура
# axiom = "LFL-F-LFL"
# rules = {"L":"+RF-LFL-FR+", "R":"-LF+RFR+FL-"}
# iterations = 0
# angle = 90
# Кривая Гильберта
# axiom = "X"
# rules = {"X":"XFYFX+F+YFXFY-F-XFYFX", "Y":"YFXFY-F-XFYFX+F+YFXFY"}
# iterations = 4
# angle = 90
# Кривая Пеано
# axiom = "F"
# rules = {"F":"F+F-F-F-F+F+F+F-F"}
# iterations = 2
# angle = 90
# Крест
# axiom = "F+F+F+F"
# rules = {"F":"F+FF++F+F"}
# iterations = 3
# angle = 90
# Треугольник
# axiom = "F+F+F"
# rules = {"F":"F-F+F"}
# iterations = 2
# angle = 120
# Кривая дракона
# axiom = "FX"
# rules = {"X":"X+YF+", "Y":"-FX-Y"}
# iterations = 8
# angle = 90
# Кривая Terdragon
# axiom = "F"
# rules = {"F":"F-F+F"}
# iterations = 5
# angle = 120
# Двойная кривая дракона
# axiom = "FX+FX"
# rules = {"X":"X+YF+", "Y":"-FX-Y"}
# iterations = 6
# angle = 90
# Тройная кривая дракона
# axiom = "FX+FX+FX"
# rules = {"X": "X+YF+", "Y": "-FX-Y"}
# iterations = 7
# angle = 90
main(axiom=axiom, angle=angle, iterations=iterations, rules=rules)
