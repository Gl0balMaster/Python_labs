
import matplotlib
import math
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as mpl
from matplotlib.patches import Ellipse, Circle, Rectangle, Polygon, PathPatch, Path


def task_1(num_amount = 100):
    def func_1(args):
        y = list()
        for item in args:
            arg = item * math.pi / 360
            y.append(math.exp(math.cos(arg)) + math.log(math.cos(arg*0.6)**2 + 1) * math.sin(arg))
        mpl.plot(args, y)
        mpl.show()

    def func_2(args):
        y = list()
        for item in args:
            arg = item * math.pi / 360
            y.append(-math.log((math.cos(arg) + math.sin(arg)) ** 2 + 2.5) + 10)
        mpl.plot(args, y)
        mpl.show()



    x = list()
    i = -360
    while i < 360:
        x.append(i)
        i+=math.pi / num_amount

    func_1(x)
    func_2(x)

# task_1()

def task_2(num_amount = 80):
    def func(args):
        y = list()
        for item in args:
            if item**2 - 9 == 0:
                y.append(np.nan)
            else:
                y.append(5/(item ** 2 - 9))
        mpl.plot(args, y)
        mpl.show()

    x = list()
    i = -10
    while i < 10:
        x.append(i)
        i+= 20/num_amount

    func(x)

# task_2()


def task_3():

    fig, ax = mpl.subplots(figsize=(14, 12))
    ax.set_aspect('equal')
    ax.axis('off')

    elephant_gray = '#6D6D6D'
    elephant_light = '#8E8E8E'
    elephant_dark = '#4A4A4A'
    eye_color = '#1A1A1A'

    # Фон
    ax.set_facecolor('#F0F8FF')  # Светло-голубой фон

    # ТЕЛО СЛОНА (основное)
    body = Ellipse((0, 0), 10, 6, color=elephant_gray, alpha=0.9)
    ax.add_patch(body)

    # СПИНА и БОКА (для объема)
    back_curve = Ellipse((0, 1), 9, 5, color=elephant_light, alpha=0.7)
    ax.add_patch(back_curve)

    # ГОЛОВА
    head = Ellipse((5, 2), 5, 4, color=elephant_gray, alpha=0.9)
    ax.add_patch(head)

    # УШИ - детализированные
    # Левое ухо
    left_ear_outer = Ellipse((1, 4), 4, 5, angle=25, color=elephant_gray, alpha=0.9)
    left_ear_inner = Ellipse((1.5, 4), 3, 4, angle=25, color=elephant_light, alpha=0.7)
    ax.add_patch(left_ear_outer)
    ax.add_patch(left_ear_inner)

    # Правое ухо
    right_ear_outer = Ellipse((4, 5), 4, 5, angle=-20, color=elephant_gray, alpha=0.9)
    right_ear_inner = Ellipse((4.5, 5), 3, 4, angle=-20, color=elephant_light, alpha=0.7)
    ax.add_patch(right_ear_outer)
    ax.add_patch(right_ear_inner)

    # ХОБОТ - детализированный с изгибами
    trunk_points = np.array([
        [6.5, 1.5],  # начало
        [8, 0.5],  # первый изгиб
        [9, -1],  # вниз
        [8, -2.5],  # назад
        [7, -3],  # кончик
        [6, -2],  # обратный изгиб
        [5.5, -0.5]  # к основанию
    ])

    trunk = PathPatch(Path(trunk_points, [Path.MOVETO, Path.CURVE4, Path.CURVE4,
                                          Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.CURVE4]),
                      facecolor='none', edgecolor=elephant_gray, linewidth=10,
                      capstyle='round', joinstyle='round')
    ax.add_patch(trunk)

    # НОГИ - с детализацией
    legs_data = [
        # x, y, width, height, rotation
        (-3.5, -2.5, 1.2, 3, 0),  # задняя левая
        (-1, -2.5, 1.2, 3, 0),  # передняя левая
        (1, -2.5, 1.2, 3, 0),  # передняя правая
        (3.5, -2.5, 1.2, 3, 0)  # задняя правая
    ]

    for i, (x, y, w, h, angle) in enumerate(legs_data):
        leg_outer = Ellipse((x, y), w, h, angle=angle, color=elephant_gray, alpha=0.9)
        leg_inner = Ellipse((x, y - 0.3), w * 0.7, h * 0.8, angle=angle, color=elephant_light, alpha=0.6)
        ax.add_patch(leg_outer)
        ax.add_patch(leg_inner)

    # СТУПНИ
    foot_positions = [(-3.5, -4), (-1, -4), (1, -4), (3.5, -4)]
    for x, y in foot_positions:
        foot = Ellipse((x, y), 1.5, 0.8, color=elephant_dark, alpha=0.8)
        ax.add_patch(foot)

    # ГЛАЗА - с бликами
    # Левый глаз
    left_eye_outer = Circle((4, 3), 0.4, color=eye_color, alpha=0.9)
    left_eye_inner = Circle((4.1, 3.1), 0.15, color='white', alpha=0.8)
    ax.add_patch(left_eye_outer)
    ax.add_patch(left_eye_inner)

    # Правый глаз
    right_eye_outer = Circle((5.5, 3.2), 0.35, color=eye_color, alpha=0.9)
    right_eye_inner = Circle((5.6, 3.3), 0.12, color='white', alpha=0.8)
    ax.add_patch(right_eye_outer)
    ax.add_patch(right_eye_inner)

    # ХВОСТ - с кисточкой
    tail_points = np.array([
        [-5, 0],
        [-6.5, -1],
        [-7, -0.5],
        [-6, 0.5]
    ])

    tail = PathPatch(Path(tail_points), facecolor='none',
                     edgecolor=elephant_gray, linewidth=6, capstyle='round')
    ax.add_patch(tail)

    # Узор на ушах
    ear_patterns = [
        (1, 4, 25, '#D4AF37'),  # левое ухо
        (4, 5, -20, '#D4AF37')  # правое ухо
    ]

    for x, y, angle, color in ear_patterns:
        pattern1 = Ellipse((x - 0.5, y + 0.5), 0.8, 0.8, angle=angle, color=color, alpha=0.3)
        pattern2 = Ellipse((x + 0.3, y - 0.3), 0.6, 0.6, angle=angle, color=color, alpha=0.3)
        ax.add_patch(pattern1)
        ax.add_patch(pattern2)

    # Устанавливаем границы
    ax.set_xlim(-9, 10)
    ax.set_ylim(-5, 7)

    mpl.tight_layout()
    mpl.show()

# task_3()

