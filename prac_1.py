# num = int(input("Enter a number: "))
# # num1 = int(num)
# print(num)
# print(type(num))
#
# num = float(input("Enter a number: "))
# # num1 = int(num)
# print(num)
# print(type(num))


# x  = 5
# quotient = x//2
# reminder = x%2
# print('quotient is: ', quotient)
# print('remindre is:', reminder)

#
# fee = 4535
#
# discount = 10
#
# get_dis = (discount/100)* fee
#
# print(get_dis)
# amount_after_discount =  fee-get_dis
# print(amount_after_discount)


# num = int(input("Enter a number: "))
#
# if (0 == num):
#     print("it is zero")
# elif (num > 0):
#     print("it is positive")
# else:
#     print("negative")

# count = 10
# number = int(input("pls enter a number: "))
# while count<=10:
#     product= number * count
#     print( number, "x", count, "=", product)
#     count =count-1
#     # print(count)
#     if count==0:
#         break


# lang = ("pyhton", "C", "C++", "Java")
#
# lang.pu="ddd"
#
# print(lang)

# text = "talk is cheap. Show me the code"

# print("1.",text[3])
#
# print("2", text.replace("code", "prgrm"))


p1 = {"name": "anas", "dept": "cse"}
# print(p1.get("institute", ["NC","bits",'ti']))
p1["institute"] = "bits", "NC"


# print(p1)
# p1.pop("dept")
# print(p1)
# for key in p1:
#     print(p1[key])

# class Student:
#     def chk_pass_fail(self):
#         if self.marks <= 40:
#             return False
#         else:
#             return True
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#
# student_1 = Student("Anas", 80)
# # print(student_1.marks)
# student_2 = Student("Zubair",35)
#
# res = student_1.chk_pass_fail()
# print(res)
# res = student_2.chk_pass_fail()
# print(res)
# student_1.name ="max"
# student_1.marks = 85
#
# result = student_1.chk_pass_fail()
# print(result)
#
# student_2 =Student()
# student_2.name ="clasrk"
# student_2.marks = 33
# result = student_2.chk_pass_fail()
# print(result)
# class Complex:
#
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
#
#     def add(self, number):
#         real = self.real + number.real
#         imag = self.imag + number.imag
#         result = Complex(real, imag)
#         return result
#
#
# n1 = Complex(5, 4)
# n2 = Complex(4, -3)
# result = n1.add(n2)
# print(result.real)
# print(result.imag)


# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def sum(self):
#         result = self.a + self.b + self.c
#         return result
#
#
# t1 = Triangle(3, 4, 5)
# res = t1.sum()
# print("The result is:", res)


# class Animal:
#     def eat(self):
#         print("AN Animal can eat")
# class Dog(Animal):
#     def bark(self):
#         print("A Dog can Bark")
#     def beef(self):
#         print("A Dog love Beef")
#
# class Cat(Animal):
#     def milk(self):
#         print("A Cat  loves milk")
# dog1 = Dog()
# dog1.beef()


# class Polygon:
#     def __init__(self, sides):
#         self.sides = sides
#
#     def display(self):
#         print("A ploygon has two dimension")
#     def perimeter(self):
#         result = sum(self.sides)
#         return result
#
# class Triangle(Polygon):
#     def display(self):
#         print("A triangle has 3 edges")
#         # super().display()
# class Quadril(Polygon):
#     def display(self):
#         print("A quadril has 4 edges")
#         super().display()
#
# t1 = Quadril([3,4,5])
# res = t1.perimeter()
# print("the result is", res)
# t1.display()
# t2 = Quadril()
# t2.display()

try:
    x1 = int(input("Enter a number: "))
    x2 = int(input("Enter a number: "))

    result = x1 / x2
    print("The result is ", result)
except:
    print("pls enter bigger than zero")
    print("The program ends")
