from pathlib import Path
from functools import wraps
from datetime import datetime



def logger(f):
    '''logs a function operation and any exceptions into a file located in the
    current directory named log.txt'''
    @wraps(f)
    def wrapper(*args, **kwargs):
        fname = 'log.txt'
        #Path(fname).touch()

        with open(fname, 'a') as log_file:
            log_file.write(f'{f.__name__}{(args, kwargs)} started at {datetime.now()}\n')

            result = f(*args, **kwargs)

            log_file.write(f'{f.__name__}{(args, kwargs)} returned {result} at {datetime.now()}\n')
        return result
    return wrapper


@logger
def double(x):
    return x*2


@logger
def print_letters(phrase):
    '''Prints the letters in a phrase one by one'''
    for let in phrase.split():
        print(let)


if __name__ == '__main__':
    import time
    y = double(5)
    time.sleep(2)
    z = double(1000)
    double(3)
