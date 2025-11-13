import numpy as np
import scipy as sp
from scipy import integrate
import random

def task_1(rand_max = 100):
    def func_1(x = np.random.randint(0,rand_max,12)):



        print(x)

        if sum(x[0:3]) < sum(x[5:8]):
            print("summer bigger")
        else:
            print("winter bugger")

        i = 1
        while i < 13:
            print(f"{i} максимум : index {np.argmax(x) + 1}, value {x[np.argmax(x)]}")
            x[np.argmax(x)] = -1
            i+=1

    # func_1()

    def func_2():
        """"
        Тест 1
    20 8 9 18 5 12 16 16 6 7
    44 70 44 66 46 38 38 37 66 67
    4
    7
    S = 49 км, T = 1.28 час, V = 38.34 км/ч
        """
        lengths = (input().split())
        np_lengths = np.array(lengths)
        np_lengths =  np_lengths.astype(int)
        velocities = (input().split())
        np_velocities = np.array(velocities)
        np_velocities =  np_velocities.astype(int)
        # print(np_lengths)
        # print(np_velocities)
        start = int(input("start "))
        end = int(input("end "))
        s = np.sum(np_lengths[start:end + 1])
        t = np.sum(np_lengths[start:end + 1]/np_velocities[start:end + 1])
        v = s / t
        print(f"S = {round(s,2)}\n"
              f"T = {round(t,2)}\n"
              f"V = {round(v,2)}")

    # func_2()

    def func_3():
        matr_a = np.array([[-2, -8.5, -3.4, 3.5],
                           [0, 2.4, 0, 8.2],
                           [2.5,1.6,2.1,3],
                           [0.3,-0.4,-4.8,4.6]])
        matr_b = np.array([-1.88,-3.28,-0.5,-2.83])
        matr_a_rev=  np.linalg.matrix_power(matr_a,-1)
        matr_res = matr_a_rev @ matr_b
        print(matr_res) # добавить округление до 1 знака после запятой

    # func_3()


    def func_4_1():

        def target_func(x):
            return x**3 + 3 * x ** 2 + 1

        def integr(start, end):
            func = "x**2 + 2*x + 1"
            result, error = integrate.quad(target_func, start, end)
            print(f"∫[{start}, {end}] (x^3 + 3x^2 + 1) dx = {result:.4f}")
            return result

        integr(0,2)
    # func_4_1()

    def func_4_2():
        def f(y,x):
            return x**2 +2*y

        integral = integrate.dblquad(f,0,1,0,2)
        print(integral)

    # func_4_2()

task_1()
