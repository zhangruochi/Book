#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


from abc import ABC,abstractmethod
from collections import namedtuple
from collections import Counter

Customer = namedtuple("Customer","name fidelity")

class LineItem:

    def __init__(self,product,quantity,price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price



class Order:
    
    def __init__(self, customer, cart, promotion = None):
        self.customer = customer
        self.cart = cart 
        self.promotion = promotion

    def total(self):
        if not hasattr(self,"__total"):
            self.__total = sum(item.total() for item in self.cart) 
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)

        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:. 2f}>'
        return fmt.format(self.total(), self.due)


#策略的抽象基类
class Promotion(ABC):
    @abstractmethod
    def discount(self,order):
        pass


#为积分为1000以上的顾客提供5%的折扣
class FidelityPromo:
    def discount(self,order):
        return order.total() * .05 if oerder.customer.fidelity > 1000 else 0        


#为单个商品20个或者以上时提供10%折扣
class BulkItemPromo:
    def discount(self,order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount = .1
                break         

        return order.total() * discount

#订单中不同商品达到10个或者以上时提供7%折扣
class LargeOrderPromo:
    def discount(self,order):
        return order.total() * .07 if len({lineItem.product for lineItem in order.cart}) >= 10 else 0


print(globals())

