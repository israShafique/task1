class Charactercount:
    def __init__(self,str1):
        if(type(str1)== int):
            print('use a string')
        else:
            self.str1=str1
    def countChar(self):
        print(len(self.str1))

str1=Charactercount('isra')
str1.countChar()