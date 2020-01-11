#!python3.8.0
# -*-encoding:utf-8-*-


class Something:
    def __init__(self, name):
        self.name = name
        self.is_a = Boolean(self, True)
        self.is_not_a = Boolean(self, False)
        self.is_the = SetProper(self)


class Proper:
    def __init__(self, attr, mid, high):
        self.mid = mid
        self.high = high
        self.attr = attr

    def __getattr__(self, attr):
        self.high.mid.__setattr__(self.attr, attr)
        return Proper(attr, self.mid, self)


class Boolean:
    def __init__(self, base, value: bool):
        self.base = base
        self.attr_value = value

    def __getattr__(self, name):
        setattr(self.base, 'is_a_' + name, self.attr_value)
        setattr(self.base, 'is_not_a_' + name, not self.attr_value)


# !python3.8.0
# -*-encoding:utf-8-*-


class SetProper:
    def __init__(self, mid):
        self.mid = mid

    def __getattr__(self, attr):
        return Proper(attr, self.mid, self)


if __name__ == '__main__':
    jane = Something('Jane')
    print(jane.name)
    jane.is_a.person
    jane.is_a.woman
    jane.is_not_a.man

    print(jane.is_a_person)
    print(jane.is_a_man)
    jane.is_the.parent_of.joe
    print(jane.parent_of)
    print(jane.is_a_person)
