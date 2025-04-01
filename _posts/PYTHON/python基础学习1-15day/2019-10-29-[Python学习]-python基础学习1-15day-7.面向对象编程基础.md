1. 创建一个类

```javascript
class person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + "是要吃饭的")


def main():
    per1 = person("张三", "18")
    per1.eat()


if __name__ == '__main__':
    main()
```



2. 属性的权限

```javascript
class animal:
    def __init__(self,name):
        # __开头，表示该属性为私有属性
        self.__name=name

    def eat(self):
        print(self.__name+"eat")


def main():
    ani=animal("xiaobai")
    ani.eat()
    # 私有属性，类外不可以访问
    print(ani.__name)

main()

# _开头表示保护属性
# 没有符号开头，表示公有属性
```

