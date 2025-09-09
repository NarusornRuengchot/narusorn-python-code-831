class ClassName:
    """Class docstring"""
    
    def __init__(self, parameters):  #ต้องมีคำว่าselfทุกอันนะจ๊ะ
        # Constructor method
        self.attribute = value
    
    def method_name(self):
        # Instance method
        return something


myObj = ClassName(parameters) #สร้างวัตถุของclass
print(myObj.attribute)
resultFromMethod = myObj.method_name()