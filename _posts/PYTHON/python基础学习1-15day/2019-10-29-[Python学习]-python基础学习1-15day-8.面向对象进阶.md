# 1.python属性权限

## 1.1 公有属性

没有任何声明的属性值，默认为公有属性

```javascript
def __init__(self, name, age):
    #公有属性
    self.name = name
    self.age = age
```



## 1.2 私有属性

当属性值前面加了两个下划线，则为私有属性

```javascript
def __init__(self, name, age):
    #私有属性
    self.__name = name
    self.__age = age
```



## 1.3 受保护的属性

```javascript
def __init__(self, name, age):
    #保护属性
    self._name = name
    self._age = age
```



# 2. @property装饰器

@property装饰器能够，构造访问保护和私有属性的方法

类似于设置get_name，set_name函数



```javascript
# 访问器 - getter方法
# 相当于get_name
@property
def name(self):
    return self._name

# 访问器 - getter方法
# 相当于get_age
@property
def age(self):
    return self._age

# 修改器 - setter方法
# 相当于set_age，此处的age为前面age函数
@age.setter
def age(self, age):
    self._age = age
```





# 3. __slots__魔法

python为动态语言，可以在程序运行时给对象绑定新的属性和方法

```javascript
class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def info(self):
        print(self._name + ":" + str(self._age))


def main():
    person = Person('王大锤', 12)
    person.info()
    person.gender="男"
    print(person.gender)


if __name__ == '__main__':
    main()
```

如果想要避免这种情况，则需要__slots__魔法函数

```javascript
class Person(object):
    __slots__ = ('_name','_age')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def info(self):
        print(self._name + ":" + str(self._age))


def main():
    person = Person('王大锤', 12)
    person.info()
    person.gender="男"
    # AttributeError: 'Person' object has no attribute 'gender'
    print(person.gender)


if __name__ == '__main__':
    main()
    
```



# 4. 静态方法和类方法

静态方法：@staticmethod

静态方法可以，直接使用类名访问

类方法：classmethod

类方法的第一个参数为cls,它代表当前类相关信息对象，通过这个参数，我们可以获取和类相关的信息，以及创建类的对象

```javascript
class Person(object):

    #静态函数
    @staticmethod
    def is_person(type):
        if type=='人':
            return True
        else:
            return False

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(self.name+":"+str(self.age))


def main():
    #类名直接调用静态函数
    if Person.is_person(input("输入type:")):
        person=Person('张三',18)
        person.show()
    else:
        print("非人哉")

if __name__ == '__main__':
    main()
```



```javascript
from time import time, localtime, sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    #类方法
    @classmethod
    def now(cls):
        ctime = localtime(time())
        
        #cls参数在此表示类对象
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
```



# 5. 继承

python的继承，不需要关键字，只需直接在子类接收的参数里写入父类名称即可

例如：

```javascript
#父类
class Person(object):
    
#子类
class Student(Person)
```



继承的子类使用super()函数来，调用父类的参数和方法

列如：

```javascript
#父类
class Person(object):
    def __init__(self,name,age):
        self._name=name
        self._age=age
        
#子类
class Student(Person):
    def __init__(self,name,age,grade):
        # super()函数调用父类函数，进行初始化
        super().__init__(self,name,age)
        self._grade=grade
```



```javascript
class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def watch_av(self):
        if self._age < 18:
            print("只能观看学习视频")
        else:
            print("可以观看动作电影")

    def play(self):
        print('%s只能观看熊出没' % self._name)


class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def play(self):
        print('%s正在玩' % self.name)

    def study(self, course):
        print('%s的%s正在学习%s' % (self._grade, self._name, course))


class Thacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title


def main():
    person = Person('张三', 18)
    person.watch_av()

    student = Student('李四', 16, '三年级')
    student.play()
    student.study('Java')


main()
```



# 6. 抽象类和方法重写

抽象类：只能被继承的类，不能实例化方法

python并没有在语法层面上提供，抽象类支持，但是可以使用abc模块的ABCMeta实现

方法重写：子类重写，父类方法，使重写的方法具备不同的功能

```javascript
from abc import ABCMeta,abstractmethod

class Pet(object,metaclass=ABCMeta):

    def __init__(self,nickname):
        self._nickname=nickname

    #抽象类
    @abstractmethod
    def make_voice(self):
        pass

class Dog(Pet):

    def __init__(self,nickname):
        super().__init__(nickname)

    def make_voice(self):
        print('%s 汪汪汪' % self._nickname)


class Cat(Pet):
    def __init__(self,nickname):
        super().__init__(nickname)

    def make_voice(self):
        print('%s 喵喵喵' % self._nickname)

def main():
    pets=[Dog('旺财'),Dog('张三'),Cat('啊喵')]

    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
```

