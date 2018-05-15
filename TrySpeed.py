import datetime

def outputif(size):
    i = 0
    start = datetime.datetime.now()
    while i < size:
        i+=1
        if(type(i) == int):
            print(i)
    end = datetime.datetime.now()
    delta = end - start
    return delta

def outputtry(size):
    i = 0
    start = datetime.datetime.now()
    while i < size:
        i+=1
        try:
            print(i)
        except BaseException as be:
            print(be)
    end = datetime.datetime.now()
    delta = end - start
    return delta

def outputpure(size):
    i = 0
    start = datetime.datetime.now()
    while i < size:
        i+=1
        print(i)
    end = datetime.datetime.now()
    delta = end - start
    return delta


def simpleif(size):
    i = 1
    start = datetime.datetime.now()
    while i < size:
        if i != 0:
            i +=1
    end = datetime.datetime.now()
    delta = end - start
    return delta

def simpletry(size):
    i = 1
    start = datetime.datetime.now()
    while i < size:
        try:
            i +=1
        except BaseException as be:
            print(be)
    end = datetime.datetime.now()
    delta = end - start
    return delta

def midleif(size):
    i = 0
    start = datetime.datetime.now()
    while i < size:
        """if i == int(size / 4):
            print(i)
        elif i == int(size / 2):
            print(i)
        elif i == size - int(size / 4):
            print(i)
        else:
            pass"""
        if type(i) == int:
            i = i / 1
        else:
            i = int(i)
        i +=1
    end = datetime.datetime.now()
    delta = end - start
    return delta

def midletry(size):
    i = 1
    start = datetime.datetime.now()
    while i < size:
        try:
            i +=1
        except BaseException as be:
            print(be)
        try:
            i = i / 1
        except BaseException as be:
            print(be)
        try:
            i = int(i)
        except BaseException as be:
            print(be)
    end = datetime.datetime.now()
    delta = end - start
    return delta

def midlepure(size):
    i = 1
    start = datetime.datetime.now()
    while i < size:
        i +=1
        i = i / 1
        i = int(i)
    end = datetime.datetime.now()
    delta = end - start
    return delta

def fibif(size):
    i = 1
    x0, x1 = 1, 1
    start = datetime.datetime.now()
    while i < size:
        if size < 2:
            return 1
        else:
            res = x0 + x1
            x0, x1 = x1, res
            i += 1
    end = datetime.datetime.now()
    delta = end - start
    return delta

def fibtry(size):
    i = 1
    x0, x1 = 1, 1
    start = datetime.datetime.now()
    while i < size:
        try:
            res = x0 + x1
        except BaseException as be:
            print(be)
        try:
            x0, x1 = x1, res
        except BaseException as be:
            print(be)
        try:
            i += 1
        except BaseException as be:
            print(be)
    end = datetime.datetime.now()
    delta = end - start
    return delta

def fibpure(size):
    i = 1
    x0, x1 = 1, 1
    start = datetime.datetime.now()
    while i < size:
        res = x0 + x1
        x0, x1 = x1, res
        i += 1
    end = datetime.datetime.now()
    delta = end - start
    return delta
    #print(f"{delta.seconds}:{delta.microseconds}")


def test(size):
    i = 100
    j = 0
    resmatrix = list()
    while i < size:
        resmatrix.append(list())
        resmatrix[j].append(outputif(i))
        resmatrix[j].append(outputtry(i))
        resmatrix[j].append(outputpure(i))
        resmatrix[j].append(midleif(i))
        resmatrix[j].append(midletry(i))
        resmatrix[j].append(midlepure(i))
        resmatrix[j].append(fibif(i))
        resmatrix[j].append(fibtry(i))
        resmatrix[j].append(fibpure(i))
        i = i * 10
        j += 1
    print("Output: if, try, pure; Midle: if, try, pure; Fib: if, try, pure:")
    for index, row in enumerate(resmatrix):
        n = 100*10**index
        print(f"{n} : {row[0].seconds} | {row[1].seconds} | {row[2].seconds} | {row[3].seconds} | {row[4].seconds} | {row[5].seconds}| {row[6].seconds} | {row[7].seconds} | {row[8].seconds}")
