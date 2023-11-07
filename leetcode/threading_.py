import threading

def print_a():
    print('A', end='')

def print_b():  
    print('B', end='')

def print_c():
    print('C', end='')

if __name__ == '__main__':
    t1 = threading.Thread(target=print_a)
    t2 = threading.Thread(target=print_b) 
    t3 = threading.Thread(target=print_c)

    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
    t3.join()
        