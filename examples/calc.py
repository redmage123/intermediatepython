#!c:\programdata\anaconda3\python.exe

class Calc(object):
    def add(self,x,y):
        return x + y



if __name__ == '__main__':

    c = Calc()
    assert c.add(1,1),2
