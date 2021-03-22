from abc import ABC


class Exp(ABC):
    def eval(self):
        pass
    def printPrefix(self):
        pass
    def printPostfix(self):
        pass
    def accept(self,process):
        if isinstance(process,Eval):
            return self.eval()
        elif isinstance(process,PrintPrefix):
            return self.printPrefix()
        elif isinstance(process,PrintPostfix):
            return self.printPostfix()

class Eval(ABC):
    pass
class PrintPrefix(ABC):
    pass
class PrintPostfix(ABC):
    pass


class BinExp(Exp):
    def __init__(self,first,op,second):
        self.first =first
        self.op = op
        self.second = second
    def eval(self):
        if self.op == '*':
            return self.first.eval()*self.second.eval()
        elif self.op == '/':
            return self.first.eval()/self.second.eval()
        elif self.op == '+':
            return self.first.eval()+self.second.eval()
        elif self.op == '-':
            return self.first-self.second.eval()
        else:
            raise ValueError()
    def printPrefix(self):
        return self.op+' '+self.first.printPrefix()+' '+self.second.printPrefix()
    def printPostfix(self):
        return str(self.first.printPostfix())+' '+str(self.second.printPostfix())+' '+self.op

class UnExp(Exp):
    def __init__(self,op,first):
        self.first = first
        self.op = op
    def  eval(self):
        if self.op == '+':
            return self.first.eval()
        elif self.op == '-':
            return -self.first.eval()
    def printPrefix(self):
        return self.op+'. '+self.first.printPrefix()
    def printPostfix(self):
        return str(self.first.printPostfix()) + ' ' + self.op+ '.'
class IntLit(Exp):
    def __init__(self,num):
        self.num = num
    def eval(self):
        return self.num
    def printPrefix(self):
        return str(self.num)
    def printPostfix(self):
        return str(self.num) 
class FloatLit(Exp):
    def __init__(self,num):
        self.num = num
    def eval(self):
        return self.num
    def printPrefix(self):
        return str(self.num)
    def printPostfix(self):
        return str(self.num)
