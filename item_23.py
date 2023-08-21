
def remainder(number, divisor):
    return number % divisor

my_kwargs = {
'number': 20,
'divisor': 7,
}
assert remainder(**my_kwargs) == 6


my_kwargs = {
'divisor': 7,
}
remainder(number=20, **my_kwargs)


def print_parameters(**kwargs):
    # for key, value in kwargs.items():
    #     print(f'{key} = {value}')
    print(kwargs)


print_parameters(**my_kwargs)