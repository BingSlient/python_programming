"""Learn how to use Enum class in python
"""

from enum import Enum, unique

@unique
class Gender(Enum):
    Male = 0
    Female =1

class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    
    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name


if __name__ == '__main__':
    # 测试:
    bart = Student('Bart', Gender.Male)
    if bart.gender == Gender.Male:
        print('测试通过!')
    else:
        print('测试失败!')
    
    pre_name = bart.name
    bart.name = 'La'
    print('change student {} name to {}'.format(pre_name, bart.name))

