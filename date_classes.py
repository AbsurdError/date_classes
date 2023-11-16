# from dataclasses import dataclass, field
# from pprint import pprint
#
# class Thing:
#
#     def __init__(self, name, weight, price, dims = []):
#         self.name = name
#         self.weight = weight
#         self.price = price
#         self.dims = dims
#
#     def __repr__(self):
#         return f'{self.__dict__}'
#
# @dataclass
#
# class ThingData:
#     name: str
#     weight: int
#     price: float
#     dims: list = field(default_factory=list)
#     def __eq__(self, other):
#         return self.price == other.price
#
#
# th = Thing('name', 15, 1500)
# th.dims.append(10)
# print(th)
# th2 = Thing('fghmm', 45, 12)
# print(th2)
# td = ThingData('name2', 12, 2.5)
# td.dims.append(10)
# print(td)
# td2 = ThingData('name2', 121, 2.5)
# print(td2)
# pprint(ThingData.__dict__)
import abc
# from dataclasses import dataclass, field, InitVar
#
#
# class Vector3D:
#     def __init__(self, x, y, z, clac_len: bool = True):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.length = (x ** 2 + y ** 2 + z ** 2) ** 0.5 if clac_len else 0
#
#
#
# @dataclass(order=True)
# class VectorData:
#     x: int
#     y: int = field(compare=False)
#     z: int = field(default=0)
#     calc_len: InitVar[bool] = True
#     length: float = field(init=False, default=0)
#     pi: float = field(init=False)
#
#     def __post_init__(self, calc_len: bool):
#         if calc_len:
#             self.length = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
#         self.pi = 3.14
#
#
#
# # v = Vector3D(1, 2, 3, False)
# # print(v.__dict__)
#
# vd = VectorData(1, 4)
# vd2 = VectorData(1, 4)
# print(vd <= vd2)
# print(vd)
# # print(vd2)


###Ошибка
# from dataclasses import dataclass, field, InitVar
# from typing import Any
# from random import randrange
# @dataclass
# class Goods:
#     current_vid = 0
#
#     vid: int = field(init=False)
#     price: Any
#     weight: Any
#
#     def __post_init__(self):
#         print('Goods')
#         Goods.current_vid += 1
#         self.vid = Goods.current_vid
#
#
# class GoodMeassureFactory:
#     @staticmethod
#     def get_init_meassure():
#         return [0, 0, 0]
#
# # @dataclass
#
# class Book(Goods):
#     price: float = 0
#     weight: int | float = 0
#     title: str
#     author: str
#     # meassure: list = field(default_factory=GoodMeassureFactory.get_init_meassure)
#
#     def __post_init__(self):
#         super().__post_init__()
#         print('Book')
#
#
#
# g = Goods(12345, 2.5)
# print(g)
# g1 = Goods(12345, 2.5)
# print(g1)
#
# b = Book(2000, 2.5, 'dfghj', 'ertyuio')
# # for i in range(len(b.meassure)):
# #     b.meassure[i] = 0
#
# print(b)

# from dataclasses import dataclass, field, InitVar, make_dataclass
# from typing import Any
#
#
# class Car:
#     def __init__(self, model, max_speed, price):
#         self.model = model
#         self.max_speed = max_speed
#         self.price = price
#
#     def get_max_speed(self):
#         return self.max_speed
#
# @dataclass
# class CarD:
#     model: str
#     max_speed: Any
#     price: int = field(default=0)
#
#     def get_max_speed(self):
#         return self.max_speed
#
#     def get_price(self):
#         return self.price
#
# CarData = make_dataclass('CarData', [('model', str), 'max_speed', ('price', int, field(default=0))], namespace={'get_max_speed': lambda self: self.max_speed, 'get_price': lambda self: self.price})
# cd = CarData('Lada Granta', 120, 60000000)
# print(cd.get_max_speed())
# print(cd.get_price())

