from decimal import Decimal
from django.conf import settings
from .models import GoodModel


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


def add(self, good, amount=1, update_amount=False):
    """
    Добавить продукт в корзину или обновить его количество.
    """
    good_id = str(good.id)
    if good_id not in self.cart:
        self.cart[good_id] = {'amount': 0, 'price': str(good.price)}
    if update_amount:
        self.cart[good_id]['amount'] = amount
    else:
        self.cart[good_id]['amount'] += amount
    self.save()


def save(self):
    # Обновление сессии cart
    self.session[settings.CART_SESSION_ID] = self.cart
    # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
    self.session.modified = True


def remove(self, good):
    """
    Удаление товара из корзины.
    """
    good_id = str(good.id)
    if good_id in self.cart:
        del self.cart[good_id]
        self.save()


def __iter__(self):
    """
    Перебор элементов в корзине и получение продуктов из базы данных.
    """
    good_ids = self.cart.keys()
    # получение объектов product и добавление их в корзину
    goods = GoodModel.objects.filter(id__in=good_ids)
    for good in goods:
        self.cart[str(good.id)]['good'] = good

    for item in self.cart.values():
        item['cost'] = Decimal(item['cost'])
        item['total_cost'] = item['cost'] * item['amount']
        yield item


def get_total_price(self):
    """
    Подсчет стоимости товаров в корзине.
    """
    return sum(Decimal(item['cost']) * item['amount'] for item in
               self.cart.values())


def clear(self):
    # удаление корзины из сессии
    del self.session[settings.CART_SESSION_ID]
    self.session.modified = True
