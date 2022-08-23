

def t1():
    try:
        x = "x"
        x = float(x)
    except:
        raise

def t2():
    try:
        x = "x"
        x = float(x)
    except:
        raise Exception('报错了')

def t3():
    try:
        x = "x"
        x = float(x)
    except:
        print('报错了')

def t4():
    try:
        x = "x"
        x = float(x)
        print('被检测的代码块')
    except SyntaxError:
        print('检测到该异常，就执行这个位置的逻辑')
    except:
        raise
    else:
        print('没有异常发生时执行的代码块')

if __name__ == '__main__':
    t4()
    t3()
    t1()
    t2()