# from dataclasses import dataclass, field
#
# @dataclass(order=True)
# class AirCastle:
#     height: int
#     blocks: int
#     color: str
#
#     def change_height(self, value):
#         self.height = value if  value >-1 else 0
#
#     def __add__(self, other):
#         if not isinstance(other, int):
#             raise TypeError('zxcvbnm')
#         self.blocks = self.blocks + other
#         self.height = self.height + other//5
#
#         return AirCastle(self.height, self.blocks, self.color)
#
#     def get_visible(self, visible):
#         return f'Видимость замка {self.height//visible*self.blocks}'
#
#     def __str__(self):
#         return f'The AirCastle at an altitude of {self.height} meters is {self.color} with {self.blocks} clouds'
#
# v = AirCastle(552, 522, 'red')
# v1 = AirCastle(55, 22, 'black')
# print(v)
# print(v1 > v)
# print(v1 < v)
# print(v1 >= v)
# print(v1 <= v)
# print(v1 == v)
# print(v1 != v)




# from dataclasses import dataclass
#
# @dataclass(order=True)
# class GoodIfrit:
#     height: int
#     name: str
#     goodness: int = 0
#
#     def change_goodness(self, value):
#         self.goodness = max(0, self.goodness + value)
#
#     def __add__(self, number):
#         return GoodIfrit(self.height + number, self.name, self.goodness)
#
#     def __call__(self, argument):
#         return argument * self.goodness // self.height
#
#     def __str__(self):
#         return f"Good Ifrit {self.name}, height {self.height}, goodness {self.goodness}"
#
#
# # gi1 = GoodIfrit(10, "Ifrit1", 5)
# # print(gi1)
# #
# # gi1.change_goodness(3)
# # print(gi1)
# #
# # gi2 = gi1 + 9
# # print(gi2)
# #
# # result = gi2(10)
# # print(result)
# #
# #
# # gi3 = GoodIfrit(10, "Ifrit2", 8)
# # print(gi1 < gi3)
# # print(gi1 > gi3)
# # print(gi1 <= gi3)
# # print(gi1 >= gi3)
# # print(gi1 == gi3)
# # print(gi1 != gi3)
#
# # gi = GoodIfrit(80, "Hazrul", 3)
# # gi.change_goodness(4)
# # print(gi)
# # gi1 = gi + 15
# # print(gi1)
# # print(gi(31))
#
# # gi = GoodIfrit(80, "Hazrul", 3)
# # gi1 = GoodIfrit(80, "Dalziel", 1)
# # print(gi < gi1)
# # gi1.change_goodness(2)
# # print(gi > gi1)
# # print(gi, gi1, sep='\n')

# from dataclasses import dataclass
# @dataclass(order=True)
# class Wizard:
#     name: str
#     rating: int
#     age: int
#
#     def change_rating(self, value):
#         new_rating = max(1, min(100, self.rating + value))
#         new_age = abs(value) // 10
#
#         self.age = max(18, self.age - new_age) if value > 0 else self.age + new_age
#
#         self.rating = new_rating
#
#     def __iadd__(self, wd: str):
#
#         self.rating += len(wd)
#         self.age -= len(wd) // 10
#
#         return self
#
#
#     def __call__(self, num: int):
#
#         return (num - self.age) * self.rating
#
#     def __str__(self):
#
#         return f"Wizard {self.name} with {self.rating} rating looks {self.age} years old"
#
#
# wizard1 = Wizard("Merlin", 10, 100)
# print(wizard1)
#
# wizard2 = Wizard("Gandalf", 15, 150)
# print(wizard2)
#
# wizard1 += "magic"
# wizard1.change_rating(20)
# print(wizard1)
# result = wizard1(5)
# print(result)
#
# print(wizard1 < wizard2)
# print(wizard1 > wizard2)
# print(wizard1 <= wizard2)
# print(wizard1 >= wizard2)
# print(wizard1 == wizard2)
# print(wizard1 != wizard2)



