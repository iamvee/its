# Simple Logger

## Part 1: logger decorator

keeps history of calls, arguments passed into decorated function and the result, all 
into a `*.csv` file

### usage

decorating `mysum()` function:

```python
import logme 

@logme.logme_part_one
def mysum(a, b):
    return a + b
```

try to call it multiple times, and out logfile will be updated. 
```
>>> mysum(1, 2)
3
>>> mysum(10, 20)
30
```

after calling `mysum` twice, out `logs.csv` will look like this sample file:

```csv
"timestamp","function","args","kwargs,"returned_vals"
"1562093798.5783381","mysum","(1, 2,)","{}","3"
"1562093825.3916304","mysum","(10, 20,)","{}","30"
```

### solution 

```python
import time 

def logme_part_one(fn):
    def inner(*args, **kwargs):
        res = fn(*args, **kwargs)

        log_str = f'"{time.time()}","{fn.__name__}","{args}","{kwargs}","{res}"\n'
        f = open('logs.csv', mode='a')
        f.write(log_str)
        f.close()

        return res
    return inner
```


## Part 2: set logfile's name

use funtions.

### usage 

```python
import logme 

@logme.logme_part_two('logs_new.csv')
def mysub(a, b):
    return a - b
```

### solution

```python
def logme_part_two(filename):
    def decorator(fn):
        def inner(*args, **kwargs):
            res = fn(*args, **kwargs)

            log_str = f'"{time.time()}","{fn.__name__}","{args}","{kwargs}","{res}"\n'
            f = open(filename, mode='a')
            f.write(log_str)
            f.close()

            return res
        return inner
    return decorator
```


## Part 3: 

same as part 2, written in classes

### usage 

```python
import logme

logtemp = logme.LogMeClass('logs_again.csv')

@logtemp
def mymul(a, b):
    return a * b 
```

### solution 

```python
class LogMeClass:
    def __init__(self, filename):
        self.__filename = filename

    def __call__(self, fn):
        def inner(*args, **kwargs):
            res = fn(*args, **kwargs)

            log_str = f'"{time.time()}","{fn.__name__}","{args}","{kwargs}","{res}"\n'
            f = open(self.__filename, mode='a')
            f.write(log_str)
            f.close()

        return inner

```