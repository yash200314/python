class uplow:
    def get_str(self):
        self.str=input("Enter the string:")
    def print_str(self):
        print(self.str)
        print(self.str.upper())
    def modify(self):
        for char in reversed(self.str):
            print(char)

d1=uplow()
d1.get_str()
d1.print_str()
d1.modify() 