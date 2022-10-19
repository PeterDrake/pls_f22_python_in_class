x = 'a'

def f():
    def g():
        def h():
            print('h: ' + x)
        global x
        x = 'b'
        print('g1: ' + x)
        h()
        print('g2: ' + x)
    print('f1: ' + x)
    g()
    print('f2: ' + x)

f()
