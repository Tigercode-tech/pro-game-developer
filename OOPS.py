class year8:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def greet(self):
        print("hello my name is: ", self.name)
        print("My age is : ", self.age)

any_variable_name = year8("戰號喜", 43)
any_variable_name.greet()

another_variable_name = year8("yittrdym", 11)
print(any_variable_name.age, another_variable_name.name)