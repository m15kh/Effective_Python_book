#bad manner

def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')


log('My numbers are', [1, 2])
log('Hi there', [])
print('-----------------------------------------')

#better manner
def log(message, * values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')


log('My numbers are', 1, 2)
log('Hi there')

favorites = [7, 33, 99]
log('favorites are',favorites)


#worst thing in *args
print('-----------------------------------------')

# first issue of *args
def my_generator():
    for i in range(10):
        yield i
def my_func(*args):
    print(args)
it = my_generator()
my_func(*it)

# secend issue of *args
print('-----------------------------------------')
def log(sequence, message, *values):
    if not values:
        print(f'{sequence} - {message}')
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{sequence} - {message}: {values_str}')
log(1, 'Favorites', 7, 33) # New with *args OK
log(1, 'Hi there') # New message only OK
log('Favorite numbers', 7, 33) # Old usage breaks