
class Value:
    """Дескриптор, который взимает комиссию"""
    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value - value * instance.commission

    def __set_name__(self, owner, name):
        self.__name = name


class Account:
    amount = Value()

    def __init__(self, commission: float):
        self.__commission = commission

    @property
    def commission(self):
        return self.__commission

    @commission.setter
    def commission(self, value: float):
        if value < 0:
            self.__commission = 0
        else:
            self.__commission = value


new_account = Account(0.1)
new_account.amount = 100
print(new_account.amount)
new_account.commission = 0.2
new_account.amount = 200
print(new_account.amount)
