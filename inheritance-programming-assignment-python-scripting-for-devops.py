# Write a class 
#   that calculates and stores the height and weight of a person in metric. 
#   The file should be named lab.py.  
#   BMI is calculated using this formula: Weight/Height^2 (kg and  m)
# The class should have two properties named:
#     Weight
#     Height
# The class should have two methods:
#     BMI_Value – This takes no arguments and returns a decimal value of the BMI
#     Equals – This should override the equals method from the object class to compare the weight and height of two BMI objects.  
#               To override the equal method you should implement this method: __eq__(self, other) and return a boolean


class BMI:
    def __init__(self, weight="", height=""):
        self.weight = weight
        self.height = height

    def BMI_Value(self):
        return self.weight / self.height ** 2

    def __eq__(self, other):
        if isinstance(other, BMI):
            return self.weight == other.weight and self.height == other.height
        return False

student1 = BMI(70, 76)
print(student1.BMI_Value())
