import sys
import timeit


def is_triangle_v1(sides):
    a, b, c = sides
    if a < b + c and b < a + c and c < a + b:
        result = True
    else:
        result = False
    return result


def is_triangle_v2(sides):
    # if max(sides) < sum(sides) - max(sides):
    a, b, c = sides
    # m = max(a, b, c)
    m = max(sides)
    if m < a+b+c - m:
        result = True
    else:
        result = False
    return result


def main():
    """
    Даны три натуральных числа.
    Возможно ли построить треугольник с такими сторонами?
    * Если это возможно, выведите строку YES, иначе выведите строку NO.
    Треугольник — это три точки, не лежащие на одной прямой.
    * Вводятся три натуральных числа.
    * Выведите ответ на задачу.
    Пример 1
        Ввод
        3
        4
        5
        Вывод
        YES
    """
    if False:
        # Экспериментирую со скоростью
        repeat = 10**4
        number = 10**3
        times_1 = timeit.repeat(
            #            "is_triangle_v1([3,4,5])",
            "is_triangle_v1(pars)",
            setup="from __main__ import is_triangle_v1\nimport random\npars = random.sample(range(1,10**6),3)",
            number=number,
            repeat=repeat,
        )

        print(sum(times_1))

        times_2 = timeit.repeat(
            #            "is_triangle_v1([3,4,5])",
            "# pars = random.sample(range(1,10**6),3)\n#print(pars)\nis_triangle_v2(pars)",
            setup="from __main__ import is_triangle_v2\nimport random\npars = random.sample(range(1,10**6),3)\n#print(pars)",
            number=number,
            repeat=repeat,
        )

        print(sum(times_2))
    else:
        # Работает по условиям
        sides = [int(input()), int(input()), int(input())]
        if is_triangle_v1(sides):
           print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
