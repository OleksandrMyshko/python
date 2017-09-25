def verify_percents(minimum, maximum):
    def wrapper1(fun):
        def wrapper2(deposit, percent):
            if percent < minimum:
                percent = minimum
            if percent > maximum:
                percent = maximum
            res = fun(deposit, percent)
            return res

        return wrapper2

    return wrapper1


@verify_percents(10, 20)
def percents(deposit, percent):
    return deposit + deposit * percent / 100


print(percents(100, 13))
