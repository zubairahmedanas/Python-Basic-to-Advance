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
class Complex:


    def __init__(self, real ,imag):
        self.real =real
        self.imag =imag

    def add(self, number):
        real = self.real+ number.real
        imag = self.imag+ number.imag
        result = Complex(real,imag)
        return  result


n1 = Complex(5,4)
n2 = Complex(4, -3)
result = n1.add(n2)
print(result.real)
print(result.imag)