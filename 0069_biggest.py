import sys
import timeit


def find_count_v1(l):
    count = 0
    for i in range(1, len(l) - 1):
        if l[i] > l[i - 1] and l[i] > l[i + 1]:
            count += 1
    return count


def find_count_v2(l):
    count = 0
    i = 1
    lenl = len(l) - 1
    while i < lenl:
        if l[i] > l[i + 1]:
            if l[i] > l[i - 1]:
                count += 1
            i += 1
        i += 1
    return count


def main():
    """ """
    if False:
        # Экспериментирую со скоростью
        repeat = 10**2
        number = 10**2
        gen_len = 10**3
        times_1 = timeit.repeat(
            #            "is_triangle_v1([3,4,5])",
            "find_count_v1(pars)",
            setup=f"from __main__ import find_count_v1\nimport random\npars = random.sample(range(1,10**6),{gen_len})",
            number=number,
            repeat=repeat,
        )

        print(sum(times_1))

        times_2 = timeit.repeat(
            #            "is_triangle_v1([3,4,5])",
            "find_count_v2(pars)",
            setup=f"from __main__ import find_count_v2\nimport random\npars = random.sample(range(1,10**6),{gen_len})",
            number=number,
            repeat=repeat,
        )

        print(sum(times_2))

    else:
        l = list(map(int, input().split()))
        count = find_count_v2(l)
        print(count)
        pass


if __name__ == "__main__":
    main()
