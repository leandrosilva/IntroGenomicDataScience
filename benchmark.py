from datetime import datetime, timedelta

def benchmark():
    start = datetime.now()
    benchmark1()
    end = datetime.now()
    diff = (end - start).total_seconds() * 1000
    print('method 1:', diff)

    start = None
    end = None

    start = datetime.now()
    benchmark2()
    end = datetime.now()
    diff = (end - start).total_seconds() * 1000
    print('method 2:', diff)

def benchmark1():
    pass

def benchmark2():
    pass

if __name__ == '__main__':
    benchmark()
