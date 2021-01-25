class Student():
    # 类变量
    sum1 = 0
    # name = '123'
    # age = 18

    def __init__(self,name,age):
        # 实例变量
        self.name = name
        self.age = age
        self.score = 0
        # 打印实例变量
        print(self.name)
        print(id(self.name))
        # 答应类变量
        print(self.__class__.sum1)
        print(Student.sum1)
        # print(name)
        # print(id(name))

    def print_score(self):
        print(self.score)

    # 实例方法
    def do_homework(self):
        print('homework')

    # 类方法
    @classmethod
    def plus_sum(cls):
        cls.sum1 += 1
        print(cls.sum1)

    # 静态方法
    def add(self):
        print('aaaaaaaaaa')
stu1 = Student('小臭臭',0)
print(stu1.__dict__)
stu1.do_homework()
stu1.score = 2
stu1.print_score()