def my_function(*args, **kwargs):
    suma = 0
    for x in args:
        if isinstance(x, int) or isinstance(x, float):
            suma += x
    print(suma)


my_function(1, 5, -3, 'abc', [12, 56, 'cad'])
my_function()
my_function(2, 4, 'abc', param_1=2)


def sum_of_n(nr):
    if nr <= 0:
        return 0
    else:
        return nr + sum_of_n(nr - 1)


def sum_of_even(nr):
    if nr <= 0:
        return 0
    elif nr % 2 == 0:
        return nr + sum_of_even(nr - 2)
    else:
        return sum_of_even(nr - 1)


def sum_of_odd(nr):
    if nr <= 0:
        return 0
    elif nr % 2 != 0:
        return nr + sum_of_odd(nr - 2)
    else:
        return sum_of_odd(nr - 1)


print(sum_of_n(10))
print(sum_of_even(10))
print(sum_of_odd(10))


def new_function():
    str = input("Valoare: ")
    try:
        nr = int(str)
        if isinstance(nr, int):
            return nr
    except ValueError:
        return 0


print(new_function())
