import sys
import math


def avg_x_2(a, b, c, test):
    res = (2 * (2 * a + 3 * b + 4 * c + 5 * test)) // (a + b + c + test)
    return res


def calc(a, b, c):
    max_5 = a + b + c
    up = max_5
    low = 0
    i = 0
    if avg_x_2(a, b, c, low) >= 7:
        return low
    while True:
        if up - low == 1:
            return up
        if i > 50:
            raise Exception("Too big number")
        i += 1
        test = low + (up - low) // 2
        res_x_2 = avg_x_2(a, b, c, test)
        if res_x_2 < 7:
            low = test
        else:
            up = test


def main():

    a, b, c = [int(input()), int(input()), int(input())]

#    if a + b + c == 0: 
#        print(1)
#        return 

    x = a + (b - c) / 3
    if x < 0:
        x = 0
#    print(math.ceil(x))


    res = calc(a, b, c)
    print(res)


if __name__ == "__main__":
    main()
