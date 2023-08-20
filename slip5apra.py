class strings:
    def getstr(self):
        self.str=input("Enter the string:")
        print(str)
    def print(self):
        print(self.str.upper())
s1=strings()
s1.getstr()
s1.print()